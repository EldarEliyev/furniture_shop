from django.urls import path 
from .swagger_views import furniture_list, create_furniture, furniture_detail, update_furniture, partial_update_furniture, delete_furniture, search_furniture, latest_furniture, furniture_count, delete_all_furniture

urlpatterns = [
    path("furnitures/",  furniture_list,  name="swagger_furniture_list"),
    path("create_furniture/",  create_furniture, name="swagger_create_furniture"),
    path("furniture/<int:pk>/detail/",  furniture_detail, name="swagger_furniture_detail"),
    path("update_furniture/<int:pk>/",  update_furniture, name="swagger_update_furniture"),
    path("partial_update_furniture/<int:pk>/",  partial_update_furniture,  name="swagger_partial_update_furniture"),
    path("delete_furniture/<int:pk>/",  delete_furniture,  name="swagger_delete_furniture"),
    path("search_furniture/",  search_furniture, name="swagger_search_furniture"),
    path("latest_furniture/",  latest_furniture,  name="swagger_latest_furniture"),
    path("furniture_count/",  furniture_count,  name="swagger_furniture_count"),
    path("delete_all_furniture",  delete_all_furniture,  name="swagger_delete_all_furniture"),
]
