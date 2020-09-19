from argparse import ArgumentParser, Namespace
import pylicense.repos as repos


def dispatch(parser: ArgumentParser, cli_args: Namespace):
    if cli_args.repository == "pypi":
        r_parser = repos.PyPIRepoParser()
    elif cli_args.repository == "anaconda":
        r_parser = repos.AnacondaRepoParser()
    elif cli_args.repository == "conda-forge":
        r_parser = repos.CondaForgeRepoParser()

    pkgs_info = r_parser.from_file(cli_args.inputfile)
    if cli_args.output_format == "csv":
        print(r_parser.as_csv(pkgs_info))
    elif cli_args.output_format == "markdown":
        print(r_parser.as_markdown(pkgs_info))