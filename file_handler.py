import yaml
import re

#TODO: Implement checks for the input files for correct format

class FileHandler:
    def __init__(self):
        """
        Handler class for reading input files and writing output files
        """

        self.loader = yaml.SafeLoader
        self.loader.add_implicit_resolver(
            u'tag:yaml.org,2002:float',
            re.compile(u'''^(?:
             [-+]?(?:[0-9][0-9_]*)\\.[0-9_]*(?:[eE][-+]?[0-9]+)?
            |[-+]?(?:[0-9][0-9_]*)(?:[eE][-+]?[0-9]+)
            |\\.[0-9_]+(?:[eE][-+][0-9]+)?
            |[-+]?[0-9][0-9_]*(?::[0-5]?[0-9])+\\.[0-9_]*
            |[-+]?\\.(?:inf|Inf|INF)
            |\\.(?:nan|NaN|NAN))$''', re.X),
            list(u'-+0123456789.'))


    def read_input(self, path="input/"):
        
        with open(path + "signal_parameters.yaml", "r") as file:
            config_dict = yaml.load(file, Loader=self.loader)

        with open(path + "targets.yaml", "r") as file:
            target_dict = yaml.load(file, Loader=self.loader)


        return config_dict, target_dict