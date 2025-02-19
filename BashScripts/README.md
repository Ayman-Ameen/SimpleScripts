# Bash Scripts Description

This document describes the purpose and usage of the bash scripts provided.

## tensorboard.sh

This script is used to launch TensorBoard for visualizing training logs.

### Usage

1.  Update the `main_hpc_dir`, `work_dir`, `conda_path`, and `conda_env_path` variables in the script with the appropriate paths for your environment.
2.  Run the script using `bash tensorboard.sh`.
3.  Access TensorBoard in your browser using the specified port (default: 6077).

## remove\_checkpoints.sh

This script is used to remove checkpoint files from the work directory.

### Usage

1.  Update the `workdir` variable in the script with the appropriate path to your work directory.
2.  Update the `checkpoint_prefix` variable if your checkpoint files have a different prefix.
3.  Run the script using `bash remove_checkpoints.sh`.
