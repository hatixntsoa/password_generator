from setuptools import setup, find_packages

setup(
    name='pypass-tool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
    ],
    entry_points={
        'console_scripts': [
            'pypass=pypass.main:main',
        ],
    },
    include_package_data=True,
    package_data={
        'pypass': ['passwords/*'],
    },
)