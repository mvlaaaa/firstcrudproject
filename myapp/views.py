from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

# Create your views here.

# READ (List all users)
def user_list(request):
    records = User.objects.all()
    return render(request, 'Listingpage.html', {'records': records})

# CREATE
def AddUser(request):
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'Add.html', {'form': form})

# UPDATE
def EditUser(request, id=None):
    one_rec = User.objects.get(pk=id)
    form = UserForm(request.POST or None, request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'Edit.html', {'form': form})

# DELETE
def DeleteUser(request, eid=None):
    one_rec = User.objects.get(pk=eid)
    if request.method == "POST":
        one_rec.delete()
        return redirect('/')
    return render(request, 'Delete.html')

# READ (Detail view)
def ViewUser(request, eid=None):
    one_rec = User.objects.get(pk=eid)
    return render(request, 'View.html', {'user': one_rec})