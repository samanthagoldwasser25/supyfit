import sys 
from SF_functions import *
from Header_Binnings import *
from params import *
import numpy as np 
import json 
import warnings
warnings.filterwarnings('ignore')

with open("parameters.json", "r") as read_file:
    data = json.load(read_file)


original = data['object_to_fit']
spectrum = np.loadtxt(original)
idx=original.rfind('/')
filename=original[idx+1:]

try:
    binned_name= obj_name_int(original, lam, resolution)[3]
    print('Running optimization for spectrum file: {0} with resolution = {1} Ang'.format(binned_name,resolution))
    save_bin = save_bin_path + binned_name

    kill_header_and_bin(original,resolution, save_bin = save_bin)
    all_parameter_space(redshift,extconstant,templates_sn_trunc,templates_gal_trunc, 
    lam, resolution, n=n, plot=plotting, kind=kind, original=save_bin, save=save_results_path, show=show, minimum_overlap=minimum_overlap)
    
    binned_res=np.loadtxt(save_bin)
    result = np.array([data,binned_res])
    ascii.write(result, save_bin, format='csv', fast_writer=False, overwrite=True)     

except:
    resolution=30
    print('Failed. Retrying with resolution = {0} Ang'.format(resolution))
    try:
        save_bin = save_bin_path + binned_name
    except: 
        import ipdb; ipdb.set_trace()
    kill_header_and_bin(original,resolution, save_bin = save_bin)
    all_parameter_space(redshift,extconstant,templates_sn_trunc,templates_gal_trunc, 
    lam, resolution, n=n, plot=plotting, kind=kind, original=save_bin, save=save_results_path, show=show, minimum_overlap=minimum_overlap)
 
    binned_res=np.loadtxt(save_bin)
    result = np.array([data,binned_res])
    ascii.write(result, save_bin, format='csv', fast_writer=False, overwrite=True)     

