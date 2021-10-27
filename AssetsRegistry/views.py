from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Prefetch
from django.shortcuts import render, redirect, get_object_or_404

from GeneralLedger.models import Category
from .forms import FormNewAR
from .models import AssetsRegistry, Item, DepartmentItem


@login_required(login_url='accounts:login')
def create_view_asset(request):
    template_name = "form_newAR.html"
    form = FormNewAR()
    objs = (AssetsRegistry.objects.all())
    if request.method == 'POST':
        form = FormNewAR(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Asset ADDED')
            print('SUCCESS Asset ADDED')
            return redirect('AssetsRegistry:newAR')
        else:
            print('Error Occurred')
    context = {'form': form,
               'objs': objs, }
    return render(request, template_name, context)


@login_required(login_url='accounts:login')
def update_data_view(request, pk):
    asset = get_object_or_404(AssetsRegistry, id=pk)
    template_name = "form_newAR.html"
    form = FormNewAR(instance=asset)
    objs = (AssetsRegistry.objects.all())
    if request.method == 'POST':
        form = FormNewAR(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Asset UPDATED')
            print('SUCCESS Asset UPDATED')
            return redirect("AssetsRegistry:newAR")
        else:
            print('Error Occurred')
    context = {'form': form,
               'objs': objs, }
    return render(request, template_name, context)


# AJAX
def load_items_asset(request):
    category_id = request.GET.get('item_category_asset')
    items_asset = Item.objects.filter(category_id=category_id).order_by('name')
    return render(request, 'item_name_dropdown_list_optionsAR.html', {'items_asset': items_asset})


def load_items_dept_asset(request):
    department_id = request.GET.get('items_dept_asset')
    items_dept = DepartmentItem.objects.filter(department_id=department_id).order_by('name')
    return render(request, 'item_name_dropdown_list_optionsAR1.html', {'items_dept': items_dept})


def load_table_items_asset(request):
    template_name = "form_newAR.html"
    category_id = request.GET.get('item_category_asset')
    items_asset = AssetsRegistry.objects.filter(category_id=category_id).order_by('name')
    return render(request, template_name, {'objs': items_asset})


@login_required(login_url='accounts:login')
def report_asset(request):
    context = {}
    template = "reportAR.html"
    return render(request, template, context)


@login_required(login_url='accounts:login')
def summary_asset(request):
    objs = (AssetsRegistry.objects.all())
    context = {'objs': objs}
    template = "summaryAR.html"
    return render(request, template, context)


@login_required
def dashboard_page(request):
    context = {}
    template = "../templates/base.html"
    return render(request, template, context)


def delete_data_view(request, pk):
    # dictionary for initial data with
    # field names as keys
    form = FormNewAR()
    objs = (AssetsRegistry.objects.all())
    context = {'form': form,
               'objs': objs, }
    # fetch the object related to passed id
    asset = AssetsRegistry.objects.get(id=pk)

    if request.method == "GET":
        # delete object
        asset.delete()
        messages.success(request, 'ASSET DELETED')
        print('SUCCESS Asset Deleted')
        # after deleting redirect to
        # home page

        return redirect("AssetsRegistry:newAR")
    return render(request, "form_newAR.html", context)


def summary_totals(request):
    categories = Category.objects.annotate(
        total=Sum('item__order__Price')
    ).prefetch_related(
        Prefetch(
            'Item_set',
            Item.objects.annotate(total=Sum('order__Price')),
            to_attr='items_with_price'
        )
    )
    return render(request, 'template.html', {'categories': categories})
