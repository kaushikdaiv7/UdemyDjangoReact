from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
# class based views
# class Another(View):
#     books = Book.objects.all()
#     output = f'We have {len(books)} books in our DB'
#
#     def get(self, request):
#         return HttpResponse(self.output)


# function based views
def first(request):
    return HttpResponse("First message from view!")


# Views using Template
def second(request):
    return render(request, 'first_template.html')


# Views using dynamic templates
def third(request):
    books = Book.objects.all()
    return render(request, 'second_template.html', {'books': books})


# View using Serializer (rest_framework)
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

