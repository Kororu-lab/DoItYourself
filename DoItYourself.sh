#!/bin/bash

# Usage: ./DoItYourself.sh 2012-01 2012-12 SuicideWatch 12

start_date=$1
end_date=$2
subreddit=$3
concurrency_limit=$4

# Hardcoded workload directory relative to the script's location
workload_dir="./workload"

# Function to increment month
increment_month() {
    echo $(date -d "$1-01 +1 month" "+%Y-%m")
}

# Prepare to process each month within the range
current_date="$start_date"
end_date_next=$(increment_month "$end_date")

# Process each month
while [[ "$current_date" != "$end_date_next" ]]; do
    echo "Processing month: $current_date for subreddit: $subreddit..."
    # Call the Python script with hardcoded parameters, including the workload directory
    (python main.py "$current_date" "$subreddit" "$workload_dir") &
    
    # Update current_date to the next month
    current_date=$(increment_month "$current_date")
    
    # Ensure not to exceed the concurrency limit
    while [[ $(jobs -r | wc -l) -ge $concurrency_limit ]]; do
        wait -n
    done
done

# Wait for all jobs to complete before exiting
wait
echo "Parallel processing of months completed!"
