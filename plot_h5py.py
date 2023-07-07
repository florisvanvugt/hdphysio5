
import sys
import pandas as pd
import os
import numpy as np
import h5py
import json
import datetime
from tkinter import filedialog


if len(sys.argv)<2:
    print("You need to supply the filename to convert.")

    file_path_string = filedialog.askopenfilename(
        initialdir=".",
        title="Select schedule file",
        filetypes=(("HDF5physio","*.hdf5"),("all files","*.*")),
    )

    if not file_path_string:
        sys.exit(-1)
    fname = file_path_string
        
else:
    fname = sys.argv[1]


if not os.path.exists(fname):
    print("File {} does not seem to exist.".format(fname))
    sys.exit(-1)


import read_h5py
d = read_h5py.read(fname)
print(d.summary())



import matplotlib.pyplot as plt

chans = d.get_channels()

def get_colors(N):
    import colorsys
    HSV_tuples = [(x*1.0/N, 0.5, 0.5) for x in range(N)]
    RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)
    return list(RGB_tuples)

COLORS = get_colors(len(chans))


f,axs =plt.subplots(len(chans),1,sharex=True,figsize=(12,7))

for i,chan in enumerate(chans):
    ax = axs[i]
    vals = d.get(chan)
    t = np.arange(vals.shape[0])/d.SR
    col = COLORS[i]
    ax.plot(t,vals,color=col)
    ax.set_title(chan)

    
for m in d.get_markers():
    evs = d.get_marker(m)
    for t in evs:
        ax.axvline(x=t)
    
    
plt.tight_layout()
plt.show()
