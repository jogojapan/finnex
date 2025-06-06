from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, UserAccountList, CreateAccountView, TransactionViewSet, RecurringTransactionViewSet

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'recurring-transactions', RecurringTransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/accounts/', CreateAccountView.as_view(), name='create_account'),
    path('api/accounts/', UserAccountList.as_view(), name='user_account_list'),
]
