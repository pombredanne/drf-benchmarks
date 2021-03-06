#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from drf_benchmarks import test_serializer_fields, test_nested_serializer_fields
from drf_benchmarks.models import RegularFieldsModel, RegularFieldsAndFKModel


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegularFieldsModel
        fields = test_serializer_fields


class TestNestedSerializer(serializers.ModelSerializer):
    fk = TestSerializer()

    class Meta:
        model = RegularFieldsAndFKModel
        fields = test_nested_serializer_fields
