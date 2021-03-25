from setuptools import setup, find_packages
import os

parent_folder = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(parent_folder, 'requirements.txt')) as req:
    INSTALL_REQUIRES = req.read().split('\n')

setup(
    author='Whitman Bohorquez',
    author_email='whitman-2@hotmail.com',
    name='hexagonal-microservice',
    license='',
    description='Hexagonal Architecture with FastAPI, RabbitMQ and MongoDB',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.9.2',
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        'Development Status :: Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9.2',
        'Intended Audience :: Developers',
    ],
)
