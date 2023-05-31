# This script exists because the proprietary observations I make use of in this repository are not on my  
#  account, so I cannot use DAXA's proprietary observation downloading on them. This is probably a stop-
#  gap measure, as I'll add a 'manual import' function to the XMM mission to account for this possibility

from shutil import copytree
import os

stor_path = "/mnt/ufs18/home-218/turne540/data/prop_OVI_XMM_data/{o}/odf/"

prop_obs_ids = ['0900700101', '0900700201']

if not os.path.exists('data/xmm_pointed_raw'):
    os.makedirs('data/xmm_pointed_raw')

for obs_id in prop_obs_ids:
    rel_path = stor_path.format(o=obs_id)
    copytree(rel_path, 'data/xmm_pointed_raw/{o}'.format(o=obs_id))