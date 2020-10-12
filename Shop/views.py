from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.


from Translator.models import Translator

from Shop.models import (Item_to_buy_work, Item_to_buy_card,
Orders, Bills, Returned_items,)

from Person.models import ContactInformation, AccountSettings

from .forms import OrdersForm

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View


from datetime import timedelta, datetime, date

from django.utils import timezone


from SALVETEIAPP.utils import render_to_pdf #created in step 4

from django.contrib import messages





def buy_item_work_view(request, id1, id2 ):


    obj = Item_to_buy_work.objects.get(id=id2)

    translator_id = Translator.objects.get(id=id1)
    obj.translator.add(translator_id)
    
  
    obj1 = Orders(id=Orders.objects.last().id+1)

    print("id", obj1.id)

    # var = Orders.objects.all()
    obj1.user=request.user

  
    obj1.save()
    obj1.works.add(obj)
    obj1.translator.add(Translator.objects.get(id=id1))

    obj1.validity_date = Orders.objects.last().date_field + timedelta(days=1)

    obj1.items_value = obj1.retrieve_items_price()

    obj1.total_price=0

    obj1.items_count += 1


    obj1.save()

    var1 = obj.translator.all().first().id
    var2 = obj.translator.all().last().id

    # print(var1)

    if var1 != id1:
        obj.translator.remove(obj.translator.all().first())

    if var2 != id1:
        obj.translator.remove(obj.translator.all().last())


    obj.translator_instance = obj.translator.last()


    print("translator id", obj.translator.all())

    print("works", obj1.works.all())

    print("Translator instance", obj.translator_instance.name)




    context = {'obj' : obj ,}

    if request.user.is_authenticated:

        template_path = "Shop/item-detail.html"

    else:

        template_path = "Person/LOGIN_FORM.html"

    return render(request, template_path, context)





def buy_item_card_view(request, id1, id2):


    obj = Item_to_buy_card.objects.get(id=id2)

    
    translator_id = Translator.objects.get(id=id1)
    obj.translator.add(translator_id)



    obj1 = Orders(id=Orders.objects.last().id+1)


    print("id", obj1.id)

    # var = Orders.objects.all()
    obj1.user=request.user


    obj1.save()
    obj1.cards.add(obj)
    obj1.translator.add(Translator.objects.get(id=id1))

    obj1.validity_date = Orders.objects.last().date_field + timedelta(days=1)

    obj1.items_value = obj1.retrieve_items_price()

    obj1.total_price=0

    obj1.items_count += 1


    obj1.save()


    var1 = obj.translator.all().first().id
    var2 = obj.translator.all().last().id


    if var1 != id1:
        obj.translator.remove(obj.translator.all().first())

    if var2 != id1:
        obj.translator.remove(obj.translator.all().last())

    obj.translator_instance = obj.translator.last()

    print("translator id", obj.translator.all())

    print("cards", obj1.cards.all())

    print("Translator instance", obj.translator_instance.name)



    context = {'obj' : obj ,}

    if request.user.is_authenticated:

        template_path = "Shop/item-detail.html"

    else:

        template_path = "Person/LOGIN_FORM.html"

    return render(request, template_path, context)






