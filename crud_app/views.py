from django.shortcuts import render , redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,ListView,CreateView,DeleteView,UpdateView,DetailView)
from . import models
from .forms import EmpresaForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
from django.core.paginator import Paginator
from django.db.models import Q
import datetime
import csv
from django.contrib import auth, messages



class IndexView(TemplateView):
     template_name = 'base.html'



#############################     EMPRESA     #############################
def ativos(request):
    if request.user.is_authenticated:
        id = request.user.id
        user_table = models.Projetos.objects.filter(id_user = id)
        user = user_table.all().values('cod_projeto')

        projetos_ativos_select = user_table.filter(ativo='1').values()  # ---> filtro pro select

        projetos_ativos = user_table.values('cod_projeto') # ---> tabela com todos
        empresa = models.Empresas.objects.filter(cod_projeto__in=projetos_ativos)
        empresa_all = models.Empresas.objects.filter(cod_projeto__in=user)
        #        projetos_ativos = user_table.filter(ativo='1').values('cod_projeto') # ---> tabela só com ativos

        projetos = request.POST.get('projeto', None)
        

        #print(projeto)
        
        projetos_final = user_table.filter(cod_projeto=projetos).values() #
        tabela_geral = user_table.filter(cod_projeto=projetos).values('cod_projeto') #
        teste = models.Empresas.objects.filter(cod_projeto__in=tabela_geral)
        print(teste)
        dados = {
            'projetos_ativos': projetos_ativos_select,
            'user': empresa_all,
            'empresa': empresa,
            'projetos_final': projetos_final,
            'teste': teste
        }
       # print('dashboard OK')
        return render(request,'crud_app/empresa/tabela.html', dados)


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
    print(len(cnpj))
    if models.Empresas.objects.filter(cnpj=cnpj).exists(): # ----> validação para cnpj existentes
        messages.error(request, 'esse cnpj ja existe')
    # if len(cnpj) >= 17:
    #     messages.error(request, 'invalido')
    else:

        try:    
            #print(projeto,empresa,safegold_ger,cnpj)
            empresa = models.Empresas(cod_projeto=projeto, empresa=empresa, safegold_ger=safegold_ger, cnpj=cnpj)
            #print(empresa)
            empresa.save()
            empresa_data={"cod_empresa": empresa.cod_empresa,"data_cadastro":empresa.data_cadastro,"error":False,"errorMensage":"Empresa adicionada com Sucesso"}
            empresa_data['detail'] = "<a href='/app/empresa/detail/"+str(empresa.pk)+"/' class='mx-3' title='Detalhar Conta'><i class='fa-solid fa-up-right-and-down-left-from-center'></i></a>"
            empresa_data['delete'] = "<a href='/app/empresa/delete/"+str(empresa.pk)+"/' class='mx-3' title='Excluir Conta'><i class='fa-solid fa-trash-can'></i></a>"


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

@csrf_exempt
def delete_empresa(request):
    id=request.POST.get("cod_empresa")
    print(id)
    try:
        empresa=models.Empresas.objects.get(cod_empresa=id)
        empresa.delete()
        empresa_data={"error":False,"errorMessage":"Deleted Successfully"}
        return JsonResponse(empresa_data,safe=False)
    except:
        empresa_data={"error":True,"errorMessage":"Failed to Delete Data"}
        return JsonResponse(empresa_data,safe=False)
    
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
    success_url = reverse_lazy("crud_app:empresa-list")

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




### CSV PDF


def export_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']= 'attachment; filename=Empresas'+str(datetime.datetime.now()) +'.csv'


    write=csv.writer(response)
    write.writerow(['COD_EMPRESA', 'COD_PROJETO', 'EMPRESA', 'DATA_CADASTRO', 'DATA_ATUALIZA', 'SAFEGOLD_GER', 'CNPJ'])

    empresa = models.Empresas.objects.all()

    for emp in empresa:
        write.writerow([emp.cod_empresa,emp.cod_projeto, emp.empresa, emp.data_cadastro, emp.data_atualiza, emp.safegold_ger, emp.cnpj])


    return response





######### LIST VIEW with API
from . import serializers

from rest_framework import viewsets

class EmpresaserializerViewSet(viewsets.ModelViewSet):
    queryset = models.Empresas.objects.all()
    serializer_class = serializers.EmpresasSerializer

class MatrizContaFornecedorViewSet(viewsets.ModelViewSet):
    queryset = models.MatrizContaFornecedor.objects.all()
    serializer_class = serializers.MatrizContaFornecedorSerializer

class ProjetosViewSet(viewsets.ModelViewSet):
    queryset = models.Projetos.objects.all()
    serializer_class = serializers.ProjetosSerializer

class DimcontasViewSet(viewsets.ModelViewSet):
    queryset = models.Dimcontas.objects.all()
    serializer_class = serializers.DimcontasSerializer






