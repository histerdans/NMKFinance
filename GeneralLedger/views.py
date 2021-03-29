from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from .forms import FormNewGL
from .models import GeneralLedger


@login_required(login_url='accounts:login')
def add_new_GL(request):
    template_name = "form_newGL.html"
    form = FormNewGL()
    if request.method == 'POST':

        form = FormNewGL(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'GL ADDED')
            print('SUCCESS GL ADDED')
        context = {'form': form}
        return render(request, template_name, context)
    else:
        context = {'form': form, }
        return render(request, template_name, context)


@login_required(login_url='accounts:login')
def new_GL(request):
    context = {}
    template = "form_newGL.html"
    return render(request, template, context)


@login_required(login_url='accounts:login')
def report_GL(request):
    context = {}
    template = "reportGL.html"
    return render(request, template, context)


@login_required(login_url='accounts:login')
def summary_GL(request):
    context = {}
    template = "summaryGL.html"
    return render(request, template, context)


def new_AR(request):
    context = {}
    template = "tableGL.html"
    return render(request, template, context)


@login_required
def dashboard_page(request):
    context = {}
    template = "base.html"
    return render(request, template, context)


