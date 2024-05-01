from textwrap import dedent
from crewai import Task

class ReportingTasks():
    def research_task(self, agent, description, file_name = None):
        return Task(
            description=description,
            expected_output=dedent("""\
                A list of at lease 5 urls containing PDF files or articlesrelated to the task description. Ensure the PDF files
                do exist on the URL and the articles are readable and complete.
                Example Output:
                [
                    'url': 'https://example.com/ai-news1/file.pdf', 
                    'url': 'https://example.com/ai-news2/file.pdf', 
                    'url': 'https://example.com/ai-news3', 
                    'url': 'https://example.com/ai-news4', 
                    'url': 'https://example.com/ai-news5', 
                ]
                """),
            agent=agent,
            async_execution=False,
            output_file=f"output/{file_name}"
        )
    def industry_analysis_task(self, agent,  context, file_name=None):
        return Task(
			description=dedent("""
				Analyze strictly each PDF file or article using the provided web and pdf search tools.
                Use information only form the extracted urls or PDF files to generate an analysis.
            """),
			expected_output=dedent("""
				A well formated detailed analysis for each news story or article. Your output should be long and as reach as possible,
                while capturing all relevant information from the sources you are analysing.
            """),
			async_execution=False,
			agent=agent,
            context = context,
            output_file=f"output/{file_name}"
        )
        
    def reporting_task(self, agent,  context, file_name=None):
        return Task(
			description=dedent("""
				A complete report on the provided contextual material.
            """),
			expected_output=dedent("""
				A well written article with technical and business information on the subject.
            """),
			async_execution=False,
			agent=agent,
            context = context,
            output_file=f"output/{file_name}",
        )
        

    
    