from django.shortcuts import render
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from data.serializers import UmpireSerializers
from data.models import Umpire
from django.http import Http404
# from django.views.decorators.csrf import csrf_exempt


def home(request):
    data = {'data': 'cool'}
    return render(request, 'home.html', data)


class DataList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Umpire.objects.all()
        serializer = UmpireSerializers(snippets, many=True)
        return Response(serializer.data)


class DataDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Umpire.objects.get(pk=pk)
        except Umpire.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UmpireSerializers(snippet)
        return Response(serializer.data)

# function based view

# @api_view(['GET', 'POST'])
# def data_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Umpire.objects.all()
#         serializer = UmpireSerializers(snippets, many=True)
#         return Response(serializer.data)


# @api_view(['GET', 'PUT', 'DELETE'])
# def data_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Umpire.objects.get(pk=pk)
#     except Umpire.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = UmpireSerializers(snippet)
#         return Response(serializer.data)


# simple preset of data

# @csrf_exempt
# def data_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         umpire = Umpire.objects.all()
#         serializer = UmpireSerializers(umpire, many=True)
#         return JsonResponse(serializer.data, safe=False)


# @csrf_exempt
# def data_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         umpire = Umpire.objects.get(pk=pk)
#     except Umpire.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         # umpire = Umpire.objects.get(pk=pk)
#         serializer = UmpireSerializers(umpire)
#         return JsonResponse(serializer.data)
