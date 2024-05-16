# Text Analysis Project on Apache OpenWhisk

> **Warning**: This serverless project is not fully functional and serves only as a project trace. Please use it for reference purposes only.

This project provides a modular and flexible framework for analyzing text files using Apache OpenWhisk. It includes functionalities such as word frequency analysis, word cloud generation, sentence summarization, and various visualizations. The project allows you to run individual analyses or all of them together in a serverless environment.

## Prerequisites

1. **Install Docker**: Ensure you have Docker installed on your machine as it is required to build actions with external packages.
2. **Install OpenWhisk CLI**: Download and install the OpenWhisk CLI (`wsk`).

## Setup

### Step 1: Clone the Repository

Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/text_analysis.git
cd text_analysis/serverless
```

### Step 2: Install Required Python Packages
Install the necessary Python packages listed in 
**serverless/packages/requirements.txt:**
```bash
pip install -r packages/requirements.txt
```

### Step 3: Configure OpenWhisk CLI
Configure the OpenWhisk CLI with your API host and authentication key:

```bash
wsk property set --apihost https://ow.services.eemi.tech --auth <your_auth>
```

### Step 4: Create Docker Image for Actions
Since we are using external Python packages, we need to create a Docker image. Create a **Dockerfile** in the **serverless** directory:


**Dockerfile**
```bash
FROM python:3.7-slim
WORKDIR /action
COPY packages/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "/action/exec.py"]
```

Build and push the Docker image to a Docker registry:

```bash
docker build -t <your_dockerhub_username>/text_analysis .
docker push <your_dockerhub_username>/text_analysis
```

### Step 5: Create Actions
Create the actions using the Docker image:

```bash
wsk action create load_text actions/load_text.py --docker <your_dockerhub_username>/text_analysis --web true --memory 256 --timeout 300000 --main load_text
wsk action create analyze actions/analyze.py --docker <your_dockerhub_username>/text_analysis --web true --memory 256 --timeout 300000 --main analyze
wsk action create visualize_wordcloud actions/visualize_wordcloud.py --docker <your_dockerhub_username>/text_analysis --web true --memory 256 --timeout 300000 --main visualize_wordcloud
wsk action create visualize_distributions actions/visualize_distributions.py --docker <your_dockerhub_username>/text_analysis --web true --memory 256 --timeout 300000 --main visualize_distributions
wsk action create summarize actions/summarize.py --docker <your_dockerhub_username>/text_analysis --web true --memory 256 --timeout 300000 --main summarize
wsk action create main actions/main.py --docker <your_dockerhub_username>/text_analysis --web true --memory 512 --timeout 300000 --main main
```

### Step 6: Create Sequences
Create the sequences to chain the actions together:

```bash
wsk action create sequence_analyze --sequence load_text,analyze --web true
wsk action create sequence_visualize_wordcloud --sequence load_text,visualize_wordcloud --web true
wsk action create sequence_visualize_distributions --sequence load_text,visualize_distributions --web true
wsk action create sequence_summarize --sequence load_text,summarize --web true
wsk action create sequence_all --sequence load_text,main --web true
```

## Usage

### Running All Analyses
To run all analyses and get the results, use the following URL (replace <namespace> and <api_host> with your OpenWhisk namespace and API host):

```bash
https://<api_host>/api/v1/web/<namespace>/default/sequence_all.json
```

### Running Individual Analyses
You can run each functionality individually using the following URLs:

- **Text Analysis:**
  ```bash
  https://<api_host>/api/v1/web/<namespace>/default/sequence_analyze.json
  ```
- **Generate Word Cloud:**
  ```bash
  https://<api_host>/api/v1/web/<namespace>/default/sequence_visualize_wordcloud.json
  
  ```
- **Plot Distributions:**
  ```bash
  https://<api_host>/api/v1/web/<namespace>/default/sequence_visualize_distributions.json
  ```
- **Summarize Text:**
  ```bash
  https://<api_host>/api/v1/web/<namespace>/default/sequence_summarize.json
  ```

<br>
<hr>
<br>
Thank you for using the Text Analysis Project on OpenWhisk! If you have any questions or suggestions, feel free to reach out. Happy analyzing!


