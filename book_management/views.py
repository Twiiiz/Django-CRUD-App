from django.shortcuts import render, redirect
from .models import *
from .forms import BookForm
from django.contrib import messages

# Create your views here.
have_records = False

def manage_form(request):
  global have_records
  if request.method=='POST':
    form = BookForm(request.POST)
    if form.is_valid():
      try:
        form.save()
        have_records = True
        return redirect("/records")
      except ValidationError:
        messages.error(request, "Invalid year. Please enter a year between 0 and the current year.")
      except:
        pass
  else:
    form = BookForm()
  return render(request, 'add_book.html', {'form':form})

def show_records(request):
  global have_records
  books = Book.objects.all()
  if len(books) == 0:
    have_records = False
  return render(request, 'show_records.html', {'books': books, 'records': have_records})