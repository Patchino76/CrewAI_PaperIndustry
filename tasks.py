from textwrap import dedent
from crewai import Task

class ReportingTasks():
    def research_task(self, agent, description):
        return Task(
            description=description,
            expected_output=dedent("""\
                A list of  detailed articles related to the task description.
                Example Output:
                [
                    {'title': 'Top AI News Articles', 
                    'url': 'https://example.com/ai-news', 
                    'description': 'The detailed description of the article'},
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
        
    def reporting_task(self, agent,  context, file_name):
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
            context = context,
            output_file=f"output/{file_name}.txt",
        )
        
    # def translation_task(self, agent,  context):
    #     return Task(
	# 		description=dedent("""
	# 			A complete translation of the provided context from English to Bulgarian language.
    #         """),
	# 		expected_output=dedent("""
	# 			A well formated detailed report in Bulgarian language.
    #         """),
	# 		async_execution=False,
	# 		agent=agent,
    #         context = context
    #     )
    
    