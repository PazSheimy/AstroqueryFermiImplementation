# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
Asynchronous downloading of Fermi LAT data files.
"""

import requests
import time
from astroquery.exceptions import QueryError
from . import conf

__all__ = ['async_download_fermi_data']

def async_download_fermi_data(result_url, output_dir, timeout=conf.retrieval_timeout, check_interval=60):
    """
    Asynchronously download Fermi data files from the FTP site once they are ready.

    Parameters
    ----------
    result_url : str
        The URL provided by the query_object_async method indicating where the query results will be available.
    output_dir : str
        The directory where the downloaded FITS files should be saved.
    timeout : int, optional
        The maximum time (in seconds) to wait for the data files to become available before timing out.
    check_interval : int, optional
        How often (in seconds) to check if the data files are available.

    Returns
    -------
    None
    """
    start_time = time.time()
    while True:
        try:
            response = requests.get(result_url, timeout=timeout)
            response.raise_for_status()  # Raise an error for bad responses

            if "data is ready" in response.text:  # This condition needs to be tailored to the actual completion message
                # Logic to extract download URLs from the response and download the files
                download_files(response.text, output_dir)
                break

            if time.time() - start_time > timeout:
                raise QueryError("Timed out waiting for Fermi data files to become available.")

            time.sleep(check_interval)
        except requests.RequestException as e:
            raise QueryError(f"Failed to check data file availability: {e}")

import os
from urllib.parse import urljoin

def download_files(page_content, output_dir):
    """
    Download FITS files based on URLs found in the page_content.
    """
    # Example regex pattern to find all FITS file URLs; adjust as needed
    fits_urls = re.findall(r'(https://[\S]+\.fits)', page_content)
    
    for url in fits_urls:
        filename = url.split('/')[-1]
        filepath = os.path.join(output_dir, filename)
        
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"Downloaded {filename} to {output_dir}")

