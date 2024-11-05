from django.urls import path
from django.conf import settings#добавленное
from django.conf.urls.static import static#добавленное
from .views import page2_view
from .views import encyclopedia_view

urlpatterns = [

path('encyclopedia/', encyclopedia_view, name='encyclopedia_view'),
path('page2/', page2_view, name='page2_view'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)