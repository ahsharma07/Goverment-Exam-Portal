from django.urls import path
from . import views
urlpatterns=[
    path('',views.currentaffairs,name="current affairs"),
    path('<str:subject>/questions',views.questions_view,name="questions_view")
]