# Design-level only (no runtime DB required)

class UserQuery:
    def __init__(self, query: str):
        self.query = query


class AgentOutput:
    def __init__(self, agent: str, output: str):
        self.agent = agent
        self.output = output
