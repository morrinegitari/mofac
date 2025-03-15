
from django.contrib import admin
from django.urls import path
from trainingapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('course_details/', views.course_details, name='course_details'),
    path('courses/', views.courses, name='courses'),
    path('events/', views.events, name='events'),
    path('pricing/', views.pricing, name='pricing'),
    path('trainers/', views.trainers, name='trainers'),
    path('starter/', views.starter_page, name='starter'),
    path('login/', views.login_view, name='login'),
    path('location/', views.location, name='location'),
    path('', views.register, name='register'),
    path('show/', views.show, name='show'),
    path('edit/<int:id>/', views.edit_contact, name='edit'),
    path('delete/<int:id>/', views.delete),
  path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('transactions/', views.transactions_list, name='transactions'),


]
