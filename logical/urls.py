from django.urls import path
from . import views
urlpatterns=[
    path('',views.logical,name="logical"),
    path('<str:subject>/questions',views.questions_view,name="questions_view")
]