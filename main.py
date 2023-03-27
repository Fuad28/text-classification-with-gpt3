from dotenv import load_dotenv
import openai
import os

load_dotenv() 

API_KEY= os.getenv("API_KEY")
openai.api_key = API_KEY
file_id = os.getenv("file_id")


# #upload file
# if not file_id:
#     file_id = openai.File.create(file=open("training.jsonl"), purpose="fine-tune")
#     os.environ["file_id"] = file_id.get("id")


text_to_clarify = "URGENT! Your Mobile number has been awarded with a \ufffd2000 prize GUARANTEED. Call 09058094455 from land line. Claim 3030. Valid 12hrs only"
ft_ada_model = "ada:ft-personal-2023-03-27-11-27-39"
res = openai.Completion.create(model=ft_ada_model, prompt=text_to_clarify + '\n\n###\n\n', max_tokens=1, temperature=0)
print(res['choices'][0]['text'])

