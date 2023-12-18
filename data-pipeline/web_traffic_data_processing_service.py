import os
import pandas as pd
import logging
from datetime import datetime
from urllib.error import HTTPError

logging.basicConfig(filename='pipeline.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

DOWNLOAD_LOCATION_PATH = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'

class WebTrafficDataProcessor:
    def __init__(self, public_url):
        self.public_url = public_url

    
    def download_file_from_public_url(self, file_name):

        file_url = f"{self.public_url}{file_name}"
        col_names = ['length','path','user_id']
        try:
            logging.info(f"Starting the download for {file_name}")
            # Read the CSV data into a DataFrame
            df = pd.read_csv(file_url, usecols=col_names)

        except HTTPError as e:
            logging.error(f"Failed to download the file {file_name} from the public URL")
            raise
        except Exception as e:
            logging.error(f"Failed to download the file {file_name} from the public URL")
            raise
        
        return df  

    
    def transform_web_data(self, data):

        #Transforming the data, filling the null values with zero
        logging.info("Transforming the data")
        pivot_df = data.pivot_table(index='user_id', columns='path', values='length', fill_value=0)
        pivot_df.reset_index(inplace=True)
        return pivot_df
    

    def run_pipeline(self):

        #creating an empty dataframe where all the data will be combined before transformation
        combined_data = pd.DataFrame()
        for file_name in 'abcdefghijklmnopqrstuvwxyz':
            current_data = self.download_file_from_public_url(f"{file_name}.csv")

            if current_data is not None and not current_data.empty :
                combined_data = pd.concat([combined_data, current_data])

        
        if not combined_data.empty:
            # Transform data
            transformed_data = self.transform_web_data(combined_data)

            # create downloads directory 
            if not os.path.exists(DOWNLOAD_LOCATION_PATH):
                os.makedirs(DOWNLOAD_LOCATION_PATH, exist_ok=True)

            # Path to save the transformed_data csv file
            formatted_datetime = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            output_file = f"{DOWNLOAD_LOCATION_PATH}combined_data_{formatted_datetime}.csv"

            # Save transformed_data output to a csv file
            transformed_data.to_csv(output_file, index=False)
            logging.info(f"Data saved to {output_file}")


public_url = 'https://public.wiwdata.com/engineering-challenge/data/'

if __name__ == "__main__":
    try:
        s3_pipeline = WebTrafficDataProcessor(public_url)
        s3_pipeline.run_pipeline()
    except Exception as e:
            logging.exception(f"Pipeline could not run due to error: {e}")
