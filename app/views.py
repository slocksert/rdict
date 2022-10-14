from django.shortcuts import render
import requests
import random

# Create your views here.
def home(request):
    response = requests.get('https://www.randomlists.com/data/words.json')
    if response.status_code == 200:
        data = response.json()
        data = data['data']
        word = random.choice(data)
        
        app_id = 'c55ecfaf'
        app_key = '1534e8f20cb15d2a855bd4af27b9ac20'
        language = 'en-us'
        word_id = word
        url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
        
        response2 = requests.get(url, headers={"app_id":app_id, "app_key":app_key})
        if response2.status_code == 200:
            try:
                data2 = response2.json()
                dictionary = {}
                word = data2['word'].upper()
                phonetic = data2['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['phoneticSpelling']
                audio = data2['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][1]['audioFile']
                origin = data2['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
                pos = data2['results'][0]['lexicalEntries'][0]['lexicalCategory']['text']
                example = data2['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples'][0]['text']
                dictionary['example'] = example
                sym1 = data2['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms'][0]['text']
                dictionary['sym1'] = sym1
                dictionary['phonetic'] = phonetic
                dictionary['word'] = word
                dictionary['audio'] = audio
                dictionary['origin'] = origin
                dictionary['pos'] = pos
                return render(request, 'index.html', dictionary)

            except KeyError:
                data2 = response2.json()
                dictionary = {}
                word = data2['word'].upper()
                phonetic = data2['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['phoneticSpelling']
                audio = data2['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][1]['audioFile']
                origin = data2['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
                pos = data2['results'][0]['lexicalEntries'][0]['lexicalCategory']['text']
                dictionary['phonetic'] = phonetic
                dictionary['word'] = word
                dictionary['audio'] = audio
                dictionary['origin'] = origin
                dictionary['pos'] = pos
                example = data2['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples'][0]['text']
                dictionary['example'] = example
                sym1 = data2['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms'][0]['text']
                dictionary['sym1'] = sym1
                return render(request, 'index.html', dictionary)
            
            except ValueError:
                data2 = response2.json()
                dictionary = {}
                word = data2['word'].upper()
                phonetic = data2['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['phoneticSpelling']
                audio = data2['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][1]['audioFile']
                origin = data2['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
                pos = data2['results'][0]['lexicalEntries'][0]['lexicalCategory']['text']
                dictionary['phonetic'] = phonetic
                dictionary['word'] = word
                dictionary['audio'] = audio
                dictionary['origin'] = origin
                dictionary['pos'] = pos
                return render(request, 'index.html', dictionary)