def retrieve_orders_associated_with_user(request):
    

    var = Orders.objects.all()

    var.orders_associated = Orders.objects.retrieve_orders_associated(request)

    var.value_total_price_items = Orders.objects.set_orders_total_price(request)

    var.value_total_price_works = Orders.objects.calculate_total_price_works(request)

    var.value_total_price_cards = Orders.objects.calculate_total_price_cards(request)


    for item in var.orders_associated.all():

        if (item.validity_date + timedelta(days=1)== timezone.now()):

            item.delete()

            messages.success(request, "Order nr. {id} was not valid and was deleted".format(id=item.id))


    var.var_quantities = Orders.objects.retrieve_items_sorted_by_quantities(request)

    var.var_total_price = Orders.objects.retrieve_items_sorted_by_total_price(request)

    var.var_the_most_recent = Orders.objects.retrieve_items_sorted_by_date_field(request)

    context = {'var' : var ,}
                # 'var1' : var1,}

    if (request.user.is_authenticated 

        and AccountSettings.objects.get(user=request.user).sort_orders_by_quantities==False

        and AccountSettings.objects.get(user=request.user).display_most_expensive_items_at_the_top==False

        and AccountSettings.objects.get(user=request.user).display_the_most_recent_items_at_the_top==False):

        template_path = "Shop/orders-associated.html"


    elif (request.user.is_authenticated 

        and AccountSettings.objects.get(user=request.user).sort_orders_by_quantities==True):

        template_path = "Shop/sort-orders-by-quantities.html"


    elif (request.user.is_authenticated 

        and AccountSettings.objects.get(user=request.user).display_most_expensive_items_at_the_top==True):

        template_path = "Shop/display-most-expensive-items-at-the-top.html"


    elif (request.user.is_authenticated 

        and AccountSettings.objects.get(user=request.user).display_the_most_recent_items_at_the_top==True):

        template_path = "Shop/display-the-most-recent-items-at-the-top.html"



    else:

        template_path = "Person/LOGIN_FORM.html"

    return render(request, template_path, context)




def  view_order_details(request, id):

    var = Orders.objects.all()

    # var.orders_associated = Orders.objects.retrieve_orders_associated(request)

    try:
   
        var1 = Orders.objects.retrieve_orders_associated(request).get(id=id)
        
    except:

        return render(request, "Shop/bad_request.html")

    var1.value_total_price_items = Orders.objects.set_orders_total_price_detail(request,id=id)

    var1.value_total_price_works = Orders.objects.calculate_total_price_works_detail(request, id=id)

    var1.value_total_price_cards = Orders.objects.calculate_total_price_cards_detail(request, id=id)


    context = {#'var' :var,
             'var1' : var1, }


    if request.user.is_authenticated:

        template_path = "Shop/order-associated-detail.html"

    else:

        template_path = "Person/LOGIN_FORM.html"

    return render(request, template_path, context)






class GeneratePdf(View):

    # 
    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:

            var = Orders.objects.all()

            obj = Orders.objects.first()

            # var.orders_associated = Orders.objects.retrieve_orders_associated(request)

            var.orders_associated = Orders.objects.retrieve_orders_not_returned(request)

            var.value_total_price_items = Orders.objects.set_orders_total_price(request)

            var.value_total_price_works = Orders.objects.calculate_total_price_works(request)

            var.value_total_price_cards = Orders.objects.calculate_total_price_cards(request)

        
    
            var1 = request.user

            var2 = Orders.objects.last().validity_date + timedelta(days=1)


            data = { 'date' : date.today(),
                'from_person': obj.from_person,
                'from_person_address': obj.from_person_address,
                'to_person' : var1,
                'to_person_address': ContactInformation.objects.get(user=request.user).address,
                'var' : var,
                'term': var2,
                'number': request.user.id}

            
        
            pdf = render_to_pdf('Shop/invoice.html', data)
            return HttpResponse(pdf, content_type='application/pdf')

        else:

            return render(request, "index_simple_layout_login.html")






def GeneratePdf_detail(request,id,*args, **kwargs):

        if request.user.is_authenticated:

            # var = Orders.objects.all()

            obj = Orders.objects.first()

            var1 = Orders.objects.retrieve_orders_associated(request).get(id=id)

            var1.value_total_price_items = Orders.objects.set_orders_total_price_detail(request,id=id)

            var1.value_total_price_works = Orders.objects.calculate_total_price_works_detail(request, id=id)

            var1.value_total_price_cards = Orders.objects.calculate_total_price_cards_detail(request, id=id)

       
            var = request.user

            var2 = Orders.objects.get(id=id).validity_date + timedelta(days=1)

            # print("var1 items", var1.value_total_price_items)
      

            data = { 'date' : date.today(),
                'from_person': obj.from_person,
                'from_person_address': obj.from_person_address,
                'to_person' : var,
                'to_person_address': ContactInformation.objects.get(user=request.user).address,
                'var1' : var1,
                'term': var2,
                'number': var1.id,

                }
           
        
            pdf = render_to_pdf('Shop/invoice-detail.html', data)
            return HttpResponse(pdf, content_type='application/pdf')


        else:

            return render(request, "index_simple_layout_login.html")






