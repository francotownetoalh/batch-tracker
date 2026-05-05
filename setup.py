from setuptools import setup, find_packages

setup(
    name='batch-tracker',
    version='0.5.27',
    packages=find_packages(),
    install_requires=['requests>=2.28.0', 'click>=8.0'],
    entry_points={'console_scripts': ['batch-tracker=batchtracker:main']},
)
