import os

from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.forms.widgets import CheckboxSelectMultiple
from django.utils.translation import gettext as _

from clinic.models import Doctor, Patient, SelfCertificationQuestion

from durationwidget.widgets import TimeDurationWidget

class TimeInput(forms.TimeInput):
	input_type = 'time'

class VolunteerForm(forms.ModelForm):
	credentials = forms.FileField(required=True)

	class Meta:
		model = Doctor
		fields = ['name', 'email', 'credentials', 'languages', 'notify', 'notify_interval', 'quiet_time_start', 'quiet_time_end', 'utc_offset', 'fcm_token', 'self_certification_questions', 'remarks']
		widgets = {
			'languages': CheckboxSelectMultiple(),
			'notify_interval': TimeDurationWidget(show_days=False, show_minutes=False, show_seconds=False),
			'quiet_time_start': TimeInput(),
			'quiet_time_end': TimeInput(),
			'self_certification_questions': CheckboxSelectMultiple(),
		}

	def clean_credentials(self):
		f = self.cleaned_data.get('credentials')

		ext = os.path.splitext(f.name)[-1].lower()
		if ext not in settings.ALLOWED_UPLOAD_EXTENSIONS:
			raise ValidationError(_("This type of file is not allowed."))

		if f.size > 20 * 1024 * 1024:
			raise ValidationError(_("Proof of credentials must be less than 20MB."))

		return f

	def clean_self_certification_questions(self):
		answered = self.cleaned_data.get('self_certification_questions')

		unanswered_count = self.fields['self_certification_questions'].queryset.exclude(id__in=answered.values_list('id', flat=True)).count()
		if unanswered_count > 0:
			raise ValidationError(_("You must confirm all items."))

		return answered

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = ['feedback_response', 'feedback_text']

class OrgRequestForm(forms.Form):
	org_name = forms.CharField(label=_("Name of organization"))
	owner_name = forms.CharField(label=_("Your name"))
	position = forms.CharField(label=_("Your position/title"))
	email = forms.EmailField()
	comments = forms.CharField(widget=forms.Textarea(), required=False)
