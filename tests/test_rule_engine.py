import unittest
from src.rule_engine import get_answer_based_on_rule

class TestRuleEngine(unittest.TestCase):
    def test_rule_matching(self):
        interpreted_question = {'type': 'general', 'content': 'Sample question'}
        answer = get_answer_based_on_rule(interpreted_question)
        self.assertNotEqual(answer, '')

if __name__ == '__main__':
    unittest.main()
