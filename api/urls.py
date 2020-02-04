from django.urls import path

from .views import item_list, item_detail

urlpatterns = [
  path('api/', item_list),
  path('api/<int:pk>', item_detail)
]