def order_delete_view(request, id):

    if id <= Orders.objects.last().id:

        obj = Orders.objects.retrieve_orders_associated(request).get(id=id)

        obj.delete()

        messages.success(request, "Order nr. {id} deleted".format(id=id))

        return redirect('retrieve_orders_associated_with_user')

    else:

        return render(request, 'Shop/bad_request.html')

    context = {'object' : obj}

    if request.user.is_authenticated:

        template_path = "Shop/orders-associated.html"

    else:

        template_path = "index_simple_layout_login.html"

    return render(request, template_path, context)





def cancel_orders_view(request):


    qs = Orders.objects.retrieve_orders_associated(request)

    qs.delete()

    messages.success(request, "Orders deleted")


    return redirect('retrieve_orders_associated_with_user')

    context = {'object' : qs}

    if request.user.is_authenticated:

        template_path = "Shop/orders-associated.html"

    else:

        template_path = "index_simple_layout_login.html"

    return render(request, template_path, context)




def return_item_view(request, id):

    if id <= Orders.objects.last().id:

        obj = Orders.objects.retrieve_orders_associated(request).get(id=id)

        var = Returned_items()

        var.save()

        var.orders.add(obj)

        var.user = request.user

        obj.returned = True

        obj.save()

        var.save()

        messages.success(request, "Order nr. {id} will be returned to the seller".format(id=id))

        return redirect('retrieve_orders_associated_with_user')

    else:

        return render(request, 'Shop/bad_request.html')

    context = {'object' : obj}

    if request.user.is_authenticated:

        template_path = "Shop/orders-associated.html"

    else:

        template_path = "index_simple_layout_login.html"

    return render(request, template_path, context)






def return_items_associated(request):


    qs = Orders.objects.retrieve_orders_associated(request)

    var = Returned_items()

    var.save()

    for item in qs:

        var.orders.add(item)

    var.user = request.user

    for item in qs:

        item.returned = True

        item.save()

    var.save()

  
    messages.success(request, "Orders will be returned to the seller")


    return redirect('retrieve_orders_associated_with_user')

    context = {'object' : qs}

    if request.user.is_authenticated:

        template_path = "Shop/orders-associated.html"

    else:

        template_path = "index_simple_layout_login.html"

    return render(request, template_path, context)





def returned_items_view(request):

    #var  = Orders.objects.retrieve_orders_associated(request)

    var = Returned_items.objects.filter(user=request.user)

    context = {'var' : var ,}
                # 'var1' : var1,}

    if request.user.is_authenticated:

        template_path = "Shop/returned-items.html"

    else:

        template_path = "index_simple_layout_login.html"

    return render(request, template_path, context)




def render_invoice(request):

    if request.user.is_authenticated:

        var = Orders.objects.all()

        var.orders_associated = Orders.objects.retrieve_orders_not_returned(request)


        if var.orders_associated.all().count() != 0:

            return redirect('GeneratePdf')

        else:
            return render(request, 'Shop/bad_request.html')

    else:

        return render(request, "index_simple_layout_login.html")




#@login_required
def update_order(request, id):

    obj=get_object_or_404(Orders, id=id)

    form = OrdersForm(request.POST or None, instance=obj)

    context_dictionary = {#'object' : obj, 

                        'form' : form, }

    if form.is_valid():
        obj=form.save()
        obj.save()
        obj.items_count = 0
        for item in obj.works.all():
            obj.items_value +=item.price
            obj.items_count+=1
         
        for item in obj.cards.all():
            obj.items_value +=item.price
            obj.items_count+=1

        obj.save()

        print("count", obj.items_count)

        return HttpResponseRedirect("/orders")

    if request.user.is_authenticated and (request.user == obj.user or request.user.is_staff):

        template_path = "Shop/update-order.html"
    else:
        template_path = "index_simple_layout_login.html"


    return render(request, template_path, context_dictionary)













