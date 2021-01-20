from django.urls import path
from api.payments.views import customers,subcription,products,plans
from api.views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='my_custom_login'),
    path('customers/', customers.as_view(), name='my_custom_login'),
    path('subcription/', subcription.as_view(), name='my_custom_login'),
    path('products/', products.as_view(), name='my_custom_login'),
    path('plans/<str:product_id>', plans.as_view(), name='my_custom_login'),
]
