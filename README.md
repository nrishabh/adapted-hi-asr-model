# Creating a Hindi Speech Recognition Model using Kaldi
<!-- TODO: Description of project -->

## Kaldi Toolkit
Before running anything, make sure you download and install [kaldi-toolkit](https://kaldi-asr.org/doc/install.html).

## Hindi Datasets
The following datasets have been found for Hindi language.

**[Common Voice](https://commonvoice.mozilla.org/en/datasets)**

**[OpenSLR: Multilingual and code-switching ASR Challenge Dataset (Sub-task 1)](http://www.openslr.org/103/)**

**[OpenSLR: Multilingual and code-switching ASR Challenge Dataset (Sub-task 2)](http://www.openslr.org/104/)**

**[Speech Lab, IITM - Hindi Corpus](https://sites.google.com/view/asr-challenge/home)**

## Structuring Dataset into IITM-ASR-Toolkit Folder
Replicate the following directory structure to develop the model.

    iitm-asr-toolkit
    ├── ...
    ├── audio
    |    ├── train: Contains all WAV files for training data
    |    ├── dev: Contains all WAV files for development data
    |    └── test: Contains all WAV files for testing data
    ├── data
    |    ├── train: Contains all transcription files for training data
    |    ├── dev: Contains all transcription files for development data
    |    ├── test: Contains all transcription files for testing data
    |    └── local
    |       └── dictionary: Contains all phonetic dictionary files for the model
    └── ...
