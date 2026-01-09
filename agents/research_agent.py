from utils.llm_provider import get_llm_provider

class ResearchAgent:
    def research(self, plan: str, query: str) -> str:
        llm = get_llm_provider()
        prompt = f"Research the topic based on plan:\n{plan}\n\nQuery:\n{query}"
        return llm.generate(prompt)
