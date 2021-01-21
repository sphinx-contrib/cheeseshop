# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst', 'r') as rm:
    long_desc = rm.read()

requires = ['Sphinx>=1.0']

setup(
    name='sphinxcontrib-cheeseshop',
    version='0.2',
    url='http://bitbucket.org/birkenfeld/sphinx-contrib',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-cheeseshop',
    license='BSD',
    author='Richard Jones, Georg Brandl',
    author_email='georg@python.org',
    description='Sphinx extension cheeseshop',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
