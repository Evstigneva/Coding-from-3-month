import h5py

with h5py.File('model4.0.h5', 'r') as f:
    model = f['code'][:]

