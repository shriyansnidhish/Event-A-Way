from django.shortcuts import render
from django.http import HttpResponse
import openai

OPENAI_TOKEN = "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"
openai.api_key = OPENAI_TOKEN
# Create your views here.
def ask_question(request):
    if request.method == "POST":
        # question = "Summarize Ramayana in 100 words"
        question = request.POST['question']
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=question,
            temperature=0,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        answer = response["choices"][0]["text"]
        return render(request, 'chatgpt_prompt.html',{"answer":answer})

    return render(request,'chatgpt_prompt.html')
    # return HttpResponse(response['choices'][0]['text'])

