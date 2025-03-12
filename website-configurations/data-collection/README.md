# Data Collection Tools
In this folder, we include the tools used for data collection. All data collection was done on Linux virtual machines in Google Cloud (gcloud). `data_collection_script_linux.py` is the entry point for all data collection and is responsible for fetching the list of websites to visit and opening each one in Chrome with the custom extensions.

## VM Tooling
This directory contains:

1) `data_collection_script_linux.py`, the python script the VM used to coordinate data collection. It is responsible for fetching a subset of websites to visit and opening Chrome with the custom extensions (in `extensions/`) installed.

2) `gcloud_functions`, tooling we deployed in gcloud functions to coordinate the virtual machines reading from a central file of websites to visit (`pixel_get_urls`) and uploading collected data to a gcloud bucket for storage (`pixel_upload_data`).

3) `vm_configuraiton.sh`, the startup script used to install and kick off collection on a new virtual machine.

## Extensions
This directory contains the two Chrome extensions used to collect data in this study. 

## Instructions
This codebase assumes a gcloud bucket for storage, gcloud functions for uploading data, and gcloud virtual machines for collecting data. These instructions include the information for that specific setup but other storage and compute options would also work with minor modifications.

1) Create a gcloud bucket to store files downloaded by the extension (ex: website_files).

2) Upload to that bucket a csv titled `data-collection-input.csv` that has the list of websites you would like to collect data from. (NOTE: the name of the CSV can be modified in `vm-tooling/gcloud_functions/pixel_get_urls/main.py` on line 20).
3) Deploy two gcloud functions:

    a) `vm-tooling/gcloud_functions/pixel_get_urls` -- this function will fetch the CSV list of websites to visit and assign them in chunks to virtual machines (through the `get_urls` endpoint). Note that the function assumes you are using 50 machines, as the study did. This can be modified on line 65 of `vm-tooling/gcloud_functions/pixel_get_urls/main.py`. This code will further keep track of websites that have been visited to avoid an unnecessary re-visit should a session be terminated before the input list is completed (this could be turned off by removing the call to `check_urls_status()` on line 79). This setup could also be modified to use a CSV that lives on the virtual machine (or a local machine) instead, by modifying the `def get_urls()` function in `data_collection_script_linux.py`, where this endpoint is called, to instead read directly from a CSv file.

    b) `vm-tooling/gcloud_functions/pixel_upload_data` -- this function is called by the Chrome extensions and will upload data to the gcloud bucket. 

Both of these functions require an environment file that specifies the project name (of the gcloud account) and bucket name (ex: website_files).

4) Update the environment variables for the Chrome extensions, so they know which endpoint to use for 3b.
You can do this by creating an `env.js` file in the root directory of mv2 and mv3. If you use the gcloud endpoint provided, it should look like this in `extensions/mv2/env.js` and `extensions/mv3/env.js`:
```
const ENV = {UPLOAD_ENDPOINT: "https://{gcloud_region}-{website_files}.cloudfunctions.net/upload-data"}
```

5) Make a few modifications to the `data_collection_script_linux.py` script. In particular, you will need create a `.env` file that includes:

    a) a key file that authorizes a gcloud service account ([instructions here](https://cloud.google.com/iam/docs/keys-create-delete#gcloud))

    b) the name of the gcloud bucket you are reading from/writing to (ex: website_files)

    c) the endpoint defined in 3a
    
For example, it will look something like this:
```
SERVER_KEYFILE_PATH = ./key_file.json
BUCKET_NAME = website_files
BASE_PATH=/home/{user}
GET_URLS_ENDPOINT=https://{gcloud_region}-{website_files}.cloudfunctions.net/get_urls"
```

Note that this script (and the extensions) use the name of the virtual machine, as it was used to help organize downloaded files. The extensions upload files in the format `date/vm_name/website_url`, which could be modified in the `background.js` files of each extension (mv2 and mv3) to remove `instanceName` from the paths of uploaded files. In the `data_collection_script_linux.py` file, you could remove the `get_vm_name()` function, called on line 157 to ignore this (and either set it to a constant value or remove all instances of it elsewhere).

6) Run the `vm_configuration.sh` file which will download Chrome, install dependencies, and kick off the `data_collection_script_linux.py` script. Chrome is downloaded from a `.deb` file stored in the gcloud bucket, to preserve Chrome versions across all data collection attempts. To configure this setup, download Chrome to a gcloud bucket, replace line 10 with the name of the file, and add a .env file with the bucket name (ex:```MY_BUCKET="gs://website_files```).
