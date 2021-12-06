from django.forms import ModelForm

from .models import Bon

class BonForm(ModelForm):
    class Meta:
        model = Bon
        fields = '__all__'
        exclude = ('owner', 'ownerName' , 'filename')
        