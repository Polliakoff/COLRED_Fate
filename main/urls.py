from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main_page'),
    path('lk',views.lk, name ='lk'),
    path('redactor/<int:usr_id>/<int:chr_id>',views.redactor, name ='redactor'),
    path('create_new',views.create_new, name ='create_new'),
]