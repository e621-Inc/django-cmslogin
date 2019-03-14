# DJANGO CMS Login

!!! ALPHA !!!  
explicitly django 1.9 atm

## configure

settings.py:
```python
INSTALLED_APPS = [
    '...',
    'cmslogin',
    '...'
]
```

project urls.py:
```python
urlpatterns = [
    '...',
    url(
        r'^cmslogin/',  # choose a name you want
        include('cmslogin.urls'),
    ),
]
```

## Plugins

* CMSLoginPlugin: provides login and logout form (logout can be prevented)
* CMSLogoutPlugin: provides logout button

## Tags

* {% cmslogin_login %}: provides only a login form
* {% cmslogin_logout %}: provides only a logout button
* {% cmslogin_loginout %}: provides login form and logout button

```html
{% load cmslogin_tags %}
<body>
    {% cmslogin_loginout %}
</body>
```