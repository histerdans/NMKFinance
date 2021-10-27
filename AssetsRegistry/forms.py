from django import forms

from .models import AssetsRegistry, Item


class FormNewAR(forms.ModelForm):
    Years = (
        ('', '----------------'),
        ('2016/2017', '2016/2017'),
        ('2017/2018', '2017/2018'),
        ('2018/2019', '2018/2019'),
        ('2019/2020', '2019/2020'),
        ('2020/2021', '2020/2021'),
        ('2021/2022', '2021/2022'),
        ('2022/2023', '2022/2023'),
    )
    Quarter = (
        ('', '----------------'),
        ('Q1', 'Quarter1'),
        ('Q2', 'Quarter2'),
        ('Q3', 'Quarter3'),
        ('Q4', 'Quarter4'),
    )
    depreciation_choice = (
        ('', '----------------'),
        ('1', 'Straight Line'),
        ('2', 'Sum of Years Digits'),
        ('3', 'Unit Of Production'),
        ('4', 'Double Declining Balance'),
    )

    YearNow = forms.ChoiceField(required=True, choices=Years)
    QuarterNow = forms.ChoiceField(required=True, choices=Quarter)
    depreciation_type = forms.ChoiceField(required=True, choices=depreciation_choice)

    class Meta:
        model = AssetsRegistry
        fields = (
            'item_category_asset', 'item_name_asset', 'notes', 'QuarterNow', 'YearNow', 'Amount', 'item_name_type',
            'depreciation_type', 'depreciation_rate', 'item_department', 'items_dept_asset', 'item_serial_no',
            'item_make_model', 'depreciation_date')

    def __init__(self, *args, **kwargs):
        super(FormNewAR, self).__init__(*args, **kwargs)
        self.fields["item_category_asset"].widget.attrs.update(
            {'type': 'text', 'class': 'span8', 'name': 'item_category_asset',
             'onclick': 'search_item();', })
        self.fields["item_name_asset"].widget.attrs.update(
            {'type': 'text', 'class': 'span8', 'name': 'item_name_asset', })
        self.fields['notes'].widget.attrs.update(
            {'type': 'text', 'class': 'span8 TextField', 'id': 'notes', 'name': 'notes', })
        self.fields['YearNow'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'id': 'YearNow', 'name': 'YearNow'})
        self.fields['QuarterNow'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'id': 'QuarterNow', 'name': 'QuarterNow'})
        self.fields['Amount'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'name': 'Amount'})
        self.fields['item_name_type'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'name': 'item_name_type'})
        self.fields['depreciation_type'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'name': 'depreciation_type'})
        self.fields['depreciation_rate'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'name': 'depreciation_rate'})
        self.fields['item_department'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'name': 'item_department'})
        self.fields['item_serial_no'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'name': 'item_serial_no'})
        self.fields['item_make_model'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'name': 'item_make_model'})
        self.fields['depreciation_date'].widget.attrs.update(
            {'type': 'text', 'class': 'span4 date-picker', 'name': 'depreciation_date',
             'data-date-format': 'dd/mm/yyyy'})
        if 'item_category' in self.data:
            try:
                category_id = int(self.data.get('item_category_asset'))
                self.fields['item_name_asset'].queryset = Item.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['item_name_asset'].queryset = self.instance.item_category_asset.item_set.order_by('name')
