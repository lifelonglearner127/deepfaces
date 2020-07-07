from django.db import models
from django.db.models import ForeignKey, OneToOneField

__all__ = (
    "FlexibleForeignKey",
    "OneToOneCascadeDeletes",
)


class FlexibleForeignKey(ForeignKey):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("on_delete", models.CASCADE)
        super(FlexibleForeignKey, self).__init__(*args, **kwargs)


class OneToOneCascadeDeletes(OneToOneField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("on_delete", models.CASCADE)
        super(OneToOneCascadeDeletes, self).__init__(*args, **kwargs)
