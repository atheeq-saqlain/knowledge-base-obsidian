---
slug:
---

## Definition

**Network segmentation** divides a network into isolated sections (**[[subnets]]**), each with its own address range, to improve security, performance, and operational organization.

## Description

Instead of placing every server and workstation on one flat network, administrators group related systems into subnets. Each subnet behaves like its own neighborhood within the larger network.

**Typical layout:**

- **Public subnet** — front-end web servers reachable from the internet
- **Private subnet** — application servers with no direct public exposure
- **Database subnet** — data stores accessible only from trusted application tiers

Segmentation limits blast radius: if one subnet is compromised, attackers cannot automatically reach every other system. It also simplifies policy — for example, only the web tier needs inbound HTTP/HTTPS from the public internet.

Subnets are defined by IP address ranges and subnet masks (e.g. `10.0.1.0/24`). [[Routing]] moves traffic between subnets; [[Firewalls]] enforce which cross-subnet traffic is allowed.
