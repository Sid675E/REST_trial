from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import table_rest
from .serializers import table_restSerializer

#Lists content in table or creates content in table
#table_rest/
class restSerializer(APIView):

    def get(self,request):
        rests = table_rest.objects.all()
        serializer = table_restSerializer(rests,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer =table_restSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=404)


    def delete(self, request):
        try:
            rests=table_rest.objects.get(pk=request.data)
        except table_rest.DoesNotExist:
            raise 404
        rests.delete()
        return Response(status=204)
