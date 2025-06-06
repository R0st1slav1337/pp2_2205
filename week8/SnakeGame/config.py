from configparser import ConfigParser

def load_config(filename='week8/SnakeGame/database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    # Get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file.')

    return config

if __name__ == '__main__':
    config = load_config()
    print(config)