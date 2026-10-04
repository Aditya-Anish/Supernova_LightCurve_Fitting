# Supernova Light Curve Fitting

This is a Python pipeline I built to simulate and fit Type Ia supernova light curves using the SALT2 model. I put this together as part of my astrophysics research portfolio to practice forward modeling, MCMC optimization, and time-series photometric analysis.

## What's in here?

The project is broken down into three simple scripts that run sequentially:

* **`01_simulate_sn_data.py`**: Generates a synthetic Type Ia supernova observation. It fakes telescope telemetry for the SDSS g, r, and i bands, injecting realistic Gaussian noise to mimic actual atmospheric and sensor interference.
* **`02_fit_lightcurve.py`**: Reads that noisy data and uses the Minuit algorithm (via `iminuit`) to mathematically reverse-engineer the true physical parameters of the event (peak time, amplitude, stretch, and color). 
* **`03_plot_supernova.py`**: Visualizes the results. It plots the noisy data points over the mathematically perfect SALT2 model and calculates the residuals to verify the fit.

## Requirements

You will need Python (I used 3.12) and a few standard astrophysics and data science libraries, use this command in your respective terminal to install them:

'''bash
pip install sncosmo iminuit astropy pandas numpy matplotlib
'''

## How to run it

Just clone the repository to your machine and run the scripts in order from the root directory:
'''bash
python scripts/01_simulate_sn_data.py
python scripts/02_fit_lightcurve.py
python scripts/03_plot_supernova.py
'''

The simulated telemetry will automatically save to the 'data/' folder, and the final light curve graphs will output to 'output/supernova_lightcurve.png'.
