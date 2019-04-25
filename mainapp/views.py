from django.shortcuts import render

def main(request):
    context = {'copyrigth': {'rigth': 'all rigth reserved'}}
    return render(request, 'mainapp/index.html', context)

def catalog(request):
    context = {'links_menu': [
{'href': 'main', 'name': 'Главная страница'},
{'href': 'catalog', 'name': 'Каталог'},
{'href': 'contacts', 'name': 'Контакты'},
{'href': 'registration', 'name': 'Регистрация'},
]}
    return render(request, 'mainapp/catalog.html', context)

def contacts(request):
    return render(request, 'mainapp/contacts.html')

def registration(request):
    return render(request, 'mainapp/registration.html')

