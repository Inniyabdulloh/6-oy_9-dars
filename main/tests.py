from django.contrib.auth.models import User
from .models import Blog, SocialMedia
from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class SocialMediaTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='admin', email='someemail@gmail.com', password='123456')
        self.user.set_password('123456')
        self.user.save()

        self.blog = Blog.objects.create(
            title='Blog',
            author=self.user,
            body='This is a blog'
        )

        self.client.login(username='admin', password='123456')

    def test_social_media(self):
        telegram = SocialMedia.objects.create(
            user=self.user,
            name_social_media='telegram',
            social_media='https://t.me/inniy_abdulloh'
        )
        telegram.save()
        instagram = SocialMedia.objects.create(
            user=self.user,
            name_social_media='instagram',
            social_media='https://www.instagram.com/inniy_abdulloh/'
        )
        instagram.save()
        youtube = SocialMedia.objects.create(
            user=self.user,
            name_social_media='youtube',
            social_media='https://www.youtube.com/channel/UCez8885tn2AisxFRggPA76A'
        )
        youtube.save()

        response = self.client.post(reverse('blog_detail', kwargs={'id': self.blog.id}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(SocialMedia.objects.count(), 3)
        self.assertContains(response, telegram.name_social_media)
        self.assertContains(response, telegram.social_media)
        self.assertContains(response, instagram.name_social_media)
        self.assertContains(response, instagram.social_media)
        self.assertContains(response, youtube.name_social_media)
        self.assertContains(response, youtube.social_media)





