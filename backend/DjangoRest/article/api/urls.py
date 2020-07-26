from django.urls import path , include 
from .view import ListView  ,DetailView

urlpatterns = [ 
	path('list/',ListView.as_view()),
    path('list/<pk>',DetailView.as_view())
]