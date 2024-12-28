from django.urls import path
from .views import FormListCreateView, QuestionCreateView, ResponseCreateView, FormAnalyticsView

urlpatterns = [
    path('forms/', FormListCreateView.as_view(), name='form-list-create'),
    path('questions/', QuestionCreateView.as_view(), name='question-create'),
    path('responses/', ResponseCreateView.as_view(), name='response-create'),
    path('forms/<int:form_id>/analytics/', FormAnalyticsView.as_view(), name='form-analytics'),
]
