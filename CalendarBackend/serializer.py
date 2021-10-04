from rest_framework import serializers
from CalendarBackend.models import Appointment, NoteLine
#from CalendarBackend.models import NoteLine
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    appointments = serializers.PrimaryKeyRelatedField(many=True, queryset=Appointment.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'appointments']



class AppointmentSerializer(serializers.Serializer):
  class Meta:
    model = Appointment
    fields = ['date', 'text', 'title', 'owner']
  date = serializers.DateTimeField(required=True)
  text = serializers.CharField(max_length=200)
  time_provided = serializers.BooleanField(required=True)
  title = serializers.CharField(max_length=25)
  owner = serializers.ReadOnlyField(source='owner.username')

  def create(self, validated_data):
    return Appointment.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.date = validated_data.get('date', instance.date)
    instance.text = validated_data.get('text', instance.text)
    instance.time_provided = validated_data.get('time_provided', instance.time_provided)
    instance.title = validated_data.get('title', instance.title)
    instance.save()
    return instance


class NoteLineSerializer(serializers.Serializer):
  class Meta:
    model = NoteLine
    fields = ['line_idx', 'line_text']
  line_idx = serializers.IntegerField(required=True)
  line_text = serializers.CharField(max_length=50)
  
  def create(self, validated_data):
    return NoteLine.objects.create(**validated_data)
  
  def update(self, instance, validated_data):
    instance.line_idx = validated_data.get('idx_line', instance.idx_line)
    instance.line_text = validated_data.get(instance.line_text, instance.line_text)
    instance.save()
    return instance


#datetime.datetime(2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC)
#curl -X POST 'http://localhost:8000' -H 'Content-Type: application/json' -d '{"date":"2021-10-01T00:00:00", "time_provided":"false","title":"3","text":"Hello i provided the field?"} -u minolle'

#python3 manage.py makemigrations CalendarBackend
