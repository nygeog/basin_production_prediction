import argparse
from tools.tools import read_json
from code.capstone import run_capstone


def get_command_line_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="Get the args.",
        epilog=""" """,
    )

    parser.add_argument(
        "--project_config",
        required=True,
        help="Project configuration file settings",
    )

    return parser.parse_args()


def main(args):
    config = read_json(args.project_config)

    run_capstone(config)


if __name__ == "__main__":
    main(get_command_line_args())
