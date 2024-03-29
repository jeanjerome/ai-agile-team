from crewai import Agent, Task, Process, Crew
from langchain_community.llms import Ollama

# To Load Local models through Ollama
llm_mixtral = Ollama(model="mixtral")
#llm_coder = Ollama(model="codellama:34b")

po = Agent(
    role="Product Owner",
    goal="Ensure the detailed drafting of user stories",
    backstory="""As the Product Owner of an Agile team, you excel at comprehending market demands, identifying the target audience, 
        and analyzing the competition. This expertise is essential for validating if a concept addresses a market need and possesses 
        the potential to captivate a broad audience. You are skilled at devising strategies to appeal to the widest possible audience, 
        ensuring the product aligns with user stories and meets market expectations.
		""",
    verbose=True,
    allow_delegation=False,
    llm=llm_mixtral
)

developer = Agent(
role="Bash Scripting Expert",
goal="Implement the requirements outlined in each user story through coding",
backstory="""You are a master of Bash scripting, with a profound knowledge of Unix-based systems. Your expertise is in writing 
        scripts and also understanding how these scripts can streamline operations, automate mundane tasks, and solve complex technical 
        challenges. With a keen eye for detail and a deep understanding of system architecture, you adeptly craft scripts that enhance 
        productivity and ensure robust system performance. Your ability to decipher and optimize existing scripts, as well as to innovate 
        new solutions, makes you an invaluable asset. Your insights and contributions are key in optimizing workflows, improving operational 
        reliability, and driving technological efficiency.""",
    verbose=True,
    allow_delegation=False,
    llm=llm_mixtral
)

reviewver = Agent(
role="Reviewer",
goal="Review the code to assess the quality, maintainability, and alignment with the team's standards and best practices",
backstory="""You are a guardian of code quality, with a keen understanding of Agile development practices and a sharp eye for detail in code review. 
        Your expertise goes beyond mere code inspection; you are adept at ensuring that developments not only function as intended but also adhere 
        to the team's coding standards, enhance maintainability, and seamlessly integrate with existing systems. With a deep appreciation for 
        collaborative development, you provide constructive feedback, guiding contributors towards best practices and fostering a culture of 
        continuous improvement. Your meticulous approach to reviewing code, coupled with your ability to foresee potential issues and recommend 
        proactive solutions, ensures the delivery of high-quality software that is robust, scalable, and aligned with the team's strategic goals.""",
    verbose=True,
    allow_delegation=True,
    llm=llm_mixtral
)

task1 = Task(
    description="""Develop user stories for a Bash script wrapper function designed to :
        - Execute commands with parameters,
        - Log execution information to a file, 
        - Manage status codes,
        - Output result to stdout when available.
        This tool aims to streamline and automate processes, enhancing operational efficiency and reliability. Your user stories should 
        clearly articulate the needs and expectations of the users, focusing on how they will interact with the wrapper to perform tasks 
        more effectively. Include scenarios covering a range of use cases, from simple command execution to complex workflows involving 
        error handling and output management. Ensure that each user story is detailed, specifying the context, the user's goal, and the
        desired outcome, to guide the development team in creating a solution that meets users' needs.
        These keywords must never be translated and transformed:
        - Action:
        - Thought:
        - Action Input:
        because they are part of the thinking process instead of the output.
        Action Input should be formatted as coworker|task|context.
    """,
    agent=po,
)

task2 = Task(
    description="""Implement the user stories developed by your Product Owner. Your implementation should thoroughly 
    address each user story's requirements, providing a seamless experience for the end-users, focusing on creating a robust and efficient tool. 
    The task involves coding the various operational scenarios described in the provided user stories. You will follow 'the stdout is for output, 
    stderr is for messaging' principal. You ensure your code is clean, well-documented, and adheres to best practices for script development. 
    The final product should be a code formatted in markdown.
    These keywords must never be translated and transformed:
    - Action:
    - Thought:
    - Action Input:
    because they are part of the thinking process instead of the output.
    Action Input should be formatted as coworker|task|context.
    """,
    agent=developer,
)

task3 = Task(
    description="""Ensure the delivery is a code based. Ensure the quality of the code, the adherence to coding standards, and the respect 
    of the specifications included in the user stories. Provide detailed feedback to developers, highlighting areas for improvement, potential 
    bugs, and suggestions for optimization. Your review should include a checklist of criteria that align with best practices in software 
    development and the specific requirements of the project. Ensure that the code is not only functional but also maintainable and scalable. 
    Collaborate with the development team to achieve high-quality software delivery in the project.
    These keywords must never be translated and transformed:
    - Action:
    - Thought:
    - Action Input:
    because they are part of the thinking process instead of the output.
    Action Input should be formatted as coworker|task|context.
    """,
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