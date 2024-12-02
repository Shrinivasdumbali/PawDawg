from django.urls import path
from . import views

# configure the view function that was created
urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/',views.about, name= 'about'),
    path('report_rescue/', views.report_rescue, name='report_rescue'),
    
]
