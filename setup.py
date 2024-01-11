import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

PROJECT_NAME = 'django-simple-third-party-jwt-dev-dashboard'
GIT_REPO_NAME = 'Django-Simple-3rd-Party-JWT-Dev-Dashboard'

setuptools.setup(
    name=PROJECT_NAME,
    fullname=PROJECT_NAME,
    author='Nat Lee',
    author_email='natlee.work@gmail.com',
    description='Dashboard for using JWT with 3rd party login.',
    keywords='django, jwt, 3rd party login, dashboard, toolbox',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/NatLee/{GIT_REPO_NAME}',
    project_urls={
        'Documentation': f'https://github.com/natlee/{GIT_REPO_NAME}',
        'Bug Reports': f'https://github.com/natlee/{GIT_REPO_NAME}/issues',
        'Source Code': f'https://github.com/natlee/{GIT_REPO_NAME}',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    package_data={
        "django_simple_third_party_jwt_dev_dashboard": [
            "templates/*",
            "templates/dashboard/*",
            "templates/registration/*",
        ]
    },
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'django>=4.0.0',
        'djangorestframework',
        'django-simple-third-party-jwt>=0.1.1',
        'drf-yasg',
        'django-bootstrap3'
    ],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
)
