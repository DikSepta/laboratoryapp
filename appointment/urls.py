from django.urls import path
from appointment.views import (
    appointment_status_view,
    appointment_list_view,
    make_appointment_view,
    appointment_edit_view,
    appointment_change_status_view,
    appointment_delete_view,
)

app_name = 'appointment'

urlpatterns = [
    path('customer/status', appointment_status_view, name = "status"),
    path('staff/list', appointment_list_view, name = "list"),
    path('customer/make-appointment', make_appointment_view, name = "add"),
    path('customer/edit-appointment/<int:id>', appointment_edit_view, name = "edit"),
    path('staff/delete-appointment/<int:id>', appointment_delete_view, name = "delete"),
    path('change-status/<int:id>/<str:status>', appointment_change_status_view, name = "change-status"),
]