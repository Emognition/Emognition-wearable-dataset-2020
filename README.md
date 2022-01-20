# Repository for the Emognition Wearable Dataset 2020

## Description
This is a supplementary repository for the Emognition Wearable Dataset 2020 and article titled [Emognition dataset: emotion recognition with self-reports, facial expressions, and physiology using wearables](https://doi.org/10.7910/DVN/R9WAF4). <br/>
The repository contains several jupyter notebooks with data manipulations and visualizations.
The code uses only physiological and questionnaire data - none of the code requires video data.

Necessary libraries are in [`requirements.txt`](./requirements.txt).
The [`helpers.py`](./helpers.py) script contains some general methods and constant values of the dataset.

Each notebook contains different analysis of the dataset:
* [`examination_signal.ipynb`](./examination_signal.ipynb) plots data of a selected participant during the study and introduce processing code for Samsung Watch BVP 
* [`muse_quality.ipynb`](./muse_quality.ipynb) provides data on quality of recorded EEG signals (time on head and quality of signal - provided by the device). It allows
* [`questionnaires_analysis.ipynb`](./questionnaires_analysis.ipynb) provides a short analysis of control and emotion questionnaires
* [`skips_delays.ipynb`](./skips_delays.ipynb) contains analysis of skips (shorter duration) and delays (longer duration) of recorded sessions for washout and stimuli clips. All skips and delays were computed using signals recorded with the Empatica E4, as it was connected directly to the device used for elicitation of emotions.  

## Dataset access
The use of the Emognition dataset is limited to the academic research purposes only.
The data will be made available after completing the End User License Agreement (EULA).
The EULA is located in [the dataset repository](https://doi.org/10.7910/DVN/R9WAF4).
It should be signed and emailed to Emognition Group at `emotions<at>pwr.edu.pl`.
The mail has to be sent from an academic email address associated with the Harvard Dataverse platform account.


## Project configuration
* Install [Python](https://www.python.org/downloads/) (at least 3.7 version is recommended),
* Setup your environment (venv, conda, etc.) and install dependencies from [`requirements.txt`](./requirements.txt) (tested on miniconda3 for windows, 05.05.2021)
* Set path to the _unzipped_ dataset in [`config.ini`](./config.ini) file. This path will be used in every notebook.


## Reference
If you use the dataset or re-use this work, please cite:
```
TBA

```
