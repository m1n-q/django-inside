=====
ex00
=====

ex00 is a Django app to upload your image.

Quick start
-----------

1. Add "ex00" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'ex00',
    ]

2. Include the ex00 URLconf in your project urls.py like this::

    path('ex00/', include('ex00.urls')),

3. Run ``python manage.py migrate`` to create the ex00 models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a ex00 (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/add-image/ to upload your image.
