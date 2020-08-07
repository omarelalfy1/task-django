from django.urls import path
from .views import homepageview,aboutpageview
urlpatterns = [ 
 path("about/",aboutpageview.as_view(), name="about"),
 path("",homepageview.as_view(), name="home")
    ]
 