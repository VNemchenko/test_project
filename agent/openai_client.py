"""Wrapper around the OpenAI API."""

from __future__ import annotations

from typing import Iterable

import openai


class OpenAIClient:
    """Simple wrapper for OpenAI API interactions."""

    def __init__(self, api_key: str) -> None:
        openai.api_key = api_key

    def chat(self, messages: Iterable[dict], model: str = "gpt-4", **kwargs) -> str:
        """Send chat completion request and return the reply content."""
        response = openai.ChatCompletion.create(model=model, messages=list(messages), **kwargs)
        return response["choices"][0]["message"]["content"]

