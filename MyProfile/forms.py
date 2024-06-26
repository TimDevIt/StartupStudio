from django import forms
from django.forms import ModelForm
from MyProfile.models import Profile


class ProfileForm(ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'}))
    graduate_date = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'}), required=False)
    class Meta:
        model = Profile
        fields = (
            'firstname', 'lastname', 'sername',
            'birth_date', 'skills', 'status_id',
            'email', 'contact_info', 'links',
            'extrainfo', 'direction', 'graduate_date',
            'company_title', 'company_info', 'company_links',
            'job_title', 'department'
        )
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'sername': forms.TextInput(attrs={'class': 'form-control'}),
           # 'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'skills': forms.Textarea(attrs={'class': 'form-control'}),
            'status_id': forms.Select(attrs={'class': 'form-control'}, choices=Profile.STATUS_CHOICES),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7', 'maxlength': 18 }),
            'links': forms.TextInput(attrs={'class': 'form-control'}),
            'extrainfo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'direction': forms.TextInput(attrs={'class': 'form-control'}),
           # 'graduate_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'company_title': forms.TextInput(attrs={'class': 'form-control'}),
            'company_info': forms.Textarea(attrs={'class': 'form-control'}),
            'company_links': forms.TextInput(attrs={'class': 'form-control'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Устанавливаем поля необязательными по умолчанию
        for field in ['direction', 'graduate_date', 'company_title', 'company_info', 'company_links', 'job_title', 'department']:
            self.fields[field].required = False

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status_id')

        if status == 'student':
            if not cleaned_data.get('direction'):
                self.add_error('direction', 'Это поле обязательно для студентов.')
            if not cleaned_data.get('graduate_date'):
                self.add_error('graduate_date', 'Это поле обязательно для студентов.')

        elif status == 'teacher':
            if not cleaned_data.get('job_title'):
                self.add_error('job_title', 'Это поле обязательно для преподавателей.')
            if not cleaned_data.get('department'):
                self.add_error('department', 'Это поле обязательно для преподавателей.')

        elif status == 'company':
            if not cleaned_data.get('company_title'):
                self.add_error('company_title', 'Это поле обязательно для компаний.')
            if not cleaned_data.get('company_info'):
                self.add_error('company_info', 'Это поле обязательно для компаний.')
            if not cleaned_data.get('company_links'):
                self.add_error('company_links', 'Это поле обязательно для компаний.')

        return cleaned_data
