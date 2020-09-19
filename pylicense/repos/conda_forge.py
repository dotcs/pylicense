import requests
from bs4 import BeautifulSoup
import re

from . import BaseRepoParser

class CondaForgeRepoParser(BaseRepoParser):
    _base_url = 'https://anaconda.org/conda-forge/{pkg}'
    _license_regex = re.compile(r'License: ([a-zA-Z\-\_ 0-9]+)', re.MULTILINE)

    def _fetch_single(self, pkg: str):
        url = self._base_url.format(pkg=pkg)
        r = requests.get(url)

        try:
            soup = BeautifulSoup(r.text, features='html.parser')
            license = self.__query_license(soup)
            version = self.__query_version(soup)
        except:
            license = 'unknown'
            version = 'unknown'

        return {
            'name': pkg,
            'license': license,
            'version': version,
        }

    def __query_license(self, soup: BeautifulSoup):
        el = soup.find('li', {'title': 'License'})
        matches = self._license_regex.match(el.text.strip())
        return matches[1] if matches else 'unknown'

    def __query_version(self, soup: BeautifulSoup):
        el = soup.find('small', {'class': 'subheader'})
        return el.text.strip()


