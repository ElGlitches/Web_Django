from .models import DireccionEnvio
from .forms import DireccionEnvioForm
from django.shortcuts import render 
from django.shortcuts import get_object_or_404 
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.messages.views import SuccessMessageMixin 
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
# Create your views here.

class DireccionEnvioListView(LoginRequiredMixin,ListView):
    login_url='login'
    model = DireccionEnvio
    template_name = 'direccion_envios/direccion_envio.html'

    def get_queryset(self):
        return DireccionEnvio.objects.filter(user=self.request.user).order_by('-default')


@login_required(login_url='login')
def FormularioDir(request):
    form = DireccionEnvioForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        direccion_envio = form.save(commit=False)
        direccion_envio.user = request.user
        direccion_envio.default = not DireccionEnvio.objects.filter(user=request.user).exists()
        direccion_envio.save()

        messages.success(request, 'Direccion creada correctamente')
        return redirect('direccion_envio')

    return render(request,'direccion_envios/formulario.html',{
        'form':form

    })

class ActualizarDireccionEnvio(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url='login'
    model = DireccionEnvio
    form_class = DireccionEnvioForm
    template_name = 'direccion_envios/actualizar.html'
    success_message = 'Direccion actualizada correctamente'

    def get_success_url(self):
        return reverse('direccion_envio')

class EliminarDireccionEnvio(LoginRequiredMixin,DeleteView):
    login_url='login'
    model = DireccionEnvio
    template_name = 'direccion_envios/eliminar.html'
    success_url = reverse_lazy('direccion_envio')

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().default:
            return redirect('direccion_envio')
        
        if request.user.id != self.get_object().user.id:
            return redirect('index')
        
        return super(EliminarDireccionEnvio, self).dispatch(request, *args, **kwargs)

@login_required(login_url='login')    
def FuncionDefault(request, pk):
        direccion_envio = get_object_or_404(DireccionEnvio, pk=pk)

        if request.user.id!= direccion_envio.user.id:
            return redirect('index')
        
        if request.user.has_direccion_envio():
            request.user.direccion_envio.update_default()

        direccion_envio.update_default(True)

        return redirect('direccion_envio')