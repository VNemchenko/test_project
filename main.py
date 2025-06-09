"""Command-line interface for the agent."""

from __future__ import annotations

import argparse

from agent import AgentConfig, OpenAIClient, GitLabClient, AgentActions


def main() -> None:
    parser = argparse.ArgumentParser(description="GitLab automation agent")
    parser.add_argument("project", help="GitLab project ID or path")
    parser.add_argument("--config", help="Path to config JSON file")
    args = parser.parse_args()

    config = AgentConfig.load(args.config)
    openai_client = OpenAIClient(config.openai_api_key)
    gitlab_client = GitLabClient(config.gitlab_token, config.gitlab_url)
    actions = AgentActions(openai_client, gitlab_client)

    summary = actions.summarize_project(args.project)
    print(summary)


if __name__ == "__main__":
    main()

