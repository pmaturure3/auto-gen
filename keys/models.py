from django.db import models
from datetime import datetime
from django.urls import reverse


def increment_reg_number_number():
    last_reg_number = Item.objects.all().order_by('id').last()
    if not last_reg_number:
        return 'KSD000001'
    reg_number = last_reg_number.reg_number
    width = 6
    reg_number_int = int(reg_number.split('KSD')[-1])
    new_reg_number_int = reg_number_int + 1
    formatted = (width - len(str(new_reg_number_int))) * \
        "0" + str(new_reg_number_int)
    new_reg_number = 'KSD' + str(formatted)
    return new_reg_number


class Item(models.Model):
    name = models.CharField(max_length=255)
    # will be autogenerated on save
    reg_number = models.CharField(
        max_length=255, default=increment_reg_number_number, null=True, blank=True)
    timestamp = models.DateField(default=datetime.now)

    def get_absolute_url(self):
        return reverse("keys:list_items")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
