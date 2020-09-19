import argparse


def configure_parser():
    parser = argparse.ArgumentParser(
        description="""
PyLicense is a CLI tool that queries license information from 
one of the following package repositories: PyPI, Anaconda or conda-forge.

It requires a file in the format of a standard requirements.txt file with one
package per line.
"""
    )

    parser.add_argument("-v", "--verbose", dest="verbosity", action="count", default=0)

    parser.add_argument(
        "inputfile", help="Input file in the form of a requirements.txt file"
    )
    parser.add_argument(
        "-r",
        "--repository",
        default="pypi",
        choices=["pypi", "anaconda", "conda-forge"],
        help="Repository that should be queried.",
    )
    parser.add_argument(
        "--output-format",
        default="markdown",
        choices=["csv", "markdown"],
        help="Output format of the resulting table",
    )

    return parser