from django.db import models


class MahouModelQuerySet(models.QuerySet):
    def all(self):
        return self.filter(archived=False)

    def removed(self):
        return self.filter(archived=True)


class MahouModelManager(models.Manager):
    def get_queryset(self):
        return MahouModelQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all().order_by('-id')

    def removed(self):
        return self.get_queryset().removed().order_by('-id')