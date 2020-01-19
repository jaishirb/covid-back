from django.db import models

from django.db import models
from backend.apps.utils.managers import MahouModelManager


class ModelBase(models.Model):
    archived = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = MahouModelManager()

    class Meta:
        abstract = True

    def set_state(self, state):
        self.archived = state
        self.save()

    def delete(self, using=None, keep_parents=False):
        self.set_state(True)

    def get_fecha_created(self):
        return self.created.strftime('%B %d de %Y, %I:%M %p')

    def get_fecha_updated(self):
        return self.updated.strftime('%B %d de %Y, %I:%M %p')
