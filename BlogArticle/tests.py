from django.test import SimpleTestCase
from django.urls import reverse, resolve
from BlogArticle.views import index, detail_article, article_category, registration, login_view, logout_view

################## Test Urls ##################
class TestUrls(SimpleTestCase):
    def test_home_url(self):
        url = reverse('BlogArticle:home')
        self.assertEqual(resolve(url).func, index)

    def test_register_url(self):
        url = reverse('BlogArticle:register')
        self.assertEqual(resolve(url).func, registration)

    def test_login_url(self):
        url = reverse('BlogArticle:login')
        self.assertEqual(resolve(url).func, login_view)

    def test_logout_url(self):
        url = reverse('BlogArticle:logout')
        self.assertEqual(resolve(url).func, logout_view)

    # Testing a Path(URL) with an identifier
    def test_detail_article_url(self):
        url = reverse('BlogArticle:detailArticle', args=['some-slug-here'])
        self.assertEqual(resolve(url).func, detail_article)

    def test_article_category_url(self):
        url = reverse('BlogArticle:articleCategory', args=['some-slug-here'])
        self.assertEqual(resolve(url).func, article_category)

################## Test Models ##################
from django.test import TestCase
from BlogArticle.models import Category,UserArticle

############## Test Category Model ##############
class CategoryModelTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        # create a Category object for testing
        image_path = "path_to_test_image.jpg"
        self.category = Category.objects.create(
            title='Test Category',
            slug='test-category',
            thumbnail=image_path,
        )
    
    # def tearDown(self):
    #     self.category.delete()
        
    def test_category_fields(self):
        self.assertEquals(self.category.title, 'Test Category')
        self.assertEquals(self.category.slug, 'test-category')
        self.assertEquals(self.category.thumbnail, 'path_to_test_image.jpg')

    def test_category_string_output(self):
        self.assertEquals(str(self.category), 'Test Category')

    @classmethod
    def tearDownClass(cls):
        pass

############## Test UserArticle Model ##############
class UserArticleTest(TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        UserArticle.objects.create(
            first_name='Somaieh',
            last_name='Aria',
            age=39,
            gender='M',
            mobile_number='09102030682',
            user_name='SomaeihAria',
            email='somaieh@gmail.com',
            password='somaieh123'
        )

    def test_user_article_creation(self):
        article = UserArticle.objects.get(user_name='SomaeihAria')
        self.assertEqual(article.first_name, 'Somaieh')
        self.assertEqual(article.last_name, 'Aria')
        self.assertEqual(article.age, 39)
        self.assertEqual(article.gender, 'M')
        self.assertEqual(article.mobile_number, '09102030682')
        self.assertEqual(article.email, 'somaieh@gmail.com')
        self.assertEqual(article.password, 'somaieh123')

    @classmethod
    def tearDownClass(cls):
        pass