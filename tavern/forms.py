""" Opentavern Forms """

from django.forms import ModelForm, DateField
from .models import TavernGroup, Event


class CreateGroupForm(ModelForm):
    """ CreateGroupForm """
    class Meta:
        model = TavernGroup
        fields = ['name', 'group_type', 'description',
                  'members_name', 'country', 'city']


class CreateEventForm(ModelForm):
    """ CreateEventForm """
    starts_at = DateField(input_formats=['%d/%m/%Y', '%d-%m-%Y'])
    end_at = DateField(input_formats=['%d/%m/%Y', '%d-%m-%Y'])

    class Meta:
        model = Event
        fields = ['group', 'name', 'description', 'starts_at',
                  'end_at', 'location']
