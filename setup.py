from setuptools import find_packages, setup

setup(
    author="CS50",
    author_email="sysadmins@cs50.harvard.edu",
    classifiers=[
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Utilities"
    ],
    description="This is check50, with which you can check solutions to problems for CS50.",
    license="GPLv3",
    message_extractors = {
        'check50': [('**.py', 'python', None),],
    },
    install_requires=["attrs>=18", "bs4>=0", "pexpect>=4.6", "lib50>=1.1.8", "pyyaml>=3.10", "requests>=2.19", "termcolor>=1.1", "jinja2>=2.10"],
    extras_require = {
        "develop": ["sphinx", "sphinx_rtd_theme"]
    },
    keywords=["check", "check50"],
    name="check50",
    packages=["check50", "check50.renderer"],
    python_requires=">= 3.6",
    entry_points={
        "console_scripts": ["check50=check50.__main__:main"]
    },
    url="https://github.com/cs50/check50",
    version="3.0.5",
    include_package_data=True
)