"""Configuration utilities for the agent."""

from dataclasses import dataclass
from pathlib import Path
import json
import os


@dataclass
class AgentConfig:
    """Configuration parameters for the agent."""

    openai_api_key: str
    gitlab_token: str
    gitlab_url: str = "https://gitlab.com"

    @classmethod
    def load(cls, path: str | Path | None = None) -> "AgentConfig":
        """Load configuration from a JSON file or environment variables."""
        data = {}
        if path:
            with open(path) as fh:
                data = json.load(fh)
        return cls(
            openai_api_key=data.get("openai_api_key") or os.getenv("OPENAI_API_KEY", ""),
            gitlab_token=data.get("gitlab_token") or os.getenv("GITLAB_TOKEN", ""),
            gitlab_url=data.get("gitlab_url") or os.getenv("GITLAB_URL", "https://gitlab.com"),
        )

