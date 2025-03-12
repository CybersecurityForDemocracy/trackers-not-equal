import psycopg2
from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import numpy as np

load_dotenv()

def fetch_data(query):
    conn = psycopg2.connect(
        host=os.environ.get("db_host"),
        user=os.environ.get("db_username"),
        password=os.environ.get("db_password"),
        dbname=os.environ.get("db_name"),
        connect_timeout=300
    )

    df = pd.read_sql(query, conn)

    conn.close()

    return df

def clean_url(df):
    df['original_website'] = df['website'].str.replace(r'-(1|2|1-2)$', '', regex=True)
    df['url'] = df['original_website'].str.replace(r'^(https?://)?(www\.)?', '', regex=True)

    return df

def generate_meta_key_analysis():
    # default keys for Meta
    DEFAULT_KEYS = ['em','fn','ln','ph','ge','zp','ct','st','country','db', 'external_id']	
    
    df = fetch_data("SELECT * from meta_static_keys")
    df = clean_url(df)
    
    # process keys and identify if this is the default list
    df['key_list'] = df['key_list'].apply(lambda x: x.split(','))
    df['using_default_keys'] = df['key_list'].apply(lambda x: True if sorted(x) == sorted(DEFAULT_KEYS) else False)

    def select_row_with_max_list_length(group):
        # Find the index of the row with the longest list in metrics1
        idx_max_length = group['key_list'].apply(len).idxmax()

        # Return the row with the maximum list length
        return group.loc[idx_max_length]
    
    # aggregate across website visits and choose the static configuration with the most keys
    aggregated_df = df.groupby(['url', 'pixel_id'], group_keys=False).apply(select_row_with_max_list_length).reset_index(drop=True)
    aggregated_df = aggregated_df.groupby('url').agg(list).reset_index()

    # filter to only websites with one pixel (due to reported errors with multiple pixels)
    aggregated_df['pixel_count'] = aggregated_df['pixel_id'].apply(len)
    aggregated_df = aggregated_df[aggregated_df['pixel_count'] == 1]
    aggregated_df['is_default_key_list'] = aggregated_df['using_default_keys'].apply(lambda x: x[0])

    # normalize, flatten, and rename columns
    aggregated_df['key_list'] = aggregated_df['key_list'].apply(lambda x: np.array(x).flatten().tolist())
    aggregated_df = aggregated_df[['url', 'is_default_key_list', 'key_list']]

    aggregated_df.to_csv('meta_static_analysis_keys.csv', index=False)
    print("Data successfully saved to 'meta_static_analysis_keys.csv'")

def generate_websites_csv():
    df = fetch_data("SELECT * FROM website_visits")
    df = clean_url(df)

    df['meta_form_data_configuration'] = df['meta_static_collection_status'].fillna(False)
    df['form_data_collection'] = df['meta_dynamic_collection_status'] | df['google_dynamic_collection_status']

    def custom_aggregate(group):
        aggregated_row = {
            'google_static_collection_status': group['google_static_collection_status'].any(),
            'meta_static_collection_status': group['meta_static_collection_status'].any(),
            'google_dynamic_collection_status': group['google_dynamic_collection_status'].any(),
            'meta_dynamic_collection_status': group['meta_dynamic_collection_status'].any()
        }
        return pd.Series(aggregated_row)

    # aggregate data across retries
    # in the case that ANY visit was true, the website is marked as true
    df_aggregated = df.groupby('url').apply(custom_aggregate).reset_index()

    # rename columns to be more readable
    df_aggregated.rename(columns={
        'google_static_collection_status': 'has_gtag',
        'google_dynamic_collection_status': 'google_form_data_collection',
        'meta_static_collection_status': 'has_meta_pixel',
        'meta_dynamic_collection_status': 'meta_form_data_collection'
    }, inplace=True)

    df_aggregated.to_csv('websites.csv', index=False)
    print("Data successfully saved to 'websites.csv'")

if __name__ == "__main__":
    generate_websites_csv()
    generate_meta_key_analysis()