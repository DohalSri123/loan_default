from django.urls import path
from .views import LoanDefaultPredictionView

urlpatterns = [
    path('predict/', LoanDefaultPredictionView.as_view(), name='loan_default_prediction'),
]
