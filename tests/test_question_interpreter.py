import unittest
from src.question_interpreter import interpret_question

class TestQuestionInterpreter(unittest.TestCase):
    def test_interpretation(self):
        question = 'What are the symptoms of a cold?'
        result = interpret_question(question)
        self.assertEqual(result['type'], 'general')

if __name__ == '__main__':
    unittest.main()
