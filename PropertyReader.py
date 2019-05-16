import configparser
import io
import os

class PropertyReader(object):
    def __init__(self, property_file_path):
        self.property_file_path = property_file_path

    def read_properties_file(self):
        with open(self.property_file_path) as f:
            config = io.StringIO()
            config.write('[dummy_section]\n')
            config.write(f.read().replace('%', '%%'))
            config.seek(0, os.SEEK_SET)

            cp = configparser.SafeConfigParser()
            cp.readfp(config)

            return dict(cp.items('dummy_section'))