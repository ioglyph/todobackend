from setuptools import setup, find_packages

setup (
    name = "todobackend",
    version = "0.0.1",
    description = "Todobackend Django ReST service",
    packages = find_packages(),
    include_package_data = True,
    scripts = ["manage.py"],
    install_requires = [
            "Django>=1.9,<2.0",
            "django-cors-headers>=1.1.0",
            "djangorestframework>=3.3.0",
            "mysqlclient>=1.3.12",
            "uwsgi>=2.0"],
    extras_require = {
            "test": [
                "colorama>=0.3.9",
                "coverage>=4.5.1",
                "django-nose>=1.4.5",
                "nose>=1.3.7",
                "pinocchio>=0.4.2",
                "pytz>=2018.3"
            ]
        }
)
