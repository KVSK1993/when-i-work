# when-i-work
# Web Traffic Data Processing

This program processes web traffic data from CSV files stored in an AWS S3 bucket.

## Prerequisites

Make sure you have python and `pyenv` (Python environment manager) installed in the system.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/KVSK1993/when-i-work.git

2. **Execute the subsequent script to set up the Python environment and install essential dependencies:**
    ```bash
    cd when-i-work
    sh scripts/setup_dev_env.sh

3. **Activate the environment**
    ```bash
    source venv/bin/activate

4. **Run the script**
    ```bash
    python3 data-pipeline/web_traffic_data_processing_service.py

5. **The final transformed CSV file gets downloaded in downloads directory**

6. **The logs would get generated in pipeline.log file**
