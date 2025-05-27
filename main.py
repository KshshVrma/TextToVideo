import requests
import base64
from google import genai
from secret import api_key
import subprocess
        
#generate some python code to draw a manim square name the method helloworld
x=input(" enter some input")

y="Generate only Python code using the manim library to draw the following. Name the method helloworld. Do not include any explanations, comments, or text outside the code. Output only valid Python code:"
z="maintain the animation for 3"
x=y+x+" "+z
print(x)

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=x
)
print(response.text)
# ...existing code...
output_lines = response.text.splitlines()
filtered_lines = []
k=len(output_lines)
ctr=0
for line in output_lines:
    if ctr!=0 and ctr!=k-1:
        filtered_lines.append(line)
    ctr+=1
        

with open('output.py', 'w') as f:
    # f.write(response.text)
    f.write('\n'.join(filtered_lines))

subprocess.run(["manim", "-pql", "output.py", "helloworld"])

