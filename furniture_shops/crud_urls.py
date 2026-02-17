from django.urls import path
from.import crud_views

urlpatterns = [
    path("",  crud_views.home,  name="home"),
    path("furnitures/",  crud_views.furniture_list,  name="furniture_list"),
    path("create_furniture/",  crud_views.add_furniture,  name="add_furniture"),
    path("furniture/<int:furniture_id>/",  crud_views.furniture_detail,  name="furniture_detail"),
    path("furniture/<int:furniture_id>/update/",  crud_views.update_furniture,  name="update_furniture"),
    path("furniture/<int:furniture_id>/delete/",  crud_views.delete_furniture,  name="delete_furniture"),
]