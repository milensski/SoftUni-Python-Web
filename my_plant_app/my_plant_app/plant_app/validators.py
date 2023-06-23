from django.core import exceptions


def validate_name_capital_letter(value):
    if not value[0].isupper():
        raise exceptions.ValidationError('Your name must start with a capital letter!')

def validate_plant_name(name):
    for ch in name:
        if not ch.isalnum():
            raise exceptions.ValidationError('Plant name should contain only letters!')