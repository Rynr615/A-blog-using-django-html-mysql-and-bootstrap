from django.shortcuts import render, redirect
from django.views.generic import ListView

from . import forms
from .models import Kontak

# Create your views here.
def KontakView(request):
    contact_form = forms.KontakForm(request.POST or None)
    if request.method == 'POST':
        if contact_form.is_valid():
            simpan_data = Kontak.objects.create(
                nama_lengkap = contact_form.cleaned_data.get('nama_lengkap'),
                jenis_kelamin = contact_form.cleaned_data.get('jenis_kelamin'),
                tanggal_lahir = contact_form.cleaned_data.get('tanggal_lahir'),
                alamat = contact_form.cleaned_data.get('alamat'),
                agree = contact_form.cleaned_data.get('agree'),
            )       
            return redirect('Contact:kontakList') 

    context = {
        'title' : 'Belajar Django',
        'kontak_saya' : contact_form,
        'formulir': 'Class Form'
    }
    return render(request, 'contact/contact_form.html', context)

class KontakList(ListView) :
    template_name = 'contact/kontak_list.html'
    queryset = Kontak.objects.all()