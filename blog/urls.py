from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:year>/', views.year_archive, name='year archive'),
    path('posts/<int:year>/<int:month>/', views.month_archive, name='month archive'),
    path('posts/<int:year>/<int:month>/<int:post_id>/', views.post_detail, name='post detail'),
]