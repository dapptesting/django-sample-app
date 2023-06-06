from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from blog.renderers import JSONRendererOnly
from blog.models import Article

# Original function view
# @api_view(["GET"])
# def article_count(request):
#     count = Article.objects.count()

#     return Response(
#         {
#             "count": count,
#         }
#     )

# We're switching from a function view to a class based view


class ArticleCountView(APIView):
    renderer_classes = [JSONRendererOnly]

    def get(self, request):
        count = Article.objects.count()

        return Response(
            {
                "count": count,
            }
        )
