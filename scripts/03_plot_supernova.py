import pandas as pd
import sncosmo
import matplotlib.pyplot as plt
import os
from astropy.table import Table
data_path = os.path.join("data", "simulated_supernova.csv")
data = Table.from_pandas(pd.read_csv(data_path))
model = sncosmo.Model(source='salt2')
model.set(z=0.05, t0=50000.0, x0=1e-4, x1=0.8, c=0.1) 
print("Generating multi-band light curve plots...")
fig = sncosmo.plot_lc(data, model=model)
os.makedirs("output", exist_ok=True)
output_path = os.path.join("output", "supernova_lightcurve.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Success! Light curve plot saved to {output_path}")