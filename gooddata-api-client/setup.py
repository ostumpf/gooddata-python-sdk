"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: support@gooddata.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

NAME = "gooddata-api-client"
VERSION = "1.2.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="OpenAPI definition",
    author="GoodData (generated by OpenAPI Generator)",
    author_email="support@gooddata.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "OpenAPI definition"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    license_file="LICENSE.txt",
    license_files=("LICENSE.txt",),
    long_description=long_description,
    long_description_content_type="text/markdown",
)