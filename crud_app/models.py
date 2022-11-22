from enum import unique
from tabnanny import verbose
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Bairros(models.Model):
    id_bairro = models.AutoField(primary_key=True)
    cod_bairro = models.CharField(max_length=10)  
    bairro = models.CharField(max_length=255)     
    uf = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'bairros'
        verbose_name_plural = 'Bairros'

    def __str__(self):
        return "{} - {}".format(self.bairro,self.uf)



class Cidades(models.Model):
    cod_cidade = models.AutoField(primary_key=True)
    cod_ibge = models.IntegerField()
    cidade = models.CharField(max_length=255)
    uf = models.ForeignKey('Estados', models.DO_NOTHING, db_column='uf')

    class Meta:
        managed = False
        db_table = 'cidades'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return "{} - {}".format(self.cidade,self.uf)



class Dimcontas(models.Model):
    desc_conta = models.CharField(max_length=255)
    grupo_conta = models.ForeignKey('Dimgrupocontas', models.DO_NOTHING, db_column='desc_grupo_conta', blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualiza = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'dimcontas'
        verbose_name_plural = 'Dimcontas'

    def __str__(self):
        return "{}".format(self.desc_conta)



class Dimgrupocontas(models.Model):
    desc_grupo_conta = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dimgrupocontas'
        verbose_name_plural = 'Dimgrupocontas'

    def __str__(self):
        return "{}".format(self.desc_grupo_conta)



NÃO = 0
SIM = 1

CHOICES_BOOL = (
    (NÃO, 'Não'),
    (SIM,'Sim'),
)



class Empresas(models.Model):
    cod_empresa = models.BigAutoField(primary_key=True)
    cod_projeto = models.ForeignKey('Projetos', models.DO_NOTHING, db_column='cod_projeto', blank=True, null=True)
    empresa = models.CharField(max_length=255, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualiza = models.DateTimeField(auto_now=True)
    safegold_ger = models.IntegerField(blank=True, null=True, default=1, choices=CHOICES_BOOL, verbose_name='Safegold Gerência? ')    
    cnpj = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresas'
        verbose_name_plural = 'Empresas'
        ordering = ['-cod_empresa']

    def __str__(self):
        return "{}".format(self.empresa)



class Estados(models.Model):
    cod_estado = models.IntegerField()
    cod_uf = models.IntegerField()
    estado = models.CharField(max_length=50)
    uf = models.CharField(primary_key=True, max_length=2)
    regiao = models.ForeignKey('Regioes', models.DO_NOTHING, db_column='regiao')

    class Meta:
        managed = False
        db_table = 'estados'        
        verbose_name_plural = 'Estados'

    def __str__(self):
        return "{}".format(self.estado)



class MatrizContaFornecedor(models.Model):
    cod_fornecedor = models.BigIntegerField()
    desc_fornecedor = models.CharField(max_length=255)
    id_conta = models.ForeignKey(Dimcontas, models.DO_NOTHING, db_column='id_conta', blank=True, null=True)
    data_importacao = models.DateField(blank=True, null=True)
    cod_projeto = models.ForeignKey('Projetos', models.DO_NOTHING, db_column='cod_projeto', blank=True, null=True)
    cod_empresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='cod_empresa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matriz_conta_fornecedor'
        verbose_name_plural = 'Matriz Conta Fornecedor'
    def __str__(self):
        return "FORNECEDOR: {} - CONTA: {}".format(self.desc_fornecedor, self.id_conta)



class Pais(models.Model):
    cod_pais = models.BigAutoField(primary_key=True)
    pais = models.CharField(max_length=60, blank=True, null=True)
    pais_pt = models.CharField(max_length=60, blank=True, null=True)
    sigla = models.CharField(max_length=2, blank=True, null=True)
    bacen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pais'
        verbose_name_plural = 'Paises'      
          
    def __str__(self):
        return "{}".format(self.pais)

class Projetos(models.Model):
    id_user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_user', blank=True, null=True)    
    cod_projeto = models.BigAutoField(primary_key=True)
    projeto = models.CharField(max_length=255, blank=True, null=True)
    chave_integracao = models.CharField(max_length=255, blank=True, null=True)
    cod_usuario = models.IntegerField(blank=True, null=True)
    chave_inteligente = models.CharField(max_length=255, blank=True, null=True)
    cod_segmento = models.IntegerField(blank=True, null=True)
    ativo = models.IntegerField(blank=True, null=True)
    cor = models.CharField(max_length=255, blank=True, null=True)
    avatar_nome_arq = models.CharField(max_length=255, blank=True, null=True)
    avatar_tipo = models.CharField(max_length=255, blank=True, null=True)
    avatar_tamanho = models.BigIntegerField(blank=True, null=True)
    avatar_atualizacao = models.DateTimeField(blank=True, null=True)
    tipo_endereco = models.CharField(max_length=255, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    end_numero = models.CharField(max_length=255, blank=True, null=True)
    end_compl = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=255, blank=True, null=True)
    end_estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='end_estado', blank=True, null=True)
    data_fecha = models.DateField(blank=True, null=True)
    id_importacao = models.IntegerField(blank=True, null=True)
    end_cidade = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)
    resp_email = models.CharField(max_length=255, blank=True, null=True)
    resp_nome = models.CharField(max_length=255, blank=True, null=True)
    resp_cod = models.CharField(max_length=255, blank=True, null=True)
    job_state = models.CharField(max_length=255, blank=True, null=True)
    job_report = models.TextField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    data_criacao = models.DateTimeField()
    data_atualiza = models.DateTimeField()
    legacy_id = models.IntegerField(blank=True, null=True)
    safegold_ger = models.IntegerField(blank=True, null=True)
    cod_sub_segmento = models.IntegerField(blank=True, null=True)
    sandbox = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'projetos'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return "{}".format(self.projeto)



class Regioes(models.Model):
    cod_regiao = models.AutoField(primary_key=True)
    regiao = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'regioes'
        verbose_name_plural = 'Regioes'        
    
    def __str__(self):
        return "{}".format(self.regiao)