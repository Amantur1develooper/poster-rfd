from django.shortcuts import render,HttpResponse
from django.views import View
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.utils import serializer_helpers
from rest_framework.views import APIView
from .serializers import PosterListSerializer,PosterCreateSerializer,PosterSerializer
from .models import Poster
from rest_framework.generics import RetrieveAPIView, get_object_or_404
# from django.chortcuts import

# Create your views here.
# def test(request):
    # return HttpResponse('<h1>Test</h1>')

# class Test:
#     def test_method(self):
#         return HttpResponse('Test')
class TestAPIVew(APIView):
    def get(self,*args,**kwargs):
        return Response(data='test3')

class PosterListAPIView(APIView):
    def get(self,*args,**kwargs):
        posters=Poster.objects.all()
        posters_json=PosterListSerializer(posters,many=True)
        return Response(data=posters_json.data)


    def post(self,request,*args,**kwargs):
        created_poster=request.data.get('poster')
        serializer=PosterCreateSerializer(data=created_poster)
        if serializer.is_valid(raise_exception=True):
            serializer_data=serializer.save()
            return Response(f"New data {serializer_data} is created")


class PosterUpdateAPIView(APIView):

    def put(self,request,pk):
        posters=get_object_or_404(Poster.objects.all(),pk=pk)
        poster = request.data.get('poster')
        serializer=PosterCreateSerializer(instance=posters, data=poster,partial=True)
        if serializer.is_valid():
            serializer_data=serializer.save()
            return Response(f"Data {serializer_data} is update ")
class PosterDeleteAPIView(APIView):
    def delete(self,request,pk):
        poster=get_object_or_404(Poster.objects.all(),pk=pk)
        poster.delete()
        return Response(f"Poster by {pk} is deleted")


class PosterCreateAPIView(APIView):
    def post(self,request,*args,**kwargs):
        data = request.POST
        serializer_data=PosterCreateSerializer(data=data)
        if serializer_data.is_valid():
            valid_data=serializer_data.save()
            valid_data_json=PosterSerializer(instance=valid_data)
            return Response(data=valid_data_json.data, status=201)
        else:
            return Response(data={
                'messages':'data not valid',
                'errors':serializer_data.errors
            },status=404)
class PosterRetriewAPIView(RetrieveAPIView):
    queryset=Poster.objects.all()
    serializer_class= PosterSerializer
        