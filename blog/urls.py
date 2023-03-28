from django.urls import path
from . import views


urlpatterns = [
    path('blog/articulos/', views.list, name="list-article"),
    path('blog/categoria/<int:id>', views.category, name="category"),
    path('blog/articulo/<int:article_id>', views.article, name="article" )  
]
