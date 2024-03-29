# Licensed under a 3-clause BSD style license - see LICENSE.rst

from ....utils.tap.model.taptable import TapTableMeta
from ....utils.tap.model.job import Job


class DummyHSATapHandler:

    def __init__(self, method, parameters):
        self.__invokedMethod = method
        self._parameters = parameters

    def reset(self):
        self._parameters = {}
        self.__invokedMethod = None

    def check_call(self, method_name, parameters):
        self.check_method(method_name)
        self.check_parameters(parameters, method_name)

    def check_method(self, method):
        if method != self.__invokedMethod:
            raise Exception(f"Method '{method}' "
                            f"not invoked. (Invoked method is "
                            f"'{self.__invokedMethod}')")

    def check_parameters(self, parameters, method_name):
        if parameters is None:
            return len(self._parameters) == 0
        if len(parameters) != len(self._parameters):
            raise Exception(f"Wrong number of parameters for method '{method_name}'. "
                            f"Found: {len(self._parameters)}. Expected {len(parameters)}")
        for key in parameters:
            if key in self._parameters:
                # check value
                if self._parameters[key] != parameters[key]:
                    raise Exception(f"Wrong '{key}' parameter value for method "
                                    f"'{method_name}'. "
                                    f"Found: '{self._parameters[key]}'. Expected: '{parameters[key]}'")
            else:
                raise Exception("Parameter '{key}' not found for method 'method_name'")
        return False

    def launch_job(self, query, name=None, output_file=None,
                   output_format="votable", verbose=False, dump_to_file=False,
                   upload_resource=None, upload_table_name=None):
        self.__invokedMethod = 'launch_job'
        self._parameters['query'] = query
        self._parameters['name'] = name
        self._parameters['output_file'] = output_file
        self._parameters['output_format'] = output_format
        self._parameters['verbose'] = verbose
        self._parameters['dump_to_file'] = dump_to_file
        self._parameters['upload_resource'] = upload_resource
        self._parameters['upload_table_name'] = upload_table_name
        return Job(False)

    def get_tables(self, only_names=True, verbose=False):
        self.__invokedMethod = 'get_tables'
        self._parameters['only_names'] = only_names
        self._parameters['verbose'] = verbose

    def get_columns(self, table_name=None, only_names=True, verbose=False):
        self.__invokedMethod = 'get_columns'
        self._parameters['table_name'] = table_name
        self._parameters['only_names'] = only_names
        self._parameters['verbose'] = verbose

    def load_tables(self,
                    only_names=True,
                    include_shared_tables=False,
                    verbose=True):
        table = TapTableMeta()
        table.name = "table"
        return [table]
