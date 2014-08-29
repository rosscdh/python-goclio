from setuptools import setup

setup(
    name="python-goclio",
    packages=['goclio'],
    version='0.0.1',
    author="Ross Crawford-d'Heureuse",
    license="MIT",
    author_email="ross@lawpal.com",
    url="https://github.com/rosscdh/python-goclio",
    description="A python module for using the goclio api",
    zip_safe=False,
    include_package_data=True,
    install_requires = [
        'requests',
        'requests-oauth2',
    ]
)
