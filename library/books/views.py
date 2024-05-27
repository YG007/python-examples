# from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
# from .models import Book, Supplier
from .models import Book
# from django.views.decorators.csrf import csrf_exempt
# import json
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# # Utility function to format book response
# def get_book_response(book):
#     return {
#         "id": book.id,
#         "name": book.name,
#         "supplier_id": book.supplier.id,
#         "price": book.price,
#         "stock_quantity": book.stock_quantity
#     }

# # Error response helper
# def error_response(message, status=400):
#     return JsonResponse({"error": message}, status=status)

# Knock-Knock endpoint
@api_view(['GET'])
def knock_knock(request):
    return Response({"message": "Who's there?"})

# Create and list books endpoint
# @csrf_exempt
@api_view(['GET', 'POST'])
def book_create_list(request):
    if request.method == "GET":
        # books = list(Book.objects.values())
        # return JsonResponse(books, safe=False, status=200)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    # elif request.method == "POST":
    #     try:
    #         data = json.loads(request.body)
    #         supplier = get_object_or_404(Supplier, pk=data["supplier"])
    #         book = Book.objects.create(
    #             name=data["name"], 
    #             supplier=supplier, 
    #             price=data["price"], 
    #             stock_quantity=data["stock_quantity"]
    #         )
    #         return JsonResponse({"id": book.id, "name": book.name}, status=201)
    #     except (KeyError, json.JSONDecodeError) as e:
    #         return error_response(str(e))
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Detail, update, and delete book endpoint
# @csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def book_detail_update_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == "GET":
        # return JsonResponse(get_book_response(book), status=200)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == "PUT":
        # try:
        #     data = json.loads(request.body)
        #     supplier = get_object_or_404(Supplier, pk=data["supplier"])
        #     book.name = data['name']
        #     book.supplier = supplier
        #     book.price = data["price"]
        #     book.stock_quantity = data["stock_quantity"]
        #     book.save()
        #     return JsonResponse(get_book_response(book), status=200)
        # except (KeyError, json.JSONDecodeError) as e:
        #     return error_response(str(e))
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        # book.delete()
        # return HttpResponse(status=204)
        try:
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Adjust book stock endpoint
# @csrf_exempt
@api_view(['PATCH'])
def book_adjust_stock(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == "PATCH":
        # try:
        #     data = json.loads(request.body)
        #     book.stock_quantity += data["stock"]
        #     book.save()
        #     return JsonResponse(get_book_response(book), status=200)
        # except (KeyError, json.JSONDecodeError) as e:
        #     return error_response(str(e))
        data = request.data
        if 'stock' not in data:
            return Response({"error": "Stock quantity is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            stock_adjustment = int(data['stock'])
        except ValueError:
            return Response({"error": "Stock quantity must be an integer."}, status=status.HTTP_400_BAD_REQUEST)

        new_stock_quantity = book.stock_quantity + stock_adjustment
        if new_stock_quantity < 0:
            return Response({"error": "Stock quantity cannot be negative."}, status=status.HTTP_400_BAD_REQUEST)

        # Use the serializer to save the book with the updated stock quantity
        serializer = BookSerializer(book, data={'stock_quantity': new_stock_quantity}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

