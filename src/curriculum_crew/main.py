#!/usr/bin/env python
import sys
from curriculum_crew.crew import CurriculumCrew

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI in healthcare'
    }
    CurriculumCrew().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'topic': 'AI in healthcare'
    }
    try:
        CurriculumCrew().crew().train(
            n_iterations=int(sys.argv[1]), inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")