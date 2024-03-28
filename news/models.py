from django.db import models
from utils.models import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=256)
    content = models.TextField()
    main_photo = models.ImageField(upload_to='news')
    photo = models.ImageField(upload_to='news', blank=True, null=True)
    watched = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.title


class Rules(BaseModel):
    description = models.TextField()

# class Photo(BaseModel):
#     photo = models.ImageField(upload_to='news', blank=True, null=True)
#     post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True)
#
#     @classmethod
#     def get_main_photo(cls, post_id):
#         photo = Photo.objects.filter(post_id=post_id).first()
#         print(photo)
#         if photo:
#             return photo.photo
#         return None
#
#     def __str__(self):
#         return self.post.title
