from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI

# List, BaseModel, and Field are for advanced use cases I'm developing
from typing import List
from pydantic import BaseModel, Field

# Initialize the callback manager
from langchain_core.callbacks import StdOutCallbackHandler, CallbackManager
callback_manager = CallbackManager([StdOutCallbackHandler()])

""" Testing making base models, need to use output_json or similar for this to be useful, just like in the marketing crew
class CurriculumOutline(BaseModel):
    '''Curriculum outline model'''
    topics: List[str] = Field(..., description="List of topics to be covered")
    resources: List[str] = Field(...,
                                 description="List of suggested resources")


class LessonPlan(BaseModel):
    '''Lesson plan model'''
    title: str = Field(..., description="Title of the lesson")
    objectives: List[str] = Field(...,
                                  description="Learning objectives of the lesson")
    activities: List[str] = Field(...,
                                  description="List of activities for the lesson")
    materials: List[str] = Field(...,
                                 description="Materials needed for the lesson")
"""


@CrewBase
class CurriculumCrew:
    '''Curriculum crew for developing a curriculum'''
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def senior_sme_software_development(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_sme_software_development'],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def senior_sme_artificial_intelligence(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_sme_artificial_intelligence'],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def senior_curriculum_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_curriculum_engineer'],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def lead_curriculum_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['lead_curriculum_engineer'],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def senior_technical_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_technical_writer'],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def senior_instructional_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_instructional_designer'],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def interactive_application_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['interactive_application_developer'],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def assessment_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['assessment_specialist'],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def ai_integration_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['ai_integration_specialist'],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def senior_qa_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_qa_specialist'],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def content_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['content_planner'],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def curriculum_director(self) -> Agent:
        return Agent(
            config=self.agents_config['curriculum_director'],
            verbose=True,
            allow_delegation=True,
        )

    '''
    Tasks could benefit from context and outputs, like so:
    output_json=Copy
    context=[self.software_development(), self.ai_content()]
    '''

    @task
    def software_development(self) -> Task:
        return Task(
            config=self.tasks_config['software_development'],
            agent=self.senior_sme_software_development()
        )

    @task
    def ai_content(self) -> Task:
        return Task(
            config=self.tasks_config['ai_content'],
            agent=self.senior_sme_artificial_intelligence()
        )

    @task
    def curriculum_development(self) -> Task:
        return Task(
            config=self.tasks_config['curriculum_development'],
            agent=self.senior_curriculum_engineer()
        )

    @task
    def curriculum_review(self) -> Task:
        return Task(
            config=self.tasks_config['curriculum_review'],
            agent=self.lead_curriculum_engineer()
        )

    @task
    def technical_documentation(self) -> Task:
        return Task(
            config=self.tasks_config['technical_documentation'],
            agent=self.senior_technical_writer()
        )

    @task
    def instructional_design(self) -> Task:
        return Task(
            config=self.tasks_config['instructional_design'],
            agent=self.senior_instructional_designer()
        )

    @task
    def interactive_apps(self) -> Task:
        return Task(
            config=self.tasks_config['interactive_apps'],
            agent=self.interactive_application_developer()
        )

    @task
    def assessment_development(self) -> Task:
        return Task(
            config=self.tasks_config['assessment_development'],
            agent=self.assessment_specialist()
        )

    @task
    def ai_tools_integration(self) -> Task:
        return Task(
            config=self.tasks_config['ai_tools_integration'],
            agent=self.ai_integration_specialist()
        )

    @task
    def qa_testing(self) -> Task:
        return Task(
            config=self.tasks_config['qa_testing'],
            agent=self.senior_qa_specialist()
        )

    @task
    def content_planning(self) -> Task:
        return Task(
            config=self.tasks_config['content_planning'],
            agent=self.content_planner()
        )

    @task
    def curriculum_management(self) -> Task:
        return Task(
            config=self.tasks_config['curriculum_management'],
            agent=self.curriculum_director()
        )

    @task
    def review_curriculum(self) -> Task:
        return Task(
            config=self.tasks_config['review_curriculum'],
            agent=self.curriculum_director()
        )

    @crew
    def crew(self) -> Crew:
        '''Creates the Curriculum crew'''
        non_manager_agents = [
            self.senior_sme_software_development(),
            self.senior_sme_artificial_intelligence(),
            self.senior_curriculum_engineer(),
            self.lead_curriculum_engineer(),
            self.senior_technical_writer(),
            self.senior_instructional_designer(),
            self.interactive_application_developer(),
            self.assessment_specialist(),
            self.ai_integration_specialist(),
            self.senior_qa_specialist(),
            self.content_planner()
        ]
        return Crew(
            agents=non_manager_agents,
            tasks=self.tasks,  # Automatically created by the @task decorator
            manager_agent=self.curriculum_director(),
            manager_llm=ChatOpenAI(model="gpt-4o", temperature=0.5),
            planning=True,
            planning_llm=ChatOpenAI(model="gpt-4o"),
            process=Process.hierarchical,
            verbose=2,
        )
    """Add memory=True once crewAI fixes windows pathing bug"""
