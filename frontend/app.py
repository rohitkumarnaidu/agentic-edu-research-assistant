import sys
import os
import streamlit as st

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agents.reasoning_agent import ReasoningAgent
from agents.critic_agent import CriticAgent


st.set_page_config(page_title="Agentic Edu Research Assistant")

st.title("Autonomous Multi-Agent Research Scientist")

query = st.text_area("Enter your learning question:")
domain = st.selectbox("Domain", ["Education", "Healthcare", "Agriculture"])

if st.button("Run Agents") and query:
    planner = PlannerAgent()
    research = ResearchAgent()
    reasoning = ReasoningAgent()
    critic = CriticAgent()

    plan = planner.plan(query)
    st.subheader("Planner Agent")
    st.write(plan)

    research_output = research.research(plan, query)
    st.subheader("Research Agent")
    st.write(research_output)

    reasoning_output = reasoning.reason(research_output, domain)
    st.subheader("Reasoning Agent")
    st.write(reasoning_output)

    review = critic.review(reasoning_output)
    st.subheader("Critic Agent")
    st.write(f"Score: {review['score']}")

    if review["approved"]:
        st.success("Final Output Approved")
    else:
        st.warning("Refinement Needed (loop back to planner)")
