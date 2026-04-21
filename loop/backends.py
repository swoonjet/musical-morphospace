"""LLM backends for field-note generation.

Three backends, selectable via --backend CLI flag or BACKEND env var:

  offline  — writes the filled prompt to a file, does not call any LLM.
             Use this when you want to paste into Claude.ai / Workbench manually.
  claude   — calls the Anthropic API directly via the `anthropic` SDK.
             Requires ANTHROPIC_API_KEY env var.
  ollama   — calls a local Ollama instance at http://localhost:11434.
             Requires an Ollama server running and a pulled model.

The returned field-note text is a markdown document that engine.py can parse
for its ```json audio spec block.
"""

import os
import sys
from pathlib import Path
from typing import Optional


class Backend:
    """Abstract LLM backend interface."""

    name: str = "base"

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        """Return the generated field-note markdown."""
        raise NotImplementedError


class OfflineBackend(Backend):
    """Writes the filled prompt to disk; does not call an LLM.

    Useful when no API key is configured. The caller is expected to paste
    the prompt into Claude.ai or similar and save the response back to
    the expedition folder as `field_notes.md`.
    """

    name = "offline"

    def __init__(self, output_path: Path):
        self.output_path = output_path

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        body = (
            "# System prompt\n\n"
            + system_prompt
            + "\n\n---\n\n# User prompt\n\n"
            + user_prompt
        )
        self.output_path.write_text(body)
        print(f"[offline] wrote prompt to {self.output_path}", file=sys.stderr)
        print("[offline] paste into your LLM of choice, save response as field_notes.md", file=sys.stderr)
        # Return an empty placeholder so downstream steps can short-circuit
        return ""


class ClaudeAPIBackend(Backend):
    """Calls the Anthropic Claude API."""

    name = "claude"

    def __init__(self, model: str = "claude-opus-4-7", max_tokens: int = 4096):
        try:
            import anthropic  # type: ignore
        except ImportError as e:
            raise RuntimeError(
                "anthropic SDK not installed. Run: pip install --user --break-system-packages anthropic"
            ) from e
        if not os.environ.get("ANTHROPIC_API_KEY"):
            raise RuntimeError(
                "ANTHROPIC_API_KEY env var not set. "
                "Get a key at https://console.anthropic.com/ and: export ANTHROPIC_API_KEY=sk-ant-..."
            )
        self.client = anthropic.Anthropic()
        self.model = model
        self.max_tokens = max_tokens

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        print(f"[claude] calling {self.model}...", file=sys.stderr)
        msg = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )
        text = "".join(block.text for block in msg.content if hasattr(block, "text"))
        print(f"[claude] received {len(text)} chars ({msg.usage.output_tokens} output tokens)", file=sys.stderr)
        return text


class OllamaBackend(Backend):
    """Calls a local Ollama server."""

    name = "ollama"

    def __init__(self, model: str = "mistral:latest", host: str = "http://localhost:11434"):
        try:
            import requests  # type: ignore
        except ImportError as e:
            raise RuntimeError(
                "requests not installed. Run: pip install --user --break-system-packages requests"
            ) from e
        self.requests = requests
        self.model = model
        self.host = host

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        print(f"[ollama] calling {self.model} at {self.host}...", file=sys.stderr)
        resp = self.requests.post(
            f"{self.host}/api/chat",
            json={
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                "stream": False,
                "options": {"temperature": 0.7, "num_ctx": 16384},
            },
            timeout=600,
        )
        resp.raise_for_status()
        data = resp.json()
        text = data["message"]["content"]
        print(f"[ollama] received {len(text)} chars", file=sys.stderr)
        return text


def make_backend(name: str, expedition_dir: Path) -> Backend:
    """Factory — construct a backend by name."""
    if name == "offline":
        return OfflineBackend(expedition_dir / "prompt.md")
    if name == "claude":
        return ClaudeAPIBackend()
    if name == "ollama":
        return OllamaBackend(model=os.environ.get("OLLAMA_MODEL", "mistral:latest"))
    raise ValueError(f"Unknown backend: {name!r}. Choose: offline, claude, ollama.")
