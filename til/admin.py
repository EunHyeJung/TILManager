from django.contrib import admin
from .models import Til, Review, Plan, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Til)
admin.site.register(Review)
admin.site.register(Plan)