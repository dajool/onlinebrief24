from setuptools import setup, find_packages

setup(
    name='onlinebrief24',
    version='1.0',
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
    long_description=open('README.rst', 'r').read(),
    keywords = ['pdf', 'mailing', 'letters', 'post'],
    platforms='any',
)
