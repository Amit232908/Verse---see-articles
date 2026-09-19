from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('features/',features,name='features'),
    path('latest/',latest,name='latest'),
    path('contactus/',contactus,name='contactus'),
    path('article/<int:id>;',article_detail,name='article_detail'),
    path('foot/',footer,name='footer')

]
