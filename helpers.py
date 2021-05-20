"""
Script with some general methods and constant values
"""
import json
import pandas as pd

SIGNAL_FREQUENCY = {
    'BVP': 64,
    'GSR': 4,
    'TEMP': 4,
    'ACC': 32,
    'ACC_X': 32,
    'ACC_Y': 32,
    'ACC_Z': 32,
}


def get_muse_sampling():
    return 256


DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S:%f'

MUSE_DTYPES = {
    'TimeStamp': 'datetime64[ms]', 'Delta_TP9': float, 'Delta_AF7': float,
    'Delta_AF8': float, 'Delta_TP10': float, 'Theta_TP9': float,
    'Theta_AF7': float, 'Theta_AF8': float, 'Theta_TP10': float,
    'Alpha_TP9': float, 'Alpha_AF7': float, 'Alpha_AF8': float, 'Alpha_TP10': float,
    'Beta_TP9': float, 'Beta_AF7': float, 'Beta_AF8': float, 'Beta_TP10': float,
    'Gamma_TP9': float, 'Gamma_AF7': float, 'Gamma_AF8': float, 'Gamma_TP10': float,
    'RAW_TP9': float, 'RAW_AF7': float, 'RAW_AF8': float, 'RAW_TP10': float,
    'AUX_RIGHT': float, 'Accelerometer_X': float, 'Accelerometer_Y': float,
    'Accelerometer_Z': float, 'Gyro_X': float, 'Gyro_Y': float, 'Gyro_Z': float,
    'HeadBandOn': float, 'HSI_TP9': float, 'HSI_AF7': float, 'HSI_AF8': float,
    'HSI_TP10': float, 'Battery': float, 'Elements': 'string',
}

PARTICIPANTS_ID = list(range(22, 65))

DEVICES = ('EMPATICA', 'SAMSUNG_WATCH', 'MUSE')

MOVIE_TYPES = ('NEUTRAL', 'DISGUST', 'ANGER', 'AMUSEMENT', 'SURPRISE', 'AWE',
               'ENTHUSIASM', 'LIKING', 'BASELINE', 'SADNESS', 'FEAR')
STIMULATION_TIMES = {
    'AMUSEMENT': pd.Timedelta('00:02:00'),
    'ANGER': pd.Timedelta('00:02:00'),
    'AWE': pd.Timedelta('00:01:56'),
    # 'BASELINE': pd.Timedelta('00:05:00'),
    'DISGUST': pd.Timedelta('00:01:08'),
    'ENTHUSIASM': pd.Timedelta('00:01:59'),
    'FEAR': pd.Timedelta('00:02:00'),
    'LIKING': pd.Timedelta('00:01:51'),
    'NEUTRAL': pd.Timedelta('00:02:01'),
    'SADNESS': pd.Timedelta('00:01:59'),
    'SURPRISE': pd.Timedelta('00:00:49'),
    'WASHOUT': pd.Timedelta('00:02:00')
}

EMOTIONS_CATEGORICAL = ('DISGUST', 'ANGER', 'AMUSEMENT', 'SURPRISE', 'AWE',
                        'ENTHUSIASM', 'LIKING', 'SADNESS', 'FEAR')
EMOTIONS_SAM = ('VALENCE', 'AROUSAL', 'MOTIVATION')

STUDY_PHASES = ('WASHOUT', 'STIMULUS', 'QUESTIONNAIRES')
BASELINE_PHASES = ('STIMULUS', 'QUESTIONNAIRES')


# read json file with signal or questionnaire data
def load_json_file(path):
    if path[-5:] != '.json':
        path += '.json'

    with open(path) as json_file:
        json_data = json.load(json_file)

    return json_data
