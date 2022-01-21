from django.contrib import admin
from django.urls import path
from .views import company_detailsAPIView,company_detail,company_list,contactAPIView,contact,contact_list,contact_detail


urlpatterns = [
    path('company_details/', company_detailsAPIView.as_view()),
    path('detail/<int:pk>/',company_detail),
    path('contact/', contactAPIView.as_view()),
    path('details/<int:pk>/',contact_detail)
]