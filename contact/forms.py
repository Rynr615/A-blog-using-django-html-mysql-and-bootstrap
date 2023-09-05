from django import forms

class KontakForm(forms.Form):
    nama_lengkap = forms.CharField()
    TAHUN = range(1930, 2024)
    tanggal_lahir = forms.DateField(required=False, widget=forms.SelectDateWidget(years=TAHUN, attrs={
        'class' : 'form-control col-sm-4'
    }))
    GENDER = [
        ('p', 'pria'),
        ('w', 'wanita'),
    ]
    jenis_kelamin = forms.ChoiceField(choices=GENDER)  # Corrected field name
    alamat = forms.CharField(widget=forms.Textarea)
    agree = forms.BooleanField(required=False)



    # null_boolean_field = forms.NullBooleanField(disabled=True)
    # integer_field = forms.IntegerField(disabled=True)
    # decimal_field = forms.DecimalField(disabled=True)
    
    #date_time
    # TAHUN = range(1930, 2024)
    # tanggal_lahir = forms.DateField(required=False, widget=forms.SelectDateWidget(years=TAHUN))
    # time_field = forms.TimeField(required=False)
    # date_time_field = forms.DateTimeField(required=False)
    
    #string_input
    # char_field = forms.CharField(widget=forms.Textarea)
    # email_field = forms.EmailField(label='Alamat Email : ')
    # file_path_field = forms.FilePathField(path='media')
    # regex_field = forms.RegexField(regex='')
    # slug_field = forms.SlugField()
    # url_field = forms.URLField(label='Link Web : ')
    
    # select_input
    # PILIHAN = [
    #     ('a', 'Pilihan 1'),
    #     ('b', 'Pilihan 2'),
    # ]
    
    # choice_field = forms.ChoiceField(choices=PILIHAN, widget=forms.SelectMultiple(attrs={
    #     'title' : 'Pilih lebih dari 1 : ',
    # }))
    # type_choice_field = forms.TypedChoiceField(choices=PILIHAN)
    # type_multi_choice = forms.TypedMultipleChoiceField(choices=PILIHAN)
    
    # # file input
    # file_upload = forms.FileField()
    # image_field = forms.ImageField()
    
    