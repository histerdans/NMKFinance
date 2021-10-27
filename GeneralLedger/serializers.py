from rest_framework import serializers
from .models import GeneralLedger


class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = GeneralLedger
        fields = (
            'slug_number', 'item_category', 'item_name', 'notes', 'QuarterNow', 'YearNow', 'Amount',)

