from django.contrib import admin
from django.urls import path,include
from . import views
#from .views import poll
urlpatterns = [
    path('',views.poll),
    path('<int:id>/',views.poll_detail),
    path('<int:id>/agree/',views.vote_agree),
    path('<int:id>/disagree/',views.vote_disagree),
    
]
