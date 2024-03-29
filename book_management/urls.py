from django.urls import path
from .views import *

urlpatterns = [
    path('add', manage_form),
    path('', show_records),
    path('update/<int:id>', update_record),
    path('delete/<int:id>', delete_record)
]