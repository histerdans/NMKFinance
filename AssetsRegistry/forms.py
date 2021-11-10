from django import forms

from .models import AssetsRegistry, Item, Station, Department


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
        ('2023/2024', '2023/2024'),
        ('2024/2025', '2024/2025'),
        ('2025/2026', '2025/2026'),
        ('2026/2027', '2026/2027'),
        ('2027/2028', '2027/2028'),
        ('2028/2029', '2028/2029'),
        ('2029/2030', '2029/2030'),
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
        ('Straight Line', 'Straight Line'),
        ('Sum of Years Digits', 'Sum of Years Digits'),
        ('Unit Of Production', 'Unit Of Production'),
        ('Double Declining Balance', 'Double Declining Balance'),
    )

    YearNow = forms.ChoiceField(required=True, choices=Years)
    QuarterNow = forms.ChoiceField(required=True, choices=Quarter)
    depreciation_type = forms.ChoiceField(required=True, choices=depreciation_choice)

    class Meta:
        model = AssetsRegistry
        fields = (
            'item_station', 'item_account', 'item_department','item_description', 'QuarterNow', 'YearNow', 'item_cost', 'item_name_asset',
            'depreciation_type', 'depreciation_rate',  'item_serial_no', 'item_make_model',
            'depreciation_date')

    def __init__(self, *args, **kwargs):
        super(FormNewAR, self).__init__(*args, **kwargs)
        self.fields["item_station"].widget.attrs.update(
            {'type': 'text', 'class': 'span6', 'name': 'item_station',
             'onclick': 'search_item();', })
        self.fields['item_department'].widget.attrs.update(
            {'type': 'text', 'class': 'span6', 'name': 'item_department'})
        self.fields["item_account"].widget.attrs.update(
            {'type': 'text', 'class': 'span6', 'name': 'item_account', })
        self.fields['item_description'].widget.attrs.update(
            {'type': 'text', 'class': 'span8 TextField', 'name': 'item_description', })
        self.fields['YearNow'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'id': 'YearNow', 'name': 'YearNow'})
        self.fields['QuarterNow'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'id': 'QuarterNow', 'name': 'QuarterNow'})
        self.fields['item_cost'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'name': 'item_cost'})
        self.fields['item_name_asset'].widget.attrs.update(
            {'type': 'text', 'class': 'span6', 'name': 'item_name_asset'})
        self.fields['depreciation_type'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'name': 'depreciation_type'})
        self.fields['depreciation_rate'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'name': 'depreciation_rate'})
        self.fields['item_serial_no'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'name': 'item_serial_no'})
        self.fields['item_make_model'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'name': 'item_make_model'})
        self.fields['depreciation_date'].widget.attrs.update(
            {'type': 'text', 'class': 'span4 date-picker', 'name': 'depreciation_date'})

        if 'item_account' in self.data:
            try:
                account_id = int(self.data.get('item_account'))
                self.fields['item_department'].queryset = Department.objects.filter(account_id=account_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['item_department'].queryset = self.instance.item_account.department_set.order_by('name')
        if 'item_department' in self.data:
            try:
                department_id = int(self.data.get('item_department'))
                self.fields['item_station'].queryset = Station.objects.filter(department_id=department_id).order_by(
                    'name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['item_station'].queryset = self.instance.item_department.station_set.order_by('name')
        if 'item_station' in self.data:
            try:
                station_id = int(self.data.get('item_station'))
                self.fields['item_name_asset'].queryset = Item.objects.filter(station_id=station_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['item_name_asset'].queryset = self.instance.item_station.item_set.order_by('name')

