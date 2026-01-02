"""Serializers of Contact us"""
from rest_framework import serializers
from core.models import ContactUs

class ContactUsSerializer(serializers.ModelSerializer):
    """Serializer of Contact us."""
    class Meta:
        model = ContactUs
        fields = ['id','subject','message']
        read_only_fields = ['id']