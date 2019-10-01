"""Retrieve the dataset, remove invalid instances, and save to disk."""
import argparse
import configparser
import requests
import csv
import os.path
import pickle
import sys

# TODO: Seperate into functions
def download_dataset(url, path):
    pass

if __name__ == "__main__":
<<<<<<< HEAD
	# Download data
	# TODO: Get csv name from data_url
	data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases' \
				'/00485/google_review_ratings.csv'
	data_path = 'data\\raw\\' \
				'google_review_ratings.csv'

	req = requests.get(data_url)

	data_path = os.path.normpath(os.path.normcase(data_path))
	print(data_path)
	with open(data_path, 'w') as csv_file:
		csv_file.write(req.text)

	# Read data as a list or lists
	data = None
	with open(data_path,'r') as csv_file:
		data = [row for row in csv.reader(csv_file)]
		
	cols = data[0]
	data = data[1:]

	# TODO: Save here before the orig is changed

	# Remove bad rows/extra columns
	cols = cols[:-1]
	data = [inst[:-1] for inst in data if inst[-1] == '']

	# Remove the User IDs
	cols = cols[1:]
	data = [inst[1:] for inst in data]

	# Convert strings to floats
	for i in range(len(data)):
		data[i] = [float(x) for x in data[i]]

	pickle.dump([cols, data], open(data_path[:-3] + 'pkl', 'wb'))
=======
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=str, \
        default='google-review-ratings.conf', help='Config file name. Assumed' \
        ' to be in the project\'s config folder. Default is ' \
        '\"google-review-ratings.conf\"')
    args = parser.parse_args()
    config_file = args.config

	# Locate/open the config file. Unrecoverable if not found.
    # Assuming top level src and config folders.
    proj_path = os.path.normpath(os.path.normcase(os.path.dirname(os.path.abspath(__file__))))
    try:
        proj_path = os.path.join(proj_path[:proj_path.index('src')-1])
    except:
        print('Cannot locate project\'s src folder.', file=sys.stderr)
        sys.exit()

    config = configparser.ConfigParser()
    try:
        config.read(os.path.join(proj_path, 'config', config_file))
    except:
        print('Cannot read config file - {}.'.format(config_file), file=sys.stderr)
        sys.exit()

    # Download data
    data_url = config['dataset-info']['url']
    dataset_name = data_url.split('/')[-1]
    req = requests.get(data_url)
    
    dataset_path = os.path.join(proj_path, 'data', 'raw')
    # # Verify directory exists
    if os.path.exists(os.path.dirname(dataset_path)) == False:
        os.makedirs(dataset_path)
    dataset_path = os.path.join(dataset_path, dataset_name)

    with open(dataset_path, 'w', newline='') as csv_file:
        csv_file.write(req.text)

    # Pickle raw data
    data = None
    with open(dataset_path,'r') as csv_file:
        data = [row for row in csv.reader(csv_file)]
        with open(dataset_path[:-3]+'pkl', 'wb') as raw_pickle:
            pickle.dump(data, raw_pickle)

    cols = config['dataset-info']['categories'].split(',')
    if cols == None:	
        cols = data[0]
    data = data[1:]

    # Remove bad rows with an extra column
    data = [inst[:-1] for inst in data if inst[-1] == '']

    # Remove the User IDs
    cols = cols[1:]
    data = [inst[1:] for inst in data]

    # Convert strings to floats
    for i in range(len(data)):
        data[i] = [float(x) for x in data[i]]

    with open(os.path.join(proj_path, 'data', 'ratings.pkl'), 'wb') as datafile:
        pickle.dump([data, cols], datafile)
>>>>>>> 47d91859cd5efb4340e7304cdd89ac528c727599
