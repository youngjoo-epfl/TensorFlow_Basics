"""Base utilities for importing datasets."""


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import collections
import os
from os import path
import tempfile
from six.moves import urllib

import numpy as np
from tensorflow.python.platform.default import _gfile as gfile

Dataset = collections.namedtuple('Dataset', ['data', 'target'])

#Load CSV file
# - Automatically transform Date info to numerical value
# - Automatically transform string class info to specific class value

def load_csv(filename, target_dtype):
    with gfile.Open(filename) as csv_file:
        print("hello youngjoo")
        data_file = csv.reader(csv_file)
        header = next(data_file)
        n_samples = int(header[0])
        n_features = int(header[1])
        target_names = np.array(header[2:])
        data = np.empty((n_samples, n_features))
        target = np.empty((n_samples,), dtype=np.int)

        for i, ir in enumerate(data_file):
            data[i] = np.asarray(ir[:-1], dtype=np.float64)
            target[i] = np.asarray(ir[-1], dtype=target_dtype)

    return Dataset(data=data, target=target)


