"""Simple CLI to run the AI tutor system."""

import argparse
import sys

from .tutor import AITutor
from .llm import create_client, LLMClient


def main():
    parser = argparse.ArgumentParser(
        description="Run the AI tutor. Optionally forward the universal prompt to an LLM."
    )
    parser.add_argument(
        "--ask-llm",
        action="store_true",
        help="Send the universal prompt to the configured LLM and print the result",
    )
    parser.add_argument(
        "--api-key",
        help="OpenAI API key (overrides OPENAI_API_KEY env var)",
    )

    args = parser.parse_args()

    tutor = AITutor()
    tutor.start()

    if args.ask_llm:
        try:
            client: LLMClient = create_client(api_key=args.api_key)
            print("\nSending prompt to LLM...")
            result = client.generate(tutor.get_prompt())
            print("\nLLM response:\n")
            print(result)
        except Exception as exc:  # pragma: no cover - best-effort
            print(f"Failed to contact LLM: {exc}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
