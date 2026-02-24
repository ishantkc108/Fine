"""Simple wrapper around an LLM provider such as OpenAI."""

import os
from typing import Optional

try:
    import openai
except ImportError:  # pragma: no cover - runtime dependency
    openai = None  # type: ignore


# helper to check which interface is available

def _uses_chat_completion() -> bool:
    return hasattr(openai, "ChatCompletion") and not hasattr(openai, "responses")



class LLMClient:
    """Basic client for generating responses from an LLM.

    Currently supports OpenAI via the `openai` package. Additional providers
    can be added later as needed.
    """

    def __init__(self, api_key: Optional[str] = None):
        if api_key is None:
            api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("No API key provided for LLM client")
        if openai is None:
            raise RuntimeError("The `openai` package is not installed")
        openai.api_key = api_key
        self._client = openai

    def generate(self, prompt: str, **kwargs) -> str:
        """Generate text from the model using a prompt.

        This method supports both legacy `ChatCompletion` (pre‑v1) and the newer
        `responses` interface. Extra keyword arguments are passed along to the
        underlying call (model, temperature, etc.).
        """
        # choose API depending on what's available
        if hasattr(self._client, "ChatCompletion"):
            response = self._client.ChatCompletion.create(
                model=kwargs.pop("model", "gpt-4o"),
                messages=[{"role": "user", "content": prompt}],
                **kwargs,
            )
            # extract text from the first choice
            return response.choices[0].message.content.strip()
        elif hasattr(self._client, "responses"):
            response = self._client.responses.create(
                model=kwargs.pop("model", "gpt-4o"),
                input=prompt,
                **kwargs,
            )
            # `output_text` is a convenience property that concatenates
            # textual output, but fall back to digging into `response.output` if
            # it's not present.
            if hasattr(response, "output_text"):
                return response.output_text
            # navigate nested structure for older versions of the v2 API
            try:
                return response.output[0].content[0].text
            except Exception:  # pragma: no cover - defensive
                return str(response)
        else:
            raise RuntimeError("No supported generation interface available")


# convenience helper

def create_client(api_key: Optional[str] = None) -> LLMClient:
    return LLMClient(api_key=api_key)
