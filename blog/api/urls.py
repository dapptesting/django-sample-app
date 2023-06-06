from django.urls import path
from .views import ArticleCountView
# from . import views


# urlpatterns = [
#     path("count", views.article_count, name="article-count"),
# ]

# We're switching from a function view to a class based view
urlpatterns = [
    path("count", ArticleCountView.as_view(), name="article-count"),
]
