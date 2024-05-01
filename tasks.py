from textwrap import dedent
from crewai import Task

class ReportingTasks():
    def research_task(self, agent):
        return Task(
            description=dedent("""\
                Conduct a web-based research focusing on the integration of AI and ML in the industrial manufacturing processes, 
                specifically within the pulp and paper industry. This includes exploring the application of digital twins for 
                real-time simulation and optimization, proactive maintenance strategies to prevent downtime, and the use of 
                Bayesian inference, machine learning, and deep learning techniques for process optimization. Investigate how 
                ML systems can recommend the best setpoints to PLCs (Programmable Logic Controllers) and SCADA (Supervisory Control 
                and Data Acquisition) systems to achieve optimum quality and energy efficiency. Gather information on recent 
                news, achievements, professional backgrounds, and any relevant information about these advanced technologies 
                and their impact on production process optimization and improvement.
                """),
            expected_output=dedent("""\
                A list of the top AI news articles related to the pulp and paper industry including a
                summary for each of them.
                Example Output:
                [
                    {'title': 'Top AI News Articles', 
                    'url': 'https://example.com/ai-news', 
                    'summary': 'Summary of the article'},
                    {{...}}
                ]
                """),
            agent=agent,
            async_execution=False
        )
    def industry_analysis_task(self, agent,  context):
        return Task(
			description=dedent("""
				Analyze each news, story or article and ensure there are at least
                5 well formated articles on the subject of process optimization, proactive maintenace, 
                and digital twins.
            """),
			expected_output=dedent("""
				A well formated detailed analysis for each news story or article.
            """),
			async_execution=False,
			agent=agent,
            context = context
        )
        
    def reporting_task(self, agent,  context):
        return Task(
			description=dedent("""
				A complete report on the process optimization sith AI, proactive maintenace, and digital twins
                in the pulp and paper industry.
            """),
			expected_output=dedent("""
				A well formated detailed report with recommendations and descriptions
                for each news story or article.
            """),
			async_execution=False,
			agent=agent,
            context = context
        )
        
    def translation_task(self, agent,  context):
        return Task(
			description=dedent("""
				A complete translation of the provided context from English to Bulgarian language.
            """),
			expected_output=dedent("""
				A well formated detailed report in Bulgarian language.
            """),
			async_execution=False,
			agent=agent,
            context = context
        )
    
    