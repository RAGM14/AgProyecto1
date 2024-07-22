import csv
from django.shortcuts import render
from .forms import CSVUploadForm
from api_usuarios.usuarios.models import Usuario

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            reader = csv.reader(file.read().decode('utf-8').splitlines())
            for row in reader:
                Usuario.objects.create(
                    nombre=row[0],
                    apellido_paterno=row[1],
                    apellido_materno=row[2],
                    edad=row[3],
                    nombre_cuenta=row[4],
                    contrasena=row[5]
                )
            return render(request, 'carga/success.html')
    else:
        form = CSVUploadForm()
    return render(request, 'carga/upload.html', {'form': form})


# Create your views here.
