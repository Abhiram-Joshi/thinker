from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Deck
from .serializers import DeckSerializer

from utilities import response_writer

# Create your views here.
class TopicAPIView(APIView):

    def get(self, request):
        
        topics = Deck.objects.values_list("topic", flat=True)

        response = response_writer("success", {"topics":topics}, 200, "Topics retrieved")
        return Response(response, status=status.HTTP_200_OK)



class DeckAPIView(APIView):

    def post(self, request):

        serializer = DeckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        response = response_writer("success", dict(serializer.validated_data), 200, "Deck created")
        return Response(response, status=status.HTTP_200_OK)


    def patch(self, request, id):

        instance = Deck.objects.get(id=id)
        print(instance.topic)
        
        serializer = DeckSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = response_writer("success", dict(serializer.validated_data), 200, "Deck updated")

        return Response(response, status=status.HTTP_200_OK)