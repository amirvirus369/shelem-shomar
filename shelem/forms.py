from captcha.fields import CaptchaField
from django import forms

class Register(forms.Form):
    phone_number = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'class':'w-full bg-slate-900 border border-slate-700 rounded-xl pr-9 pl-3 py-2 text-sm text-slate-100 placeholder-slate-600 focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 transition-all','placeholder':'09....'}))
    full_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'w-full bg-slate-900 border border-slate-700 rounded-xl pr-9 pl-3 py-2 text-sm text-slate-100 placeholder-slate-600 focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 transition-all','placeholder':'مثلا امیرمهدی '}))
    avatar = forms.ImageField(required=False,widget=forms.ClearableFileInput(attrs={'class':'hidden','id':'avatarInput'}))
    captcha = CaptchaField()
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      self.fields['captcha'].widget.widgets[1].attrs.update({
        'class': 'bg-white text-black border rounded px-3 py-2 w-full'
     })