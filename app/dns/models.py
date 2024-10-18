from django.db import models


class Domain(models.Model):

    name = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name


class Record(models.Model):

    class RecordType(models.TextChoices):
        A = 'a'
        AAAA = 'aaaa'

    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name='records')

    record_type = models.CharField(choices=RecordType.choices, max_length=4, null=False, blank=False)

    ip_address = models.TextField(verbose_name='ipv4/6', null=False, blank=False)

    def __str__(self):
        return f'{self.domain.name} | {self.record_type.capitalize()}'
