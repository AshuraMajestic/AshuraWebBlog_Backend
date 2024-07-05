from rest_framework import generics, status

from .serializers import *
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializerWithData
    lookup_field = "pk"


class BlogPostListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


@csrf_exempt
def increment_visitor_count(request):
    if request.method == "POST":
        try:
            visitor = Visitor.objects.get(id=1)
        except Visitor.DoesNotExist:
            visitor = Visitor.objects.create(id=1, count=0)

        visitor.count += 1
        visitor.save()
        return JsonResponse({"count": visitor.count})
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)


def get_visitor_count(request):
    try:
        visitor = Visitor.objects.get(id=1)
        return JsonResponse({"count": visitor.count})
    except Visitor.DoesNotExist:
        return JsonResponse({"count": 0})
