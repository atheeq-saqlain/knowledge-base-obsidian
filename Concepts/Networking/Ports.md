---
slug:
---

## Definition

A **port** is a numbered endpoint (1–65,535) on a host identified by an [[IP Address]] that lets multiple applications share the same machine while incoming traffic is delivered to the correct service.

## Description

A single server often runs many programs at once — a web server, database, and payment API, for example. All of them may share one public IP address. Ports distinguish which application should receive each connection.

**Common examples:**

| Port | Typical service |
|------|-----------------|
| 80 | HTTP (unencrypted web) |
| 443 | HTTPS (encrypted web) |
| 3306 | MySQL database |
| 5432 | PostgreSQL database |

When a client connects to `203.0.113.42:443`, the IP identifies the host and `443` tells the operating system to hand the traffic to the process listening on that port.

Ports are a transport-layer concept (TCP and UDP). Firewalls and load balancers frequently filter or forward traffic based on port numbers alongside IP addresses.
