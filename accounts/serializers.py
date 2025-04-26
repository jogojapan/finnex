from rest_framework import serializers
from .models import Account, Transaction, RecurringTransaction

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id',
            'user',
            'name',
            'bank_name',
            'account_id',
            'account_type',
            'currency',
            'opening_balance',
            'current_balance',
        ]

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class RecurringTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecurringTransaction
        fields = '__all__'
