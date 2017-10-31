from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import Dictionary
import json

def index(request):
    return render(request, 'dictajaxapp/index.html', {})


def getdict(request):
    dict_words = Dictionary.objects.all()
    dict_full = {'words': []}
    for dict_word in dict_words:
        dict_full['words'].append({
            'id': dict_word.id,
            'word': dict_word.word,
            'definition': dict_word.definition,
            'synonym': dict_word.synonym
        })
    return JsonResponse(dict_full)


def createdict(request):
    data = json.loads(request.body)
    word_text = data['word_text']
    def_text = data['def_text']
    synonym_text = data['synonym_text']
    dict_full = Dictionary(word=word_text, definition=def_text, synonym=synonym_text)
    dict_full.save()
    return HttpResponse('word saved')


def deletedict(request, delete_id):
    print(delete_id)
    # delete_data = get_object_or_404(Dictionary, pk=delete_id)
    # delete_data.delete()
    return HttpResponse('word deleted')




