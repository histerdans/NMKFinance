from django import forms

from .models import GeneralLedger, Item, DepartmentGeneralLedger, Department, Station


class FormNewGL(forms.ModelForm):
    Years = (
        ('', '----------------'),  # year choices
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
        ('', '----------------'),  # Quarter choices
        ('Q1', 'Quarter1'),
        ('Q2', 'Quarter2'),
        ('Q3', 'Quarter3'),
        ('Q4', 'Quarter4'),
    )

    YearNow = forms.ChoiceField(required=True, choices=Years)
    QuarterNow = forms.ChoiceField(required=True, choices=Quarter)

    class Meta:
        model = GeneralLedger
        fields = (
            'item_category', 'item_name', 'notes', 'QuarterNow', 'YearNow', 'Amount',)

    def __init__(self, *args, **kwargs):
        super(FormNewGL, self).__init__(*args, **kwargs)
        self.fields["item_category"].widget.attrs.update(
            {'type': 'text', 'class': 'span8', 'name': 'item_category',
             'onclick': 'search_item();', })
        self.fields["item_name"].widget.attrs.update(
            {'type': 'text', 'class': 'span8', 'name': 'item_name', })
        self.fields['notes'].widget.attrs.update(
            {'type': 'text', 'class': 'span8 TextField', 'id': 'notes', 'name': 'notes', })
        self.fields['YearNow'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'id': 'YearNow', 'name': 'YearNow'})
        self.fields['QuarterNow'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'id': 'QuarterNow', 'name': 'QuarterNow'})
        self.fields['Amount'].widget.attrs.update(
            {'type': 'text', 'class': 'span4 number-separator', 'name': 'Amount'})
        if 'item_category' in self.data:
            try:
                category_id = int(self.data.get('item_category'))
                self.fields['item_name'].queryset = Item.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['item_name'].queryset = self.instance.item_category.item_set.order_by('name')


class FormNewDeptGL(forms.ModelForm):
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

    YearNow = forms.ChoiceField(required=True, choices=Years)
    QuarterNow = forms.ChoiceField(required=True, choices=Quarter)

    class Meta:
        model = DepartmentGeneralLedger
        fields = (
            'item_station_gl', 'item_department_gl', 'item_dept_category', 'item_dept_name',
            'notes', 'QuarterNow',
            'YearNow', 'Amount',)

    def __init__(self, *args, **kwargs):
        super(FormNewDeptGL, self).__init__(*args, **kwargs)
        self.fields["item_station_gl"].widget.attrs.update(
            {'type': 'text', 'class': 'span6', 'name': 'item_station',
             'onclick': 'search_item();', })
        self.fields['item_department_gl'].widget.attrs.update(
            {'type': 'text', 'class': 'span6', 'name': 'item_department'})
        self.fields["item_dept_category"].widget.attrs.update(
            {'type': 'text', 'class': 'span8', 'name': 'item_dept_category',
             'onclick': 'search_item();', })
        self.fields["item_dept_name"].widget.attrs.update(
            {'type': 'text', 'class': 'span8', 'name': 'item_dept_name', })
        self.fields['notes'].widget.attrs.update(
            {'type': 'text', 'class': 'span8 TextField', 'id': 'notes', 'name': 'notes', })
        self.fields['YearNow'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'id': 'YearNow', 'name': 'YearNow'})
        self.fields['QuarterNow'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'id': 'QuarterNow', 'name': 'QuarterNow'})
        self.fields['Amount'].widget.attrs.update(
            {'type': 'text', 'class': 'span4 number-separator', 'name': 'Amount'})
        if 'item_dept_category' in self.data:
            try:
                category_id = int(self.data.get('item_dept_category'))
                self.fields['item_dept_name'].queryset = Item.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['item_dept_name'].queryset = self.instance.item_dept_category.item_set.order_by('name')

        if 'item_department_gl' in self.data:
            try:
                department_id = int(self.data.get('item_department_gl'))
                self.fields['item_station_gl'].queryset = Station.objects.filter(department_id=department_id).order_by(
                    'name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['item_station_gl'].queryset = self.instance.item_department_gl.station_set.order_by('name')
