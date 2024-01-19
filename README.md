# Semantic Kernel Example

This project is an example for the [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/), which is a system that allows for the execution of various skills or plugins. The kernel is initialized in `app.py` and one plugin, `JobSearchPlugin`, is imported and used.

## JobSearchPlugin

The `JobSearchPlugin` is defined in [plugins/JobSearch.py](plugins/JobSearch.py). It uses the Google Jobs API to search for jobs based on a query. The `search_jobs` method is decorated with `sk_function` and `sk_function_context_parameter` decorators to provide metadata about the function.

## Running the Project

To run the project, execute the `main` function in `app.py`. This will initialize the kernel, import the plugins, and run a job search (using the SerpAPI internally).
