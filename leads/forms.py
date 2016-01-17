from django import forms
from . import models
from django.core.validators import RegexValidator
from django.forms import inlineformset_factory, BaseInlineFormSet
from django.utils.safestring import mark_safe


class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class FormControlMixin(object):
    def __init__(self, **kwargs):
        super(FormControlMixin, self).__init__(**kwargs)
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
    languages = forms.ModelMultipleChoiceField(queryset=models.Languages.objects.all())

    class Meta:
        model = models.TourLeads
        fields = ('name', 'gender', 'languages', 'card_number', 'expiry_date', 'professional')

    def clean(self):
        card_number = self.cleaned_data.get('card_number')
        expiry_date = self.cleaned_data.get('expiry_date')
        if not card_number:
            message = 'Card number must not to be empty for expiry date'
            del self.cleaned_data['expiry_date']
            self._errors['card_number'] = self.error_class([message])
        elif card_number and not expiry_date:
            message = 'Empty value of expiry date'
            self._errors['card_number'] = self.error_class([message])
        else:
            return self.cleaned_data


class Language(FormControlMixin, forms.ModelForm):
    name = forms.CharField(label='Language', widget=forms.TextInput(attrs={'placeholder': 'Chinese'}),)

    class Meta:
        model = models.Languages
        fields = ('name',)


# LanguagesFormSet = inlineformset_factory(models.TourLeads, models.TourLeadsLanguage, form=Language, extra=1)
LanguagesFormSet = forms.formset_factory(Language)
