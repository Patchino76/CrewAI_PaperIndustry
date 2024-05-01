import os
from exa_py import Exa
from langchain.agents import tool

class ExaSearchToolSet:
    
    @tool
    def search(query: str) -> str:
        """Search the web for the given query."""
        return ExaSearchToolSet._init_exa().search(query, use_autoprompt = True, num_results = 3)
    
    @tool
    def find_similar(url: str) -> str:
        """Search for webpages similar to a given URL.
        The url passed in should be a URL returned from `search`.
        """
        return ExaSearchToolSet._init_exa().search(url, use_autoprompt = True, num_results = 3)
    
    @tool
    def get_content(ids: str) -> str:
        """Get the contents of a webpage.
        The ids must be passed in as a list, a list of ids returned from `search`.
        """
        
        ids = eval(ids)
        contents = ExaSearchToolSet._init_exa().get_content(ids)
        contents = contents.split("URL: ")
        contents = [content[:1000] for content in contents]
        return "\n\n".join(contents)
    
    def tools():
        return [ExaSearchToolSet.search, ExaSearchToolSet.find_similar, ExaSearchToolSet.get_content]

    
    
    def _init_exa():
        return Exa(api_key = os.environ.get('EXA_API_KEY'))