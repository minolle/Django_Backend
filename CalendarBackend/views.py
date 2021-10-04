#from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
from CalendarBackend.models import Appointment, NoteLine
from CalendarBackend.serializer import AppointmentSerializer, NoteLineSerializer

from django.contrib.auth.models import User
from CalendarBackend.serializer import UserSerializer

from rest_framework import generics
from rest_framework import permissions

#@api_view(['GET', 'POST'])
#def appointment_list(request):
#    if request.method == 'GET':
#        appointments = Appointment.objects.all()
#        serializer = AppointmentSerializer(appointments, many=True)
#        return Response(serializer.data)
#
#    elif request.method == 'POST':
#        serializer = AppointmentSerializer(data=request.data)
#        if serializer.is_valid:
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppointmentList(generics.ListCreateAPIView):
  queryset = Appointment.objects.all()
  serializer_class = AppointmentSerializer
  permission_classes = [permissions.IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)
  
    
    


class NoteLineList(generics.ListAPIView):
  queryset = NoteLine.objects.all()
  serializer_class = NoteLineSerializer
  permission_classes = [permissions.IsAuthenticated]
  

#class UserList(generics.ListAPIView):
    #queryset = User.objects.all()
    #serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

#class UserDetail(generics.RetrieveAPIView):
    #queryset = User.objects.all()
    #serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

# Create your views here.
