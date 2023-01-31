from django.test import TestCase
from products.models import Product, MainCategory, Category, Subcategory, Brand


class TestProductsModels(TestCase):
    """ Test for products app models """

    def setUp(self):
        """
        Creates test product objects (MainCategory, Category, Subcategory,
        Brand and Product)
        """

        self.main_category1 = MainCategory.objects.create(
            name='Makeup',
            slug='makeup',
        )

        self.category1 = Category.objects.create(
            main_category=self.main_category1,
            name='Face',
            friendly_name='Face',
            slug='face',
        )

        self.subcategory1 = Subcategory.objects.create(
            category=self.category1,
            name='foundation',
            friendly_name='Foundation',
            slug='foundation',
        )

        self.brand1 = Brand.objects.create(
            name='Makeup Brand',
            friendly_name='Makeup Brand',
            slug='makeup-brand',
            description='brand description goes here',
            is_featured=False,
        )

        self.product1 = Product.objects.create(
            main_category=self.main_category1,
            category=self.category1,
            subcategory=self.subcategory1,
            brand=self.brand1,
            sku='axi-sk-fc-spt-0005',
            name='New Foundation',
            slug='new-foundation',
            is_featured=True,
            total_quantity=100,
            availability=100,
            description='new foundation description goes here',
            how_to_use='new foundation how to use goes here',
            ingredients='new foundation ingredients goes here',
            has_sizes=False,
            price=26.99,
            discount=0.00,
            original_price=26.99,
            image_url='image_url',
        )

    def test_main_category_str_method(self):
        """ tests the string representation of main category model """
        main_category = MainCategory(name='MainCategory Name')
        self.assertEqual(str(main_category), main_category.name)

    def test_category_str_method(self):
        """ tests the string representation of the category model """
        category = Category(name='Category Name')
        self.assertEqual(str(category), category.name)

    def test_subcategory_str_method(self):
        """ tests the string representation of the subcategory model """
        subcategory = Subcategory(name='Subcategory Name')
        self.assertEqual(str(subcategory), subcategory.name)

    def test_brand_str_method(self):
        """ tests the string representation of the brand model """
        brand = Brand(name='Brand Name')
        self.assertEqual(str(brand), brand.name)

    def test_main_category_name(self):
        """ test the category name field """
        self.assertEqual(self.main_category1.name, 'Makeup')
        self.assertEqual(self.main_category1.slug, 'makeup')

    def test_brand_and_product_is_featured(self):
        """ test the brand and product are featured """
        self.assertEqual(self.brand1.is_featured, False)
        self.assertEqual(self.product1.is_featured, True)

    def test_category_verbose_name_plural(self):
        """ test the category model class meta verbose name plural """
        self.assertEqual(str(Category._meta.verbose_name_plural), "Categories")

    def test_subcategory_verbose_name_plural(self):
        """ test the subcategory model class meta verbose name plural """
        self.assertEqual(str(Subcategory._meta.verbose_name_plural),
                         "Subcategories")
