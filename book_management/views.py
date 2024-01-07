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
        return redirect("/")
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
  else:
    have_records = True
  return render(request, 'show_books.html', {'books': books, 'records': have_records})

def update_record(request, id):
   book = Book.objects.get(id=id)
   if request.method == 'POST':
     book.name = request.POST['book_name']
     book.author = request.POST['book_author']
     book.genre = request.POST['book_genre']
     book.publisher = request.POST['book_publisher']
     book.release_year = request.POST['book_release_year']
     try:
      book.full_clean()
      book.save()
      response = redirect("/")
     except ValidationError:
      messages.error(request, "Invalid year. Please enter a year between 0 and the current year.")
   else:
    book = Book.objects.get(id=id)
    response =  render(request, 'update_book.html', {'book': book})
   return response

def delete_record(request, id):  
    book = Book.objects.get(id=id)  
    book.delete()  
    return redirect("/")