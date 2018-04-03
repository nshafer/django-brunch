import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

long_description = """
This replaces the `runserver` management command with a version that fires up a `brunch watch` process alongside the
Django development server to automatically recompile css and javascript. The brunch process is not interrupted when
the Django server reloads, but it will die when you shut down the Django server.

`Full Documentation on GitHub <https://github.com/nshafer/django-brunch>`_
"""

setup(
    name='django-brunch',
    version='1.0.2',
    packages=['brunch'],
    include_package_data=True,
    install_requires=['Django>=1.8.0,<2.0.0'],
    license='BSD License',
    description='Integrate a Brunch workflow with Django.',
    long_description=long_description,
    url='https://github.com/nshafer/django-brunch',
    author='Nathan Shafer',
    author_email='nate-github@lotech.org',
    keywords='django brunch',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
