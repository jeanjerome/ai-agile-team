# AI-Driven Agile Team

This Python project demonstrates an innovative approach to collaborative development using AI-driven agents. By leveraging the `crewai` library alongside the `langchain_community.llms` module, the project showcases how different roles within a software development team can be simulated and automated to perform tasks such as drafting user stories, coding, and code review.

## Features

- **AI-Driven Agents**: Utilizes `crewai` to create agents with specific roles and goals, including a Product Owner, Bash Scripting Expert, and Reviewer.
- **Language Model Integration**: Leverages `Ollama` from `langchain_community.llms` to load `Mixtral-8x7B` local models, enabling sophisticated language understanding and generation capabilities.
- **Collaborative Task Management**: Demonstrates how these agents can work together as an Agile team, following a sequential process to ***Define*** user stories, ***Build*** implementation and ***Review*** code.

## Installation

1. Ensure you have Python 3.11+ installed on your system:

```bash
conda create -n ai-agile-team python=3.11 -y
conda activate ai-agile-team
```

2. Install Ollama and Mixtral-8x7B model

    - First install Ollama, see: [https://ollama.com/download](https://ollama.com/download)
    - Then install Mixtral-8x7B model, run: `ollama run mixtral`

2. Then, clone this repository and install the required dependencies:

```bash
git clone https://github.com/jeanjerome/ai-agile-team.git
cd ai-agile-team
pip install -r requirements.txt
```

## Usage

To run the project and see the AI-driven development process in action:

```bash
conda activate ai-agile-team
python main.py
```

## Dependencies

- `crewai`: A library for creating and managing AI agents in collaborative tasks.
- `langchain_community.llms`: Provides access to language models like `Ollama` for natural language understanding and generation.

## Contributing

We welcome contributions! If you have ideas for new features or improvements, please open an issue or submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE.md).
