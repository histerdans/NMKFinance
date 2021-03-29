from django.contrib import messages
from django.contrib.auth.decorators import login_required
import psycopg2 as pgdb
from django.shortcuts import render

from .forms import FormNewGL
from .models import GeneralLedger

DB_HOST = 'localhost'
DB_USER = 'Admin'
DB_USER_PASSWORD = "123456l7"
DB_NAME = 'NMKFinancedb'
PORT = "5432"


def pg_connect(self):
    self.__conn = pgdb.connect(user=DB_USER,
                               password=DB_USER_PASSWORD,
                               host=DB_HOST,
                               port=PORT,
                               database=DB_NAME)

    # self.conn = mdb.connect(DB_HOST, DB_USER, DB_USER_PASSWORD, DB_NAME)
    _cur = self.__conn.cursor()

    return True


@login_required(login_url='accounts:login')
def add_new_GL(request):
    template_name = "form_newGL.html"
    form = FormNewGL()
    try:

        if pg_connect():

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
    except(Exception, pgdb.Error) as error:
        print(str(error))
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
