from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AbstractUser
from django.db import models
from follower.models import UserFollows


class User(AbstractUser):
    SUBSCRIBER = "SUBSCRIBER"

    profil_photo = models.ImageField(verbose_name="Photo de profil")

    # attribut:following => represents the users followed by the User instance
    following = models.ManyToManyField(
        "self",
        through=UserFollows,
        symmetrical=False,
        related_name="followers",
    )

    def user_followed_by_user_and_followers(self):
        """gets the users followed by the instance and the followers of the user's instance"""
        self.user_followed_by_user = self.following.all()
        self.followers_of_user = self.followers.all()

    def delete_user_follow(self, user_follow_id):
        """deleting a user's follow-up(user_follow_id)

        Args:
            user_follow_id (_type_): id of User instance

        Returns:
            _type_: User Instance
        """
        user_follow = get_object_or_404(User, id=user_follow_id)
        self.following.remove(user_follow)

        return user_follow
