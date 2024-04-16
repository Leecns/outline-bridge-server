# Outline Bridge Server

This repository includes Docker Compose files for running the Xray (V2Ray fork) proxy as a bridge (relay) server for the Outline proxy.
Its purpose is to enable the Outline proxy to work effectively in severely restricted networks where direct, secure, or reliable access may not be available.

## Documentation

### Outline

[Outline](https://getoutline.org), developed by Google, is a user-friendly proxy based on Shadowsocks.
It simplifies the process of creating and managing Shadowsocks servers.
Additionally, Outline offers well-designed client applications that are compatible with various platforms.

It normally works as below.

```
[Outline client] <-> [Outline server] <-> (Internet)
```

Read the [Outline official documentation](https://getoutline.org/get-started) to set up an Outline server.

### Xray as Bridge Server

The bridge (relay) server acts as an intermediary between clients and Outline servers.
It facilitates the connection between the two in cases where a direct, secure, or stable connection is not feasible.
The [Xray](https://github.com/XTLS/Xray-core) proxy is used to transmit incoming Shadowsocks traffic (both TCP and UDP) from clients to the Outline servers.

The bridge server changes the flow as below.

```
[Outline client] <-> [Xray server] <-> [Outline server] <-> (Internet)
```

### Setup

Follow these steps to set up the Xray and Outline:

1. Install Docker and Docker-compose on the bridge server.
1. Clone this repository into the bridge server.
1. Run `./configure.py` script. It prompts the following items:
    1. `Number of Outline servers`: Please provide the number of servers with Outline installed, typically just `1`
    1. `Outline server i Host`: Find it in Outline Manager > `{server i}` > Settings > Hostname
    1. `Outline server i Port`: Find it in Outline Manager > `{server i}` > Settings > Port
    1. Allow the port for incoming/outgoing traffic if you have a firewall.
1. Run `docker-compose up -d`.
1. Change Outline Manager > `{server i}` > Settings > Hostname field to the bridge server IP address.
1. Delete old access keys in the Outline Manager and generate new ones.
1. Download [Outline client applications](https://getoutline.org/get-started/#step-3) and add the new access keys there.
1. Enjoy the freedom!

## More

* [V2Ray Docker Compose](https://github.com/miladrahimi/v2ray-docker-compose)
