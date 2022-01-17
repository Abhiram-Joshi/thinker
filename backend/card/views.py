from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from deck.models import Deck
from .models import Card
from .serializers import CardSerializer

from utilities import response_writer

# Create your views here.
class CardsAPIView(APIView):

    def get(self, request):
        deck_id = request.query_params.get('deck_id')
        cards = Card.objects.filter(deck = Deck.objects.get(id=deck_id)).values()

        if cards:
            response = response_writer("success", cards, 200, "Cards retrieved")
            return Response(response, status=status.HTTP_200_OK)

        else:
            response = response_writer("error", None, 404, "Cards not available")
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)


    def post(self, request):
        deck_id = request.query_params.get('deck_id')
        
        serializer = CardSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        serializer.save(deck=Deck.objects.get(id=deck_id))

        response = response_writer("success", serializer.validated_data, 200, "Card created")

        return Response(response, status=status.HTTP_200_OK)



class CardsDeleteAPIView(APIView):

    def delete(self, request):
        id = request.query_params.get('id')
        instance = Card.objects.get(id=id)
        instance.delete()

        response = response_writer("success", None, 200, "Card deleted")

        return Response(response, status=status.HTTP_200_OK)

    
    def patch(self, request):
        id = request.query_params.get('id')
        instance = Card.objects.get(id=id)

        serializer = CardSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = response_writer("success", serializer.validated_data, 200, "Card updated")

        return Response(response, status=status.HTTP_200_OK)