import configparser

def getValue(section, name, vtype):
    config = configparser.ConfigParser()
    config.read('config.ini')
    if vtype == 'int':
        return int(config[section][name])
    elif vtype == 'bool':
        if config[section][name] == '1':
            return True
        return False
    elif vtype == 'float':
        return float(config[section][name])
    else:
        return config[section][name]