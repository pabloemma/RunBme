# class controlling the configuration

import json

class SetupBME:
    def __init__(self, config_file = None):

        if config_file is None:
            self.config_file = '/Users/klein/git/RunBme/config/BME280.json'
        else:
            self.config_file = config_file        

     
    def get_config(self):
        # this read the configuration file
        with open(self.config_file, 'r') as f:
            config = json.load(f)

        self.server_ip = config['Server']['host']
        self.server_port = config['Server']['port']


        self.DEBUG = config['Control']['DEBUG']
        self.column_names = config['Control']['column_names']
        self.output_dir = config['Control']['output_dir']
        self.frequency = config['Control']['frequency']
        self.altitude = config['Control']['altitude']
        

        if(self.DEBUG == "True"):
            print(self.server_ip, self.server_port)
        return 
    
if __name__ == "__main__":
    config = SetupBME()
    config.get_config()