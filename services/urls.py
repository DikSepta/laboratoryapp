from django.urls import path
from services.views import service_add_view, service_list_view, service_edit_view, service_delete_view

app_name = 'services'

urlpatterns = [
    path('list', service_list_view, name = 'list' ),
    path('add', service_add_view, name = 'add' ),
    path('edit/<int:id>', service_edit_view, name = "edit"),
    path('delete/<int:id>', service_delete_view, name = "delete"),
]