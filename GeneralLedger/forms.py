from django.forms import ModelForm

from .models import GeneralLedger


class FormNewGL(ModelForm):
    class Meta:
        model = GeneralLedger
        fields = (
            'slug_number', 'item_name', 'description', 'partner', 'invoice', 'transaction_ref_number', 'account_name',
            'account_number', 'debit', 'credit', 'date_due', 'tax_amount', 'paye_amt', 'invoice_amount',)

    def __init__(self, *args, **kwargs):
        super(FormNewGL, self).__init__(*args, **kwargs)
        self.fields["item_name"].widget.attrs.update(
            {'type': 'text', 'class': 'span10', 'id': 'item_name', 'name': 'item_name', })
        self.fields['description'].widget.attrs.update(
            {'type': 'text', 'class': 'span8', 'id': 'description', 'name': 'description', })
        self.fields['partner'].widget.attrs.update(
            {'type': 'email', 'class': 'span8', 'id': 'partner', 'name': 'partner', })
        self.fields['invoice'].widget.attrs.update(
            {'type': 'text', 'class': 'span6', 'id': 'invoice', 'name': 'invoice', })
        self.fields['transaction_ref_number'].widget.attrs.update(
            {'type': 'text', 'class': 'span6', 'id': 'transaction_ref_number', 'name': 'transaction_ref_number', })
        self.fields['account_name'].widget.attrs.update(
            {'type': 'text', 'class': 'span10', 'id': 'account_name', 'name': 'account_name', })
        self.fields['account_number'].widget.attrs.update(
            {'type': 'text', 'class': 'span6', 'id': 'account_number', 'name': 'account_number'})
        self.fields['debit'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'id': 'debit', 'name': 'debit'})
        self.fields['credit'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'id': 'credit', 'name': 'credit', })
        self.fields['date_due'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'id': 'date_due', 'name': 'date_due', })
        self.fields['tax_amount'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'id': 'tax_amount', 'name': 'tax_amount', })
        self.fields['paye_amt'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'id': 'paye_amt', 'name': 'paye_amt', })
        self.fields['invoice_amount'].widget.attrs.update(
            {'type': 'text', 'class': 'span4', 'id': 'invoice_amount', 'name': 'invoice_amount'})
