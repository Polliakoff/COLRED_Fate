from django.shortcuts import render,redirect
from .forms import Clr_Rgister_Form
from main.models import Avatar_of_choice
from django.contrib.auth.models import User

# Create your views here.
def register(response):
    if response.method == "POST":
        form = Clr_Rgister_Form(response.POST)
        if form.is_valid():
            form.save()
            u = form.cleaned_data["username"]
            av = Avatar_of_choice(usr = User.objects.get(username = u), name = 'blank')
            av.save()
            return redirect('main_page')
                

    else:
        form = Clr_Rgister_Form()

    return render(response, 'usr_auth/register.html', {'form':form})