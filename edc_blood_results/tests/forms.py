from django import forms
from edc_action_item.forms import ActionItemFormMixin
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators import FormValidator
from edc_lab_panel.panels import fbc_panel

from edc_blood_results.form_validator_mixins import BloodResultsFormValidatorMixin

from .models import BloodResultsFbc


class BloodResultsFbcFormValidator(BloodResultsFormValidatorMixin, FormValidator):
    panels = [fbc_panel]


class BloodResultsFbcForm(ActionItemFormMixin, CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = BloodResultsFbcFormValidator

    def validate_against_consent(self):
        """Skip for tests"""
        pass

    class Meta:
        model = BloodResultsFbc
        fields = "__all__"