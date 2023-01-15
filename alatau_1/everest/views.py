from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
import aspose.words as aw

# doc = aw.Document("C:\\Users\\dimaw\\Desktop\\Вак.docx")
# doc.save("C:\\Users\\dimaw\\Desktop\\Output.html")

# Create your views here.

def index(request):

    return HttpResponse('<h1>My first site on django<h1>')


def error(request, exception):
    raise Http404("Page not found!!!")