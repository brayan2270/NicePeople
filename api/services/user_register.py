""" It handle the addition of profiles to an user """

from django.shortcuts import get_object_or_404
from ..models.profile import Profile


class UserProfiles:
    def __init__(self, user, profiles=None):
        """ Initializes class with an user and an optional list of pk profiles.

        Parameters:
            user (User):User model instance.
            profiles (List):Primary keys list about profiles instances.

        """

        self.user = user
        self.profiles = profiles if profiles else None

    def add_profile(self, profile):
        """ Add the default 'cliente' profile to an user.

        Returns:
            user (User):User instance with 'cliente within its ManyToMany
                        relation.

        """
        # pylint: disable=no-member
        client_profile = Profile.objects.get_or_create(profile=profile)
        self.user.profile.add(client_profile[0])
        return self.user
