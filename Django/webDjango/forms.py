from django import forms
from users.models import User




class Registro(forms.Form):
    username = forms.CharField(required=True, min_length= 4, max_length= 150 ,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de usuario'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@gmail.com'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'introduzca su contraseña '}))
    password2 = forms.CharField(label='Confirmar password',required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirmar su contraseña '}))
    

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('usuario creado')
        return username


    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('correo ya creado')
        
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'El password no coincide')

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')
        )