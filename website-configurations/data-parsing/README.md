# Data Parsing
This directory contains the logic used to parse downloaded website files and identify if any of the following are TRUE for each website: Meta Pixel installation, Meta Pixel Form Data Collection Configuration, Meta Pixel Form Data Collection, Google Tag installation, and Google Tag Form Data Collection.

## Instructions

### Set up the database

If you'd like to run this locally, you can install postgres and create a database with the name `processed_pixel_data`. Then, add a `.env` file to point to your database. The file needs to include the following environment variables:
```
db_host=localhost
db_username=$user$
db_username=''
db_name=processed_pixel_data
````

Our script will create the required tables in the database. 

### Install dependencies

The scripts have been tested in Python3.8. You can install the dependencies by running:

```l
pip install -r requirements.txt
```

Note that if you are using a Mac with a new chip, you may need the binary version of the psycopg2 package. If you hit an error running with psycopg2, you can switch versions by running additionally:

```
pip uninstall psycopg2
pip install psycopg2-binary
```

### Raw data folder placement

The parser needs to read the raw data as an argument. The raw data should be located in one folder within the same directory as the `data_parser.py` script. The collected data should adhere to the following folder structure:
```
date/vm_name/website
```

The date must follow the format `%m-%d-%Y`. Therefore, for March 7, 2025, it would be `3-7-2025`, while for December, 31st, 2024 it would be `12-31-2024`.

### Running the parser

To run the parser, you execute the main script (`data_parser.py`) and specify the date (the outer folder), i.e.:

```
python data_parser.py --path date
```

This means that if you have data collected through different dates you should run the command for each date folder separately.

### Testing on a subset of our data.

You can test the parser on a small subset of our full dataset. You can download the dataset [here](https://nyu.app.box.com/s/u3oapbdcppqz1fxjax5k4v6h5z8tvvyb). Make sure you extract it and place the extracted folder in the same directory with the `data_parser.py` script. Then, you can run:

```
python data_parser.py --path 9-21-2024
```

If you'd like to run the paper analysis on this data, you can generate the required csv files by running:
``` python generate_csv_files.py ```

This will create two CSV files that can be plugged in to the table notebooks in `website-configurations/data-analysis/`.
 
## Database Schema

There are two key data tables that back the analysis:

### website_visits
This table logs one row for every website visit (note that a website is visited more than once), including the visit results. The following columns are used for analysis:

- `meta_static_collection_status`: indicates if a Meta Pixel was installed on the website (note that this value can True or False for historical reasons, but both values indicate an installation).
- `meta_dynamic_collection_status`: indicates if Meta FDC was detected on a website.
- `google_static_collection_status`: indicates if a Google Tag was installed on the website (note that this value can True or False for historical reasons, but both values indicate an installation).
- `google_dynamic_collection_status`: indicates if Google FDC was detected on a website.

For more in-depth information, the `meta_static_ids`, `meta_dynamic_ids`, `google_static_ids`, and `google_dynamic_ids` contain the ID numbers of the trackers identified as installed and collecting FDC for Meta and Google, respectively.

### meta_static_keys
This table logs one row for each Meta installation file configured for data collection. Since we visit a website multiple times, the same installation file may be logged more than once. The `key_list` column contains the specific PII values (as detailed in Table 6 of the paper) in the Meta configuration.



