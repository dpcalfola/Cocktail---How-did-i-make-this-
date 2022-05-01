from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserResisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# class UserResisterFormA(forms.ModelForm):
#     password_1 = forms.CharField(label='password_1', widget=forms.PasswordInput)
#     password_2 = forms.CharField(label='password_2', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#
#         # 여기서 fields로 추가 할 수 잇는 필드는 User Model에 미리 선언되어 있는 필드만 가능
#         # 가능한 fields 목록:
#         # username, first_name, last_name, email, is_staff, is_active, date_joined
#         # 따라서
#         # fields = ['nickname'] 은 사용할 수 없음. Meta 클래스가 아닌 위에서 필드 타입과 함꼐 선언해야함
#         fields = ['email']
#
#     def clean_password_2(self):
#         clean_data = self.cleaned_data
#
#         if clean_data['password_1'] != clean_data['password_2']:
#             raise forms.ValidationError('패스워드가 일치하지 않습니다.')
#         return clean_data['password_2']
