from django.contrib import admin

# Register your models here.

from .models import (Item_to_buy_work, Item_to_buy_card, Orders,
	Bills, Returned_items)





admin.site.register(Item_to_buy_work)
admin.site.register(Item_to_buy_card)
admin.site.register(Orders)
admin.site.register(Bills)
admin.site.register(Returned_items)


















