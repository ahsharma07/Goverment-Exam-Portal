from django.urls import path
from . import views
urlpatterns=[
    path('',views.generalknowledge,name="general knowledge"),
    path('<str:subject>/questions',views.questions_view,name="questions_view")
]