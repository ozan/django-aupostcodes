from setuptools import setup, find_packages
 
setup(name='django-aupostcodes',
    version='0.1',
    description='Django field and helpers for validating an Australian post code',
    long_description=open('README').read(),
    author='Ozan Onay',
    author_email='ozan.onay@gmail.com',
    url='http://github.com/ozan/django-aupostcode',
    packages=find_packages(),
    classifiers=[
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
    ]
)