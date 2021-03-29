from django import forms
from django.db import models
from django.db.models.signals import pre_save

from Finance.utils import unique_slug_generator


class LedgerQuerySet(models.query.QuerySet):

    def search(self, query):
        lookups = (Q(item_name__icontains=query) |
                   Q(description__icontains=query) |
                   Q(transaction_ref_number__icontains=query) |
                   Q(slug_number__icontains=query)
                   )
        return self.filter(lookups).distinct()


class LedgerManager(models.Manager):
    def get_queryset(self):
        return LedgerQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)  # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().search(query)


class GeneralLedger(models.Model):
    slug_number = models.SlugField(blank=True, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    item_name = models.CharField(max_length=255)
    description = models.TextField(blank=False,)
    partner = models.CharField(max_length=120)
    invoice = models.CharField(max_length=255)
    transaction_ref_number = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    date_due = models.DateTimeField()
    debit = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    credit = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    tax_amount = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    paye_amt = models.CharField(max_length=255)
    invoice_amount = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    balanced = models.BooleanField(default=True)

    objects = LedgerManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_absolute_url(self):
        return "/GeneralLedger/{slug}/".format(slug=self.slug_number)
        # return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.item_name

    def __unicode__(self):
        return self.item_name

    @property
    def name(self):
        return self.item_name

    # def get_downloads(self):
    #    qs = self.productfile_set.all()
    #    return qs


def newGL_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(newGL_pre_save_receiver, sender=GeneralLedger)
