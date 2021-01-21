from rest_auth.views import LoginView
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from djstripe import webhooks
from django.contrib.auth import get_user_model
from djstripe.models import Customer

User = get_user_model()
import stripe
stripe.api_key='sk_test_51I95BeASHHtyF3trJggBAPAglOlaDRO6jV48P036Xl4sFzvYJfqFljNcvII8MpyKnXmROfrR7PID8HBBkn8k2AHf00uSj14Xuk'


class customers(APIView):
    def get(self,request):
        list =stripe.Customer.list()
        return Response(list,status=status.HTTP_200_OK)
    def post(self, request, pk):
        customer =User.objects.get(pk=pk)

        print(pk)
        stripe.Customer.create(
        name=pk,
        email=customer.email,
        )
        data ='success'
        return Response(data,status=status.HTTP_202_ACCEPTED)
class subcription(APIView):
    def get(self, request):
        data =stripe.Subscription.list()
        return Response(data,status=status.HTTP_200_OK)
    def post(self , request,pk):
        customer=Customer.objects.get(name=pk)
        stripe.Subscription.create(
            customer=customer.id,
            items=[
            {"price": request.POST['price_id']},
            ],
        )
        data ='success'
        return Response(data,status=status.HTTP_202_ACCEPTED)
class products(APIView):

    def get(self, request):
        data =stripe.Product.list()
        return Response(data,status=status.HTTP_200_OK)


def filterbyproduct(i,target_id):
    if(i["product"]==target_id):
        return True
    else:
        return False
class plans(APIView):
    def get(self, request,product_id):
        data =stripe.Plan.list()
        data=filter(lambda  x: x["product"]==product_id,data["data"])
        return Response(data,status=status.HTTP_200_OK)
