from datetime import timedelta
from django import forms
from . import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import inlineformset_factory, BaseInlineFormSet
from django.utils import timezone
from django.utils.safestring import mark_safe


class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class FormControlMixin(object):
    def __init__(self, *args, **kwargs):
        super(FormControlMixin, self).__init__(*args, **kwargs)
        for key, field in self.fields.iteritems():
            if key != 'gender' and key != 'professional':
                field.widget.attrs.update({'class': 'form-control'})


class TourLeadCreateForm(FormControlMixin, forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'John Doe'}))
    card_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'XXXXXXXXXXXX'}),
                                  validators=[RegexValidator(
                                      regex='^[XTW0-9]*$',
                                      message='Only numbers and capital letters: X, T, W are allowed'
                                  )])
    gender = forms.ChoiceField(label='Gender', widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                               choices=models.TourLeads.GENDER_CHOICES)
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': '2015-12-01'}))
    professional = forms.ChoiceField(label='Professional', widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                     choices=models.TourLeads.PROF_CHOICES)

    class Meta:
        model = models.TourLeads
        fields = ('name', 'gender', 'card_number', 'expiry_date', 'professional')

    def clean(self):
        super(TourLeadCreateForm, self).clean()



    def clean_expiry_date(self):
        card_number = self.cleaned_data.get('card_number')
        expiry_date = self.cleaned_data.get('expiry_date')
        if not card_number and expiry_date:
            message = 'Card number must not to be empty for expiry date'
            # self._errors['card_number'] = self.error_class([message])
            raise ValidationError(message)
        if card_number and not expiry_date:
            message = 'Empty value of expiry date'
            self._errors['expiry_date'] = self.error_class([message])
            raise ValidationError(message)
        else:
            time_futur = (timezone.now() + timedelta(days=180)).date()
            if self.cleaned_data['expiry_date'] < time_futur:
                message = 'Has to be at least 6 months into the future'
                self._errors['expiry_date'] = self.error_class([message])
                raise ValidationError(message)

    def clean_card_number(self):
        card_number = self.cleaned_data.get('card_number')
        if len(card_number) < 8:
            raise ValidationError('Card number must contain 8 or 16 character')

class TourLeadsLanguagesForm(FormControlMixin, forms.ModelForm):
    tourlead = forms.HiddenInput()

    class Meta:
        model = models.TourLeadsLanguages
        exclude = ['id', ]

    def __init__(self, *args, **kwargs):
        super(TourLeadsLanguagesForm, self).__init__(*args, **kwargs)
        for field in self.fields.itervalues():
            field.widget.attrs['class'] += ' select_language'


class LanguagesInlineFormset(BaseInlineFormSet):
    def clean(self):
        super(LanguagesInlineFormset, self).clean()
        language = self.forms[0].cleaned_data.get('language')
        if not language:
            message = 'Must have at least one language'
            raise forms.ValidationError(message)

LanguagesFormSet = inlineformset_factory(
    models.TourLeads,
    models.TourLeadsLanguages,
    extra=1,
    can_delete=True,
    form=TourLeadsLanguagesForm,
    formset=LanguagesInlineFormset,
    max_num=4,
)
