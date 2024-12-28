from django.contrib import admin

from .models import Produtos


@admin.register(Produtos)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome','preco','estoque','imagem','slug','criado','modificado','ativo']



