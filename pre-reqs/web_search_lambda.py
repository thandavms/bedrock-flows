import json
import os
import urllib.request
import urllib.error
import urllib.parse

def lambda_handler(event, context):

    try:
        print(event)

        inputs = event['node']['inputs']
        for input_item in inputs:
            if input_item['name'] == 'codeHookInput':
                query = input_item['value']
        
        api_key = os.environ.get('TAVILY_API_KEY')
        #api_key = ''

        if not api_key:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': 'Tavily API key not configured'})
            }
        
        # Tavily API endpoint for search
        url = "https://api.tavily.com/search"
        
        # Request parameters
        payload = {
            "api_key": api_key,
            "query": query,
            "search_depth": "basic",  # Use 'basic' for faster results, 'advanced' for more comprehensive
            "include_domains": [],     # Optional: domains to prioritize
            "exclude_domains": []      # Optional: domains to exclude
        }
        
        # Convert payload to JSON and encode as bytes
        data = json.dumps(payload).encode('utf-8')
        
        # Create request with headers
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        req = urllib.request.Request(url, data=data, headers=headers, method='POST')
        
        # Make the request
        with urllib.request.urlopen(req) as response:
            response_data = response.read().decode('utf-8')
            search_results = json.loads(response_data)
        
        print(response_data)
        return json.dumps(search_results)
    
    except urllib.error.HTTPError as e:
        return {
            'statusCode': e.code,
            'body': json.dumps({
                'error': f'HTTP Error: {e.code} {e.reason}',
                'details': e.read().decode('utf-8') if hasattr(e, 'read') else None
            })
        }
    except urllib.error.URLError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'URL Error: {str(e.reason)}'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }