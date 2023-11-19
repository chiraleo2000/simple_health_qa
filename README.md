# Simple Health Q&A Project

## Project Overview

The Simple Health Q&A Project is a Python-based application designed to answer health-related questions using a rule-based system and the Microsoft/BioGPT-Large model from Hugging Face. It interprets user queries about health and medicine and provides answers based on predefined rules or by generating responses using BioGPT.

## Features

- **Question Interpreter**: Analyzes the user's question to understand the context.
- **Rule Engine**: Applies predefined rules for common health-related questions, particularly focused on symptoms like fever, aches, etc.
- **BioGPT Integration**: Utilizes the BioGPT-Large model for advanced query interpretation and generating detailed responses.
- **Answer Generator**: Combines rule-based responses with BioGPT-generated content to provide comprehensive answers.

## Technology Stack

- Python
- Hugging Face Transformers
- Microsoft/BioGPT-Large model
- PyTorch

## Project Structure

```
simple_health_qa/
│
├── src/
│   ├── __init__.py
│   ├── question_interpreter.py
│   ├── rule_engine.py
│   ├── biogpt_handler.py
│   └── answer_generator.py
│
└── tests/
    ├── __init__.py
    ├── test_question_interpreter.py
    ├── test_rule_engine.py
    └── test_answer_generator.py
```

## Setup

1. **Clone the Repository**:
   ```
   git clone [repository-url]
   ```

2. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the application, execute the following command in the terminal:

```
python -m src.answer_generator
```

## Testing

Run unit tests by executing:

```
python -m unittest
```

## Additional Notes

- The responses generated by the BioGPT model should be reviewed for accuracy, especially in a sensitive domain like healthcare.
- The system is designed for informational purposes and is not a substitute for professional medical advice.
- Ensure that you comply with local regulations and ethical considerations when providing health-related information.

## Contributing

Contributions to the Simple Health Q&A Project are welcome. Please read the contributing guidelines before submitting pull requests.

## License
No License for this as it is a test project!.
