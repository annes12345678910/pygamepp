from setuptools import setup, find_packages

setup(
    name="pygameplusplus",
    version="0.1.0",
    author="Your Name",
    description="Enhanced tools and helpers for Pygame",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pygameplusplus",
    packages=find_packages(),
    install_requires=["pygame"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
