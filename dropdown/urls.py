from django.urls import include, path

from . import views 

urlpatterns = [
    path('', views.ProfileListView.as_view(), name='profile_changelist'),
    path('add/', views.ProfileCreateView.as_view(), name='profile_add'),
    path('<int:pk>/', views.ProfileUpdateView.as_view(), name='profile_change'),
    path('ajax/load-state/', views.load_state, name='ajax_load_state'),
    path('ajax/load-district/', views.load_district, name='ajax_load_district'),
    path('ajax/load-city/', views.load_city, name='ajax_load_city'),
   ]