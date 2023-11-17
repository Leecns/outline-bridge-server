# Outline Bridge Server

This repository includes Docker Compose files for running the V2Ray proxy as a bridge (relay) server for the Outline proxy.
Its purpose is to enable the Outline proxy to function effectively in severely restricted networks where direct, secure, and reliable access may not be available.

## Documentation

### Outline

[Outline](https://getoutline.org), developed by Google, is a user-friendly proxy based on Shadowsocks.
It simplifies the process of creating and managing Shadowsocks servers.
Additionally, Outline offers well-designed client applications that are compatible with various platforms.

It usually works as below.

```
[Outline client] <-> [Outline server] <-> (Internet)
```

Read the [Outline official documentation](https://getoutline.org/get-started) to set up an Outline server.

### V2Ray as Bridge Server

The bridge server acts as an intermediary between clients and a server, facilitating the connection between the two in cases where a direct, secure, or stable connection is not feasible.
It operates a V2Ray proxy to efficiently transmit incoming Shadowsocks traffic (both TCP and UDP) from clients to the Outline server.

The bridge server changes the flow as below.

```
[Outline client] <-> [V2Ray server] <-> [Outline server] <-> (Internet)
```

### Setup

Follow these steps to set up the V2Ray and Outline:

1. Install Docker and Docker-compose on the bridge server.
1. Clone this repository into the bridge server.
1. Run `./setup.py` script. It gets the following inputs:
    1. `Outline Server Hostname`: Find it in Outline Manager > {Server} > Settings > Hostname
    1. `Outline Server Port`: Find it in Outline Manager > {Server} > Settings > Port
    1. Allow the port for incoming/outgoing traffic if you have a firewall.
1. Run `docker-compose up -d`.
1. Change Outline Manager > {Server} > Settings > Hostname field to the bridge server IP address.
1. Delete old access keys in the Outline Manager and generate new ones.
1. Download [Outline client applications](https://getoutline.org/get-started/#step-3) and add the new access keys there.
1. Enjoy the freedom!

### Docker Images

By default, this repository uses the GitHub Docker registry.
You can modify the Docker-compose file to use Docker Hub instead.

* GitHub:
    * Image: ```ghcr.io/getimages/v2fly-core:v4.45.2```
    * URL: https://github.com/orgs/getimages/packages/container/package/v2fly-core
    * Digest: `sha256:289fc9451f21a265f95615e29f05ea23bc32026db152863eee317738813521d7`
* Docker Hub:
    * Image: ```v2fly/v2fly-core:v4.45.2```
    * URL: https://hub.docker.com/r/v2fly/v2fly-core/tags
    * Digest: `sha256:289fc9451f21a265f95615e29f05ea23bc32026db152863eee317738813521d7`

## More

* [V2Ray Docker Compose](https://github.com/miladrahimi/v2ray-docker-compose)
