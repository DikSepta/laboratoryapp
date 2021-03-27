from django import forms
from appointment.models import Appointment
from services.models import Services

class MakeAppointmentForm(forms.ModelForm):
    
    
    class Meta :
        model = Appointment
        fields = ['service', 'date']

    # def clean(self):
    #     print(self.cleaned_data)
    #     service = Services.objects.get(service=self.cleaned_data.get('service'))
    #     self.cleaned_data['service'] = service
    #     return         super(MakeAppointmentForm, self)