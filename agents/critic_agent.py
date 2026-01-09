from utils.evaluation import evaluate_response

class CriticAgent:
    def review(self, answer: str, threshold: float = 0.7):
        score = evaluate_response(answer)
        approved = score >= threshold
        return {
            "score": score,
            "approved": approved
        }
