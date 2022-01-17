from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from utilities import response_writer

from .models import Deck
from .serializers import DeckSerializer, CreateDeckSerializer, UpdateDeckSerializer


# Create your views here.
class TopicAPIView(APIView):
    def get(self, request):

        topics = Deck.objects.values_list("topic", flat=True)

        response = response_writer(
            "success", {"topics": topics}, 200, "Topics retrieved"
        )
        return Response(response, status=status.HTTP_200_OK)


class DeckAPIView(APIView):

    def get(self, request):

        deck = Deck.objects.filter(id=request.query_params.get("id")).first()
        serializer = DeckSerializer(deck)

        if deck.user != request.user:
            deck.views+=1
            deck.save()
        
        response = response_writer("success", serializer.data, 200, "Deck retrieved")

        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = CreateDeckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        response = response_writer(
            "success", serializer.validated_data, 200, "Deck created"
        )
        return Response(response, status=status.HTTP_200_OK)

    def patch(self, request):

        id = request.query_params.get("id")
        deck = Deck.objects.get(id=id)

        if deck.user == request.user:
            serializer = UpdateDeckSerializer(deck, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            response = response_writer(
                "success", serializer.validated_data, 200, "Deck updated"
            )
            return Response(response, status=status.HTTP_200_OK)

        else:
            response = response_writer(
                "error", None, 403, "You are not authorized to update this deck"
            )
            return Response(response, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request):

        id = request.query_params.get("id")
        deck = Deck.objects.get(id=id)

        if deck.user == request.user:
            deck.delete()
            response = response_writer("success", None, 200, "Deck deleted")
            return Response(response, status=status.HTTP_200_OK)

        else:
            response = response_writer(
                "error", None, 403, "You are not authorized to delete this deck"
            )
            return Response(response, status=status.HTTP_403_FORBIDDEN)


class DeckViewsAPIView(APIView):

    def post(self, request):

        id = request.query_params.get("id")
        deck = Deck.objects.get(id=id)
        deck.bookmarks += 1
        deck.save()

        response = response_writer("success", None, 200, "Views increased by 1")

        return Response(response, status=status.HTTP_200_OK)

class DeckCreatedListAPIView(ListAPIView):

    serializer_class = DeckSerializer

    def get_queryset(self):
        return Deck.objects.filter(user=self.request.user)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        response = response_writer(
            "success", serializer.data, 200, "Decks retrieved"
        )
        return Response(response, status=status.HTTP_200_OK)