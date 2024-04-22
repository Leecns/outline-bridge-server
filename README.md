# Outline Bridge Server

This repository contains Docker Compose files designed to deploy V2Ray as a bridge (relay) server for the Outline proxy.
The primary goal is to enhance the functionality of the Outline in highly restricted networks where direct connections to the Outline server is not possible.

## Documentation

### What's Outline?

[Outline](https://getoutline.org) is a set of proxy tools developed by Google based on the shadowsocks protocol.
It includes Outline Manager, a desktop application for setting up servers, managing users, and tracking traffic, and Outline Client,
a user-friendly app compatible with various mobile and desktop platforms.

It normally works as below.

```
[Outline Client] <-> [Outline Server] <-> (Internet)
```

Read the [Outline official documentation](https://getoutline.org/get-started) to set up an Outline server.

### What's V2Ray?

[V2Ray](https://github.com/v2fly/v2ray-core) is a proxy tool that supports multiple protocols, including the `dokodemo-door` protocol.
This specific protocol forwards incoming traffic (TCP and UDP) from a specified port to a designated destination port.

### What's a Bridge Server?

A bridge server connects clients to Outline servers by forwarding their traffic.

It changes the Outline flow as below.

```
[Outline Client] <-> [Bridge Server] <-> [Outline Server] <-> (Internet)
```

### Setup V2Ray as Bridge Server

Follow these steps to set up the Xray and Outline:

1. Install Docker and Docker-compose on the bridge server.
1. Clone this repository into the bridge server.
1. Run `./setup.py`. It prompts the following items:
    1. `Number of Outline servers`: Please provide the number of servers, typically just `1`
    1. `Outline server i Host`: Find it in Outline Manager > `{server i}` > Settings > Hostname
    1. `Outline server i Port`: Find it in Outline Manager > `{server i}` > Settings > Port
    1. If you are using a firewall such as `ufw`, add the port to the whitelist.
1. Run `docker-compose up -d` (or `docker compose up -d`).
1. Change Outline Manager > `{server i}` > Settings > Hostname field to the bridge server IP address.
1. Delete old access keys in the Outline Manager and generate new ones.
1. Download [Outline Client](https://getoutline.org/get-started/#step-3) and import a generated access key.
1. Press "CONNECT" and enjoy the freedom!

## More

* [V2Ray Docker Compose](https://github.com/miladrahimi/v2ray-docker-compose)
