from unicodedata import decimal

from django.db import models
from django.db.models import Q
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

    def get_by_id(self, pk):
        qs = self.get_queryset().filter(id=pk)  # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None



    def search(self, query):
        return self.get_queryset().search(query)


class Department(models.Model):
    name = models.CharField(max_length=130)
    objects = LedgerManager()

    class Meta:
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name


class Station(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=130)
    objects = LedgerManager()

    class Meta:
        verbose_name_plural = 'Stations'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=130)
    objects = LedgerManager()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=130)
    objects = LedgerManager()

    def __str__(self):
        return self.name


class GeneralLedger(models.Model):
    slug_number = models.SlugField(blank=True, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    item_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    item_name = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(blank=True, max_length=1250)
    Amount = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)
    subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    YearNow = models.CharField(max_length=25, default='2023/2024')
    QuarterNow = models.CharField(max_length=25, default='Q1')

    objects = LedgerManager()

    class Meta:
        verbose_name_plural = 'General Ledgers'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_absolute_url(self):
        return "/item-{slug}/".format(slug=self.slug_number)
        # return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return str(self.item_name)


class DepartmentGeneralLedger(models.Model):
    slug_number = models.SlugField(blank=True, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    item_department_gl = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    item_station_gl = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True)
    item_dept_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    item_dept_name = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(blank=True, max_length=1250)
    Amount = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    YearNow = models.CharField(max_length=25, default='2023/2024')
    QuarterNow = models.CharField(max_length=25, default='Q1')

    objects = LedgerManager()

    class Meta:
        verbose_name_plural = 'Department General Ledgers'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_absolute_url(self):
        return "/item-{slug}/".format(slug=self.slug_number)
        # return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return str(self.item_dept_name)

    def __unicode__(self):
        return self.item_dept_name

    @property
    def name(self):
        return self.item_dept_name


def newDeptGL_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug_number:
        instance.slug_number = unique_slug_generator(instance)


def newGL_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug_number:
        instance.slug_number = unique_slug_generator(instance)


pre_save.connect(newGL_pre_save_receiver, sender=GeneralLedger)

pre_save.connect(newDeptGL_pre_save_receiver, sender=DepartmentGeneralLedger)
