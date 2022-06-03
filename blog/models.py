from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Profile(models.Model):
    """
    Class for the profile model
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
        )
    avatar = CloudinaryField(
        'profile_image',default='default_image.svg'
        )
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    updated_on = models.DateTimeField(
        auto_now=True
        )
    
    def __str__(self):
        return f' profile of {self.user.username}'
    
class Post(models.Model):
    """
    A class for the post model
    """
    title = models.CharField(
        verbose_name=("title"),
        max_length=200,
        unique=True
        )
    slug = models.SlugField(
        verbose_name=("slug"),
        max_length=150,
        unique=True
        )
    body = models.TextField(
        verbose_name=("body"),
        blank=True
        )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="post_owner")
    updated = models.DateTimeField(
        verbose_name=("updated"),
        auto_now=True
        )
    created_on = models.DateTimeField(
        verbose_name=("created_on"),
        auto_now_add=True
        )
    post_image = models.ImageField(
        verbose_name=("post_image"),
        null=True,
        blank=True,
        upload_to=""
    )
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns the post name string
        Args:
            self (object): self.
        Returns:
            The post title string
        """
        return str(self.title)

    def get_absolute_url(self):
        """
        Returns the post.pk string
        Args:
            self (object): self.
        Returns:
            The url string posts/post pk
        """
        return f"/posts/{self.pk}"

class Comment(models.Model):
    """
    A class for the comment model
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name="comment_post"
    )
    name = models.CharField(
        verbose_name=("name"),
        max_length=80
        )
    comment_body = models.TextField(
        verbose_name=("comment_body"),
        )
    created_on = models.DateTimeField(
        verbose_name=("created_on"),
        auto_now_add=True
        )

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns the comment name string
        Args:
            self (object): self.
        Returns:
            The comment body by name string
        """
        return f"Comment {self.comment_body} by {self.name}"

    def get_absolute_url(self):
        """
        Returns the post.id string
        Args:
            self (object): self.
        Returns:
            The url string posts/post id
        """
        return f"/posts/{self.post_id}"