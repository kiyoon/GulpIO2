#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os
import sys
from shutil import rmtree

from setuptools import setup, Command, find_packages
from pathlib import Path

_here = os.path.dirname(__file__)
about = {}  # type: ignore
with open(os.path.join(_here, "src", "gulpio2", "__version__.py")) as f:
    exec(f.read(), about)

# Package meta-data.
REQUIRES_PYTHON = ">=3.6.0"

# What packages are required for this module to be executed?
REQUIRED = [
    # 'requests', 'maya', 'records',
    "simplejpeg>=1.0.0",
    "pillow",
    "docopt",
    "jinja2",
    "numpy",
    "sh",
    "tqdm",
]

# What packages are optional?
EXTRAS = {}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!


# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANIFEST.in file!
try:
    with io.open(
        os.path.join(_here, "README.rst"), encoding="utf-8"
    ) as f:  # type: ignore
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = about["__description__"]



class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []  # type: ignore

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(_here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Checking packages")
        os.system("twine check dist/*")

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        self.status("Pushing git tags…")
        os.system("git tag v{0}".format(about["__version__"]))
        os.system("git push --tags")

        sys.exit()


# Where the magic happens:
setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description_content_type="text/x-rst",
    long_description=long_description,
    author=about["__author__"],
    author_email=about["__author_email__"],
    python_requires=REQUIRES_PYTHON,
    url=about["__url__"],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    scripts=[
        str(script_path) for script_path in Path('src/gulpio2/scripts').iterdir()
    ],
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    # $ setup.py publish support.
    cmdclass={"upload": UploadCommand},
)
