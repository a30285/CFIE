import openai

from pdftext import read_lines_from_text_file
from prompts.propmt_en import prompt_en_few, prompt_en_zero
from prompts.prompt_zh_v1 import prompt_zh_zero, prompt_zh_few

test_key = ""
model = "gpt-3.5-turbo"

def single_paper(prompt, model, text) -> str:

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": text}
    ]

    client = openai.OpenAI(api_key=test_key)
    response = client.chat.completions.create(
        model=model,
        messages=messages)
    return response.choices[0].message.content



def muti_segment(prompt, model, file_path):
    faultjson = []
    lines = read_lines_from_text_file(file_path)
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        for line in lines:
            messages = [
                {"role": "system", "content": prompt},
                {"role": "user", "content": line}
            ]
            client = openai.OpenAI(api_key=test_key)
            response = client.chat.completions.create(
                model=model,
                messages=messages)
            content = response.choices[0].message.content
            content = content.replace('\n','')
            print(content)
            faultjson.append(content)
            output_file.write(content + '\n')
    return faultjson
        # return response.choices[0].message.content

file_path = "./pdf2text/dataset.txt"
muti_segment(prompt_zh_few, model, file_path)