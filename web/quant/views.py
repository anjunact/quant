from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
def index(request):
    # return HttpResponse("hello world")
    template = loader.get_template('quant/index.html')
    context ={
        "a":23
    }
    return HttpResponse(template.render(context,request))