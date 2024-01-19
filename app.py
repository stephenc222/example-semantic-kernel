from dotenv import load_dotenv
import semantic_kernel as sk
from plugins.JobSearch import JobSearchPlugin

load_dotenv()


async def main():
    # Initialize the kernel
    kernel = sk.Kernel()

    # Import the JobSearchPlugin
    jobs_plugin = kernel.import_skill(
        JobSearchPlugin(), skill_name="JobSearchPlugin")

    # Run the SearchJobs function with the context
    result = await kernel.run_async(
        jobs_plugin["SearchJobs"],
        input_str="software engineer, Spain",
    )

    print("Job Search Results:", result)

# Run the main function
if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
