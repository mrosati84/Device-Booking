from django.db import models

# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    serial_number = models.CharField(max_length=50, null=False, blank=False, default='H-ART 2015 XXXXXXXXXXX')
    reserved_by = models.ForeignKey('User', null=True, blank=True)

    def reserve(self, user):
        self.reserved_by = user
        self.save()

    def is_reserved(self):
        if self.reserved_by is not None:
            return True

        return False

    def set_free(self):
        self.reserved_by = None
        self.save()

    def __unicode__(self):
        return self.name

class User(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=40, null=False, blank=False)
    last_name = models.CharField(max_length=40, null=False, blank=False)

    def __unicode__(self):
        return ' '.join([self.first_name, self.last_name])
