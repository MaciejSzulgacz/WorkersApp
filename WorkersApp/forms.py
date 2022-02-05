from django.forms import ModelForm
from .models import Worker


class WorkerCreateForm(ModelForm):
    class Meta:
        model = Worker
        fields = ['name', 'surname', 'age', 'profession', 'picture']
