from django.shortcuts import render

# Create your views here.

from .models import SearchQuery

from Translator.models import Translator

# Create your views here.



def search_view(request):
	query = request.GET.get('q', None)
	user = None 
	if request.user.is_authenticated:
		user = request.user
		context = {'query' : query}
		if query is not None:
			SearchQuery.objects.create(user=user, query=query)
			translators = Translator.objects.search(query=query)    
			context['translators'] = translators
		return render(request, 'Searches/view.html', context)

	else:
		return render(request, "index_simple_layout_login.html")







	
	
	
