from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(Post, related_name="images",
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Image for {self.post.title}"
