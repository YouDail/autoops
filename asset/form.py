from    django import forms
from .models import asset,system_users
from	django.forms	import		ValidationError

# from django.utils.translation import gettext_lazy as _


class AssetForm(forms.ModelForm):
    class Meta:
        model = asset
        fields = '__all__'
        # exclude = ('ps',)
        # fields = [
        #    'id', 'network_ip', 'manage_ip', 'model', 'data_center', 'cabinet', 'position',
        #     'sn', 'cpu', 'memory', 'disk', 'port', 'ship_time', 'end_time', 'product_line', 'ps'
        # ]
        labels={
            "network_ip":"外网IP"
        }
        widgets = {
            'ship_time': forms.DateInput(
                attrs={'type': 'date',}
            ),
            'end_time': forms.DateInput(
                attrs={'type': 'date', }
            ),
            'ps': forms.Textarea(
                attrs={'cols': 80, 'rows': 3}
            ),
            'product_line': forms.SelectMultiple(
                attrs={'class': 'select2',
                       'data-placeholder': ('选择产品线')}),
            # 'admin_user': forms.Select(
            #     attrs={'class': 'select2',
            #            'data-placeholder': ('Select asset admin user')}),
        }
        help_texts = {
            # 'network_ip': '必填项目',
            'network_ip': ('必填项目'),
        }
        error_messages = {
            'model':{
                'max_length': ('太短了'),
            }
        }

    # def clean_model(self):
    #     model = self.cleaned_data['model']
    #     if len(model) < 3:
    #         raise ValidationError("不能短于3个字符")
    #     return model

    #
    # def clean(self):
    #     cleaned_data = super(PublisherForm, self).clean()
    #     network_ip = cleaned_data.get('network_ip')
    #     if len(network_ip) < 4:
    #         raise ValidationError('network_ip 不能小于4')


class SystemUserForm(forms.ModelForm):
    class Meta:
        model = system_users
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(
            ),
            'ps': forms.Textarea(
                attrs={'cols': 80, 'rows': 3}
            ),
        }
        help_texts = {

            'password': ('在更新页面,如果不想修改当前用户的密码,保持为空即可.'),
        }
