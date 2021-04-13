from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='accounts:login')
def new_AR(request):
    context = {}
    template = "form_newAR.html"
    return render(request, template, context)
