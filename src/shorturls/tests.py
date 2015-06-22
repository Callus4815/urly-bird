from django.test import TestCase
from .models import Link
from django.core.urlresolvers import reverse
# Create your tests here.

class ShortenerText(TestCase):
    def test_shortness(self):

        url = 'http://www.example.com/'
        l = Link(url=url)
        short_url = Link.shorten(l)
        self.assertLess(len(short_url), len(url))


    def test_recover_link(self):

        url = 'http://www.example.com/'
        l = Link(url=url)
        short_url = Link.shorten(l)
        l.save()
        exp_url = Link.expand(short_url)
        self.assertEqual(url, exp_url)


    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)

    def test_shortener_form(self):
        url = 'http://example.com/'
        response = self.client.post(reverse("home"),
                                    {'url': url}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('link', response.context)
        l = response.context['link']
        short_url = Link.shorten(l)
        self.assertEqual(url, l.url)
        self.assertIn(short_url, response.content)

    def test_redirect_to_long_link(self):
        url = "http://example.com"
        l = Link.objects.create(url=url)
        short_url = Link.shorten(l)
        response = self.client.get(
            reverse("redirect_short_url",
                    kwargs={"short_url": short_url}))
        self.assertRedirects(response, url)
