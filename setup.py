from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing1605",
    version="0.0.2",
    author="emy",
    author_email="edsonmy@gmail.com",
    description="Image processing Package using skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edsonmy/dio-image-processing1605",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)