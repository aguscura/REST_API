from django import forms

class operacionform(forms.Form):

    operacion_math = forms.ChoiceField(choices=[("SUMA","SUMA"),("RESTA", "RESTA"),("MULTIPLICACION", "MULTIPLICACION"), ("DIVISION" ,"DIVISION")]) #Suma, resta, etc.
    num1 = forms.IntegerField()
    num2 = forms.IntegerField()