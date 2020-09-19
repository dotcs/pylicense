from .conda_forge import CondaForgeRepoParser

class AnacondaRepoParser(CondaForgeRepoParser):
    _base_url = 'https://anaconda.org/anaconda/{pkg}'