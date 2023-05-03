from django.contrib import admin

# Register your models here.
from .models import Portfolio, Post

admin.site.register(Portfolio)
admin.site.register(Post)