import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "utilsPy",
    version = "0.0.2",
    author = "Joli Holmes",
    author_email = "holmesjoli@gmail.com",
    description = "Python package with basic utility functions",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/holmesjoli/utilsPy",
    packages = setuptools.find_packages(),
    install_requires = [
        'pyyaml==5.4'
    ]
)
