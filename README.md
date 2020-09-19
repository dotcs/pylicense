# PyLicense

PyLicense is a CLI tool that queries license information from one of the
following package repositories: PyPI, Anaconda or conda-forge.

PyLicense uses the online information of those repositories, e.g. the license
information that is listed on `pypi.org/pypi/<packagename>`, e.g. https://pypi.org/project/dcs-pylicense/.
While this means that the package must not be installed on the local system,
it also shows information about the lastest package version and not every
possible package version.

## Installation

To install the package run 

```console
$ pip install dcs-pylicense
```

The tool registers itself as `pylicense`.
To learn about the available arguments refer to its help:

```console
$ pylicense --help
```

## Usage

PyLicense requires a file in the format of a requirements file.
The format is described [here](https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format).

To query license information of the packages run

```console
$ pylicense path/to/my/requirements.txt
| name       | license   | version   |
|:-----------|:----------|:----------|
| black      | MIT       | 20.8b1    |
| pylint     | GPL       | 2.6.0     |
| pytest     | MIT       | 6.0.2     |
| pytest-cov | MIT       | 2.10.1    |
| sphinx     | BSD       | 3.2.1     |
| twine      | unknown   | 3.2.1     |
```

It is also possible to read from stdin
```console
$ cat /path/to/my/requirements.txt | pylicense
```

By default the result is returned as a markdown table.
Other format options are available, e.g. output formatting as CSV.

```console
$ pylicense --output-format csv path/to/my/requirements.txt
name|license|version
black|MIT|20.8b1
pylint|GPL|2.6.0
pytest|MIT|6.0.2
pytest-cov|MIT|2.10.1
sphinx|BSD|3.2.1
twine|unknown|3.2.1
```

By default the [Python Package Index (PyPI)](https://pypi.org) is queried.
This can be changed with the `--repository` flag.

For example to query the anaconda package repository use the following command

```console
$ pylicense --repository anaconda path/to/my/requirements.txt
| name       | license      | version   |
|:-----------|:-------------|:----------|
| black      | MIT          | 19.10b0   |
| pylint     | GPL-2        | 2.6.0     |
| pytest     | MIT          | 6.0.2     |
| pytest-cov | MIT          | 2.10.1    |
| sphinx     | BSD-2-Clause | 3.2.1     |
| twine      | Apache  2    | 2.0.0     |
```