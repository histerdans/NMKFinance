from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404

from .forms import FormNewGL
from .models import GeneralLedger, Item


@login_required(login_url='accounts:login')
def create_view_gl(request):
    template_name = "form_newGL.html"
    form = FormNewGL()
    amt = GeneralLedger.objects.all()
    sum_amt = amt.aggregate(Sum('Amount'))
    objs = GeneralLedger.objects.all()
    if request.method == 'POST':
        form = FormNewGL(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'GL ADDED')
            print('SUCCESS GL ADDED')
            return redirect('GeneralLedger:newGL')
        else:
            print('Error Occurred')
    context = {'form': form,
               'objs': objs,
               'amt': sum_amt['Amount__sum']}

    return render(request, template_name, context)


@login_required(login_url='accounts:login')
def update_data_view(request, pk):
    ledger = get_object_or_404(GeneralLedger, id=pk)
    template_name = "form_newGL.html"
    form = FormNewGL(instance=ledger)
    objs = (GeneralLedger.objects.all())
    if request.method == 'POST':
        form = FormNewGL(request.POST, instance=ledger)
        if form.is_valid():
            form.save()
            messages.success(request, 'GL UPDATED')
            print('SUCCESS GL UPDATED')
            return redirect("GeneralLedger:newGL")
        else:
            print('Error Occurred')
    context = {'form': form,
               'objs': objs, }
    return render(request, template_name, context)


def load_table_items(request):
    category_id = request.GET.get('item_category')
    items = GeneralLedger.objects.filter(category_id=category_id).order_by('name')
    return render(request, 'ledger_table_filter.html', {'items_table': items})


# AJAX
def load_items(request):
    category_id = request.GET.get('item_category')
    items = Item.objects.filter(category_id=category_id).order_by('name')
    return render(request, 'item_name_dropdown_list_options.html', {'items': items})


@login_required(login_url='accounts:login')
def report_gl(request):
    objs = (GeneralLedger.objects.all())
    context = {'objs': objs}
    template = "reportGL.html"
    return render(request, template, context)


@login_required(login_url='accounts:login')
def summary_gl(request):
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
    template = "../templates/base.html"
    return render(request, template, context)


@login_required
def generalLedgers(request, category_id=None):
    category_id = request.GET.get('item_category')
    ledgers = Item.objects.filter(category_id)
    return render(request, 'form_newGL.html', {'ledgers': ledgers})




def delete_data_view(request, pk):
    # dictionary for initial data with
    # field names as keys
    form = FormNewGL()
    objs = (GeneralLedger.objects.all())
    context = {'form': form,
               'objs': objs, }
    # fetch the object related to passed id
    ledger = GeneralLedger.objects.get(id=pk)

    if request.method == "GET":
        # delete object
        ledger.delete()
        messages.success(request, 'GL DELETED')
        print('SUCCESS GL Deleted')
        # after deleting redirect to
        # home page

        return redirect("GeneralLedger:newGL")
    return render(request, "form_newGL.html", context)


def export_excel_view():
    return None


def export_pdf_view():
    return None


def export_csv_view():
    return None
