"""
Documentation

cmd.py Module

Generates CLI interface in order to interact with cytopipe.
"""
import sys
import shutil
from pathlib import Path

from .args import *
from .cli_checker import cli_check, _check_mode_help_arg
from .exec.workflow_exec import exec_preprocessing
from .cli_docs import cli_docs


def run_cmd() -> None:
    """obtains all parameters and executes workflows

    Parameters
    ----------
    params : list
        list of user provided parameters

    Returns
    -------
    None
    """
    # create args handler
    # -- Cli Control Panel
    args_handler = CliControlPanel(sys.argv)
    print(args_handler.__repr__())

    # checking is user wanted to cli help
    if args_handler.cli_help is True:
        print(cli_docs)
        sys.exit(0)

    match args_handler.mode:

        case "init":

            if args_handler.mode_help is True:
                print(init_doc)
                sys.exit(0)

            init_args = args_handler.parse_init_args()

            # # setting up file paths
            # barcode_path = str(Path(init_args.barcode).absolute())
            # metadata_path = str(Path(init_args.metadata).absolute())

            # # create data folder
            # # raises error if data directory exists (prevents overwriting)
            # data_dir_obj = Path("data")
            # data_dir_obj.mkdir(exist_ok=False)
            # data_dir_path = str(data_dir_obj.absolute())

            # # moving all input files
            # for data_file in init_args.data:
            #     f_path = str(Path(data_file).absolute())
            #     shutil.move(f_path, data_dir_path)

            # shutil.move(barcode_path, data_dir_path)
            # shutil.move(metadata_path, data_dir_path)

#         case "run":
#             # selecting workflow process
#             proc_sel = params[1]

#             # executing process
#             if proc_sel == "cp_process":
#                 cp_process_args = parse_cp_process_args(params)

#                 print("executing cell profiler preprocessing")
#                 status = exec_preprocessing(n_cores=cp_process_args.max_cores)

#                 # CLI exit based on status
#                 if status:
#                     sys.exit(0)
#                 else:
#                     sys.exit("Workflow unsuccessful")

#         # display documentation of all modes
#         case "help":
#             print(cli_docs)


if __name__ == "__main__":

    run_cmd()
