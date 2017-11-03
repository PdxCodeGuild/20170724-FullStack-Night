from django.db import models
from django.contrib.auth.models import User


class Skills(models.Model):
    skill_name = models.TextField()
    skill_level = models.IntegerField()

    def __str__(self):
        return self.skill_name

    def __repr__(self):
        return 'Skills(skill_level={!r} of skill={!r})'.format(
            self.skill_name,
            self.skill_level)


class User_skills(models.Model):
    fk_skill = models.ForeignKey(Skills)
    user = models.TextField(User)
    fk_user = models.ForeignKey(User)
    email = models.EmailField(User)

    def __str__(self):
        return self.user

    def __repr__(self):
        return 'User_skills(fk_skill={!r}, user={!r}, fk_user={!r}, email={!r})'.format(
            self.fk_user,
            self.user,
            self.fk_skill,
            self. email
        )

