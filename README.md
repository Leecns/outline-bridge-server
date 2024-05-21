# Outline Bridge Server

This repository contains a Docker Compose file designed to run V2Ray as a bridge (relay) server for the Outline (a shadowsocks proxy by Google Jigsaw).
The primary goal is to enhance the functionality of the Outline in highly restricted networks where direct connections to Outline servers is not possible.

## Documentation

### What's Outline?

[Outline](https://getoutline.org) is a set of proxy tools developed by Google based on the shadowsocks protocol.
It includes Outline Manager, a desktop application for setting up servers, managing users, and tracking traffic, and Outline Client,
a user-friendly app compatible with various mobile and desktop platforms.

It originally works as below.

```
[Outline Client] <-> [Outline Server] <-> (Internet)
```

Read the [Outline official documentation](https://getoutline.org/get-started) to set up an Outline server.

### What's V2Ray?

[V2Ray](https://github.com/v2fly/v2ray-core) is a proxy tool that supports multiple protocols, including the `dokodemo-door` protocol.
This specific protocol forwards incoming traffic (TCP and UDP) from a specified port to a designated destination port.

### What's a Bridge Server?

A bridge (relay) server connects clients to Outline servers by forwarding their traffic.

It changes the Outline flow as below.

```
[Outline Client] <-> [Bridge Server] <-> [Outline Server] <-> (Internet)
```

### Setup Bridge Server using V2Ray

To set up a bridge (relay) server using V2Ray, follow these steps:

1. Install Docker and Docker-compose on the bridge (relay) server.
1. Clone this repository into the bridge server.
1. Run `./setup.py`. It prompts the following items:
    1. `Number of Outline servers`: Please provide the number of servers, typically just `1`
    1. `Outline server i host`: Find it in $\color{green}{\textsf{Outline Manager}}$ > `Settings` > `Hostname`
    1. `Outline server i port`: Find it in $\color{green}{\textsf{Outline Manager}}$ > `Settings` > `Port for new access keys`
    1. If you are using a firewall such as `ufw`, add the port to the whitelist.
1. Run `docker-compose up -d` or `docker compose up -d`.
1. Change $\color{green}{\textsf{Outline Manager}}$ > `Settings` > `Hostname` field to the bridge server IP address.
1. Delete old access keys in the $\color{green}{\textsf{Outline Manager}}$ and generate new ones.
1. Download [Outline Client](https://getoutline.org/get-started/#step-3) and import a generated access key.
1. Press $\color{green}{\textsf{CONNECT}}$ and enjoy the freedom!

## More

* [V2Ray Docker Compose](https://github.com/miladrahimi/v2ray-docker-compose)
