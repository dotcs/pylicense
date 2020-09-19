from pylicense.dispatcher import dispatch
from pylicense.parser import configure_parser
from pylicense.logger import configure_logger
import pylicense.constants as pc

def run():
    logger = configure_logger()
    parser = configure_parser()

    cli_args = parser.parse_args()
    log_level = pc.LOG_LEVELS[min(cli_args.verbosity, len(pc.LOG_LEVELS) - 1)]
    logger.setLevel(log_level)

    logger.debug(f"Parsed CLI arguments: {cli_args}")

    dispatch(parser, cli_args)


if __name__ == "__main__":
    run()