from django.db import models
from django.utils.text import slugify


class Main_Category(models.Model):
    """ Main Category model """
    name = models. CharField(max_length=100, null=False, unique=True,
                             blank=False, verbose_name='Main Category title',
                             help_text='format: required, max_length=150')
    slug = models.SlugField(max_length=150, null=False, unique=True,
                            blank=False, verbose_name='Main Category slug',
                            help_text='format: required, max_length=150')

    class Meta:
        """ Meta class for Main Category model """
        verbose_name = 'Main Category'
        verbose_name_plural = 'Main Categories'
        ordering = ['name']

    def __str__(self):
        """ String representation of Main Category model """
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(models.Model):
    """ Category model """
    main_category = models.ForeignKey(Main_Category, on_delete=models.CASCADE,
                                      verbose_name='main category title')
    name = models.CharField(max_length=100, null=False, unique=True,
                            blank=False, verbose_name='Category title',
                            help_text='format: required, max_length=100')
    friendly_name = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=150, null=False, unique=True,
                            blank=False, verbose_name='Category slug',
                            help_text='format: required, max_length=150')

    class Meta:
        """ Meta class for Category model """
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        """ String representation of Category model """
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Subcategory(models.Model):
    """ Subcategory model """
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='category title')
    name = models. CharField(max_length=100, null=False, unique=True,
                             blank=False, verbose_name='Subcategory title',
                             help_text='format: required, max_length=100')
    slug = models.SlugField(max_length=150, null=False, unique=True,
                            blank=False, verbose_name='Subcategory slug',
                            help_text='format: required, max_length=150')

    class Meta:
        """ Meta class for Subcategory model """
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'
        ordering = ['name']

    def __str__(self):
        """ String representation of Category model """
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Brand(models.Model):
    """ Brand model """
    name = models. CharField(max_length=100, null=False, unique=True,
                             blank=False, verbose_name='Brand name',
                             help_text='format: required, max_length=100')
    friendly_name = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=100, null=False, unique=True,
                            blank=False, verbose_name='Brand slug',
                            help_text='format: required, max_length=100')
    description = models.TextField(max_length=2500, null=False, blank=False,
                                   verbose_name='Brand description',
                                   help_text='format: reqd, max_length=2500')
    image_url = models.URLField(max_length=1500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        """ Meta class for Brand model """
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['name']

    def __str__(self):
        """ String representation of Product model """
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    """ Product model """
    main_category = models.ForeignKey('Main_Category',
                                      on_delete=models.CASCADE,
                                      verbose_name='main category title')
    category = models.ForeignKey('Category', on_delete=models.CASCADE,
                                 verbose_name='category title')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE,
                                    verbose_name='subcategory title')
    brand = models. ForeignKey('Brand', on_delete=models.CASCADE,
                               related_name='products',
                               verbose_name='brand title')
    sku = models.CharField(max_length=50, null=False, unique=False,
                           blank=False,
                           help_text='format: required,max_length=50')
    name = models. CharField(max_length=200, null=False, unique=True,
                             blank=False, verbose_name='Product name',
                             help_text='format: required, max_length=200')
    slug = models.SlugField(max_length=250, null=False, unique=True,
                            blank=False, verbose_name='Product slug',
                            help_text='format: required, max_length=250')
    is_featured = models.BooleanField(default=False)
    total_quantity = models.IntegerField(null=False, unique=False, blank=False,
                                         verbose_name='Product quantity')
    availability = models.IntegerField(null=False, unique=False, blank=False)
    description = models.TextField(max_length=2500, null=False, blank=False,
                                   verbose_name='Product description',
                                   help_text='format: reqd, max_length=2500')
    how_to_use = models.TextField(max_length=2500, null=False, blank=False,
                                  verbose_name='How to use',
                                  help_text='format: reqd, max_length=2500')
    ingredients = models.TextField(max_length=2500, null=False, blank=False,
                                   verbose_name='Product ingredients',
                                   help_text='format: reqd, max_length=2500')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1500, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)

    class Meta:
        """ Meta class for Product model """
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['sku']

    def __str__(self):
        """ String representation of Product model """
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_tags(self):
        """ Get all available tags of products """
        return self.tags.all()
