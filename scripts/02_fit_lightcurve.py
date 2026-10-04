import pandas as pd
import sncosmo
import os
from astropy.table import Table
data_path = os.path.join("data", "simulated_supernova.csv")
df = pd.read_csv(data_path)
data = Table.from_pandas(df)
model = sncosmo.Model(source='salt2')
model.set(z=0.05)
print("Running Minuit optimization to fit the SALT2 template...")
result, fitted_model = sncosmo.fit_lc(
    data, model, 
    vparam_names=['t0', 'x0', 'x1', 'c'], 
    bounds={'t0': (49950, 50050)}
)
print("\n--- MCMC FIT RESULTS ---")
print(f"Optimization Successful: {result.success}")
print(f"Recovered t0 (Peak Time): {result.parameters[1]:.2f} days  (True: 50000.00)")
print(f"Recovered x0 (Amplitude): {result.parameters[2]:.2e}       (True: 1.00e-04)")
print(f"Recovered x1 (Stretch):   {result.parameters[3]:.4f}         (True: 0.8000)")
print(f"Recovered c (Color):      {result.parameters[4]:.4f}         (True: 0.1000)")