from django.urls import path
from .views import *

urlpatterns = [
    path('add', manage_form),
    path('records', show_records),
    path('edit/<int:id>', edit_record),
    path('update/<int:id>', update_record)
]