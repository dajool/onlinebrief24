from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='onlinebrief24',
    version='1.2',
    packages=find_packages("."),
    include_package_data=True,
    url='https://github.com/dajool/onlinebrief24',
    license='MIT License',
    author='Jochen Breuer',
    author_email='breuer@dajool.com',
    install_requires=[
        'paramiko>=1.15.3',
    ],
    description='Python client for onlinebrief24.de - a German letter sending service.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords = ['pdf', 'mailing', 'letters', 'post'],
    platforms='any',
)
