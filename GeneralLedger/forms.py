from django import forms

from .models import GeneralLedger, Item


class FormNewGL(forms.ModelForm):
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
            {'type': 'text', 'class': 'span8',  'name': 'item_name', })
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

