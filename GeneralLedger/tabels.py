import django_tables2 as tables

from GeneralLedger.models import GeneralLedger


class GeneralLedgerTable(tables.Table):
    class Meta:
        model = GeneralLedger
        fields = (
            'slug_number', 'item_category', 'item_name', 'notes', 'QuarterNow', 'YearNow', 'Amount',)
