from django.shortcuts import render, HttpResponse

from datetime import date

from .models import Holiday
from .get_holiday import get_api_data
from .serializers import HolidaySerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from rest_framework.viewsets import ModelViewSet, ViewSet


class HolidayViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer


class HolidayListViewSet(viewsets.ViewSet):
    def list(self, request):
        year = date.today().year

        if not Holiday.objects.filter(year=year):
            holidays = get_api_data(year)
            serializer_list = []

            for holiday in holidays['results']:
                serializer = HolidaySerializer(data={
                    "name": holiday['name'],
                    "year": holiday['year'],
                    "month": holiday['month'],
                    "day": holiday['day'],
                })

                if serializer.is_valid():
                    serializer.save()

                    serializer_list.append(serializer.data)
                else:
                    return Response({
                        "code": 409,
                        "message": "non-field-error",
                    })

            return Response(serializer_list)
        else:
            datas = Holiday.objects.filter(year=year)
            # Todo: 일단 돌아가긴 하는데 dict 형태로 따로 한번 빼는게 맞는지 확인

            data_list = []

            for data in datas:
                json_data = {
                    'name': data.name,
                    'year': data.year,
                    'month': data.month,
                    'day': data.day,
                }

                data_list.append(json_data)

            return Response({
                'holidays': data_list,
            })
    def create(self, request):
        if request.data:
            year = request.data['year']
            print("request data")
        else:
            print("no request data")
            year = date.today().year
            # year = str(year)

        if not Holiday.objects.filter(year=year):
            holidays = get_api_data(year)
            serializer_list = []

            for holiday in holidays['results']:
                serializer = HolidaySerializer(data={
                    "name": holiday['name'],
                    "year": holiday['year'],
                    "month": holiday['month'],
                    "day": holiday['day'],
                })

                if serializer.is_valid():
                    serializer.save()

                    serializer_list.append(serializer.data)
                else:
                    return Response({
                        "code": 409,
                        "message": "non-field-error",
                    })

            return Response(serializer_list)
        else:
            datas = Holiday.objects.filter(year=year)
            # Todo: 일단 돌아가긴 하는데 dict 형태로 따로 한번 빼는게 맞는지 확인

            data_list = []

            for data in datas:
                json_data = {
                    'name': data.name,
                    'year': data.year,
                    'month': data.month,
                    'day': data.day,
                }

                data_list.append(json_data)

            return Response({
                'holidays': data_list,
            })


# @api_view(['GET', 'POST'])
# def holiday_list(request):
#     # data = get_api_data()
#     if request.data:
#         year = request.data['year']
#         print("request data")
#     else:
#         print("no request data")
#         year = date.today().year
#         # year = str(year)
#
#     if not Holiday.objects.filter(year=year):
#         holidays = get_api_data(year)
#         serializer_list = []
#
#         for holiday in holidays['results']:
#             serializer = HolidaySerializer(data={
#                 "name": holiday['name'],
#                 "year": holiday['year'],
#                 "month": holiday['month'],
#                 "day": holiday['day'],
#             })
#
#             if serializer.is_valid():
#                 serializer.save()
#
#                 serializer_list.append(serializer.data)
#             else:
#                 return Response({
#                     "code": 409,
#                     "message": "non-field-error",
#                 })
#
#         return Response(serializer_list)
#     else:
#         datas = Holiday.objects.filter(year=year)
#         # Todo: 일단 돌아가긴 하는데 dict 형태로 따로 한번 빼는게 맞는지 확인
#
#         data_list = []
#
#         for data in datas:
#             json_data = {
#                 'name': data.name,
#                 'year': data.year,
#                 'month': data.month,
#                 'day': data.day,
#             }
#
#             data_list.append(json_data)
#
#         return Response({
#             'holidays': data_list,
#         })