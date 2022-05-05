from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Image_Upload_Form, Image_Upload_Form_ava_edition, psw_ch
from .forms import Image_Upload_Form
from django.contrib.auth import update_session_auth_hash
from .models import Character, Avatar_of_choice

@login_required
def main(request):
    av = request.user.chosen_avatar

    if av.custom_avatar:
        path_string = '/media/' + str(av.portrait)
    else:
        path_string = '/static/main/images/avatars/blank.png'

    cont = {
        'username' : request.user.username,
        'avatar' : path_string,
    }
    return render(request, 'main/main_page.html', cont)

@login_required
def docs(request):
    av = request.user.chosen_avatar

    if av.custom_avatar:
        path_string = '/media/' + str(av.portrait)
    else:
        path_string = '/static/main/images/avatars/blank.png'
    cont = {
        'username' : request.user.username,
        'avatar' : path_string,
    }
    return render(request, 'main/docs.html', cont)

@login_required
def search(request):
    av = request.user.chosen_avatar
    if av.custom_avatar:
        path_string = '/media/' + str(av.portrait)
    else:
        path_string = '/static/main/images/avatars/blank.png'
    cont = {
        'username' : request.user.username,
        'avatar' : path_string,
    }
    return render(request, 'main/search.html', cont)

@login_required
def characters(request):
    av = request.user.chosen_avatar
    if av.custom_avatar:
        path_string = '/media/' + str(av.portrait)
    else:
        path_string = '/static/main/images/avatars/blank.png'
    chrctrs = request.user.character_set.all()
    cont = {
        'username' : request.user.username,
        'avatar' : path_string,
        'characters': chrctrs,
    }
    return render(request, 'main/characters.html', cont)

@login_required
def lk(response):

    av = response.user.chosen_avatar
    
    if av.custom_avatar:
        path_string = '/media/' + str(av.portrait)
    else:
        path_string = '/static/main/images/avatars/blank.png'

    portrait_form = Image_Upload_Form_ava_edition(instance=av)

    if response.method == "POST":
        sent_image_form = Image_Upload_Form_ava_edition(response.POST)
        if sent_image_form.is_valid():
            av.portrait = response.FILES['portrait']
            av.custom_avatar = True
            av.save()
            form = psw_ch(response.user)
            return(redirect('/lk'))
        else:
            form = psw_ch(response.user, response.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(response, user)
    else:
        form = psw_ch(response.user)

    cont = {
        'big_username' : response.user.username,
        'form':form,
        'portrait_form':portrait_form,
        'avatar' : path_string,
    }
    return render(response, 'main/lk.html', cont)    

@login_required
def redactor(request,usr_id,chr_id):
    av = request.user.chosen_avatar
    if av.custom_avatar:
        path_string = '/media/' + str(av.portrait)
    else:
        path_string = '/static/main/images/avatars/blank.png'
    current_character = Character.objects.get(id = chr_id)
    
    if current_character.custom_avatar:
        path_string_chr = '/media/' + str(current_character.portrait)
    else:
        path_string_chr = '/static/main/images/avatars/blank.png'

    if not(usr_id == current_character.usr.id and usr_id == request.user.id):
        return redirect('/') 

    if request.method == 'POST':
        sent_image_form = Image_Upload_Form(request.POST)
        if sent_image_form.is_valid():
            current_character.portrait = request.FILES['portrait']
            current_character.custom_avatar = True
            current_character.save()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

    portrait_form = Image_Upload_Form(instance=current_character)
    
    cont = {
        'username' : request.user.username,
        'avatar' : path_string,
        'chr_portrait': path_string_chr, 
        'portrait_form' : portrait_form,
        'current_character': current_character,
    }
    return render(request, 'main/list.html', cont)

@login_required
def create_new(request):
    new_character = Character(usr = request.user, name = 'Новый Персонаж')
    new_character.save()
    cont = {

        'current_character': new_character,
    }
    return redirect('/redactor/'+str(request.user.id)+'/'+str(new_character.id))
