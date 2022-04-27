from django.core.exceptions import ValidationError


def only_char_validator(value):
    for el in value:
        if not el.isalpha():
            raise ValidationError('Value must contain only letters!')


def only_digit_validator(value):
    for el in value:
        if not el.isdigit():
            raise ValidationError('Value must contain only numbers!')


def image_size_validator_in_mb(image):
    if image:
        if image.size > 4 * 1024 * 1024:
            raise ValidationError("Image file too large. Must be under 4mb")
        return image
    else:
        raise ValidationError("Couldn't read uploaded image")
