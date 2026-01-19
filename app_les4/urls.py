from django.urls import path
from .views import index, top_sellers, advertisement, advertisement_post, advertisement_detail

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement/<int:pk>/', advertisement_detail, name='advertisement-detail'),
    path('advertisement/', advertisement, name='advertisement'),
    path('advertisement-post/', advertisement_post, name='advertisement-post'),
]
