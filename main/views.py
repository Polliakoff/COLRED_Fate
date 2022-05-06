from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Image_Upload_Form, Image_Upload_Form_ava_edition, psw_ch
from .forms import Image_Upload_Form, name_desc_form, main_aspects_form, fate_points_form
from django.contrib.auth import update_session_auth_hash
from .models import Character, Avatar_of_choice, aspect, stunt, extra, consequence, stress, skill

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
    chrctrs = request.user.character_set.all()
    if av.custom_avatar:
        path_string = '/media/' + str(av.portrait)
    else:
        path_string = '/static/main/images/avatars/blank.png'
    cont = {
        'username' : request.user.username,
        'avatar' : path_string,
        'characters': chrctrs,
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
        if 'ava_form' in response.POST and sent_image_form.is_valid():
            print('WE ARE HERE')
            av.portrait = response.FILES['portrait']
            av.custom_avatar = True
            av.save()
            form = psw_ch(response.user)
            return(redirect('/lk'))
        else:
            print('WE ARE HERE_1')
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
    chrctrs = request.user.character_set.all()
    if av.custom_avatar:
        path_string = '/media/' + str(av.portrait)
    else:
        path_string = '/static/main/images/avatars/blank.png'
    
    current_character = Character.objects.get(id = chr_id)
    aspects = current_character.character_aspects.all()
    stunts = current_character.character_stunts.all()
    extras = current_character.character_extras.all()
    consequences = current_character.character_consequences.all()
    stress_es = current_character.character_stress.all()
    skills = current_character.character_skills.all()
    
    if current_character.custom_avatar:
        path_string_chr = '/media/' + str(current_character.portrait)
    else:
        path_string_chr = '/static/main/images/avatars/blank.png'

    if not(usr_id == current_character.usr.id and usr_id == request.user.id):
        return redirect('/') 

    if request.method == 'POST':
        form_1 = name_desc_form(request.POST)
        sent_image_form = Image_Upload_Form(request.POST, request.FILES)
        main_aspects = main_aspects_form(request.POST)
        fate_points = fate_points_form(request.POST)

        if 'ava_form' in request.POST and sent_image_form.is_valid():
            current_character.portrait = request.FILES['portrait']
            current_character.custom_avatar = True
            current_character.save()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if 'form_1' in request.POST and form_1.is_valid():
            current_character.name = request.POST.get('name')
            current_character.desc = request.POST.get('desc')
            current_character.save()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))
            
        if 'main_aspects' in request.POST and main_aspects.is_valid():
            current_character.high_concept = request.POST.get('high_concept')
            current_character.trouble = request.POST.get('trouble')
            current_character.save()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if 'fate_points' in request.POST and fate_points.is_valid():
            current_character.fate_point_number = request.POST.get('fate_point_number')
            current_character.fate_point_refresh = request.POST.get('fate_point_refresh')
            current_character.save()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if 'add_new_aspect' in request.POST:
            new_asp = aspect(chr = current_character)
            new_asp.save()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if 'delete_aspect_form' in request.POST:
            aspect.objects.filter(id = request.POST.get('to_delete_ident_input')).delete()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if 'update_aspect_form' in request.POST:
            to_be_updated = aspect.objects.filter(id = request.POST.get('to_update_ident_input'))
            for upd in to_be_updated:
                upd.desc = request.POST.get('to_update_text_input')
                upd.save()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))
        
        if 'add_new_stunt' in request.POST:
            new_stunt = stunt(chr = current_character)
            new_stunt.save()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if 'delete_stunt_form' in request.POST:
            stunt.objects.filter(id = request.POST.get('stunt_to_delete_ident_input')).delete()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if 'update_stunt_form' in request.POST:
            to_be_updated = stunt.objects.filter(id = request.POST.get('stunt_to_update_ident_input'))
            for upd in to_be_updated:
                upd.name = request.POST.get('stunt_to_update_text_input')
                upd.desc = request.POST.get('stunt_to_update_desc_text_input')
                upd.save()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if 'add_new_extra' in request.POST:
            new_extra = extra(chr = current_character)
            new_extra.save()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if 'delete_extra_form' in request.POST:
            extra.objects.filter(id = request.POST.get('extra_to_delete_ident_input')).delete()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if 'update_extra_form' in request.POST:
            to_be_updated = extra.objects.filter(id = request.POST.get('extra_to_update_ident_input'))
            for upd in to_be_updated:
                upd.name = request.POST.get('extra_to_update_text_input')
                upd.cost = request.POST.get('extra_to_update_cost_text_input')
                upd.attached_aspects = request.POST.get('extra_to_update_attached_aspects_text_input')
                upd.attached_stunts= request.POST.get('extra_to_update_attached_stunts_text_input')
                upd.attached_skills = request.POST.get('extra_to_update_attached_skills_text_input')
                upd.details = request.POST.get('extra_to_update_details_text_input')
                upd.save()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if 'add_new_consequence' in request.POST:
            new_consequence = consequence(chr = current_character)
            new_consequence.save()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if 'delete_consequence_form' in request.POST:
            consequence.objects.filter(id = request.POST.get('consequence_to_delete_ident_input')).delete()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if 'update_consequence_form' in request.POST:
            to_be_updated = consequence.objects.filter(id = request.POST.get('consequence_to_update_ident_input'))
            for upd in to_be_updated:
                upd.severity = request.POST.get('consequence_to_update_text_input')
                upd.desc = request.POST.get('consequence_to_update_desc_text_input')
                upd.save()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if 'add_new_stress' in request.POST:
            new_stress = stress(chr = current_character)
            new_stress.save()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if 'delete_stress_form' in request.POST:
            stress.objects.filter(id = request.POST.get('stress_to_delete_ident_input')).delete()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if 'update_stress_form' in request.POST:
            to_be_updated = stress.objects.filter(id = request.POST.get('stress_to_update_ident_input'))
            for upd in to_be_updated:
                upd.type = request.POST.get('stress_to_update_text_input')
                upd.level = request.POST.get('stress_to_update_level_number_input')
                upd.avaliable = request.POST.get('stress_to_update_avaliable_number_input')
                upd.spent = request.POST.get('stress_to_update_spent_number_input')
                upd.save()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if 'add_new_skill' in request.POST:
            new_skill = skill(chr = current_character)
            new_skill.save()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if 'delete_skill_form' in request.POST:
            skill.objects.filter(id = request.POST.get('skill_to_delete_ident_input')).delete()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

        if 'update_skill_form' in request.POST:
            to_be_updated = skill.objects.filter(id = request.POST.get('skill_to_update_ident_input'))
            for upd in to_be_updated:
                upd.name = request.POST.get('skill_to_update_text_input')
                upd.level = request.POST.get('skill_to_update_level_number_input')
                upd.save()
            return redirect('/redactor/'+str(request.user.id)+'/'+str(current_character.id))

    form_1 = name_desc_form(instance=current_character)    
    main_aspects = main_aspects_form(instance=current_character)     
    sent_image_form = Image_Upload_Form(instance=current_character)
    fate_points = fate_points_form(instance=current_character)
    
    cont = {
        'username' : request.user.username,
        'avatar' : path_string,
        'chr_portrait': path_string_chr, 
        'form_1': form_1,
        'aspects' : aspects,
        'stunts' : stunts, 
        'consequences' : consequences,  
        'extras' : extras,
        'stress' : stress_es,
        'skills' : skills,
        'main_aspects': main_aspects,
        'fate_points': fate_points,
        'portrait_form' : sent_image_form,
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
