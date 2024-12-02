# LocalStack Concept Learning

This repository contains hands-on examples for learning AWS concepts with **LocalStack**. LocalStack is a fully functional local AWS cloud stack that simulates many AWS services, allowing developers to experiment with them locally. It helps to learn and test AWS services without the need for an actual AWS account.

## Getting Started

### Prerequisites

To follow along with the examples in this repository, you need the following tools installed:

- **Python 3.x** (Recommended version: Python 3.8 or higher)
- **Docker** (LocalStack runs in Docker, so make sure Docker is installed and running)
- **AWS CLI** (LocalStack simulates AWS, so AWS CLI will be used to interact with LocalStack)
- **LocalStack** installed via `pip` or Docker
- **Boto3** for interacting with AWS services in Python
- **awscli-local** for simplified AWS CLI interactions with LocalStack

### Installation

#### 1. **Install LocalStack**:
To install LocalStack with `pip`, use the following command:

```bash
pip install localstack

```
More details on localstack site: https://www.localstack.cloud/