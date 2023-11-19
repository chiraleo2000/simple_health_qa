
from .biogpt_handler import BioGPTHandler
from .question_interpreter import interpret_question

def generate_answer(question):
    interpreted_question = interpret_question(question)
    biogpt_handler = BioGPTHandler()
    return biogpt_handler.generate_answer(interpreted_question['content'])
