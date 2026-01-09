DOMAIN_RULES = {
    "education": "Explain concepts clearly with examples.",
    "healthcare": "Do NOT provide diagnosis or treatment.",
    "agriculture": "Provide best practices, not prescriptions."
}


def apply_domain_rules(domain: str, text: str) -> str:
    rule = DOMAIN_RULES.get(domain.lower())
    if rule:
        return f"{text}\n\n[Domain Rule Applied]: {rule}"
    return text
