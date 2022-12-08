from django.urls import path
from django.views.decorators.cache import cache_page
from .import views

urlpatterns = [
    path("",views.AdministracionView.as_view(),name="index"),
    path('create/', views.ProyectoCreate.as_view(), name="create"),
    path('delete/<int:id>', views.deleteProyecto, name="delete"),
]
