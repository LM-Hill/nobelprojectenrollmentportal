from django.urls import path
from . import views

urlpatterns = [
    path('<int:participant_id>', views.survey_page),
    path('<int:participant_id>/add_demographics', views.demographics_survey),
    path('<int:participant_id>/create', views.create_demographics),
    path('<int:participant_id>/<int:caregiver_id>/add_caregiver_demographics', views.caregiver_demographics_survey),
    path('<int:participant_id>/<int:caregiver_id>/create_caregiver_demo', views.create_caregiver_demographics),
    path('<int:participant_id>/<int:caregiver_id>/caregiver_survey', views.caregiver_survey_page),
    path('<int:participant_id>/add_interest_survey', views.interest_survey),
    path('<int:participant_id>/create_interest_survey', views.create_interest_survey),
    path('<int:participant_id>/<int:caregiver_id>/add_caregiver_interest', views.add_caregiver_interest),
    path('<int:participant_id>/<int:caregiver_id>/create_caregiver_interest', views.create_caregiver_interest),
    path('<int:participant_id>/add_assent_form', views.add_assent_form),
    path('<int:participant_id>/create_assent_form', views.create_assent_form),
    path('<int:participant_id>/<int:caregiver_id>/add_consent_form', views.add_consent_form),
    path('<int:participant_id>/<int:caregiver_id>/create_consent_form', views.create_consent_form),
    path('<int:participant_id>/<int:caregiver_id>/add_stipend_form', views.add_stipend_form),
    path('<int:participant_id>/<int:caregiver_id>/create_stipend_form', views.create_stipend_form),
]