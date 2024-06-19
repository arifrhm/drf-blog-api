from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from cms_app.models import Post, Image
from cms_app.serializers import PostSerializer, ImageSerializer


# Create your tests here.
class PostAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.post_data = {"title": "Test Post", "content": "Content of test post"}
        self.post = Post.objects.create(
            title="Test Post", content="Content of test post"
        )

    def test_post_list(self):
        response = self.client.get(reverse("post-list-create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_post_create(self):
        response = self.client.post(
            reverse("post-list-create"), data=self.post_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_post_detail(self):
        response = self.client.get(reverse("post-detail", kwargs={"pk": self.post.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Post")

    def test_post_update(self):
        updated_data = {
            "title": "Updated Test Post",
            "content": "Updated content of test post",
        }
        response = self.client.put(
            reverse("post-detail", kwargs={"pk": self.post.id}),
            data=updated_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.get(id=self.post.id).title, "Updated Test Post")

    def test_post_delete(self):
        response = self.client.delete(
            reverse("post-detail", kwargs={"pk": self.post.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)


class ImageModelTestCase(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title="Test Post", content="Content of test post"
        )
        self.image = Image.objects.create(
            post=self.post, image="test_image.jpg", description="Test image"
        )

    def test_image_model(self):
        image = Image.objects.get(post=self.post)
        self.assertEqual(image.description, "Test image")


class ImageSerializerTestCase(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title="Test Post", content="Content of test post"
        )
        self.image_data = {
            "post": self.post.id,
            "image": "test_image.jpg",
            "description": "Test image",
        }

    def test_image_serializer_valid(self):
        serializer = ImageSerializer(data=self.image_data)
        self.assertTrue(serializer.is_valid())

    def test_image_serializer_create(self):
        serializer = ImageSerializer(data=self.image_data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(
            Image.objects.count(), 1
        )  # Check that a new image has been created
