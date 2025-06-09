"""High-level actions performed by the agent."""

from __future__ import annotations

from typing import Iterable

from .openai_client import OpenAIClient
from .gitlab_client import GitLabClient


class AgentActions:
    """Collection of operations that combine GitLab and OpenAI."""

    def __init__(self, openai_client: OpenAIClient, gitlab_client: GitLabClient) -> None:
        self.openai = openai_client
        self.gitlab = gitlab_client

    def summarize_project(self, project_id: str | int) -> str:
        """Generate a summary of a GitLab project using OpenAI."""
        project = self.gitlab.get_project(project_id)
        messages = [
            {"role": "system", "content": "You are a coding assistant."},
            {"role": "user", "content": f"Summarize the GitLab project: {project.path_with_namespace}"},
        ]
        return self.openai.chat(messages)

