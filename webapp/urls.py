from django.urls import path
from webapp import views


urlpatterns = [
    path('home_page/', views.home_page, name="home_page"),
    path('Categorypage/', views.Categorypage, name="Categorypage"),
    path('productpage/<catname>', views.productpage, name="productpage"),
    path('singlepage/<int:dataid>', views.singlepage, name="singlepage"),
    path('registration_page/', views.registration_page, name="registration_page"),
    path('regdata/', views.regdata, name="regdata"),
    path('user_login/', views.user_login, name="user_login"),
    path('signout/', views.signout, name="signout"),
    path('contactus/', views.contactus, name="contactus"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('cart_page/', views.cart_page, name="cart_page"),
    path('cart_data/', views.cart_data, name="cart_data"),
    path('cart_delete/<int:dataid>/', views.cart_delete, name="cart_delete"),
    path('checkout_page/', views.checkout_page, name="checkout_page"),
    path('checkout_data/', views.checkout_data, name="checkout_data")


    ]