from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView, ArticleList, ArticleDetail


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomePageView)

    def test_articles_list_view_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_articles_list_url_resolves_articles_list_view(self):
        url = reverse('articles-list')
        view = resolve(url)
        self.assertEqual(view.func.view_class, ArticleList)



    def test_news_detail_url_resolves_news_detail_view(self):
        url = reverse('news-detail', kwargs={
            'year': '2023',
            'month': '10',
            'day': '19',
            'slug': 'sample-article'
        })
        view = resolve(url)
        self.assertEqual(view.func.view_class, ArticleDetail)

    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=['name'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


# Create your tests here.
