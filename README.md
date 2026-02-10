# Fine

This repository contains a minimal AI tutoring system built around a universal prompt designed to support academic learning, critical thinking, and real-world skill development.

## Project Structure

- `ai_system/` - Python package with the core logic and prompt constant.
  - `tutor.py` - Defines `AITutor` and stores the universal AI prompt.
  - `main.py` - Simple CLI entry point to display the prompt.

## Getting Started

1. **Install dependencies** (none for now; plain Python 3 required).
2. Run the tutor using:
   ```bash
   python -m ai_system.main
   ```

   To have the CLI forward the universal prompt to an LLM (OpenAI), set the
   `OPENAI_API_KEY` environment variable or pass `--api-key` and include
   `--ask-llm`:
   ```bash
   export OPENAI_API_KEY="sk-..."
   python -m ai_system.main --ask-llm
   ```

   The project includes a simple `ai_system/llm.py` module that wraps the
   OpenAI SDK.
3. The prompt used by the system is defined in `ai_system/tutor.py` and can be adapted for integration with an LLM.

Feel free to expand this starter project with real AI integrations, analytics, and UI components!
contribution on 2026-02-18T12:00:00
contribution on 2026-02-19T12:00:00
contribution on 2026-02-20T12:00:00
contribution on 2026-02-21T12:00:00
contribution on 2026-02-22T12:00:00
contribution on 2026-02-23T12:00:00
contribution on 2026-02-24T12:00:00
extra commit on 2026-02-01T10:00:00
extra commit on 2026-02-01T16:00:00
extra commit on 2026-02-02T10:00:00
extra commit on 2026-02-02T16:00:00
extra commit on 2026-02-03T10:00:00
extra commit on 2026-02-03T16:00:00
extra commit on 2026-02-04T10:00:00
extra commit on 2026-02-04T16:00:00
extra commit on 2026-02-05T10:00:00
extra commit on 2026-02-05T16:00:00
extra commit on 2026-02-06T10:00:00
extra commit on 2026-02-06T16:00:00
extra commit on 2026-02-07T10:00:00
extra commit on 2026-02-07T16:00:00
extra commit on 2026-02-08T10:00:00
extra commit on 2026-02-08T16:00:00
extra commit on 2026-02-09T10:00:00
extra commit on 2026-02-09T16:00:00
extra commit on 2026-02-10T10:00:00
