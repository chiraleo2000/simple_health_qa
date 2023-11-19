def get_answer_based_on_rule(interpreted_question):
    # Match the question to a set of predefined rules
    answer = 'General health advice.' if interpreted_question['type'] == 'general' else 'Specific information based on the question type.'
    return answer
