# GitLab OpenAI Agent

This project provides a basic framework for building an automation agent that
integrates GitLab with the OpenAI API. The agent can analyze repositories,
propose fixes, and generate summaries or new code.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a configuration JSON file or set environment variables `OPENAI_API_KEY`
and `GITLAB_TOKEN`. Example `config.json`:

```json
{
  "openai_api_key": "sk-...",
  "gitlab_token": "glpat-...",
  "gitlab_url": "https://gitlab.com"
}
```

## Usage

Run the agent from the command line:

```bash
python main.py <project-id-or-path> --config config.json
```

This will produce an OpenAI-generated summary of the specified GitLab project.

