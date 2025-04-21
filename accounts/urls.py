from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, TransactionViewSet, RecurringTransactionViewSet

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'recurring-transactions', RecurringTransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
