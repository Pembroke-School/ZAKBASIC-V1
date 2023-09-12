import os

from gpt4all import GPT4All
# device='amd', device='intel'
model = GPT4All("wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin")
output = model.generate(input("User Input: "), max_tokens=20)
os.system("say " + output)
