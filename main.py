# %%
import os
from dotenv import load_dotenv
from crewai import Crew
from tasks import ReportingTasks
from agents import ReportingAgents
from crewai.process import Process
from uuid import uuid4
from inputs.task_inputs import task_inputs

# %%

load_dotenv()

unique_id = uuid4().hex[0:8]
os.environ["LANGCHAIN_PROJECT"] = f"Tracing Walkthrough - {unique_id}"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"


# %% create agents

agents = ReportingAgents()

research_agent = agents.research_agent()
industry_analysis_agent = agents.industry_analysis_agent()
writer_agent = agents.writer_agent()
translation_agent = agents.translator_agent()


# %% create tasks
tasks = ReportingTasks()
research_tasks = []
industry_analysis_tasks = []
reporting_tasks = []

inputs = task_inputs
counter = 1
for task in inputs:
  description = "Conduct a web-based research on the topic: " + task["task"] + ". Focus on: " + task["description"]
  research_task = tasks.research_task(agent=research_agent, description=description)
  
  industry_analysis_task = tasks.industry_analysis_task(
    agent=industry_analysis_agent,
    context=[research_task],
  )
  reporting_task = tasks.reporting_task(
    agent=writer_agent,
    context=[industry_analysis_task],
    file_name=f"{counter}:  {task["task"]}",
  )
  
  research_tasks.append(research_task)
  industry_analysis_tasks.append(industry_analysis_task)
  reporting_tasks.append(reporting_task)
  counter+=1



# # %%
crew = Crew(
  agents=[research_agent, industry_analysis_agent, writer_agent, translation_agent],
  tasks=[*research_tasks, *industry_analysis_tasks, *reporting_tasks],
  process = Process.sequential,
  verbose=2,
  max_rpm=29,
)

result = crew.kickoff()
# %%
# print(result)
# %%
