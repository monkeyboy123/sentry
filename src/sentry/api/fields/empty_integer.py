from __future__ import absolute_import

from rest_framework import serializers
from rest_framework.fields import empty


class EmptyIntegerField(serializers.IntegerField):
    """
    DRF used to translate a blank field as a null integer, but after 3.x it
    doesn't accept an empty string as a value. We rely on this behaviour in some
    cases, so this restores it.
    """

    def to_internal_value(self, data):
        if data == "":
            return None
        return super(EmptyIntegerField, self).to_internal_value(data)

    def run_validation(self, data=empty):
        if data == "":
            return None
        return super(EmptyIntegerField, self).run_validation(data)
