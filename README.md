# Amazon Bedrock Flows

This repository contains examples, patterns, and resources for working with Amazon Bedrock Flows - a visual builder for creating AI applications with multi-step workflows.

## Overview

Amazon Bedrock Flows enables you to build sophisticated AI applications by connecting foundation models (FMs) with other AWS services and custom logic. This project provides examples of common patterns and implementations to help you get started with Bedrock Flows.

## Repository Structure

- **notebooks/** - Jupyter notebooks demonstrating various Bedrock Flows patterns
  - **node_patterns/** - Examples of different node implementations and patterns
  - **agent_patterns/** - Examples of agent-based workflows and patterns
- **data/** - Sample data files for use with the examples
  - **agenticmemory.pdf** - Sample document for memory-based agent examples
- **pre-reqs/** - Setup scripts and prerequisites
  - **web_search_lambda.py** - Lambda function for web search capabilities
  - **0.create_role.ipynb** - Notebook for setting up required IAM roles

## Getting Started

### Prerequisites

1. An AWS account with access to Amazon Bedrock
2. Appropriate permissions to create and manage Bedrock Flows
3. Python 3.8+ and Jupyter Notebook environment

### Setup

1. Clone this repository
2. Run the setup notebook in the pre-reqs directory:
   ```
   jupyter notebook pre-reqs/0.create_role.ipynb
   ```
3. Follow the instructions in the notebook to set up the necessary IAM roles and permissions

## Example Patterns

### Node Patterns

The `notebooks/node_patterns` directory contains examples of different node implementations, including:

- Prompt engineering techniques
- Knowledge base integration
- Function calling
- Multi-model orchestration
- Input/output handling

### Agent Patterns

The `notebooks/agent_patterns` directory demonstrates agent-based workflows, including:

- Agentic memory implementations
- Multi-agent collaboration
- Tool use and reasoning
- Specialized agent patterns for different use cases

## Usage

Each notebook is self-contained with detailed explanations and code examples. To use a notebook:

1. Navigate to the desired notebook directory
2. Open the notebook in Jupyter
3. Follow the step-by-step instructions

## Contributing

Contributions to this repository are welcome! Please feel free to submit pull requests with additional examples, improvements, or bug fixes.

## Resources

- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Amazon Bedrock Flows User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html)
- [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
