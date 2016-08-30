from django.db import models


class Attribute(models.Model):
    class Meta:
        app_label = 'dsd'
        db_table = 'attributes'

    uid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    value_type = models.CharField(max_length=255)
    org_unit_attr = models.BooleanField(default=True)
