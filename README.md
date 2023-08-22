# Warm-Hot Gas in Low Redshift, Massive OVI/Ly-α Absorption Line Systems

This repository contains sample files, outputs, and analysis notebooks for a set of galaxy groups selected using UV absorption of Lyman Alpha, with follow-up observations by XMM-Newton.

## Contents of the repository

### Sample files
The input sample file lives here, along with the region files necessary for analysing our XMM observations.

### Notebooks
This should be everything necessary to recreate this analysis:

1. **sample_preparation.ipynb** - A very simple notebook that simply changes the original Excel file into a csv, and plots the group's positions on the sky.
2. **get_xray_data.ipynb** - Here we determine how much XMM data is available for these objects, download it, and process it into a scientifically usable state.
3. **visualisation/visualise_groups.ipynb** - X-ray and X-ray/optical visualisations of the groups are created.
4. **visualisation/visualise_other_relevant_structures.ipynb** - Other sources that we have identified as possibly being relevant have similar visualisations created.
5. **lum_temp_rad_pipeline/running_LTR_pipeline.ipynb** - We run a luminosity-temperature-radius pipeline to measure temperatures and luminosities within $R_{500}$ and $R_{2500}$, as well as the $R_{500}$ and $R_{2500}$ values themselves.
6. **lum_temp_rad_pipeline/other_structures_running_LTR_pipeline.ipynb** - Essentially the same as above, but for the other identified structures.


### Outputs
Contains anything generated and saved as part of this analysis, , e.g.:
* Source positions and redshifts
* Detection regions
* Figures
* Temperature and luminosities measured within overdensity radii

Output X-ray data products are not included because of storage limitations on GitHub.