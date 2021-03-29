from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from .forms import RegisterForm
from .models import User


def register_page(request):
    if request.user.is_authenticated:
        return redirect('GeneralLedger:dashboard')
    else:

        form = RegisterForm()
        template_name = 'register.html'
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'USER ADDED')
                print('SUCCESS USER ADDED')
                return redirect('accounts:login')
            context = {'form': form}
            return render(request, template_name, context)
        else:
            context = {'form': form, }
            return render(request, template_name, context)


def register_page_t(request):
    template_name = 'register.html'
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


def login_page(request):
    if request.user.is_authenticated:
        return redirect('GeneralLedger:dashboard')
    else:
        context = {}
        template = "login.html"
        if request.method == 'POST':
            username = request.POST.get('Username')
            password = request.POST.get('Password')
            qs = User.objects.filter(username=username)
            if qs.exists():
                # user email is registered, check active/
                not_active = qs.filter(is_active=False)

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('GeneralLedger:dashboard')
            else:
                messages.info(request, 'Username or Password is incorrect')
                return render(request, template, context)
        else:
            context = {}
            return render(request, template, context)


def logout_user(request):
    logout(request)
    return redirect('accounts:login')


@login_required(login_url='accounts:login')
def table_view(request):
    context = {}
    template = "tableGL.html"
    return render(request, template, context)
