from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,ListView,CreateView,DeleteView,UpdateView,DetailView)
from . import models
from .forms import EmpresaForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
class IndexView(TemplateView):
     template_name = 'base.html'

#############################     EMPRESA     #############################
class EmpresaListView(ListView):
    template_name = 'crud_app/empresa/tabela.html'
    model = models.Empresas
    def get_context_data(self, **kwargs):
        context = super(EmpresaListView, self).get_context_data(**kwargs)
        context['form'] = EmpresaForm()
        return context

# def cadastro_empresa(request):
#     if request.POST:
#         form = EmpresaForm(request.POST)
#         if form.is_valid():           
#             form.save()
#         return redirect('crud_app:empresa-list')
    
#     return render(request,'crud_app/empresa/tabela.html', {'form': EmpresaForm})

# def get_empresa(self, request):
#     form = EmpresaForm(request.POST)
#     if form.is_valid():
#         teste = form.cleaned_data['empresa']
#         print(teste)


@csrf_exempt
def saveempresa(request):
    id=request.POST.get('id','')
    type = request.POST.get('type', '')
    value = request.POST.get('value', '')
    print(id,type,value)
    empresa = models.Empresas.objects.get(cod_empresa=id)
    if type == "empresa":
        empresa.empresa = value
    if type == "data_cadastro":
        empresa.data_cadastro = value
    if type == "data_atualiza":
        empresa.data_atualiza = value
    if type == "cnpj":
        empresa.cnpj = value

    empresa.save()
    return JsonResponse({"success":"Updated"})

@csrf_exempt
def insertempresa(request):
    teste=request.POST.get("cod_projeto")
    projeto = models.Projetos.objects.get(cod_projeto=teste)
    empresa = request.POST.get("empresa")
    safegold_ger = request.POST.get("safegold_ger")
    cnpj = request.POST.get("cnpj")
    print(projeto)

    try:    
        #print(projeto,empresa,safegold_ger,cnpj)
        empresa = models.Empresas(cod_projeto=projeto, empresa=empresa, safegold_ger=safegold_ger, cnpj=cnpj)
        #print(empresa)
        empresa.save()
        empresa_data={"cod_empresa": empresa.cod_empresa,"data_cadastro":empresa.data_cadastro,"error":False,"errorMensage":"Empresa adicionada com Sucesso"}
        empresa_data['detail'] = "<a href='/app/empresa/detail/"+str(empresa.pk)+"/' class='mx-3' title='Detalhar Conta'><i class='fa-solid fa-up-right-and-down-left-from-center'></i></a>"
        empresa_data['delete'] = "<a href='/app/empresa/delete/"+str(empresa.pk)+"/' class='mx-3' title='Excluir Conta'><i class='fa-solid fa-trash-can'></i></a>"
     
        # path('empresa/detail/<int:pk>/',views.EmpresaDetailView.as_view(),name='empresa-detail'),

        return JsonResponse(empresa_data,safe=False)
    except:
        empresa_data={"error":True,"errorMensage":"Failed to add"}
        return JsonResponse(empresa_data,safe=False)

