from django.contrib import admin

#from .models import UserSkill, Skill, Profile
from .models import Skill, UserSkill


admin.site.register(UserSkill)
#admin.site.register(Profile)
admin.site.register(Skill)

