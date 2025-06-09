"""Utilities for interacting with GitLab."""

from __future__ import annotations

import gitlab
from gitlab.v4.objects import Project


class GitLabClient:
    """Wrapper around python-gitlab."""

    def __init__(self, token: str, url: str = "https://gitlab.com") -> None:
        self.gl = gitlab.Gitlab(url, private_token=token)

    def get_project(self, project_id: str | int) -> Project:
        """Fetch a GitLab project."""
        return self.gl.projects.get(project_id)

