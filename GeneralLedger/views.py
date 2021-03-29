from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def register_page_t(request):
    template_name = "form_newGL.html"
    if request.method == 'POST':

        form = RegisterForm(request.POST)
        if form.is_valid():

            first_name = request.POST.get('Firstname', '')
            last_name = request.POST.get('Lastname', '')
            email = request.POST.get('Email', '')
            username = request.POST.get('Username', '')
            phone = request.POST.get('Phone', '')
            idno = request.POST.get('idno', '')
            password1 = request.POST.get('Password1', '')
            password2 = request.POST.get('Password2', '')
            user_obj = User(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            username=username,
                            phone=phone,
                            idno=idno,
                            password1=password1,
                            password2=password2, )
            user_obj.save()
            print('SUCCESS USER ADDED')
            # return HttpResponseRedirect(reverse('login'))
            # return JsonResponse(reverse('login'),{"message": "Thank you for your submission"})


        else:
            form = RegisterForm()
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
