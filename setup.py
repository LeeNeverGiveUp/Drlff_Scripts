"""
"""
import re
import ast
from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('drlff/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name='DRLFF',
    version=version,
    url='http://neu-git.ddns.net/NEUMIS/DRLFF/',
    author='Charles Xu',
    author_email='the0demiurge@gmail.com',
    description='DRLFF',
    long_description=__doc__,
    packages=['drlff'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'tensorflow>=1.0',
        'gym>=0.8.1',
    ],
)
