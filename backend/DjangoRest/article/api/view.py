from rest_framework.generics import ListAPIView , RetrieveAPIView
from article.models import Article
from .serializers import ArticleSerializer


class ListView(ListAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer


class DetailView(RetrieveAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer