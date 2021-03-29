from django.shortcuts import render
from django.views.generic import CreateView


def home_page(request):
    context = {}
    template = "index.html"

    return render(request, template, context)
