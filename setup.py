import setuptools

with open('README.md', 'r') as handle:
    long_description = handle.read()

setuptools.setup(
    name="annasys-console",
    version="1.0.5",
    author="Anna Poulakos",
    author_email="anna.poulakos@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apoulakos/python-console",
    packages=[
        "annasys.console"
    ],
    install_required=[
        "Click==7.0",
        "colorama==0.4.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
