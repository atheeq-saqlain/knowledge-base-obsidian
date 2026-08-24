---
slug:
---

## Definition

A **firewall** inspects network traffic and permits or blocks it according to configured rules, acting as a security boundary between trusted and untrusted networks or hosts.

## Description

Firewalls enforce policy: which sources may reach which destinations, on which [[Ports|ports]], using which protocols. They are the network equivalent of a guarded checkpoint.

**Two common placements:**

| Type | Scope |
|------|-------|
| **Host firewall** | Runs on an individual server; filters traffic to that machine |
| **Network firewall** | Sits between [[Network Segmentation and Subnets|subnets]] or at the network edge; filters traffic crossing boundaries |

**Example rules:**

- Allow inbound TCP port 443 to web servers in the public subnet
- Deny all inbound traffic to the database subnet except from application servers
- Block outbound connections to known malicious IP ranges

Firewalls may operate on IP addresses, port numbers, protocol, and increasingly on application-layer context (next-generation firewalls). They complement — but do not replace — secure application design and authentication.
