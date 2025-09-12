# """project_settings URL Configuration
# """
# from django.contrib import admin
# from django.urls import path, include
# from . import views
# from .views import about, index, predict_page,cuda_full

# app_name = 'ml_app'
# handler404 = views.handler404

# urlpatterns = [
#     path('', index, name='home'),
#     path('about/', about, name='about'),
#     # path('predict/', predict_page, name='predict'),
#     path("predict2/", views.predict_api, name="predict_api"),

#     path('cuda_full/',cuda_full,name='cuda_full'),
# ]

"""project_settings URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import os
from . import views
from .views import about, index, predict_page, cuda_full, predict_api

app_name = 'ml_app'
handler404 = views.handler404

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    # path('predict/', predict_page, name='predict'),
    path("predict2/", predict_api, name="predict_api"),
    path('cuda_full/', cuda_full, name='cuda_full'),
]

# Serve media files (uploaded videos)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    # Serve uploaded_images directory as static files
    uploaded_images_dir = os.path.join(settings.PROJECT_DIR, 'uploaded_images')
    urlpatterns += static('/uploaded_images/', document_root=uploaded_images_dir)
    
    # Also serve the regular static files
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
