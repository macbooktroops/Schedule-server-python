from django.shortcuts import render

from .models import FriendRelation

from .serializers import FriendRelationSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from django.utils import timezone


class FriendRelationViewSet(viewsets.ModelViewSet):
    queryset = FriendRelation.objects.all()
    serializer_class = FriendRelationSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)

        # Todo: Is_valid 에러 코드 작성 필요
        serializer.is_valid(raise_exception=True)

        # self.perform_create(serializer)

        if serializer.is_valid():
            data = serializer.validated_data

            print(data)

            friend_request = FriendRelation.objects.filter(request_user=data['response_user'], response_user=data['request_user'])

            print(friend_request)

            if friend_request:
                friend_request = friend_request[0]

                now = timezone.now()

                friend_request.assent = 1
                friend_request.assented_at = now
                friend_request.save()

                headers = self.get_success_headers(serializer.data)

                return Response({
                    'status': 200,
                    'message': "친구 요청 수락"
                }, status=status.HTTP_200_OK, headers=headers)
            else:
                serializer.save()
                headers = self.get_success_headers(serializer.data)

                return Response({
                    'status': 201,
                    'message': "친구 요청 완료"
                }, status=status.HTTP_201_CREATED, headers=headers)

        return Response({
            'message': 'testing'
        })