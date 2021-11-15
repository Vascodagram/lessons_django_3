from django.urls import path, include
from .views import index, base, image
urlpatterns = [
    path('', index, name='index'),
    path('base/', base, name='base'),
    path('image', image, name='image')

]
