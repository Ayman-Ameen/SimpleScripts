# Auto submit jobs in a loop to the queue system if the job is not found in the queue

# Set the folder containing the job scripts
folder="/path/to/your/folder"

# Check every 1h if the job is in the queue
while true; do
    echo "Checking the queue"

    # Find all .sh files in the specified folder
    all_files=$(find $folder -name "*.sh")

    # Get the job names from the queue
    job_names=$(squeue -o "%.18i %.9P %.50j %.8u %.2t %.10M %.6D %R" | awk '{print $3}')

    # Loop through all the files found
    for file in $all_files
    do
        # Extract the job name from the filename
        job_name=$(echo $file | awk -F"/" '{print $NF}' | awk -F".sh" '{print $1}')
        echo "Job name: $job_name"

        # Check if the job is in the queue
        if [[ ! $job_names =~ $job_name ]]; then
            echo "Job $job_name not found in the queue"
            echo "Submitting job $job_name"
            # Submit the job
            sbatch $file
        else
            echo "Job $job_name found in the queue"
        fi
    done

    # Wait for 1 hour before checking again
    sleep 1h
done
