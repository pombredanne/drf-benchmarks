#!/usr/bin/env python
# -*- coding: utf-8 -*-

from drf_benchmarks import test_serializer_fields, test_nested_serializer_fields
from drf_benchmarks.models import RegularFieldsModel, RegularFieldsAndFKModel
from drf_benchmarks.serializers.cython_ordered_dict import CythonOrderedDictMixin
from drf_benchmarks.serializers.immutable.base import ImmutableModelSerializer


class TestSerializer(CythonOrderedDictMixin, ImmutableModelSerializer):
    class Meta:
        model = RegularFieldsModel
        fields = test_serializer_fields


class TestNestedSerializer(CythonOrderedDictMixin, ImmutableModelSerializer):
    fk = TestSerializer()

    class Meta:
        model = RegularFieldsAndFKModel
        fields = test_nested_serializer_fields