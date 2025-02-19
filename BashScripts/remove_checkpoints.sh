# This script removes all files with the prefix checkpoint_0 in the work directory.
workdir=path_to_work_dir
cd $workdir
checkpoint_prefix=checkpoint_0
rm -r $(find * -name $checkpoint_prefix*)
