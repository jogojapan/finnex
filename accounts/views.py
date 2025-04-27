from rest_framework import viewsets, generics
from .models import Account, Transaction, RecurringTransaction
from .serializers import AccountSerializer, TransactionSerializer, RecurringTransactionSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class CreateAccountView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class   = AccountSerializer

    def perform_create(self, serializer):
        print('perform_create')
        print(self.request.user)
        print('continue')
        serializer.save(user=self.request.user)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class RecurringTransactionViewSet(viewsets.ModelViewSet):
    queryset = RecurringTransaction.objects.all()
    serializer_class = RecurringTransactionSerializer
