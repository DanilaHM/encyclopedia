from django.urls import path
from .views import encyclopedia_view

urlpatterns = [

path('encyclopedia/', encyclopedia_view, name='encyclopedia_view'),

]