from django.contrib import admin

from .models import Author, Post, Gender, Topic

admin.AdminSite.site_header = 'Blog Administration'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'website', 'locality', 'age', 'gender')
    list_filter = ['locality', 'age', 'gender']
    search_fields = ['full_name', 'email', 'website', 'locality']

admin.site.register(Author, AuthorAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author')
    list_filter = ['pub_date', 'topics']
    search_fields = ['title', 'content', 'topics__topic', 'author__full_name']

admin.site.register(Post, PostAdmin)


admin.site.register(Gender)
admin.site.register(Topic)
