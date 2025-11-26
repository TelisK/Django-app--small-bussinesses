from rest_framework import serializers
from .models import Income, Expenses

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['income_cash','income_pos','income_sum','date']
        