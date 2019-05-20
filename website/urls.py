
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('about/', views.aboutpage, name = 'about'),
    path('web-design', views.web_design, name = 'web-design'),
    path('consulting', views.consulting, name = 'consulting'),
    path('graphic-design', views.graphic_design, name = 'graphic-design'),
    path('media-publishing', views.media_publishing, name = 'media-publishing'),
    path('system-solution', views.system_solution, name = 'system-solution'),
    path('social-entrepreneurship', views.social_entrepreneurship, name = 'social-entrepreneurship'),

]
