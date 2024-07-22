
# AI Crew for Software Development Curriculum
## Introduction
This project demonstrates the use of the CrewAI framework to automate the creation of software dev curriculum and programs. CrewAI orchestrates autonomous AI agents, enabling them to collaborate and execute complex tasks efficiently.

By [@joaomdmoura](https://x.com/joaomdmoura)

- [CrewAI Framework](#crewai-framework)
- [Running the script](#running-the-script)
- [Details & Explanation](#details--explanation)
- [Contributing](#contributing)
- [Support and Contact](#support-and-contact)
- [License](#license)

## CrewAI Framework
CrewAI is designed to facilitate the collaboration of role-playing AI agents. This is a modified and enhanced version of a marketing example that crewAI provided, repurposed and replaced with curriculum engineers and other agents. Over time, tools and refinements will be developed to further improve performance.

## Running the Script
It uses GPT-4o by default so you should have access to that to run it.

***Disclaimer:** This will use gpt-4o unless you change it to use a different model, and by doing so it may incur in different costs.*

- **Configure Environment**: Set up the environment variables in .env for [OpenAI](https://platform.openai.com/api-keys) and other tools as needed, like [Serper](serper.dev).
- **Install Dependencies**: Run `poetry lock && poetry install`.
- **Customize**: Modify `src/curriculum_crew/main.py` to add custom inputs for your agents and tasks.
- **Customize Further**: Check `src/curriculum_crew/config/agents.yaml` to update your agents and `src/curriculum_crew/config/tasks.yaml` to update your tasks.
- **Execute the Script**: Run `poetry run curriculum_crew` and input your project details.

## Details & Explanation
- **Running the Script**: Execute `poetry run curriculum_crew`. The script will leverage the CrewAI framework to generate quality curriculum for university programs to use as a basis for human review and modification.
- **Key Components**:
  - `src/curriculum_crew/main.py`: Main script file.
  - `src/curriculum_crew/crew.py`: Main crew file where agents and tasks come together, and the main logic is executed.
  - `src/curriculum_crew/config/agents.yaml`: Configuration file for defining agents.
  - `src/curriculum_crew/config/tasks.yaml`: Configuration file for defining tasks.
  - `src/curriculum_crew/tools`: Contains tool classes used by the agents.

## License
This project is released under the MIT License.
