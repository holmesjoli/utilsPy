import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "utils",
    version = "0.0.1",
    author = "Joli Holmes",
    author_email = "jh111@rice.edu",
    description = "Python package with basic utility functions",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "XXX",
    packages = setuptools.find_packages(),
    install_requires = [
        'pyyaml==5.1'
    ]
)
