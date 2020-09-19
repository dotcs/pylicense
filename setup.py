import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.readlines()

with open("requirements_develop.txt", "r") as fh:
    requirements_develop = fh.readlines()

setuptools.setup(
    name="dcs-pylicense",
    version="0.0.2",
    author="Fabian Mueller",
    author_email="repository@dotcs.me",
    description="",
    license="GPLv3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dotcs/pylicense",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        # see: https://pypi.org/classifiers/
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Office/Business",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    extras_require={"develop": requirements_develop},
    entry_points={
        "console_scripts": [
            "pylicense=pylicense.cli:run",
        ]
    },
)