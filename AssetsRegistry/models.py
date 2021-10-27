from django.db import models
from django.db.models import Q, Sum
from django.db.models.signals import pre_save
from Finance.utils import unique_slug_generator


class AssetsQuerySet(models.query.QuerySet):

    def search(self, query):
        lookups = (Q(item_name__icontains=query) |
                   Q(description__icontains=query) |
                   Q(transaction_ref_number__icontains=query) |
                   Q(slug_number__icontains=query)
                   )
        return self.filter(lookups).distinct()


class AssetsManager(models.Manager):
    def get_queryset(self):
        return AssetsQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def get_by_id(self, pk):
        qs = self.get_queryset().filter(id=pk)  # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().search(query)


class Category(models.Model):
    name = models.CharField(max_length=130)
    objects = AssetsManager()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=130)
    objects = AssetsManager()

    class Meta:
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name


class ItemType(models.Model):
    name = models.CharField(max_length=130)
    objects = AssetsManager()

    class Meta:
        verbose_name_plural = 'Types'

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=130)
    objects = AssetsManager()

    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name


class DepartmentItem(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=130)
    objects = AssetsManager()

    class Meta:
        verbose_name_plural = 'DepartmentsItems'

    def __str__(self):
        return self.name


class AssetsRegistry(models.Model):
    slug_number = models.SlugField(blank=True, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    item_category_asset = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    item_name_asset = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    item_name_type = models.ForeignKey(ItemType, on_delete=models.SET_NULL, null=True)
    item_department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    items_dept_asset = models.ForeignKey(DepartmentItem, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(blank=True, max_length=1250)
    Amount = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    YearNow = models.CharField(max_length=25, default='2023/2024')
    QuarterNow = models.CharField(max_length=25, default='Q1')
    depreciation_type = models.CharField(max_length=225)
    depreciation_rate = models.FloatField(max_length=225, default='0.1')
    depreciation_date = models.DateTimeField(auto_now_add=False)
    item_serial_no = models.CharField(max_length=225)
    item_make_model = models.CharField(max_length=225)

    objects = AssetsManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_absolute_url(self):
        return "/item-{slug}/".format(slug=self.slug_number)
        # return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.item_name_asset

    def __unicode__(self):
        return self.item_name_asset

    @property
    def name(self):
        return self.item_name_asset

    @property
    def sum_amount(self):
        return Sum(self.Amount)

    # def get_downloads(self):
    #    qs = self.productive_set.all()
    #    return qs


def newGL_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug_number:
        instance.slug_number = unique_slug_generator(instance)


pre_save.connect(newGL_pre_save_receiver, sender=AssetsRegistry)
