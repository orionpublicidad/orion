from django.core.files.uploadedfile import UploadedFile
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from pip._internal.commands import create_command
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from Orion.models import models_comproba
from Orion.forms import ComprobaForm

class ComprobaListView(ListView):
    model = models_comproba.Comproba
    template_name = 'MoConfiguracion/list_comproba.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in models_comproba.Comproba.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Comprobantes'
        context['create_url'] = reverse_lazy('ComprobaAdd')
        context['list_url'] = reverse_lazy('ComprobaList')
        context['entity'] = 'Comprobantes'
        return context

class ComprobaCreateView(CreateView):
    model = models_comproba.Comproba
    form_class = ComprobaForm
    template_name = 'MoConfiguracion/create_comproba.html'
    success_url = reverse_lazy('ComprobaList')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Comprobante'
        context['entity'] = 'Comprobantes'
        context['list_url'] = reverse_lazy('ComprobaList')
        context['action'] = 'add'
        return context


class ComprobaUpdateView(UpdateView):
    model = models_comproba.Comproba
    form_class = ComprobaForm
    template_name = 'MoConfiguracion/create_comproba.html'
    success_url = reverse_lazy('ComprobaList')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Comprobante'
        context['entity'] = 'Comprobantes'
        context['list_url'] = reverse_lazy('ComprobaList')
        context['action'] = 'edit'
        return context

class ComprobaDeleteView(DeleteView):
    model = models_comproba.Comproba
    form_class = ComprobaForm
    template_name = 'MoConfiguracion/delete_comproba.html'
    success_url = reverse_lazy('ComprobaList')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Comprobante'
        context['entity'] = 'Comprobantes'
        context['list_url'] = reverse_lazy('ComprobaList')
        return context