from django.urls import path
from . import views
urlpatterns=[
    path('', views.register, name='register'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    # path('registerteacher/',views.registerteacher,name="register teacher"),
    path('profile/<str:username>/', views.teacherprofile, name="profile"),
    path('<str:username>/editquestion/<int:question_id>', views.editquestion, name="editquestion"),
    path('<str:username>/addquestion', views.addquestion, name="addquestion"),
    path('<str:username>/deletequestion/<int:question_id>', views.deletequestion, name="deletequestion"),
]