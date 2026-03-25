from django.shortcuts import render
from rest_framework import generics
from .models import Payroll
from .serializers import PayrollSerializer
from rest_framework.permissions import IsAuthenticated

# List all payroll records OR create new payroll
class PayrollListCreateView(generics.ListCreateAPIView):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
    permission_classes = [IsAuthenticated]


# Retrieve, update, delete single payroll
class PayrollDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
    permission_classes = [IsAuthenticated]

# Create your views here.
