from django.shortcuts import render , redirect 
from django.http import HttpResponse, HttpResponseRedirect, request

from user.models import Users
from user.forms  import UsersForm

# Create your views here.
def user (request): 
    if request.method == "GET":
        form = UsersForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect ('/view')
            except:
                pass
        else:
            form = UsersForm()
        return render(request , 'index.html' , {'form':form})


def view (request):
    users = Users.objects.all()
    return render(request , "view.html" , {'users':users})
    


