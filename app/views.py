from django.shortcuts import render
import requests
import random

# Create your views here.
def home(request, word=None):
    if not word:
        word_request = requests.get('https://www.randomlists.com/data/words.json')
        if word_request.status_code == 200:
            data = word_request.json()
            data = data['data']
            word = random.choice(data)
    
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.lower()}"
    dict_request = requests.get(url)
    if dict_request.status_code == 200:
        dict_json = dict_request.json()[0]
        return render(request, 'index.html', dict_json)
    return home(request)
    
def saved_words(request):
    return render(request, 'favorite_words.html')