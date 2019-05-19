Brunch with Django
==================

Integrate a [Brunch](http://brunch.io/) workflow with [Django](https://www.djangoproject.com/).

This replaces the `runserver` management command with a version that fires up a `brunch watch` process alongside the
Django development server to automatically recompile css and javascript. The brunch process is not interrupted when
the Django server reloads, but it will die when you shut down the Django server.


Features
--------

- Run the Django development web server and brunch watch with one command in one window
- Leaves Brunch completely decoupled from Django, so there is no interdependency between the two. This is simply a
convenience module.
- Can optionally enable the brunch server so that brunch plugins like `auto-reload-brunch` will do live reloading of
app assets such as CSS and Javascript upon saving. Set up brunch to also watch your templates and/or views to get
live-reloading on modification of anything.


Requirements
------------

- Brunch >= 2.0
- Django == 1.11, 2.0, 2.1, 2.2

Integrate brunch in your Django project
---------------------------------------

> **Note:** These instructions assume you have installed Brunch globally as directed by brunch.io. If you prefer to only have brunch
> installed locally in `node_modules/` then modify all of these instructions to run brunch with `npx brunch` instead of
> `brunch`.

1. Initialize brunch in your Django project directory. This skeleton will create a brunch-config.js and package.json
file in the root of your project directory.

    ```bash
    cd myproject
    brunch new -s https://github.com/nshafer/django-brunch-skeleton
    ```

2. Put your CSS and JS files in `app/`, images and other files in `app/assets/`

3. Test brunch. This will output to `public/`

    ```bash
    brunch build
    ```

4. Add brunch's output directory `public/` to the STATICFILES_DIRS list so that Django will find the files that Brunch
will create. Remove any existing reference to `app/` since we now only want to include assets output by brunch.

    ```python
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "public"),
    ]
    ```

5. Link the brunch output in your templates

    ```html
    <link rel="stylesheet" href="{% static "app.css" %}"/>
    <script src="{% static "app.js" %}"></script>
    ```


Install the Django Module
-------------------------

1. Install 'django-brunch' from PyPI

    ```bash
    pip install django-brunch
    ```
    
2. Add `brunch` to INSTALLED_APPS, but BEFORE `django.contrib.staticfiles` so that it overrides the `runserver` command:

    ```python
    INSTALLED_APPS = [
        ...
        'brunch',
        ...
        'django.contrib.staticfiles'
    ]
    ```

3. Configure django-brunch in your settings.py file. At a minimum, `BRUNCH_DIR` must be defined. This needs to be an
absolute path to the directory where your `brunch-config.js` or `brunch-config.coffee` file lives.

    ```python
    BRUNCH_DIR = BASE_DIR
    ```
    
4. Run `runserver` like you normally would. A brunch process will be started alongside the Django development web server
in the directory you provided with BRUNCH_DIR. One terminal, both processes!

    ```bash
    ./manage.py runserver
    ```


Live Reloading
--------------

By default, the 'brunch-config.js' that is installed from
[django-brunch-skeleton](https://github.com/nshafer/django-brunch-skeleton)
will enable auto-reloading upon modification of files in `app/` and `template/` as long as you enable
`BRUNCH_SERVER` in your Django settings.
Add your individual app static and template directories to `paths.watched` to get the same for all of your apps.


Building for production
-----------------------

Building for production will be much the same, with just one extra step to do before you run `collectstatic`. You need
to have brunch build a final production version of your assets.

```
brunch build --production
./manage.py collectstatic
```


Settings
--------

### BRUNCH_DIR (required)

This should be an absolute path to the location of your brunch directory; where your `brunch-config.js` or
`brunch-config.coffee` file lives. This is used as the working directory of the brunch command.

Example:

```python
BRUNCH_DIR = os.path.join(BASE_DIR, "brunch")
```

### BRUNCH_CMD (optional)

Default:

```python
BRUNCH_CMD = ("/usr/bin/env", "brunch")
```

This is the location of your `brunch` CLI command. It is passed to
[subprocess.Popen](https://docs.python.org/3.4/library/subprocess.html#popen-constructor) so it needs to either be a
string or a sequence type (list, tuple). It is recommended that this is a tuple or list of arguments so that
we can spawn it without involving shell parsing. If it is a string AND the string has a space or other shell characters,
then you will need to set BRUNCH_SHELL to True as well, so that Popen knows to spawn a shell to parse the command.

If you install brunch as a local dependency in the local `node_modules` directory, then you'll probably want something
like this:

```python
BRUNCH_CMD = ("/usr/bin/npx", "brunch")
```

Or if you have an older version of Node.js / npm:

```python
BRUNCH_CMD = os.path.join(BASE_DIR, "brunch", "node_modules", ".bin", "brunch")
```

### BRUNCH_SHELL (optional)

Default:

```python
BRUNCH_SHELL = False
```

If your BRUNCH_CMD requires a shell to parse, then set this to True. This is passed directly to
[subprocess.Popen](https://docs.python.org/3.4/library/subprocess.html#popen-constructor)'s `shell` argument. For
example, this needs to be True if your BRUNCH_CMD has a space in it or any other kind of special shell syntax.

### BRUNCH_SERVER (optional)

Default:

```python
BRUNCH_SERVER = False
```

If this is enabled, then the `brunch watch` command will be started with the `--server` argument. This will instruct
Brunch to start up its internal server alongside Django's. This shouldn't be needed in a lot of cases, however one very
useful time for this is if you're using the "auto-reload-brunch" plugin in brunch. If you are, then enabling the brunch
server will allow it to inform the browser of changes to your assets and do live reloads.


Example project
---------------

To run the example Django project, follow these steps

1. Create a new virtualenv (assuming [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/))

    ```
    mkvirtualenv django-brunch-example
    ```

2. Clone the github repository and install requirements

    ```
    git clone https://github.com/nshafer/django-brunch.git
    cd django-brunch/example
    pip install -r requirements.txt
    npm install
    ```

3. Migrate if needed

    ```
    ./manage.py migrate
    ```

4. Run the server and brunch

    ```
    ./manage.py runserver
    ```

5. Log in to http://localhost:8000 and see them working together. Modify the stylesheet in `app/style/site.css` and
save it to live reloading in action. If you need to get in to the admin, the username and password are 'admin'.


Inspiration
-----------

Inspiration for how to integrate Brunch with Django comes from how the [Phoenix Framework](http://www.phoenixframework.org/)
does it by default in a new Phoenix project. I used their example as a model for the highly customized `brunch-config.js`
that departs from brunch conventions a bit.


TODO
----

- Add hook in `collectstatic` to automatically run `brunch build --production` before collecting files
- Add command-line `--disable-brunch` to the `runserver` command in cases where you might not want to fire it up. Right
now you have to disable `brunch` in `INSTALLED_APPS` in your setup.py to turn it off.
- Add a `initbrunch` management command that clones down django-brunch-skeleton and copies files over safely into an
existing Django project. Perhaps pre-initialize the `brunch-config.js` based on existing Django static configuration.
- Add a bit of javascript to `brunch-config.js` to allow globs in the `paths.watched` array, so you can just specify
something like `**/templates` and `**/static` to get all app assets automatically without having to automatically add
them.
