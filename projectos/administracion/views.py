from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView, View
from .models import Proyectos
from .forms import ProyectosForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

class AdministracionView(LoginRequiredMixin, TemplateView):
    template_name = "administracion/index.html"
    extra_content = {"proyectos":Proyectos.objects.all()}
    def get_context_data(self,**kwargs):
       context = super().get_context_data(**kwargs)
       context["proyectos"] = Proyectos.objects.all()
       fichero = open('ip_visitantes.txt', 'r')
       visitas = fichero.readlines()
       context["visitas"] = visitas
       return context

class ProyectoCreate(LoginRequiredMixin, FormView):
    model = Proyectos
    template_name = "administracion/create.html"
    form_class = ProyectosForm

    def form_valid(self, form):
        Proyectos.objects.create(**form.cleaned_data)
        return redirect('index')

@login_required
def deleteProyecto(request, id):
    classroom = Proyectos.objects.get(id=id)
    classroom.delete()
    return redirect("index")