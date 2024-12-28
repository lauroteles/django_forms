from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm,ProdutoModelForm
from .models import Produtos

def index(request):
    context = {
        'produtos': Produtos.objects.all()
    }
    return render(request,'index.html',context)

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            
            form.send_email()

            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            messages.success(request,'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request,'Erro ao enviar e-mail!')

    context = {
        'form': form
    }
    return render(request,'contato.html',context)


def produto(request):
    print(f'Usuario:{request.user}')
    if str(request.user) == 'AnonymousUser':
        messages.error(request,'É necessário estar logado para cadastrar produtos!')
        return render(request,'index.html')
    
    if str(request.user) != 'AnonymousUser':

        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,'Produto salvo com sucesso!')
                form = ProdutoModelForm()
        return render(request,'produto.html')



