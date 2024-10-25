from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.shpia, name="shpia"),
    path('login/', views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('singup/', views.SingUp.as_view(), name='singup'),
    path("polls/", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("results/", views.results, name="results"),
    path('vote/', views.vote, name='vote')

]
