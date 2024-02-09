# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
Access to Fermi Gamma-ray Space Telescope data.

https://fermi.gsfc.nasa.gov
https://fermi.gsfc.nasa.gov/ssc/data/
"""
from astropy import config as _config

# Import statements
from .async_download import async_download_fermi_data
from .core import FermiLAT, FermiLATClass, GetFermilatDatafile, get_fermilat_datafile

# Define __all__ for what's available to import from this module
__all__ = ['FermiLAT', 'FermiLATClass',
           'GetFermilatDatafile', 'get_fermilat_datafile',
           'Conf', 'conf', 'async_download_fermi_data']  # Included async_download_fermi_data here

class Conf(_config.ConfigNamespace):
    """
    Configuration parameters for `astroquery.fermi`.
    """
    url = _config.ConfigItem(
        'https://fermi.gsfc.nasa.gov/cgi-bin/ssc/LAT/LATDataQuery.cgi',
        'Fermi query URL.')
    timeout = _config.ConfigItem(
        60,
        'Time limit for connecting to Fermi server.')
    retrieval_timeout = _config.ConfigItem(
        120,
        'Time limit for retrieving a data file once it has been located.')

conf = Conf()

import warnings
warnings.warn("Experimental: Fermi-LAT has not yet been refactored to have "
              "its API match the rest of astroquery.")
