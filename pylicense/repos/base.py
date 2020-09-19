from typing import Union, List, Dict, Optional
import re
import pandas as pd
import json


class BaseRepoParser(object):
    _base_url: str = ""
    _line_regex = re.compile(r"^([A-Za-z0-9\-\_]+)")

    def _fetch_single(self, pkg: str):
        raise NotImplementedError()

    def _fetch_multiple(self, pkgs: List[str]):
        return [self._fetch_single(pkg) for pkg in pkgs]

    def _fetch(self, pkgs: Union[str, List[str]]):
        if type(pkgs) == str:
            return self._fetch_single(pkgs)
        else:
            return self._fetch_multiple(pkgs)

    def _match_input_line(self, line):
        return self._line_regex.match(line)

    def _read_from_file(self, filepath: str):
        with open(filepath, "r") as f:
            lines = f.read().split("\n")
        return self._postprocess_lines(lines)

    def _read_from_io(self, io):
        lines = io.read().split("\n")
        return self._postprocess_lines(lines)

    def _postprocess_lines(self, lines: List[str]):
        pkgs = []
        for line in lines:
            matches = self._match_input_line(line)
            if matches is None:
                continue
            pkgs.append(matches[1])
        return sorted(pkgs)

    def from_file(self, filepath: str):
        pkgs = self._read_from_file(filepath)
        pkgs_info = self._fetch(pkgs)
        return pkgs_info

    def from_io(self, io):
        pkgs = self._read_from_io(io)
        pkgs_info = self._fetch(pkgs)
        return pkgs_info

    def as_csv(self, pkgs_info: List[Dict], separator="|"):
        df = pd.DataFrame.from_dict(pkgs_info)
        return df.to_csv(index=False, sep=separator)

    def as_markdown(self, pkgs_info: List[Dict]):
        df = pd.DataFrame.from_dict(pkgs_info)
        return df.to_markdown(index=False)

    def as_json(self, pkgs_info: List[Dict], indent: Optional[int] = None):
        return json.dumps(pkgs_info, indent=indent)
