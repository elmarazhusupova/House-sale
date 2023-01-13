from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs= {'placeholder': 'Ваше имя'}
        )
    ) 

    email = forms.EmailField(
        widget=forms.EmailInput(
            {'placeholder': 'E-mail'}
        )
    )

    number = forms.CharField(
        widget=forms.NumberInput(
            {'placeholder': 'Телефон номера'}
        )
    )

    message = forms.CharField(
        min_length=10,
        widget=forms.TextInput(
            attrs={'placeholder':'Сообщение','class': 'form_container'}
        )
    )
