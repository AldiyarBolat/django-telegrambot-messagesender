from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers import MessageSerializer
from ..management.commands import bot
from ..models import Message
from ..models import Profile


class MessageAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        request.data['profile'] = profile.id
        serializer = MessageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            print(serializer)
            bot.send_message(profile.telegram_id, request.user.first_name, request.data['text'])
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        messages = Message.objects.filter(profile=profile)

        res = []
        for message in messages:
            serializer = MessageSerializer(message)
            res.append(serializer.data)

        return Response(res, status=status.HTTP_200_OK)

