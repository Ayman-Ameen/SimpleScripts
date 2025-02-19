#!/bin/bash -l
main_hpc_dir=path_to_hpc_dir
work_dir=path_to_work_dir
conda_path=~/miniconda3/bin/activate
conda_env_path=path_to_env
port=6077
cd $work_dir
source $conda_path $main_hpc_dir/$conda_env_path
tensorboard --logdir $main_hpc_dir/$work_dir --port $port

