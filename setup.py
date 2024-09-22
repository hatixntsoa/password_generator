from setuptools import setup, find_packages

setup(
    name='pypass-tool',
    version='0.2.2',
    description='A CLI tool for password generation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Hatix Ntsoa',
    author_email='hatixntsoa@gmail.com',
    url='https://github.com/h471x/password_generator',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    install_requires=[
        'Flask',
    ],
    entry_points={
        'console_scripts': [
            'pypass=pypass.main:main',
            'pypass-web=pypass.app.gui.web.pypass_web:main',
            'pypass-gui=pypass.app.gui.desktop.pypass_gui:main',
        ],
    },

    include_package_data=True,
    package_data={
        'pypass': ['passwords/infos.md'],
    },
)