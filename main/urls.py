from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('platos', views.PlatoListView.as_view(), name='plato-list'),
    path('platos/<int:pk>', views.PlatoDetailView.as_view(), name='plato-detail'),
    path('registro/', views.RegistrationView.as_view(), name='register'),
    path('perfil/', views.ClienteListView.as_view(), name='perfillist'),
    path('perfil/<int:pk>', views.ClienteDetailView.as_view(), name='perfil'),
    path('perfilupdate/<int:pk>', views.PerfilUpdateView.as_view(), name='perfil-update'),
    path('menu/', views.MenuDetailView.as_view(), name='menu-detail'),
    path('checkout/<int:pk>', views.MenuUpdateView.as_view(), name='menu-update'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('complete_payment/', views.CompletePaymentView.as_view(), name='complete-payment'),
]
