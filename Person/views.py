from django.conf import settings

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.http import HttpResponseRedirect


from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth import get_user_model


User = settings.AUTH_USER_MODEL  


from .models import AccountSettings, ContactInformation, MailMessage


from .forms import (SettingsForm, Add_contact_details_Form, 
ContactInformation_Form, SendMessageForm)







def salvetei_view(request):


	if request.user.is_authenticated:

		template_path = "Translator/salvetei.html"

	else:

		template_path = "Person/LOGIN_FORM.html"


	return render(request, template_path)







def signup_function_view(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            User = get_user_model()
            form.save()
            var = AccountSettings()
            var.user = User.objects.last()
            var.save()
            var1 = ContactInformation()
            var1.user = User.objects.last()
            var1.save()
            print("Username", var.user)


            return redirect('salvetei_view')

    else:
        form = UserCreationForm()
        
    return render(request, 'Person/SIGNUP_FORM.html', {'form': form})






def user_account_view(request, id):


    User=get_user_model()

    obj = User.objects.get(id=id)


    if (request.user.is_authenticated and request.user.id == obj.id):

        template_path = "Person/user-account.html"


    elif request.user.is_authenticated and request.user.id != obj.id:

        template_path = "Person/you-are-not-authorized-to-view-this-page.html"

    else:

        template_path = "Person/LOGIN_FORM.html"

    context = {'obj' : obj}

    return render(request, template_path, context)







def settings_view(request,id):


    obj=get_object_or_404(AccountSettings, id=id)

    form = SettingsForm(request.POST or None, instance=obj)

    context_dictionary = {'form' : form, }

    if form.is_valid():

        obj=form.save()
        obj.save()
        return HttpResponseRedirect("/settings/{id}".format(id=obj.id))

    if request.user.is_authenticated and (request.user == obj.user or request.user.is_staff):

        template_path = "Person/account-settings.html"
    else:
        template_path = "Person/LOGIN_FORM.html"

    return render(request, template_path, context_dictionary)





def user_account_delete_view(request, id):

    User=get_user_model()

    obj = get_object_or_404(User, id=id)

    if request.method== 'POST':

        if 'yes' in request.POST:
            obj.delete()
            return redirect('login')

        elif 'no' in request.POST:
            return HttpResponseRedirect("/user-account/{id}".format(id=obj.id))

    context = {'object' : obj}

    if request.user.is_authenticated:

        template_path = "Person/delete-user-account.html"

    else:

        template_path = "Person/LOGIN_FORM.html"

    return render(request, template_path, context)







def add_contact_details_view_function(request):

  form =  Add_contact_details_Form(request.POST)

  if request.method == 'POST': 

      if form.is_valid():
          form.save()
          form = Add_contact_details_Form()
          return HttpResponseRedirect("/user-account/{id}".format(id=request.user.id))

  else:
          form = Add_contact_details_Form()

  
  context_dictionary = {
                         'form' : form,}

  if request.user.is_authenticated:
      template_path = "Person/add-contact-details.html"
  else:
      template_path = "Person/LOGIN_FORM.html"

  return render(request, template_path, context_dictionary)







def edit_contact_information(request):

    if ContactInformation.objects.filter(user=request.user):


        form = ContactInformation_Form(request.POST or None,  instance=obj)

        context_dictionary = {'form' : form, }

        if form.is_valid():
            obj=form.save()
            obj.save()
            return HttpResponseRedirect("/user-account/{id}".format(id=request.user.id))

    else:

        return HttpResponseRedirect("/add-contact-details")

    print(request.user.id)
    print(obj.user.id)

    if request.user.is_authenticated and (request.user == obj.user or request.user.is_staff):

        template_path = "Person/edit-contact-information.html"
    else:
        template_path = "Person/LOGIN_FORM.html"


    return render(request, template_path, context_dictionary)






def send_email_message_to_user(request,id):

    form = SendMessageForm(request.POST)

    User = get_user_model()

    sender = User.objects.get(id=request.user.id)

    receiver = User.objects.get(id=id)

    if request.user.is_staff:


        if request.method == 'POST':

            if form.is_valid():

                form.save()
                obj = MailMessage.objects.last()
                obj.to_user.add(User.objects.get(id=id))
                obj.save()
                form = SendMessageForm()
                return HttpResponseRedirect('/user-account/{sender_id}'.format(
                sender_id=request.user.id))

         
        else:
            form = SendMessageForm()

    else:

        return render(request, "Shop/bad_request.html")
    

    context_dictionary = {'form' : form,}
                          

    if (request.user.is_authenticated  

    and AccountSettings.objects.get(user=receiver).receive_marketing_emails==True):

        template_path = "Person/send-mail-message-to-user.html"


    elif (request.user.is_authenticated  

    and AccountSettings.objects.get(user=receiver).receive_marketing_emails==False):

        template_path = "Person/now-this-user-is-not-receiving-messages.html"

        
    else:
        template_path = "Person/LOGIN_FORM.html"

    return render(request, template_path, context_dictionary)







def display_mail_messages(request):

    qs = AccountSettings.objects.get(user=request.user)

    qs1 =  MailMessage.objects.filter(to_user=request.user)

    print("Qs count =", qs1.count())

    for item in qs1:
        print(item.to_user)
   
    receiver = request.user

    context_dictionary = {"qs" : qs,

                        "qs1" : qs1,

                        "to_user": receiver,}
    

    if request.user.is_authenticated:

        template_path = "Person/email-messages.html"

    else:

        template_path = "Person/LOGIN_FORM.html"


    return render(request, template_path, context_dictionary)





























