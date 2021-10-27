from django import forms

from .models import Documents, Item


class FileUploadForm(forms.ModelForm):
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
        model = Documents
        fields = (
            'document_item_category', 'document_item_name', 'description', 'QuarterNow', 'YearNow', 'document_file',)

    def __init__(self, *args, **kwargs):
        super(FileUploadForm, self).__init__(*args, **kwargs)
        self.fields["document_item_category"].widget.attrs.update(
            {'type': 'text', 'class': 'span8', 'name': 'document_item_category',
             'onclick': 'search_item();', })
        self.fields["document_item_name"].widget.attrs.update(
            {'type': 'text', 'class': 'span8', 'name': 'document_item_name', })
        self.fields['description'].widget.attrs.update(
            {'type': 'text', 'class': 'span8 TextField', })
        self.fields['YearNow'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'id': 'YearNow', 'name': 'YearNow'})
        self.fields['QuarterNow'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'id': 'QuarterNow', 'name': 'QuarterNow'})
        self.fields['document_file'].widget.attrs.update(
            {'type': 'file', 'multiple': True, 'class': 'span4', 'name': 'document_file'})
        if 'document_item_category' in self.data:
            try:
                category_id = int(self.data.get('item_category'))
                self.fields['document_item_name'].queryset = Item.objects.filter(category_id=category_id).order_by(
                    'name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['document_item_name'].queryset = self.instance.document_item_category.item_set.order_by('name')
