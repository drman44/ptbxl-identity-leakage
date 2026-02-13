import numpy as np
import wfdb

def spectral_signature(path, n_bins=200):
    sig, fields = wfdb.rdsamp(path)

    lead_names = getattr(fields, "sig_name", [])
    idx = lead_names.index("II") if ("II" in lead_names) else 0

    lead = sig[:, idx].astype(float)
    lead = lead - np.mean(lead)

    fft = np.abs(np.fft.rfft(lead))

    if len(fft) < n_bins:
        vec = np.zeros(n_bins)
        vec[:len(fft)] = fft
    else:
        vec = fft[:n_bins]

    s = vec.sum()
    if s > 0:
        vec = vec / s

    return vec
