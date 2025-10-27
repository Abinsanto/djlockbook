# from django import forms
# ##contact
# from.models import customer
#
#
# ##contact store in db
# class customerform(forms.ModelForm):
#     class Meta:
#         model=customer
#         fields='__all__'


from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        # fields = '__all__'
        exclude = ['user']
