import torch
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering

if torch.cuda.is_available():
  device = "cuda"
else:
  device = "cpu"

# Load pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("gp-tar4/QA_FineTuned_ArabianGpt-01B")
model = AutoModelForQuestionAnswering.from_pretrained("gp-tar4/QA_FineTuned_ArabianGpt-01B").to(device)
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer, device=device)


def model_pipe(context: str, question: str):

  answer = qa_pipeline(question=question, context=context)['answer']
  return answer