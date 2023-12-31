from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_list_create_view),
    path('<int:pk>/create', views.product_update_view),
    path('<int:pk>/', views.product_detail_view),
    path('delete/<int:pk>', views.product_destroy_view),
    path("all/<int:pk>/", views.product_all_view)
]
