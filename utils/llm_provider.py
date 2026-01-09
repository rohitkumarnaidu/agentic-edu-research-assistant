# utils/llm_provider.py

import os
from abc import ABC, abstractmethod

try:
    from google import genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False


class BaseLLMProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass


class MockLLMProvider(BaseLLMProvider):
    """
    Zero-cost default provider.
    Safe fallback when no API key is available.
    """

    def generate(self, prompt: str) -> str:
        return (
            "MOCK RESPONSE (Zero-cost mode)\n\n"
            f"Prompt:\n{prompt}\n\n"
            "This response simulates an LLM output."
        )


class GeminiProvider(BaseLLMProvider):
    """
    Gemini provider using official google-genai SDK.
    Activated only if GOOGLE_API_KEY is set.
    """

    def __init__(self, api_key: str):
        if not GEMINI_AVAILABLE:
            raise RuntimeError("google-genai is not installed")

        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return response.text


def get_llm_provider() -> BaseLLMProvider:
    api_key = os.getenv("GOOGLE_API_KEY")

    if api_key and GEMINI_AVAILABLE:
        try:
            return GeminiProvider(api_key)
        except Exception:
            pass

    return MockLLMProvider()
