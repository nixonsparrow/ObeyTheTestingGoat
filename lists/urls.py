from django.urls import path
from lists import views

urlpatterns = [
    path('new', views.new_list, name='new_list'),
    path('<int:pk>/', views.SingleListView.as_view(), name='view_list'),
    path('<int:list_id>/add_item', views.add_item, name='add_item'),
]
