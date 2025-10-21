import setuptools

with open("../README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # Here is the module name.
    name="hangman-terminal",

    # version of the module
    version="1.0.1",

    # Name of Author
    author="Krishna Menon",

    # your Email address
    author_email="menonkrishna57@gmail.com",

    # #Small Description about module
    description="Hangman in terminal",

    # long_description=long_description,

    # Specifying that we are using markdown file for description
    long_description=long_description,
    long_description_content_type="text/markdown",

    # Any link to reach this module, ***if*** you have any webpage or github profile
    url="https://github.com/menonkrishna57/Hangman-Game-in-Python",
    packages=setuptools.find_packages(),


    # if module has dependencies i.e. if your package rely on other package at pypi.org
    # then you must add there, in order to download every requirement of package



    #     install_requires=[
    #      "package1",
    #    "package2",
    #    ],


    license="MIT",

    # classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
    'console_scripts': [
        # The command can have a hyphen, but the module path MUST use an underscore.
        'hangman-terminal = hangman_terminal.main:main',
    ],
    }
)