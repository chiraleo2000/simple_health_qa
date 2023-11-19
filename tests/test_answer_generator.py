import unittest
from src.answer_generator import generate_answer

class TestAnswerGenerator(unittest.TestCase):
    def test_answer_generation(self):
        question = 'How to treat a headache?'
        answer = generate_answer(question)
        self.assertIsInstance(answer, str)

if __name__ == '__main__':
    unittest.main()
