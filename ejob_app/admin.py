from django.contrib import admin
from .models import User,SeekerProfile,RecruiterProfile,Job,SeekerSkillset, Category, Subcategory

admin.site.register(User)
admin.site.register(SeekerProfile)
admin.site.register(Job)
admin.site.register(RecruiterProfile)
admin.site.register(SeekerSkillset)
admin.site.register(Category)
admin.site.register(Subcategory)