from django.urls import path
from .views import index, detail_article, article_category, login_view, registration, logout_view

app_name = "BlogArticle"
urlpatterns = [
    path('', index, name="home"),
    path('article/<slug:slug>', detail_article, name="detailArticle"),
    path('category/<slug:slug>', article_category, name="articleCategory"),
    path('register', registration , name="register"),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout")
]
