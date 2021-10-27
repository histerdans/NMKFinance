from random import random

from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save
import os
from Finance.utils import unique_slug_generator


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    # print(filename)
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class DocumentQuerySet(models.query.QuerySet):

    def search(self, query):
        lookups = (Q(item_name__icontains=query) |
                   Q(description__icontains=query) |
                   Q(transaction_ref_number__icontains=query) |
                   Q(slug_number__icontains=query)
                   )
        return self.filter(lookups).distinct()


class DocumentManager(models.Manager):
    def get_queryset(self):
        return DocumentQuerySet(self.model, using=self._db)

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
    objects = DocumentManager()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=130)
    objects = DocumentManager()

    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Documents(models.Model):
    slug_number = models.SlugField(blank=True, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    document_item_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    document_item_name = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True, max_length=1250)
    document_file = models.FileField(upload_to='documents/%Y.%m.%d.')
    YearNow = models.CharField(max_length=25, default='2023/2024')
    QuarterNow = models.CharField(max_length=25, default='Q1')

    objects = DocumentManager()

    class Meta:
        verbose_name_plural = 'Documents'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_absolute_url(self):
        return "/item-{slug}/".format(slug=self.slug_number)
        # return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.document_item_name

    def __unicode__(self):
        return self.document_item_name

    @property
    def name(self):
        return self.document_item_name

    # def get_downloads(self):
    #    qs = self.productive_set.all()
    #    return qs


def new_document_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug_number:
        instance.slug_number = unique_slug_generator(instance)


pre_save.connect(new_document_pre_save_receiver, sender=Documents)
