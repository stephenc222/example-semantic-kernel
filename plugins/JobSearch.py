import os
from serpapi import search as GoogleSearch
from semantic_kernel.skill_definition import (
    sk_function,
    sk_function_context_parameter,
)


class JobSearchPlugin:
    # optionally pass the api_key directly or set it in the environment variables
    def __init__(self, api_key: str = None):
        # get environment variable SERPAPI_API_KEY if not passed
        self.api_key = api_key or os.getenv("SERPAPI_API_KEY")

    @sk_function(
        description="Searches for jobs using Google Jobs API",
        name="SearchJobs",
    )
    @sk_function_context_parameter(
        name="query",
        description="The input search query, e.g., 'barista new york'",
    )
    def search_jobs(self, query: str) -> str:
        params = {
            "engine": "google_jobs",
            "q": query,
            "hl": "en",
            "api_key": self.api_key
        }

        search = GoogleSearch(params)
        jobs_results = search.get("jobs_results", [])

        if not jobs_results:
            return "No job results found."

        # Process and format the results for output
        formatted_results = [
            f"{job['title']} at {job['company_name']}" for job in jobs_results]
        return '\n'.join(formatted_results)
