# %%
import os
from dotenv import load_dotenv
from crewai import Crew
from tasks import ReportingTasks
from agents import ReportingAgents
from crewai.process import Process
from uuid import uuid4
from inputs import task_inputs

# %%

load_dotenv()

unique_id = uuid4().hex[0:8]
os.environ["LANGCHAIN_PROJECT"] = f"Tracing Walkthrough - {unique_id}"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"


# %% create agents
tasks = ReportingTasks()
agents = ReportingAgents()

research_agent = agents.research_agent()
industry_analysis_agent = agents.industry_analysis_agent()
writer_agent = agents.writer_agent()
translation_agent = agents.translator_agent()



# %% create tasks
research_task = tasks.research_task(agent=research_agent)

industry_analysis_task = tasks.industry_analysis_task(
  agent=industry_analysis_agent,
  context=[research_task],
)


reporting_task = tasks.reporting_task(
  agent=writer_agent,
  context=[industry_analysis_task],
)

translation_task = tasks.translation_task(
  agent=translation_agent,
  context=[reporting_task],
)


# %%
crew = Crew(
  agents=[research_agent, industry_analysis_agent, writer_agent, translation_agent],
  tasks=[research_task, industry_analysis_task, reporting_task, translation_task],
  process = Process.sequential,
  verbose=2,
  max_rpm=29,
)

result = crew.kickoff()
# %%
print(result)
# %%
