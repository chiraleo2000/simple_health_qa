
from transformers import AutoModelForCausalLM, AutoTokenizer

class BioGPTHandler:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/BioGPT-Large")
        self.model = AutoModelForCausalLM.from_pretrained("microsoft/BioGPT-Large")

    def generate_answer(self, question):
        inputs = self.tokenizer.encode(question, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=100, num_return_sequences=1)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
