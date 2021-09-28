from django import forms

from allauth.account.forms import SignupForm


class StuffExchangeSignupForm(SignupForm):
    phonenumber = forms.CharField()
    vk_link = forms.CharField(required=False)
    telegram_link = forms.CharField(required=False)
    city = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def custom_signup(self, request, user):
        user.vk_link = self.cleaned_data['vk_link']
        user.telegram_link = self.cleaned_data['telegram_link']
        user.city = self.cleaned_data['city']
        user.phonenumber = self.cleaned_data['phonenumber']
        user.save()
