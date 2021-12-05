from django.forms import ModelForm
from .models import Customer
from .models import Users

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
    
class CustomerForm(ModelForm):
	class Meta:
		model = Users
		fields = '__all__'