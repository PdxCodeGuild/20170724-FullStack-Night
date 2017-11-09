from django.db import models
from django.contrib.auth.models import User



class Skill(models.Model):
    skill_name = models.TextField()

    def __str__(self):
        return f'{self.skill_name}'


class UserSkill(models.Model):
    fk_user = models.ForeignKey(User)
    fk_skill = models.ForeignKey(Skill, related_name='skill')
    teach_boolean = models.BooleanField()

    def __str__(self):
        return f'{self.fk_user.id} - {self.fk_user.username} - {self.fk_skill.skill_name} - {self.fk_skill.id}'

    def __repr__(self):
        return f'UserSkill(fk_skill={self.fk_skill}, fk_user={self.fk_user})'

