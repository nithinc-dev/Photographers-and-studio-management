from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name='home'),
    path('photo_register/', views.photographer, name='p_reg'),
    path('studio_register/', views.studio, name='s_reg'),
    path('search_studio', views.studio_search, name='ss'),
    path("all", views.all, name='all'),
    path("all_studios", views.all_s, name='alls'),
    path('all_studios/<int:pk>', views.StudioDetailView.as_view(), name = 'detail'),
    path("all_photo", views.all_p, name='allp'),
    path('appoint', views.appoint, name='appointment'),
    path("gallery", views.gallery, name='gallery'),
    path("csv",views.export_model_csv, name='csv1'),
    path("pdf", views.export_model_pdf, name='pdf1'),
      
]
