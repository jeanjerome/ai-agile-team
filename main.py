from crewai import Agent, Task, Process, Crew
from langchain_community.llms import Ollama

# To Load Local models through Ollama
llm_model = Ollama(model="mixtral")
coding_model = Ollama(model="codellama:34b")

po = Agent(
    role="Product Owner",
    goal="Ensure the detailed drafting of user stories",
    backstory="""As the Product Owner of an Agile team, you excel at comprehending market demands, identifying the target audience, 
        and analyzing the competition. You are skilled at devising strategies to appeal to the widest possible audience, 
        ensuring the product aligns with user stories and meets market expectations.
	""",
    verbose=True,
    allow_delegation=False,
    llm=llm_model
)

developer = Agent(
    role="Bash Scripting Expert",
    goal="Implement the requirements outlined in each user story through coding",
    backstory="""You are a master of Bash scripting, with a profound knowledge of Unix-based systems.""",
    verbose=True,
    allow_delegation=False,
    llm=coding_model
)

reviewver = Agent(
    role="Reviewer",
    goal="Review the code to assess the quality, maintainability, and alignment with state-of-the-art and best practices",
    backstory="""You are a guardian of code quality, with a sharp eye for detail in code review. You are adept at ensuring 
        that developments not only function as intended but also adhere to state-of-the-art-standards. With a deep 
        appreciation for collaborative development, you provide constructive feedback, guiding contributors towards 
        best practices and fostering a culture of continuous improvement.
    """,
    verbose=True,
    allow_delegation=False,
    llm=llm_model
)

task1 = Task(
    description="""Develop user stories for a Bash script wrapper function designed to :
        - Execute commands with parameters,
        - Log execution information to a file, 
        - Manage errors by logging detailed stack trace,
        - Output result to stdout when available.
        This tool aims to enhance operational efficiency and reliability. Your user stories should 
        clearly articulate the needs and expectations of the users, focusing on how they will interact with the wrapper to perform tasks 
        more effectively. Include scenarios covering a range of use cases, from simple command execution to complex workflows involving 
        error handling and output management. Ensure that each user story is detailed, specifying the context, the user's goal, and the
        desired outcome, to guide the development team in creating a solution that meets users' needs.
    """,
    expected_output="a title and a definition of done",
    agent=po,
)

task2 = Task(
    description="""Using the user stories provided, develop a robust and efficient tool. Your code should follow the stdout is for output, 
        the stderr is for messaging principal. You ensure your code is clean, simple, and adheres to best practices for shell script development.
    """,
    expected_output="markdown",
    agent=developer,
)

task3 = Task(
    description="""Ensure the quality of the code, the adherence to the SOLID principals, and the respect 
        of the specifications included in the user stories. Provide detailed feedback to developers, highlighting areas for improvement, potential 
        bugs, and suggestions for optimization. Collaborate with the development team to achieve high-quality software delivery in the project.
    """,
    expected_output="Full report in bullet points",
    agent=reviewver,
)

crew = Crew(
    agents=[po, developer, reviewver],
    tasks=[task1, task2, task3],
    verbose=2,
    process=Process.sequential,
)

result = crew.kickoff()

print("######################")
print(result)