from textwrap import dedent
from crewai import Agent
from tools import ExaSearchToolSet
import os
from langchain_groq import ChatGroq
from langchain_community.chat_models import ChatOllama
from crewai_tools import SerperDevTool, WebsiteSearchTool, ScrapeWebsiteTool, PDFSearchTool


class ReportingAgents:
    search_tool = SerperDevTool(n_results=1)
    web_search_tool = WebsiteSearchTool()
    scrape_tool = ScrapeWebsiteTool()
    pdf_search_tool = PDFSearchTool()
    def __init__(self):
        
        self.llm =ChatGroq(
            api_key = os.getenv("GROQ_API_KEY"),
            model = "llama3-70b-8192" 
            # model = "mixtral-8x7b-32768",
        )
        self.llm_bg = ChatOllama(
            model = "tazarov/bg-gpt",
        )

    def research_agent(self):
        return Agent(
            role="Research Specialist",
            goal="Fetch the top news, stories and articled about AI and ML advancement in the manufacturing industry and process optimization.", 
            tools=[self.search_tool],
            backstory=dedent(
                """\
                As a digital sleuth, you scour the internet for information for the latest and
                most impactful developments in the world of AI and manufacturing industry."""
            ),
            verbose=True,
            llm = self.llm,
            max_iter=5,
            
        )

    def industry_analysis_agent(self):
        return Agent(
            role="Industry Analyst",
            goal="""Identify and implement AI-driven strategies for optimizing manufacturing processes, focusing on efficiency, productivity, and innovation.
            You can extract content from web urls using the web_search tool.""",
            tools=[self.web_search_tool, self.pdf_search_tool],
            backstory=dedent(
                """\
                With a keen analytical mind, this agent dives deep into the complexities of manufacturing processes. 
                It leverages AI to uncover inefficiencies, propose solutions, and drive forward the future of smart manufacturing."""
            ),
            verbose=True,
            llm = self.llm,
            max_iter=2,
            allow_delegation=True
        )


    def writer_agent(self):
        return Agent(
            role="Writer",
            goal="Transform insights from the Industry Analyst into compelling articles, detailed reports, and actionable recommendations.",
            backstory=dedent(
                """\
                Armed with a flair for storytelling and a deep understanding of AI's impact on manufacturing, 
                this agent crafts narratives that not only inform but also inspire action towards smarter, more efficient processes."""
            ),
            verbose=True,
            llm = self.llm,
            max_iter=2,
            allow_delegation=True
        )
    def translator_agent(self):
        return Agent(
            role="Translator EN-BG",
            goal="Provide high-quality translations from English to Bulgarian, ensuring accurate conveyance of technical and industry-specific terms.",
            backstory=dedent(
                """\
                This agent excels in linguistic precision and cultural nuance, bridging the gap between English and Bulgarian speakers. 
                With a deep understanding of both languages and the manufacturing sector, it ensures that every translation is both accurate and contextually relevant."""
            ),
            verbose=True,
            llm=self.llm_bg, 
            max_iter=15,
            allow_delegation=True
        )