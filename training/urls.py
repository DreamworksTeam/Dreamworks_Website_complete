from django.urls import path
from . import views

urlpatterns = [
    path('', views.training, name = 'training'),
    path('training-detail/<int:id>', views.training_detail, name = 'training-detail')
]
