from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from crud_app.models import Projetos
from django.contrib import auth, messages
# Create your views here.



def cadastro(request):
    if request.method == 'POST': 
        nome = request.POST['nome']
        email = request.POST['email']
        senha1 = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            messages.error(request, 'Nenhum campo pode estar em branco')
            print('O Campo não pode ficar em branco')
            return redirect(cadastro)
        if not email.strip():
            messages.error(request, 'Nenhum campo pode estar em branco')
            print('O Campo email não pode ficar em branco')
            return redirect(cadastro)

        if senha1 != senha2:
            messages.error(request,'As senhas não são iguais')
            print('As senhas estão diferentes')
            return redirect(cadastro)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Essa conta já está registrada')
            print('Usuario ja registrado')
            return redirect(cadastro)
        user = User.objects.create_user(username=nome,email=email,password=senha2)
        user.save()
        messages.success(request, 'Conta criada com sucesso')
        print('Usuario Salvo com sucesso')

        print(nome, email, senha1, senha2)
        print('usuario cadastrado')
        return redirect('login')
    else:        
        return render(request,'auth/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            messages.error(request, 'Os campos não podem estar em branco!')
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                request.session.set_test_cookie()
                next_page = request.POST.get('next')
                print(next_page)
                print(f'Login de {nome} realizado com sucesso')
                return redirect('dashboard')

        else:
            messages.error(request, 'O usuário não está cadastrado!')
            print('O usuário não está cadastrado!')
            return redirect('login')

    return render(request, 'auth/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def dashboard(request):
    if request.user.is_authenticated:
        if request.session.test_cookie_worked():
            print ("The test cookie worked!!!")
            request.session.delete_test_cookie()
        id = request.user.id
        projetos = Projetos.objects.filter(id_user=id).values()
        ativos = Projetos.objects.filter(id_user = id)
        projetos_ativos = ativos.filter(ativo='1').values()
        print(projetos)
        dados = {
            'projetos': projetos,
            'projetos_ativos': projetos_ativos
        }
        print('dashboard OK')
        return render(request,'auth/dashboard.html', dados)
    else:
        return redirect('login')

