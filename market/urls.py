from django.urls import path, include
from market.views.auth import AuthView
from market.views.product_view import ProductListView
from market.views.category_view import CategoryListView
from market.views.basket_view import BasketInfoView
from market.views.google_auth import GoogleView
from market.views.init_view import InitView

urlpatterns = [
    path('userlogin', AuthView.as_view()),
    path('category_list', CategoryListView.as_view()),
    path('product_list', ProductListView.as_view()),
    path('basket_list', BasketInfoView.as_view()),
    path('google_auth', GoogleView.as_view()),
    path('init', InitView.as_view()),
]
