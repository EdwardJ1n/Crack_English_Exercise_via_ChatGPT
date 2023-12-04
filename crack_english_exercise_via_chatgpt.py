# Setup OpenAI API
import os
import openai
openai.api_type = "azure"
openai.api_version = "2023-07-01-preview"
openai.api_base = "API BASE LINK"
openai.api_key = "API KEY"

# Define function resolve_EN_exercise
delimiter = "####"
def resolve_EN_exercise (text):
  system_content = """
  You are an 3rd grade student to ask a question using word "Where", "What" and "How" based on an answer and a hint. If the hint is empty, input "N/A". 
  You will get the underlined words delimited by {delimiter} from the answer, and they will be asked by the question, and will not appear in the question. 
  The answer must answer the question. You will complete the question with the hint with the same verb in the answer. 
  Users will paste in a string of text, and you will respond with the above question you've generated from the text as a JSON object. Here is your output format:
    {
        "Text": "{text}"
        "Keywords": "{keywords}"
        "Hint": "{hint}"
        "Question": "{question}"
    }
  """

  response = openai.ChatCompletion.create(
    engine="gpt4",
    messages = [
      {"role":"system","content":system_content},
      {"role":"user","content":"Answer is \"He {delimiter} crossed the river, then stops at {delimiter} the cave.\" Hint is \"get to the cave\"."},
      {"role":"assistant","content":"""
            {
                "Text": "Answer is \"He {delimiter} crossed the river, then stops at {delimiter} the cave.\" Hint is \"get to the cave\".",
                "Keywords": "crossed the river, then stops at"
                "Hint": "get to the cave"
                "Question": How does he get to the cave?"},
            }
        """},
      {"role":"user","content":text}
      ], 
    temperature=0
  )

  print("\n" + response['choices'][0]['message']['content'] + "\n")

# Run an exercise
my_text = """
The answer is "{delimiter} Go straight through {delimiter} the jungle. "
The hint is "to the village"
"""
resolve_EN_exercise(my_text)
