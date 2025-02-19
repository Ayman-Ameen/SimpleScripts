# Slurm Job Submission Loop Script

This script is designed to automatically submit jobs to a Slurm-managed cluster. It checks the queue for existing jobs and submits new ones if they are not found.

## Usage

1.  Place the `loop.sh` script in a directory with your Slurm job submission scripts (`*.sh`).
2.  Modify the `folder` variable in `loop.sh` to point to the directory containing your job scripts.
3.  Run the `loop.sh` script. It will continuously monitor the queue and submit jobs as needed.

## Script Details

The script uses the following commands:

*   `find`: To locate all `.sh` files in the specified directory.
*   `squeue`: To check the Slurm queue for running jobs.
*   `sbatch`: To submit jobs to the Slurm queue.
*   `awk`: To parse the output of `find` and `squeue`.

## Configuration

*   `folder`:  The directory containing the Slurm job scripts.  Modify this variable in the `loop.sh` script.
*   The script checks the queue every 1 hour.  This can be adjusted by modifying the `sleep` duration.

## Notes

*   Ensure that the user running the script has the necessary permissions to submit jobs to the Slurm queue.
*   Adjust the `squeue` command options as needed to match your Slurm configuration.
