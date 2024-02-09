from astroquery.fermi.core import FermiLAT

# Make sure to adjust the parameters according to your needs
output_dir = "/path/to/your/download/directory"
FermiLAT.query_object_async("M87", download=True, output_dir=output_dir)
