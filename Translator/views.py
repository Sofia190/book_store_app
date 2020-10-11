from django.shortcuts import render, redirect

# Create your views here.

from Translator.models import Translator

#from django.http import FileResponse

# import os 

# from django.conf import settings





def list_view(request):


    var=Translator.objects.all()

    var.sorted_authors_list = Translator.objects.display_sorted_authors()

    print(var.sorted_authors_list)

    context_dictionary = {"var" : var,}

    if request.user.is_authenticated:

    	template_path = "Translator/translators_names.html"

    else:

    	template_path = "index_simple_layout_login.html"

    return render(request, template_path, context_dictionary)





def subjects_list_view(request):


    var=Translator.objects.all()

    var.sorted_subjects_list = Translator.objects.display_sorted_subjects()

    print(var.sorted_subjects_list)

    context_dictionary = {"var" : var,}

    if request.user.is_authenticated:

        template_path = "Translator/subjects.html"

    else:
        template_path = "index_simple_layout_login.html"

    return render(request, template_path, context_dictionary)






def works_list_view(request):


    var=Translator.objects.all()

    var.sorted_works_list = Translator.objects.display_sorted_works_authors()

    print(var.sorted_works_list)

    print(len(var.sorted_works_list))
    
    context_dictionary = {"var" : var,}

    if request.user.is_authenticated:

        template_path = "Translator/works.html"

    else:
        template_path = "index_simple_layout_login.html"

    return render(request, template_path, context_dictionary)







def translators_view_20(request):
	

    var = Translator.objects.all()


    var.qs_date_count_20th = Translator.objects.get_time_frame_20th()

    var.qs_with_subjects_sorted = Translator.objects.retrieve_sorted_subjects_20()

    var.qs_with_works_sorted = Translator.objects.retrieve_sorted_works_20()



    print(var.qs_with_subjects_sorted)


    context = {'var' : var ,}
    		

    if request.user.is_authenticated :

    	template_path = "Translator/authors-20th.html"

    else:

    	template_path = "index_simple_layout_login.html"

    return render(request, template_path, context)





def translators_view_21(request):
	

    var = Translator.objects.all()


    var.qs_date_count_21th = Translator.objects.get_time_frame_21st()

    var.qs_with_subjects_sorted = Translator.objects.retrieve_sorted_subjects_21()

    var.qs_with_works_sorted = Translator.objects.retrieve_sorted_works_21()


    context = {'var' : var ,}
    			

    if request.user.is_authenticated:

    	template_path = "Translator/authors-21th.html"

    else:

    	template_path = "index_simple_layout_login.html"

    return render(request, template_path, context)





def translators_about_view(request, id):


    obj = Translator.objects.get(id=id)

    obj.works_sorted = Translator.objects.retrieve_sorted_works(id=id)

    print("list sorted", obj.works_sorted)


    context = {'obj' : obj ,}

    if request.user.is_authenticated:

        template_path = "Translator/translator-about-page.html"

    else:

        template_path = "index_simple_layout_login.html"

    return render(request, template_path, context)






def shop_items_view(request):

    var=Translator.objects.all()

    var.sorted_authors_list = Translator.objects.display_sorted_authors()

    print(var.sorted_authors_list)

    context_dictionary = {"var" : var,}

    if request.user.is_authenticated:

        template_path = "Translator/shop-items.html"
    else:
        template_path = "index_simple_layout_login.html"

    return render(request, template_path, context_dictionary)





def shop_items_detail_view(request, id):

    obj = Translator.objects.get(id=id)


    context_dictionary = {"obj" : obj,}
                            
    if request.user.is_authenticated:

        template_path = "Translator/shop-items-detail-page.html"
    else:
        template_path = "index_simple_layout_login.html"

    return render(request, template_path, context_dictionary)





def contact(request):

    if request.user.is_authenticated:

        return render(request, 'Translator/contact.html')

    else:

        return render(request, "index_simple_layout_login.html")





















