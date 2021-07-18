from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return f'Category: {self.category_name}'

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    post_name = models.CharField(max_length=200)
    post_description = models.CharField(max_length=200)

    def __str__(self):
        return f'Post Name: {self.post_name} \nPost Description: {self.post_description}'