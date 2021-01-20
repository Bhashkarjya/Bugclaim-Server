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
import stripe

stripe.api_key='sk_test_51I95BeASHHtyF3trJggBAPAglOlaDRO6jV48P036Xl4sFzvYJfqFljNcvII8MpyKnXmROfrR7PID8HBBkn8k2AHf00uSj14Xuk'


class customers(APIView):
    def get(self,request):
        list =stripe.Customer.list()
        return Response(list,status=status.HTTP_200_OK)
    def post(self, request, *Args, **kwargs):
        print(request)
        stripe.Customer.create(
        name=request.data['name'],
        email=request.data['email']
        )
        data ='success'
        return Response(data,status=status.HTTP_202_ACCEPTED)
class subcription(APIView):

    def get(self, request):
        data =stripe.Subscription.list()
        subscription = djstripe.models.Subscription.sync_from_stripe_data(stripe_subscription)
        return Response(data,status=status.HTTP_200_OK)
    def post(self , request):
        stripe.Subscription.create(
            customer=request.data.customer_id,
            items=[
            {"price": request.data.price_id},
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
