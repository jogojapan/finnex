from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Account, Transaction, RecurringTransaction
from .serializers import AccountSerializer, AccountListSerializer, TransactionSerializer, RecurringTransactionSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class UserAccountList(generics.ListAPIView):
 permission_classes = [IsAuthenticated]
 serializer_class = AccountListSerializer

 def get_queryset(self):
     return Account.objects.filter(user=self.request.user)

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
