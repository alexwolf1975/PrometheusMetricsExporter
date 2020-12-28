import yaml

config = {
    'prometheus': {
        'host': 'localhost',
        'port': '9090',
        'prefix': 'prometheus.'
    },
    'graphite': {
        'host': 'localhost',
        'port': '2003',
        'prefix': 'graphite.'
    },
    'time': {
        'disconnect': '10',
        'repeat': '1m'
    }
}


def conf_update(old, new):
    for k in new:
        if isinstance(old[k], dict):
            conf_update(old[k], new[k])
        else:
            old[k] = new[k]


def conf_export(dictionary, prefix=[]):
    for k in dictionary:
        if isinstance(dictionary[k], dict):
            conf_export(dictionary[k], prefix + [k])
        else:
            print('_'.join(prefix + [k]) + '="{}"'.format(dictionary[k]))


with open('config/config.yml') as f:
    conf_update(config, yaml.load(f, Loader=yaml.FullLoader))

conf_export(config)
