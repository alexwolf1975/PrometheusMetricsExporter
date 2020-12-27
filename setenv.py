import yaml

config = {
    'prometheus': {
        'host': 'localhost',
        'port': '9090'
        },
    'graphite': {
        'host': 'localhost',
        'port': '2003'
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

with open('config/config.yml') as f:
    conf_update(config, yaml.load(f, Loader=yaml.FullLoader))

print('prometheus_host="{}"'.format(config['prometheus']['host']))
print('prometheus_port="{}"'.format(config['prometheus']['port']))
print('graphite_host="{}"'.format(config['graphite']['host']))
print('graphite_port="{}"'.format(config['graphite']['port']))
print('time_disconnect="{}"'.format(config['time']['disconnect']))
print('time_repeat="{}"'.format(config['time']['repeat']))
