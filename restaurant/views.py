from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets, permissions
from .models import Menu, Booking
from django.contrib.auth.models import User
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 
   
   
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
# class MenuView(APIView):
    
#     def get(self, request):
#         items = Menu.objects.all()
#         serializer = MenuSerializer(items, many=True)
#         return Response(serializer.data) #Return JSON
    
#     def post(self, request):
#         serializer = MenuSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data})