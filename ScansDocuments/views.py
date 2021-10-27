from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from .forms import FileUploadForm
from .models import Documents, Item


@login_required(login_url='accounts:login')
def create_view_doc(request):
    template_name = "form_new_document.html"
    form = FileUploadForm()
    objs = (Documents.objects.all())
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'DOCUMENT ADDED')
            print('SUCCESS DOCUMENT ADDED')
            return redirect('Document:uploaded_file_url')
        else:
            print('Error Occurred')

    context = {'form': form,
               'objs': objs, }

    return render(request, template_name, context)


@login_required(login_url='accounts:login')
def update_data_view_doc(request, pk):
    doc = get_object_or_404(Documents, id=pk)
    template_name = "form_new_document.html"
    form = FileUploadForm(instance=doc)
    objs = (Documents.objects.all())
    if request.method == 'POST':
        f = request.FILES['']

        form = FileUploadForm(request.POST, request.FILES['document_file'], instance=doc)
        if form.is_valid():
            f.delete()
            form.save()
            messages.success(request, 'DOCUMENT UPDATED')
            print('SUCCESS DOCUMENT UPDATED')
            return redirect("Document:uploaded_file_url")
        else:
            print('Error Occurred')
    context = {'form': form,
               'objs': objs, }
    return render(request, template_name, context)


# AJAX
def load_items_doc(request):
    category_id = request.GET.get('document_item_category')
    items = Item.objects.filter(category_id=category_id).order_by('name')
    return render(request, 'item_name_document_dropdown_list_options.html', {'items_doc': items})


@login_required(login_url='accounts:login')
def report_doc(request):
    objs = (Documents.objects.all())
    context = {'objs': objs, }
    template = "file_document_report.html"
    return render(request, template, context)


@login_required(login_url='accounts:login')
def summary_doc(request):
    context = {}
    template = "summaryGL.html"
    return render(request, template, context)


@login_required
def dashboard_page(request):
    context = {}
    template = "../templates/base.html"
    return render(request, template, context)


def delete_data_view_doc(request, pk):
    # dictionary for initial data with
    # field names as keys
    form = FileUploadForm()
    objs = (Documents.objects.all())
    context = {'form': form,
               'objs': objs, }
    # fetch the object related to passed id
    doc = Documents.objects.get(id=pk)

    if request.method == "GET":
        # delete object
        doc.delete()
        messages.success(request, 'DOCUMENT DELETED')
        print('SUCCESS DOCUMENT Deleted')
        # after deleting redirect to
        # home page

        return redirect("Document:uploaded_file_url")
    return render(request, "form_new_document.html", context)


def pdf_viewer(request, pk):
    # Handle file upload
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Documents(docfile=request.FILES['document_file'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('Document:uploaded_file_url'))
    else:
        form = FileUploadForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Documents.objects.all()
    template_name = "details.html"

    # Render list page with the documents and the form
    context = {'form': form,
               'documents': documents, }
    return render(request, template_name, context)
