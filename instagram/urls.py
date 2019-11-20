from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.feed,name = 'feed'),

    # url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)