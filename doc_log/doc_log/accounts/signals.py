from django.db.models import signals
from django.dispatch import receiver
import os

from doc_log.accounts.models import DoctorsModel


@receiver(signals.pre_save, sender=DoctorsModel)
def delete_old_file(sender, instance, **kwargs):
    # on creation, signal callback won't be triggered
    if instance._state.adding and not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).profile_picture
    except sender.DoesNotExist:
        return False

    # comparing the new file with the old one
    file = instance.profile_picture
    if not old_file == file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


@receiver(signals.post_delete, sender=DoctorsModel)
def del_profile_pic(instance, **kwargs):
    pic = instance.profile_picture
    if pic:
        try:
            os.remove(pic.path)
        except:
            return
    # ask for optimisation
