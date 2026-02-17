from django.urls import path 
from.swagger_views import furniture_list, create_furniture, furniture_detail, update_furniture, partial_update_furniture, delete_furniture, search_furniture, latest_furniture, furniture_count, delete_all_furniture

urlpatterns = [
    path("furnitures/",  furniture_list,  name="furniture_list"),
    path("create_furniture/",  create_furniture, name="create_furniture"),
    path("furniture/<int:pk>/detail/",  furniture_detail, name="furniture_detail"),
    path("update_furniture/<int:pk>/",  update_furniture, name="update_furniture"),
    path("partial_update_furniture/<int:pk>/",  partial_update_furniture,  name="partial_update_furniture"),
    path("delete_furniture/<int:pk>/",  delete_furniture,  name="delete_furniture"),
    path("search_furniture/",  search_furniture, name="search_furniture"),
    path("latest_furniture/",  latest_furniture,  name="latest_furniture"),
    path("furniture_count/",  furniture_count,  name="furniture_count"),
    path("delete_all_furniture",  delete_all_furniture,  name="delete_all_furniture"),
]