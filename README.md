# Hot Gas in Low Redshift, Massive OVI/Ly-α Absorption Line Systems

This repository contains sample files, outputs, and analysis notebooks for a set of galaxy groups selected using UV absorption of Lyman Alpha, with follow-up observations by XMM-Newton.

## Contents of the repository

### Notebooks
1. **sample_preparation.ipynb** - A very simple notebook that simply changes the original Excel file into a csv, and plots the group's positions on the sky.
2. **get_xray_data.ipynb** - Here we determine how much XMM data is available for these objects, download it, and process it into a scientifically usable state.
3. **visualise_groups.ipynb** - Simple visualisations of the groups are created.
4. **running_LTR_pipeline.ipynb** - We run a luminosity-temperature-radius pipeline to measure temperatures and luminosities within $R_{500}$ and $R_{2500}$, as well as the $R_{500}$ and $R_{2500}$ values themselves.