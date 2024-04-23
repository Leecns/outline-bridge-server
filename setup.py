#!/usr/bin/python3

import os
import json


def add_inbound(i):
    host = input(f"Outline server {i} host: ")
    port = int(input(f"Outline server {i} port: "))
    return {
        'port': port,
        'protocol': 'dokodemo-door',
        'listen': '0.0.0.0',
        'settings': {
            'address': host,
            'port': port,
            'network': 'tcp,udp'
        }
    }


def main():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(current_directory, 'configs', 'config.json')

    config = {
        "log": {
            "loglevel": "warning"
        },
        "outbounds": [
            {
                "protocol": "freedom",
                "tag": "freedom"
            }
        ],
        "inbounds": []
    }

    num_inbounds = int(input("Number of Outline servers: ") or 1)
    if num_inbounds < 1 or num_inbounds > 5:
        print('Number of Outline servers must be between 1 and 5')
        return

    inbounds = []
    for i in range(num_inbounds):
        inbounds.append(add_inbound(i + 1))

    config['inbounds'] = inbounds

    with open(filename, 'w') as file:
        json.dump(config, file, indent=2)
    print("The config updated. Run 'docker compose up -d' or 'docker compose restart'.")


if __name__ == "__main__":
    main()
