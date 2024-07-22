from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

'''List, BaseModel, and Field are for advanced use cases I'm developing'''
from typing import List
from pydantic import BaseModel, Field


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

    '''
    Tasks could benefit from context and outputs, like so:
    output_json=Copy
    context=[self.task_software_development(), self.task_ai_content()]
    '''

    @task
    def task_software_development(self) -> Task:
        return Task(
            config=self.tasks_config['task_software_development'],
            agent=self.senior_sme_software_development()
        )

    @task
    def task_ai_content(self) -> Task:
        return Task(
            config=self.tasks_config['task_ai_content'],
            agent=self.senior_sme_artificial_intelligence()
        )

    @task
    def task_curriculum_development(self) -> Task:
        return Task(
            config=self.tasks_config['task_curriculum_development'],
            agent=self.senior_curriculum_engineer()
        )

    @task
    def task_curriculum_review(self) -> Task:
        return Task(
            config=self.tasks_config['task_curriculum_review'],
            agent=self.lead_curriculum_engineer()
        )

    @task
    def task_technical_documentation(self) -> Task:
        return Task(
            config=self.tasks_config['task_technical_documentation'],
            agent=self.senior_technical_writer()
        )

    @task
    def task_instructional_design(self) -> Task:
        return Task(
            config=self.tasks_config['task_instructional_design'],
            agent=self.senior_instructional_designer()
        )

    @task
    def task_interactive_apps(self) -> Task:
        return Task(
            config=self.tasks_config['task_interactive_apps'],
            agent=self.interactive_application_developer()
        )

    @task
    def task_assessment_development(self) -> Task:
        return Task(
            config=self.tasks_config['task_assessment_development'],
            agent=self.assessment_specialist()
        )

    @task
    def task_ai_tools_integration(self) -> Task:
        return Task(
            config=self.tasks_config['task_ai_tools_integration'],
            agent=self.ai_integration_specialist()
        )

    @task
    def task_qa_testing(self) -> Task:
        return Task(
            config=self.tasks_config['task_qa_testing'],
            agent=self.senior_qa_specialist()
        )

    @crew
    def crew(self) -> Crew:
        '''Creates the Curriculum crew'''
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=2,
        )
    """Add memory=True once crewAI fixes windows pathing bug"""
