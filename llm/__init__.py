# example
import os
from llm.openai_wrapper import call_openai
from llm.anthropic_wrapper import call_anthropic

SUPPORTED_PROVIDERS = ["openai", "anthropic"]
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai").lower()


def call_llm(prompt, model=None, temperature=0.7, max_tokens=1024):
    if LLM_PROVIDER not in SUPPORTED_PROVIDERS:
        raise ValueError(f"Unsupported LLM provider: {LLM_PROVIDER}")

    if LLM_PROVIDER == "openai":
        return call_openai(prompt, model or "gpt-4", temperature, max_tokens)
    elif LLM_PROVIDER == "anthropic":
        return call_anthropic(prompt, model or "claude-3-opus-20240229", temperature, max_tokens)

    raise NotImplementedError(f"Provider not implemented: {LLM_PROVIDER}")