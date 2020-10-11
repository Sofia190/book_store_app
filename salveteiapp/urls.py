"""SALVETEI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from django.conf import settings

from django.contrib.auth.views import LoginView

from django.contrib.auth.views import LogoutView


from Person.views import (salvetei_view, signup_function_view, user_account_view,

settings_view, user_account_delete_view, add_contact_details_view_function, edit_contact_information,

send_email_message_to_user, display_mail_messages)

from Translator.views import (list_view, translators_view_20, translators_view_21,

translators_about_view, shop_items_view, shop_items_detail_view, 

subjects_list_view, works_list_view, contact)

from Shop.views import (buy_item_work_view, buy_item_card_view,

    retrieve_orders_associated_with_user, GeneratePdf, GeneratePdf_detail, order_delete_view,

    view_order_details, cancel_orders_view, return_item_view, return_items_associated, 

    returned_items_view, render_invoice, update_order)



from Searches.views import search_view





urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', LoginView.as_view(template_name="Person/LOGIN_FORM.html"),
    name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('search/', search_view),

    path('salvetei/', salvetei_view, name='salvetei_view'),

    path('authors/', list_view, name='list_view'),

    path('subjects/', subjects_list_view, name='subjects_list_view'),

    path('works/', works_list_view, name='works_list_view'),

    path('translators-time-frames-20/', translators_view_20, name='translators_view_20'),

    path('translators-time-frames-21/', translators_view_21, name='translators_view_21'),

    path('translators-about-page/<int:id>/', translators_about_view, name='translators_about_view'),

    path('shop-items/', shop_items_view, name='shop_items_view'),

    path('shop-items-detail/<int:id>/', shop_items_detail_view, name='shop_items_detail_view'),
 
    path('signup', signup_function_view, name='signup'),

    path("user-account/<int:id>/", user_account_view, name="user_account_view"), 

    path("buy-item-work/<int:id1>/<int:id2>/", buy_item_work_view, name="buy_item_work_view"), 

    path("buy-item-card/<int:id1>/<int:id2>/", buy_item_card_view, name="buy_item_card_view"), 

    path("orders", retrieve_orders_associated_with_user, name="retrieve_orders_associated_with_user"), 

    path("order-details/<int:id>", view_order_details, name="view_order_details"),

    path("settings/<int:id>/", settings_view, name="settings_view"),

    path("user-account-delete/<int:id>/", user_account_delete_view, name="user_account_delete_view"),

    path("download-invoice/", GeneratePdf.as_view(), name="GeneratePdf"),

    path("download-invoice-detail/<int:id>/", GeneratePdf_detail, name="GeneratePdf_detail"),

    path("order-details/<int:id>/download-invoice-detail/", GeneratePdf_detail, name="GeneratePdf_detail"),

    path("delete-order/<int:id>", order_delete_view, name="order_delete_view"),

    path("cancel-orders/", cancel_orders_view, name="cancel_orders_view"),

    path("add-contact-details/", add_contact_details_view_function, name="add_contact_details_view_function"),

    path("update-contact-information/", edit_contact_information, name="edit_contact_information"),

    path("return-item/<int:id>/", return_item_view, name="return_item_view"),

    path("return-orders/", return_items_associated, name="return_items_associated"),

    path("returned-items-list/", returned_items_view, name="returned_items_view"),

    path("request-invoice/", render_invoice, name="render_invoice"),

    path("send-mail-to-user/<int:id>/", send_email_message_to_user, name="send_email_message_to_user" ),

    path("access-emails/", display_mail_messages, name="display_mail_messages" ),

    path('update-order-details/<int:id>/', update_order, name="update_order"),

    path('contact-information/', contact, name='contact'),

]


if settings.DEBUG:
  #test mode
  from django.conf.urls.static import static
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





