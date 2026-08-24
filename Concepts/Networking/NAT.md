---
slug:
---

## Definition

**NAT** (Network Address Translation) rewrites packet addresses so multiple devices with private [[IP Address|IP addresses]] can share one public IP address when communicating with external networks.

## Description

Private ranges (e.g. `10.x.x.x`, `192.168.x.x`) are not routable on the public internet. Homes and offices assign these addresses locally. NAT on a router or gateway translates outbound traffic so replies return to the correct internal device.

**Outbound example:**

1. Laptop `192.168.1.5` requests a page from `203.0.113.42`
2. Home router replaces the source address with its public IP `198.51.100.7` and records the mapping
3. The remote server replies to `198.51.100.7`
4. The router translates the destination back to `192.168.1.5` and forwards the packet

NAT conserves scarce public IPv4 addresses and adds a layer of obscurity — internal hosts are not directly addressable from the internet unless port forwarding or similar rules are configured.

NAT is common at network edges and works alongside [[Routing]] and [[Firewalls]]. It is distinct from DNS: NAT changes addresses in flight; DNS resolves names to addresses before a connection starts.
