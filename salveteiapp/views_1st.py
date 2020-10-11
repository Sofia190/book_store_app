from django.shortcuts import render, redirect



def welcome(request):
    if request.user.is_authenticated:
        return redirect('salvetei_view')
    else:
        return render(request, 'Person/LOGIN_FORM.html')

























