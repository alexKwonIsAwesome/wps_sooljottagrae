from django.db import models
from django.core.urlresolvers import reverse

from posts.models import Post
from users.models import User


class PlaceTag(models.Model):

    place_name = models.CharField(
            max_length=20,
            )

    post_set = models.ManyToManyField(Post)

    user_set = models.ManyToManyField(User)

    def __str__(self):
        return self.place_name

    def get_absolute_api_url(self):
        return reverse(
            "apis:tags:place-detail",
            kwargs={
                "pk": self.id,
            },
        )
