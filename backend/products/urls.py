from django.urls import path
from . import views

urlpatterns = [
    # path('', views.product_alt_view),
    path('', views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailAPIView.as_view())
    # path('<int:pk>/', views.product_alt_view)

]
