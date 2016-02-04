import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-brunch',
    version='0.0.9',
    packages=['brunch'],
    include_package_data=True,
    install_requires=['Django>=1.8.9,<1.10.0'],
    license='BSD License',
    description='Integrate a Brunch workflow with Django.',
    long_description=README,
    url='https://github.com/nshafer/django-brunch',
    author='Nathan Shafer',
    author_email='nate-github@lotech.org',
    classifiers=[
        'Development Status :: 4 - Beta'
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
