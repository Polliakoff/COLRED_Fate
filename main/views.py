from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Image_Upload_Form, psw_ch
from .forms import Great_List_Form, Image_Upload_Form
from django.contrib.auth import update_session_auth_hash
from .models import Character

@login_required
def main(request):
    av = request.user.chosen_avatar
    chrctrs = request.user.character_set.all()
    cont = {
        'username' : request.user.username,
        'avatar' : av,
        'characters': chrctrs,
    }
    return render(request, 'main/main_page.html', cont)

@login_required
def lk(response):
    av = response.user.chosen_avatar
    if response.method == "POST":
        if response.POST.get('_blank'):
            av.name = 'blank'
            av.save(update_fields = ['name'])
            form = psw_ch(response.user)
        elif response.POST.get('_elf'):
            av.name = 'elf'
            av.save(update_fields = ['name'])
            form = psw_ch(response.user)
        elif response.POST.get('_dwarf'):
            av.name = 'dwarf'
            av.save(update_fields = ['name'])
            form = psw_ch(response.user)
        elif response.POST.get('_cobalt'):
            av.name = 'cobalt'
            av.save(update_fields = ['name'])
            form = psw_ch(response.user)

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
        'avatar' : 'main/images/avatars/'+str(av)+'.png',
    }
    return render(response, 'main/lk.html', cont)    

@login_required
def redactor(request,usr_id,chr_id):
    av = request.user.chosen_avatar
    chrctrs = request.user.character_set.all()
    current_character = Character.objects.get(id = chr_id)

    if not(usr_id == current_character.usr.id and usr_id == request.user.id):
        return redirect('/') 

    if request.method == 'POST':
        sent_gerat_form = Great_List_Form(request.POST)
        sent_image_form = Image_Upload_Form(request.POST)
        
        if sent_gerat_form.is_valid():
            current_character.name = request.POST.get('name')
            current_character.attrib_strength = request.POST.get('attrib_strength')
            current_character.attrib_agility = request.POST.get('attrib_agility')
            current_character.attrib_charisma = request.POST.get('attrib_charisma')
            current_character.attrib_endurance = request.POST.get('attrib_endurance')
            current_character.attrib_intelligence = request.POST.get('attrib_intelligence')
            current_character.attrib_wisdom = request.POST.get('attrib_wisdom')
            current_character.background = request.POST.get('background')
            current_character.diety = request.POST.get('diety')
            current_character.origin = request.POST.get('origin')
            current_character.worldview = request.POST.get('worldview')
            current_character.xp = request.POST.get('xp')
            current_character.chr_class = request.POST.get('chr_class')
            current_character.hp = request.POST.get('hp')
            current_character.armour_class = request.POST.get('armour_class')
            current_character.speed = request.POST.get('speed')
            current_character.is_dying = request.POST.get('is_dying')
            current_character.mortal_wounds = request.POST.get('mortal_wounds')


            current_character.save()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if sent_image_form.is_valid():
            print('WE ARE HERE')
            current_character.portrait = request.FILES['portrait']
            current_character.save()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        print(str(sent_image_form.errors))
        print(sent_image_form.non_field_errors)

 

    form = Great_List_Form(instance=current_character)
    portrait_form = Image_Upload_Form(instance=current_character)
    
    cont = {
        'username' : request.user.username,
        'avatar' : av,
        'form' : form,
        'portrait_form' : portrait_form,
        'current_character': current_character,
        'characters': chrctrs,
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
