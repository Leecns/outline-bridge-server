# Outline Bridge Server

Outline Bridge Server is a Docker Compose for running V2Ray as bridge (relay) server for Outline (a shadowsocks proxy by Google Jigsaw).
It enables users to connect to Outline servers in restricted networks where direct connections are impossible.

## Documentation

### What's Outline?

[Outline](//getoutline.org) is a set of proxy tools developed by [Google Jigsaw](//jigsaw.google.com) based on the shadowsocks protocol.
It includes these tools:
* Outline Manager: A desktop app for setting up servers, managing users, and tracking used traffic.
* Outline Server: A shadowsocks server that will be installed on the servers by the Outline Manager app.
* Outline Client: A user-friendly and cross-platform app for users.

The original Outline proxy flow:

```
Outline Client <->  Outline Server   <-> (Internet)
(User Network) <-> (Upstream Server) <-> (Internet)
```

Read the [Outline official documentation](//getoutline.org/get-started) to set up an Outline server.

### What's V2Ray?

[V2Ray](//github.com/v2fly/v2ray-core) is a proxy tool that supports multiple protocols, including the `dokodemo-door` protocol.
This protocol only forwards incoming traffic (TCP and UDP) from a specific port to a destination port, without changing the data.

### What's Bridge Server?

A bridge (relay) server acts as an intermediary, accessible to users from restricted networks and connected to upstream servers.
It's an appropriate place for running V2Ray to relay incoming user traffic to Outline servers.

It changes the Outline flow as below.

```
(User Network) <-> (Bridge Server) <-> (Upstream Server) <-> (Internet)
Outline Client <->   V2Ray Proxy   <->  Outline Server   <-> (Internet)
```

### Setup

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
1. Delete old access keys in the $\color{green}{\textsf{Outline Manager}}$ and generate new one.
1. Download [Outline Client](//getoutline.org/get-started/#step-3) and add the generated access key.
1. Press $\color{green}{\textsf{CONNECT}}$ and enjoy the freedom!

## Links

* [V2Ray Docker Compose](https://github.com/miladrahimi/v2ray-docker-compose)
