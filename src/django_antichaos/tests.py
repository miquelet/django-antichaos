from django.test import TestCase
from django.db import models
from tagging.fields import TagField

class Post(models.Model):
    tags = TagField()

class Link(models.Model):
    tags = TagField()

class TagCloudTests(TestCase):
    def testCreatePost(self):
        self.assertEqual(0, Post.objects.count())
        Post(tags = 'one, two, three').save()
        self.assertEqual(1, Post.objects.count())

    def testContentTypes(self):
        from django_antichaos import get_tagged_models

        Post(tags = 'one, two, three').save()
        Link(tags = 'six, seven').save()

        mods = get_tagged_models()
        self.assertEqual(2, len(mods))
        self.assert_(Post in mods)
        self.assert_(Link in mods)