@csrf_exempt
def update_all(request):
    data=request.POST.get("data")
    dict_data=json.loads(data)
    try:
        for dic_single in dict_data:
            empresa=models.Empresas.objects.get(cod_empresa=dic_single['cod_empresa'])
            empresa.empresa=dic_single['empresa']
            empresa.cnpj=dic_single['cnpj']
            empresa.save()
            print(empresa)
        stuent_data={"error":False,"errorMessage":"Updated Successfully"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Failed to Update Data"}
        return JsonResponse(stuent_data,safe=False)

# @csrf_exempt
# def delete_empresa(request):
#     id=request.POST.get("cod_empresa")
#     print(id)
#     try:
#         empresa=models.Empresas.objects.get(cod_empresa=id)
#         empresa.delete()
#         empresa_data={"error":False,"errorMessage":"Deleted Successfully"}
#         return JsonResponse(empresa_data,safe=False)
#     except:
#         empresa_data={"error":True,"errorMessage":"Failed to Delete Data"}
#         return JsonResponse(empresa_data,safe=False)

    
class EmpresaCreateView(CreateView):
    template_name = 'crud_app/empresa/cadastro.html'
    fields = ("empresa","cod_projeto","cnpj","safegold_ger")
    model = models.Empresas
    success_url = reverse_lazy("crud_app:empresa-list")

class EmpresaDeleteView(DeleteView):
     model = models.Empresas
     template_name= 'crud_app/empresa/excluir.html'
     success_url = reverse_lazy("crud_app:empresa-list")

class EmpresaUpdateView(UpdateView):
    template_name = 'crud_app/empresa/cadastro.html'
    fields = ("empresa","cod_projeto","cnpj","safegold_ger")
    model = models.Empresas
    success_url = reverse_lazy("crud_app:empresa-list")

class EmpresaDetailView(DetailView):
    model = models.Empresas
    template_name = 'crud_app/empresa/detail.html'
###########################################################################

#############################     PROJETO     #############################
class ProjetoListView(ListView):
    template_name = 'crud_app/tabelas/projeto-tabela.html'
    model = models.Projetos

class ProjetoCreateView(CreateView):
    template_name = 'crud_app/cadastro.html'
    fields = ("desc","fornecedor")
    model = models.Projetos
    success_url = reverse_lazy("crud_app:list")

class ProjetoDeleteView(DeleteView):
     model = models.Projetos
     template_name= 'crud_app/excluir-cadastro.html'
     success_url = reverse_lazy("crud_app:list")

class ProjetoUpdateView(UpdateView):
    template_name = 'crud_app/cadastro.html'
    fields = ("desc","fornecedor")
    model = models.Projetos
    success_url = reverse_lazy("crud_app:list")

class ProjetoDetailView(DetailView):
    model = models.Projetos 
    template_name = 'crud_app/detail.html'
###########################################################################

#############################    DIMCONTAS    #############################
class DimContasListView(ListView):
    template_name = 'crud_app/conta/tabela.html'
    model = models.Dimcontas

class DimContasCreateView(CreateView):
    template_name = 'crud_app/conta/cadastro.html'
    fields = ("desc_conta","id_grupo_conta")
    model = models.Dimcontas
    success_url = reverse_lazy("crud_app:conta-list")

class DimContasDeleteView(DeleteView):
     model = models.Dimcontas
     template_name= 'crud_app/conta/excluir.html'
     success_url = reverse_lazy("crud_app:conta-list")

class DimContasUpdateView(UpdateView):
    template_name = 'crud_app/conta/cadastro.html'
    fields = ("desc_conta","id_grupo_conta")
    model = models.Dimcontas
    success_url = reverse_lazy("crud_app:conta-list")

class DimContasDetailView(DetailView):
    model = models.Dimcontas 
    template_name = 'crud_app/conta/detail.html'
###########################################################################

############################# CONTAFORNECEDOR #############################
class MatrizFornecedorListView(ListView):
    template_name = 'crud_app/matriz/tabela.html'
    model = models.MatrizContaFornecedor

class MatrizFornecedorCreateView(CreateView):
    template_name = 'crud_app/matriz/cadastro.html'
    fields = ("desc","fornecedor")
    model = models.MatrizContaFornecedor
    success_url = reverse_lazy("crud_app:matriz-list")

class MatrizFornecedorDeleteView(DeleteView):
     model = models.MatrizContaFornecedor
     template_name= 'crud_app/matriz/excluir.html'
     success_url = reverse_lazy("crud_app:matriz-list")

class MatrizFornecedorUpdateView(UpdateView):
    template_name = 'crud_app/cadastro.html'
    fields = ("desc","fornecedor")
    model = models.MatrizContaFornecedor
    success_url = reverse_lazy("crud_app:matriz-list")

class MatrizFornecedorDetailView(DetailView):
    model = models.MatrizContaFornecedor 
    template_name = 'crud_app/matriz/detail.html'
###########################################################################




# testes


class EmpresaTeste(ListView):
    template_name = 'crud_app/empresa/tabelateste.html'
    model = models.Projetos




