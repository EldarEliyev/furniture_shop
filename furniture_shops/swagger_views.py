from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Furniture
from .serializers import FurnitureSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# LIST
@swagger_auto_schema(
    method='get',
    operation_description="Bütün furniture məhsullarını siyahı şəklində qaytarır.",
    responses={200: FurnitureSerializer(many=True)}
)
@api_view(['GET'])
def furniture_list(request):
    items = Furniture.objects.all()
    serializer = FurnitureSerializer(items, many=True)
    return Response(serializer.data)


# CREATE
@swagger_auto_schema(
    method='post',
    operation_description="Yeni furniture məhsulu yaradır.",
    request_body=FurnitureSerializer,
    responses={201: FurnitureSerializer}
)
@api_view(['POST'])
def create_furniture(request):
    serializer = FurnitureSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# DETAIL
@swagger_auto_schema(
    method='get',
    operation_description="Furniture məhsulunun detallarını göstərir.",
    responses={200: FurnitureSerializer}
)
@api_view(['GET'])
def furniture_detail(request, pk):
    item = get_object_or_404(Furniture, pk=pk)
    serializer = FurnitureSerializer(item)
    return Response(serializer.data)


# UPDATE
@swagger_auto_schema(
    method='put',
    operation_description="Furniture məhsulunu tam yeniləyir.",
    request_body=FurnitureSerializer,
    responses={200: FurnitureSerializer}
)
@api_view(['PUT'])
def update_furniture(request, pk):
    item = get_object_or_404(Furniture, pk=pk)
    serializer = FurnitureSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# PARTIAL UPDATE
@swagger_auto_schema(
    method='patch',
    operation_description="Furniture məhsulunu qismən yeniləyir.",
    request_body=FurnitureSerializer,
    responses={200: FurnitureSerializer}
)
@api_view(['PATCH'])
def partial_update_furniture(request, pk):
    item = get_object_or_404(Furniture, pk=pk)
    serializer = FurnitureSerializer(item, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# DELETE
@swagger_auto_schema(
    method='delete',
    operation_description="Furniture məhsulunu silir.",
    responses={204: "Deleted"}
)
@api_view(['DELETE'])
def delete_furniture(request, pk):
    item = get_object_or_404(Furniture, pk=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# SEARCH
@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter(
            'keyword',
            openapi.IN_PATH,
            description="Axtarış sözü",
            type=openapi.TYPE_STRING
        ),
    ],
    operation_description="Ada görə axtarış edir.",
    responses={200: FurnitureSerializer(many=True)}
)
@api_view(['GET'])
def search_furniture(request, keyword):
    items = Furniture.objects.filter(name__icontains=keyword)
    serializer = FurnitureSerializer(items, many=True)
    return Response(serializer.data)


# LATEST
@swagger_auto_schema(
    method='get',
    operation_description="Ən son əlavə olunan furniture məhsulu qaytarır.",
    responses={200: FurnitureSerializer}
)
@api_view(['GET'])
def latest_furniture(request):
    item = Furniture.objects.order_by('-created_at').first()
    if item:
        serializer = FurnitureSerializer(item)
        return Response(serializer.data)
    return Response({"detail": "No item found"}, status=status.HTTP_404_NOT_FOUND)


# COUNT
@swagger_auto_schema(
    method='get',
    operation_description="Furniture məhsullarının ümumi sayını qaytarır.",
    responses={200: openapi.Response(
        "Count",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={'count': openapi.Schema(type=openapi.TYPE_INTEGER)}
        )
    )}
)
@api_view(['GET'])
def furniture_count(request):
    count = Furniture.objects.count()
    return Response({'count': count})


# DELETE ALL
@swagger_auto_schema(
    method='delete',
    operation_description="Bütün furniture məhsullarını silir.",
    responses={204: "All deleted"}
)
@api_view(['DELETE'])
def delete_all_furniture(request):
    Furniture.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
