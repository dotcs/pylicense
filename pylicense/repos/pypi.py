import requests

from . import BaseRepoParser

class PyPIRepoParser(BaseRepoParser):
    _base_url = 'https://pypi.org/pypi/{pkg}/json'

    def _fetch_single(self, pkg: str):
        url = self._base_url.format(pkg=pkg)
        r = requests.get(url)

        try:
            content = r.json()
            license = content['info']['license']
            version = content['info']['version']
        except:
            license = 'unknown'
            version = 'unknown'

        return {
            'name': pkg,
            'license': license,
            'version': version,
        }

