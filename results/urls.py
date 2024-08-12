from django.urls import path
from . import views

app_name = "results"

urlpatterns = [
    path('polling-unit/<int:polling_unit_id>/', views.polling_unit_results, name='polling_unit_results'),
    path('lga-results/', views.lga_results, name='lga_results'),
    path('new-polling-unit/', views.new_polling_unit, name='new_polling_unit'),
]