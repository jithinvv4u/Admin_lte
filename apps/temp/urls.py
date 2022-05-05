from django.urls import path
from .views import vegitableView,getVegitable
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('temp/vegitables/',vegitableView,name='vegitable'),
    path('temp_vegitable/',getVegitable)


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)