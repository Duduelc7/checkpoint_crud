from django.urls import path
from crud_app import views

app_name = 'crud_app'

urlpatterns = [

    ###############################     EMPRESA     ###############################
    #path('empresa/',views.EmpresaListView.as_view(),name='empresa-list'),
    #path('empresa/',views.empresalistview,name='empresa-list'),
    path('empresa/create/',views.EmpresaCreateView.as_view(),name='empresa-create'),
    path('empresa/update/<int:pk>/',views.EmpresaUpdateView.as_view(),name='empresa-update'),
    path('empresa/delete/<int:pk>/',views.EmpresaDeleteView.as_view(),name='empresa-delete'),
    path('empresa/detail/<int:pk>/',views.EmpresaDetailView.as_view(),name='empresa-detail'),
    #path('empresa/add',views.cadastro_empresa,name='add-empresa'  ),
    path('empresa/save',views.saveempresa,name='saveempresa'),
    path('empresa/add',views.insertempresa,name='insert'),
    path('empresa/update',views.update_all, name= 'update_all'),
    # path('empresa/pag',views.paginacao, name= 'paginacao'),
    path('empresa/delete',views.delete_empresa,name='delete'),
    path('empresa/',views.ativos,name='empresa-list'),

    
    




    ###############################     PROJETO     ###############################
    path('projeto/',views.ProjetoListView.as_view(),name='projeto-list'),
    path('projeto/create/',views.ProjetoCreateView.as_view(),name='create'),
    path('projeto/update/<int:pk>/',views.EmpresaUpdateView.as_view(),name='update'),
    path('projeto/delete/<int:pk>/',views.ProjetoDeleteView.as_view(),name='delete'),
    path('projeto/detail/<int:pk>/',views.ProjetoDetailView.as_view(),name='detail'),
    
    ###############################    DIMCONTAS    ###############################
    path('conta/',views.DimContasListView.as_view(),name='conta-list'),
    path('conta/create/',views.DimContasCreateView.as_view(),name='conta-create'),
    path('conta/update/<int:pk>/',views.DimContasUpdateView.as_view(),name='conta-update'),
    path('conta/delete/<int:pk>/',views.DimContasDeleteView.as_view(),name='conta-delete'),
    path('conta/detail/<int:pk>/',views.DimContasDetailView.as_view(),name='conta-detail'),

    ###############################  CONTAFORNECEDOR     ###############################
    path('matrizfornecedorconta/',views.MatrizFornecedorListView.as_view(),name='matriz-list'),
    # path('matrizfornecedorconta/create/',views.MatrizFornecedorCreateView.as_view(),name='matriz-create'),
    # path('matrizfornecedorconta/update/<int:pk>/',views.MatrizFornecedorUpdateView.as_view(),name='matriz-update'),
    path('matrizfornecedorconta/delete/<int:pk>/',views.MatrizFornecedorDeleteView.as_view(),name='matriz-delete'),
    path('matrizfornecedorconta/detail/<int:pk>/',views.MatrizFornecedorDetailView.as_view(),name='matriz-detail'),




    ############# TESTE     




        ############################### CSV AND PDF ###############################
    path('projeto/csv',views.export_csv,name='export-csv'),
    # path('projeto/pdf',views.export_pdf,name='export-pdf'),



]

