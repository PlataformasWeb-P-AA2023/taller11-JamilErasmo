from django import forms

class DepartamentoForm(forms.Form):
    propietario = forms.CharField(max_length=200)
    costo = forms.DecimalField(max_digits=8, decimal_places=2)
    numero_cuartos = forms.IntegerField()

    def clean_costo(self):
        costo = self.cleaned_data.get('costo')
        if costo and costo > 100000:
            raise forms.ValidationError("El costo no puede ser mayor a $100,000.")
        return costo

    def clean_numero_cuartos(self):
        numero_cuartos = self.cleaned_data.get('numero_cuartos')
        if numero_cuartos == 0 or numero_cuartos > 7:
            raise forms.ValidationError("El número de cuartos debe ser mayor a 0 y no mayor a 7.")
        return numero_cuartos

    def clean_propietario(self):
        propietario = self.cleaned_data.get('propietario')
        palabras = propietario.split()
        if len(palabras) < 3:
            raise forms.ValidationError("El nombre completo del propietario debe tener al menos 3 palabras.")
        return propietario
    
    
