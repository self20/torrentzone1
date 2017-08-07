from django.forms import ModelForm
from .models import torrentModel

class torrentForm(ModelForm):
    # TODO: Define other fields here
    class Meta:
        model = torrentModel
        fields = ['torrentName','torrentLink']
