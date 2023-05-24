from rest_framework import serializers

from .base import *
from .features import *
from .generic import *
from .nested import *


#
# Base model serializers
#

class NetBoxModelSerializer(TaggableModelSerializer, CustomFieldModelSerializer, ValidatedModelSerializer):
    """
    Adds support for custom fields and tags.
    """
    pass


class NestedGroupModelSerializer(NetBoxModelSerializer):
    """
    Extends PrimaryModelSerializer to include Tree support.
    """
    _depth = serializers.IntegerField(source='tree_depth', read_only=True)


class BulkOperationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
