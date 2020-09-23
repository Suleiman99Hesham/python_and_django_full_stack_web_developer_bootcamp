from django.shortcuts import render
from basicapp.forms import FormName

# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def Form_name_view(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)
        
        if form.is_valid():
            print('Validation Success!')
            print('name: '+form.cleaned_data['name'])
            print('email: '+form.cleaned_data['email'])
            print('text: '+form.cleaned_data['text'])
            form = FormName()
    return render(request, 'basicapp/form_page.html', {'form' : form})
    