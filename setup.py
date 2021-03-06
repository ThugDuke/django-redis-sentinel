from setuptools import setup

description = """
Plugin for django-redis that supports Redis Sentinel
"""

setup(
    name="django-redis-sentinel",
    url="https://github.com/KabbageInc/django-redis-sentinel",
    author="Chris Heisel",
    author_email="cheisel@kabbage.com",
    version="1.0",
    packages=[
        "django_redis_sentinel",
    ],
    description=description.strip(),
    install_requires=[
        "django-redis>=4.7.0",
    ],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)
