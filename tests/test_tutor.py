"""Basic tests for the AI tutor package."""

import os
import sys
import pytest

# ensure package is importable when tests run from workspace root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai_system.tutor import AITutor, UNIVERSAL_PROMPT
# LLMClient is imported within individual tests to allow monkeypatching


def test_prompt_contains_goal():
    tutor = AITutor()
    prompt = tutor.get_prompt()
    assert "expert education innovator" in prompt
    # the constant should match too
    assert prompt == UNIVERSAL_PROMPT


def test_llm_client_no_key_raises():
    # ensure environment variable not set in this context
    if "OPENAI_API_KEY" in os.environ:
        del os.environ["OPENAI_API_KEY"]
    # import after clearing environment
    from ai_system.llm import LLMClient
    with pytest.raises(ValueError):
        LLMClient()


def test_create_client_integration(monkeypatch):
    # simulate an installed openai module with minimal interface
    class Dummy:
        def __init__(self):
            self.api_key = None
        class ChatCompletion:
            @staticmethod
            def create(model, messages, **kwargs):
                class Choice:
                    message = type("", (), {"content": "dummy response"})
                return type("", (), {"choices": [Choice()]})
        class responses:
            @staticmethod
            def create(model, input, **kwargs):
                # mimic v2 API with output_text attribute
                return type("", (), {"output_text": "dummy response"})
    # ensure ai_system.llm has not yet imported openai by clearing cache
    monkeypatch.setitem(sys.modules, "openai", Dummy())
    # remove any existing import of ai_system.llm so it will re-import our Dummy
    sys.modules.pop("ai_system.llm", None)
    from ai_system.llm import create_client
    client = create_client(api_key="fake")
    out = client.generate("hi")
    assert out == "dummy response"
