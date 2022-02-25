from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('participant/add_participant', views.add_participant),
    path('participant/create', views.create_participant),
    path('participant/<int:participant_id>/delete', views.delete_participant),
    path('participant/<int:participant_id>/edit', views.edit_participant),
    path('participant/<int:participant_id>/update', views.update_participant),
    path('participant/<int:participant_id>/add_caregiver', views.add_caregiver),
    path('participant/<int:participant_id>/create_caregiver', views.create_caregiver),
    path('participant/<int:participant_id>/profile', views.profile_page),
    path('participant/<int:participant_id>/more_caregivers', views.add_more_caregivers),
    path('participant/<int:participant_id>/create_contact', views.create_contact),
    path('participant/<int:participant_id>/<int:caregiver_id>/remove', views.remove_caregiver),
    path('participant/<int:participant_id>/<int:caregiver_id>/edit_caregiver', views.edit_caregiver),
    path('participant/<int:participant_id>/<int:caregiver_id>/update_caregiver', views.update_caregiver),
    path('participant/<int:participant_id>/<int:caregiver_id>/delete_caregiver', views.delete_caregiver),
    path('participant/<int:participant_id>/<int:contact_id>/edit_contact', views.edit_contact),
    path('participant/<int:participant_id>/<int:contact_id>/update_contact', views.update_contact),
    path('participant/<int:participant_id>/<int:contact_id>/delete_contact', views.delete_contact),
    path('<int:participant_id>/progress',views.progress_page),
    path('<int:participant_id>/success', views.success_page),
    path('contactus', views.contact_us),
    path('about', views.about),
    path('<int:participant_id>/responses', views.responses)
]