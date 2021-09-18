from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView, ListView, DetailView, View, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.db.models import F
from random import randint
from django.contrib import messages
from django.contrib.auth.models import User


# Importamos forms.py
from .forms import *

#Importamos las clases recien creadas
from .models import *

class HomePageView(TemplateView):
  template_name = "main/home.html"
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['latest_platos'] = Plato.objects.all()[:5]
    return context

class PlatoListView(ListView):
  model = Plato
  template_name = "main/plato_list.html"
  object_list = Plato.objects.all()

class PlatoDetailView(DetailView):
  model = Plato
  template_name = "main/plato_detail.html"

class RegistrationView(FormView):
  template_name = 'registration/register.html'
  form_class = UserForm
  success_url = reverse_lazy('home')

  def form_valid(self, form):
    # This methos is called when valid from data has been POSTed
    # It should return an HttpResponse

    # Create User
    username = form.cleaned_data['username']
    first_name = form.cleaned_data['first_name']
    last_name = form.cleaned_data['last_name']
    email = form.cleaned_data['email']
    password = form.cleaned_data['password1']

    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
    user.save()
    # Create Profile
    documento_identidad = form.cleaned_data['documento_identidad']
    edad = form.cleaned_data['edad']
    genero = form.cleaned_data['genero']
    talla = form.cleaned_data['talla']
    peso = form.cleaned_data['peso']
    nivelactividad = form.cleaned_data['nivelactividad']
    alimentacion = form.cleaned_data['alimentacion']
    user_profile = Profile.objects.create(user=user, documento_identidad=documento_identidad,
                                          edad=edad, talla=talla, genero=genero, peso=peso, nivelactividad=nivelactividad, alimentacion=alimentacion)
    user_profile.save()
    # Login the user
    login(self.request, user)
    return super().form_valid(form)

class ClienteListView(ListView):
  model = Profile
  template_name = "main/perfilist.html"

class ClienteDetailView(DetailView):
  model = Profile
  template_name = "main/perfil.html"
  def get_object(self):
    # Obten el cliente
    user_profile = Profile.objects.get(user=self.request.user)
    # Obtén/Crea un/el pedido en proceso (EP) del usuario
    profile = Profile.objects.get(id=user_profile.id)
    return profile

class PerfilUpdateView(UpdateView):
  model = Profile
  fields = ['talla', 'edad', 'peso', 'objetivo', 'alimentacion']
  success_url = reverse_lazy('home')
  template_name = "main/perfil_update.html"

  def get_object(self):
    # Obten el cliente
    user_profile = Profile.objects.get(user=self.request.user)
    # Obtén/Crea un/el pedido en proceso (EP) del usuario
    profile = Profile.objects.get(id=user_profile.id)
    return profile

  def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
    self.object = form.save(commit=False)
    return super().form_valid(form)

class MenuDetailView(DetailView):
  model = Menu
  template_name = "main/menu_detail.html"
  def get_object(self):
    # Obten el cliente
    user_profile = Profile.objects.get(user=self.request.user)
    # Obtén/Crea un/el pedido en proceso (EP) del usuario
    menu, created = Menu.objects.get_or_create(profile=user_profile, estado='No Pagado')
    return menu

class MenuUpdateView(UpdateView):
    model = Menu
    fields = ['alimentacion', 'fecha_fin']
    success_url = reverse_lazy('payment')
    template_name = "main/menu_form.html"

    def get_object(self):
      # Obten el cliente
      user_profile = Profile.objects.get(user=self.request.user)
      # Obtén/Crea un/el pedido en proceso (EP) del usuario
      menu, created = Menu.objects.get_or_create(profile=user_profile, estado='No Pagado')
      return menu
    def form_valid(self, form):
      self.object = form.save(commit=False)
      return super().form_valid(form)

class PaymentView(TemplateView):
  template_name = "main/payment.html"
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    # Obten el cliente
    user_profile = Profile.objects.get(user=self.request.user)
    context['menu'] = Menu.objects.get(profile=user_profile, estado='No Pagado')
    return context

class CompletePaymentView(View):
  def get(self, request):
    # Obten el cliente
    user_profile = Profile.objects.get(user=request.user)
    # Obtén/Crea un/el pedido en proceso (EP) del usuario
    menu = Menu.objects.get(profile=user_profile, estado='No Pagado')
    # Cambia el estado del pedido
    menu.estado = 'Pagado'
    # Guardamos los cambios
    menu.save()
    messages.success(request, 'Gracias por tu compra! Este es el inicio de una nueva vida saludable.')
    return redirect('home')