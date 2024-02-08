
from astroquery.query import BaseQuery
from astroquery.utils import commons
from astroquery import utils
import requests
from astropy.table import Table

class MyAstroServiceQuery(BaseQuery):
    # Define the base URL of your service
    BASE_URL = 'https://example.com/myastroservice/query'

    # A method to perform a query
    def query(self, query_parameters):
        """
        Query the MyAstroService service with specified parameters.
        
        Parameters
        ----------
        query_parameters : dict
            A dictionary of query parameters.
            
        Returns
        -------
        table : `astropy.table.Table`
            An Astropy table containing the query results.
        """
        response = self._request('GET', self.BASE_URL, params=query_parameters)
        return self._parse_result(response)

    def _parse_result(self, response):
        """
        Parse the response from the service and return an Astropy table.
        
        Parameters
        ----------
        response : `requests.Response`
            The response object from requests.
            
        Returns
        -------
        table : `astropy.table.Table`
            An Astropy table constructed from the parsed data.
        """
        # Example parsing logic. Adjust according to your response format.
        table = Table.read(response.text, format='csv')  # Example: CSV format
        return table

# Define a function to make querying easier
def query_myastroservice(*args, **kwargs):
    return MyAstroServiceQuery().query(*args, **kwargs)
