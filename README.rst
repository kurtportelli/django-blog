====
Blog
====

Blog is a Django app to read a blog. Visitors can view a yearly or
monthly archive along with the complete index, as well as read
individual posts in detail.

Quick start
-----------

1. Add "blog" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'blog',
    ]

2. Include the blog URLconf in your project urls.py like this::

    path('blog/', include('blog.urls')),

3. Run `python manage.py migrate` to create the blog models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to add authors and posts (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/blog/ to read the blog.