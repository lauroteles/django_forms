from django import forms
from django.core.mail.message import EmailMessage
from .models import Produtos

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome',max_length=100)
    email = forms.EmailField(label='E-mail',max_length=100)
    assunto = forms.CharField(label='Assunto',max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='Email enviado pelo sistema Django2',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            headers={'Reply-To': email},
            to=['contato2@seudominio.com.br']
        )
        mail.send()

class ProdutoModelForm(forms.Form):
    class Meta:
        model = Produtos
        fields = ['nome','preco','estoque','imagem']
        
