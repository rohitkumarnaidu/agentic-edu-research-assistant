from utils.llm_provider import get_llm_provider
from utils.domain_contexts import apply_domain_rules

class ReasoningAgent:
    def reason(self, research_text: str, domain: str) -> str:
        llm = get_llm_provider()
        explanation = llm.generate(
            f"Explain clearly based on the following research:\n{research_text}"
        )
        return apply_domain_rules(domain, explanation)
