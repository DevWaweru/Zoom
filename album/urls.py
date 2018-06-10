from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.index, name = 'home'),
    url(r'^image/(?P<category_name>\w+)/(?P<image_id>\d+)',views.single_image, name='art')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# (?P<category>)/