from django.urls import path
from . import views

urlpatterns = [
    path('',views.fn_myIndex),
    path('html',views.fn_index)
]