from django.urls import path,include,re_path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('',views.homeview,name="homepage"),
    path('aptitude/',include("aptitude.urls")),
    path('logical/',include("logical.urls")),
    path('verbal/',include("verbal.urls")),
    path('generalknowledge/',include("generalknowledge.urls")),
    path('currentaffairs/',include("currentaffairs.urls")),
    path('accounts/',include("accounts.urls")),
    path('onlinetest/',views.onlinetest,name="online test"),

    # path('<str:subject>/questions',views.questions_view,name="questions_view"),
]