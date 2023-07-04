from django.urls import path
from . import views

app_name = 'administrativo'

urlpatterns = [
        path('', views.index, name='index'),
        path('edificio/<int:id>', views.obtener_edificio, 
            name='obtener_edificio'),
        path('crear/edificio', views.crear_edificio, 
            name='crear_edificio'),
        path('editar_edificio/<int:id>', views.editar_edificio, 
            name='editar_edificio'),
        path('eliminar/edificio/<int:id>', views.eliminar_edificio, 
            name='eliminar_edificio'),
        
        path('crear/departamento/', views.crear_departamento, 
            name='crear_departamento'),
        path('editar/departamento/<int:id>', views.editar_departamento, 
            name='editar_departamento'),
        path('eliminar/departamento/<int:id>', views.eliminar_departamento, 
            name='eliminar_departamento'),
        
 ]
