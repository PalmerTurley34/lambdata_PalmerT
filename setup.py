# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata_PalmerT", # the name that you will install via pip
    version="1.0",
    author="Palmer Turley",
    author_email="palmerturley34@gmail.com",
    description="Helper Functions",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/PalmerTurley34/lambdata_PalmerT",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)