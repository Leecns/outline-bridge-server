#!/usr/bin/python3

import os
import json


def add_inbound(i):
    host = input(f"Enter server {i} host: ")
    port = int(input(f"Enter server {i} port: "))
    inbound = {
        'port': port,
        'protocol': 'dokodemo-door',
        'listen': '0.0.0.0',
        'settings': {
            'address': host,
            'port': port,
            'network': 'tcp,udp'
        }
    }
    return inbound


def main():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(current_directory, 'configs', 'config.json')

    config = {
        "log": {
            "loglevel": "warning"
        },
        "inbounds": []
    }

    num_inbounds = int(input("Enter the number of outline servers: ") or 1)
    if num_inbounds < 1 or num_inbounds > 5:
        print('Number of outline servers must be between 1 and 5')
        return

    inbounds = []
    for i in range(num_inbounds):
        inbounds.append(add_inbound(i + 1))

    config['inbounds'] = inbounds

    with open(filename, 'w') as file:
        json.dump(config, file, indent=2)
    print("The config file updated. Run 'docker compose up -d' or 'docker compose restart'.")


if __name__ == "__main__":
    main()
