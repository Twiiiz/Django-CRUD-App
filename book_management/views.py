from django.shortcuts import render, redirect
from .models import *
from .forms import BookForm
from django.contrib import messages

# Create your views here.

def manage_form(request):
  if request.method=='POST':
    form = BookForm(request='POST')
    if form.is_valid():
      try:
        form.save()
        return redirect("/show")
      except ValidationError:
        messages.error(request, "Invalid year. Please enter a year between 0 and the current year.")
      except:
        pass
  else:
    form = BookForm()
  return render(request, 'add_book.html', {'form':form})