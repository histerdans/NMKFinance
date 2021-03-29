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
            slug_number = request.POST.get('slug_number', '')
            item_name = request.POST.get('item_name', '')
            description = request.POST.get('description', '')
            partner = request.POST.get('partner', '')
            invoice = request.POST.get('invoice', '')
            invoice_amount = request.POST.get('invoice_amount', '')
            transaction_ref_number = request.POST.get('transaction_ref_number', '')
            account_name = request.POST.get('account_name', '')
            account_number = request.POST.get('account_number', '')
            debit = request.POST.get('debit', '')
            credit = request.POST.get('credit', '')
            paye_amt = request.POST.get('paye_amt', '')
            user_obj = GeneralLedger(slug_number=slug_number,
                                     item_name=item_name,
                                     description=description,
                                     partner=partner,
                                     invoice=invoice,
                                     invoice_amount=invoice_amount,
                                     transaction_ref_number=transaction_ref_number,
                                     account_name=account_name,
                                     account_number=account_number,
                                     debit=debit,
                                     credit=credit,
                                     paye_amt=paye_amt, )
            user_obj.save()
            print('SUCCESS GL ADDED')
    else:
        return render(request, template_name, {'form': form, })


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


