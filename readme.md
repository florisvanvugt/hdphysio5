

# HDPhysio5 - Python Implementation of HDF5 format for physiological data

## Requirements

`pip install h5py`

## Usage

```{python}

import read_h5py
d = read_h5py.read('example.hdf5')
print(d.summary())

```




# Specification for HDF5 physiology format


The root of the HDF5 file should contain an attribute `participants` which is a list of participant IDs.

Store datasets as follows:

`/<participant>/<dataset>`

Required attributes for each dataset:
* `SR` sampling rate in Hz.
* `modality` the measurement modality (e.g. `ecg`, `ppg`, etc.) in lower case.
* `units` is the measurement units (e.g. `mV`, `microsiemens` or whatever), in lower case.
* `participant` the participant (redundant but hey)




## Event markers

Event markers such as triggers can be added in the attributes of the root dataset.

There should be an attribute `markers` which contains a list of all markers (as strings).

Then for each marker, there should be an attribute, again the root dataset, which contains a list of time codes (in s) at which the event happened.




## Converting

The purpose is to use a clean and straight-forward HDF5-compliant format
to store physiology data.

* `convert_acq_to_h5py.py` converts Biopac Acknowledge data into HDF5. Note that you need to edit the script for the column assignments to make sense.
* `convert_B3_to_h5py.py` converts Brams Bio Box data into HDF5. Again, review the conversion file whether the assumptions apply.





## Future

* TODO Add a header as well, so that we can list participants as well as have other data
* TODO Add a time vector? How?



