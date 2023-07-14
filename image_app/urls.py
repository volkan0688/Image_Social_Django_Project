from django.urls import path
from . import views

app_name = 'image_app'

urlpatterns = [
    path('', views.list_image, name='list_image'),
    path('add_image/', views.add_image, name='add_image'),
    path('search/', views.search_feature, name='search-view'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('delete_image/<int:id>', views.delete_image, name='delete_image'),
]