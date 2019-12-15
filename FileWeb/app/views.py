from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from hashlib import md5
from .models import Field,after_update_field,before_update_field,notifier
from django.db.models.signals import post_save, pre_save


def home(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['myFile']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        field = Field()
        with uploaded_file.open() as f:
            strd = str(f.readlines()[0])
            field.fileField = uploaded_file.name
            field.charField = md5(strd.encode()).hexdigest()
        pre_save.connect(before_update_field)
        field.save()
        post_save.connect(after_update_field)
        redirect('/')
    return render(request, 'index.html')
