from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name='trek'
urlpatterns=[
    path('',views.index,name='home'),
    path('book',views.bookk,name='book'),
    path('package',views.package,name='packk'),
                path('pack1', views.pack1, name='blog1'),
path('pack2', views.pack2, name='blog2'),
path('pack3', views.pack3, name='blog3'),
path('pack4', views.pack4, name='blog4'),
path('pack5', views.pack5, name='blog5'),
    path('final',views.pricc,name='price'),
path('render/pdf', views.GeneratePdf.as_view(),name='pdf')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()