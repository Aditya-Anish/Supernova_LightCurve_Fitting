import sncosmo
import pandas as pd
import numpy as np
import os
model = sncosmo.Model(source='salt2')
model.set(z=0.05, t0=50000., x0=1e-4, x1=0.8, c=0.1)
obs_times = np.arange(49980, 50040, 3)
bands = ['sdssg', 'sdssr', 'sdssi']
np.random.seed(42)
data = []
print("Simulating telescope observations in g, r, and i bands...")
for t in obs_times:
    for b in bands:
        true_flux = model.bandflux(b, t, zp=25., zpsys='ab')
        flux_error = 0.05 * true_flux + 1e-7  
        observed_flux = np.random.normal(true_flux, flux_error)
        
        data.append({
            'time': t, 'band': b, 'flux': observed_flux, 
            'flux_err': flux_error, 'zp': 25.0, 'zpsys': 'ab'
        })
df = pd.DataFrame(data)
os.makedirs("data", exist_ok=True)
output_path = os.path.join("data", "simulated_supernova.csv")
df.to_csv(output_path, index=False)
print(f"Success! Simulated telescope telemetry saved to {output_path}")