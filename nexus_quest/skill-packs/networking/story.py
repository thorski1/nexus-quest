"""
story.py — Narrative for Network Ops (networking skill pack).
Theme: The network is the nervous system of the digital world.
"""

INTRO_STORY = """
[bold red]NEXUS TERMINAL — NETWORK OPERATIONS DIVISION[/bold red]

The evidence is locked behind seven proxy layers, three encrypted tunnels,
and a DNS infrastructure that NEXUS rewired from the inside.

You thought the hard part was getting into the system. But the system is
just a node. The network is the nervous system — and NEXUS has been
rewriting the nerve pathways for months.

CIPHER's voice crackles through static: [bold cyan]"The exfiltration pipeline
isn't a single server. It's a network. Packets flowing through load balancers,
DNS aliases, firewalls with custom rules — all designed to look like normal traffic."[/bold cyan]

A network topology map flickers on your screen. Nodes, edges, protocols.
Hundreds of connections. Most legitimate. Some... not.

[bold white]"I need to read the traffic."[/bold white]

[bold cyan]"Then you need to understand the network. Every layer. Every protocol.
OSI model to application layer. TCP handshakes to DNS resolution chains.
Subnets, NAT, firewalls, load balancers. The works."[/bold cyan]

A pause. Then: [bold cyan]"The network is the nervous system of the digital world.
Learn to read it — or NEXUS keeps using it to move data right under your nose."[/bold cyan]

[italic]Tracing route to nexus-proxy-07.darknet... 14 hops.[/italic]
"""

ZONE_INTROS = {
    "osi_model": (
        "[bold cyan]ZONE 1 — THE SEVEN LAYERS[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Before you touch a single packet, you need the map. "
        "The OSI model — seven layers, Physical to Application. "
        "Every protocol, every device, every header exists at a specific layer. "
        "Know the model and you know where to look when something breaks.'[/bold white]"
    ),
    "tcp_ip": (
        "[bold cyan]ZONE 2 — THE TRANSPORT GRID[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The NEXUS exfil channel uses TCP on non-standard ports "
        "with keepalive to avoid idle timeouts. Their backup channel? UDP — fire and forget. "
        "You need to understand both. The three-way handshake, connection states, "
        "port ranges, sockets. This is how data actually moves.'[/bold white]"
    ),
    "dns": (
        "[bold cyan]ZONE 3 — THE NAME AUTHORITY[/bold cyan]\n\n"
        "[bold white]CIPHER: 'NEXUS didn't just compromise the servers — they hijacked the DNS. "
        "Rogue CNAME records pointing to their proxy infrastructure. TTLs set to 86400 so the "
        "poison sticks for a full day. You need to understand every record type, the resolution "
        "chain, and how to interrogate a nameserver with dig.'[/bold white]"
    ),
    "http": (
        "[bold cyan]ZONE 4 — THE PROTOCOL LAYER[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The exfiltrated data leaves as HTTP POST requests to a "
        "legitimate-looking API endpoint. Status 200 on the way out, 204 on the callback. "
        "GET, POST, PUT, DELETE — every method has a purpose. Headers carry auth tokens. "
        "TLS encrypts the payload. You need to read HTTP like a language.'[/bold white]"
    ),
    "ip_addressing": (
        "[bold cyan]ZONE 5 — THE ADDRESS GRID[/bold cyan]\n\n"
        "[bold white]CIPHER: 'NEXUS carved out a /20 inside the corporate VPC — hidden "
        "in the gap between 10.0.16.0 and 10.0.31.255. Four thousand addresses, invisible "
        "to anyone who can't read a subnet mask. IPv4, IPv6, CIDR notation, NAT — "
        "this is how networks are mapped and divided.'[/bold white]"
    ),
    "firewalls_and_security": (
        "[bold cyan]ZONE 6 — THE PERIMETER[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The firewall rules look clean on paper. But NEXUS added "
        "three iptables rules in the FORWARD chain that redirect matching traffic to their "
        "proxy. Security groups wide open on port 8443. No WAF in front of the API. "
        "You need to understand firewalls — host-level, cloud-level, application-level — "
        "or you'll never see the holes.'[/bold white]"
    ),
    "load_balancing": (
        "[bold cyan]ZONE 7 — THE DISTRIBUTION MATRIX[/bold cyan]\n\n"
        "[bold white]CIPHER: 'They're using the company's own ALB to route exfil traffic. "
        "Path-based rules — /api/v2/sync/* goes to NEXUS backend targets. Health checks "
        "keep it looking alive. Sticky sessions pin the operator's connection. "
        "Layer 4 vs Layer 7, round-robin, least-connections, CDN caching — "
        "the load balancer is the traffic controller. Learn to read it.'[/bold white]"
    ),
    "troubleshooting": (
        "[bold cyan]ZONE 8 — THE WIRE[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Theory is done. Now you trace the actual traffic. "
        "ping to check reachability. traceroute to map the path. ss to see what's "
        "listening. tcpdump to capture raw packets. curl to replay the HTTP calls. "
        "These are your diagnostic instruments. The wire doesn't lie — "
        "if you know how to read it.'[/bold white]"
    ),
}

ZONE_COMPLETIONS = {
    "osi_model": (
        "[bold green]ZONE CLEAR — THE SEVEN LAYERS[/bold green]\n\n"
        "You can name every layer, identify which protocols live where, and trace "
        "data through the full encapsulation stack. CIPHER marks the OSI module clear. "
        "The map is in your head now."
    ),
    "tcp_ip": (
        "[bold green]ZONE CLEAR — THE TRANSPORT GRID[/bold green]\n\n"
        "TCP and UDP — you know the tradeoffs, the handshake, the states, the ports. "
        "Every socket on this network is now readable. "
        "CIPHER: 'You can read the transport layer. Good. Now you can trace the flow.'"
    ),
    "dns": (
        "[bold green]ZONE CLEAR — THE NAME AUTHORITY[/bold green]\n\n"
        "A records, CNAMEs, MX, NS, TTL — the full DNS stack decoded. "
        "CIPHER: 'You just found the rogue CNAME chain. Three aliases deep, "
        "pointing to a proxy in a jurisdiction that doesn't cooperate. "
        "Now we know where the traffic actually goes.'"
    ),
    "http": (
        "[bold green]ZONE CLEAR — THE PROTOCOL LAYER[/bold green]\n\n"
        "HTTP methods, status codes, headers, TLS — the application protocol is an open book. "
        "CIPHER: 'You can read every request and response in the exfil pipeline now. "
        "The POST to /api/v2/sync carried a 4MB payload. Let's find out what was in it.'"
    ),
    "ip_addressing": (
        "[bold green]ZONE CLEAR — THE ADDRESS GRID[/bold green]\n\n"
        "Subnets, CIDR blocks, private ranges, NAT — the address space is mapped. "
        "CIPHER: 'The hidden /20 is visible now. Every host in NEXUS's shadow subnet "
        "is on our target list. Good work.'"
    ),
    "firewalls_and_security": (
        "[bold green]ZONE CLEAR — THE PERIMETER[/bold green]\n\n"
        "iptables, security groups, WAF, zero-trust — you know where the walls are "
        "and where the holes were. "
        "CIPHER: 'The three rogue FORWARD rules are identified. The open security group "
        "on port 8443 is flagged. We're closing the gaps.'"
    ),
    "load_balancing": (
        "[bold green]ZONE CLEAR — THE DISTRIBUTION MATRIX[/bold green]\n\n"
        "L4, L7, round-robin, health checks, sticky sessions, CDN — you own the traffic layer. "
        "CIPHER: 'The ALB path rule routing to NEXUS targets is documented. "
        "We have the listener ARNs, the target group, the health check path. "
        "Time to pull it from rotation.'"
    ),
    "troubleshooting": (
        "[bold green]ZONE CLEAR — THE WIRE[/bold green]\n\n"
        "ping, traceroute, ss, tcpdump, curl — the diagnostic toolkit is yours. "
        "CIPHER: 'You just traced the full exfil path: 14 hops, three continents, "
        "two CDN edges, one rogue load balancer. The network is no longer a black box. "
        "The nervous system is mapped. NEXUS can't hide in the wire anymore.'"
    ),
}

BOSS_INTROS = {
    "osi_model": (
        "[bold red]BOSS CHALLENGE — LAYER IDENTIFICATION[/bold red]\n\n"
        "[bold white]CIPHER: 'A packet is being inspected at a device that reads "
        "MAC addresses and forwards frames. Name the OSI layer. "
        "Get this wrong and every diagnosis you make will be off by a layer.'[/bold white]"
    ),
    "tcp_ip": (
        "[bold red]BOSS CHALLENGE — HANDSHAKE ANALYSIS[/bold red]\n\n"
        "[bold white]CIPHER: 'The tcpdump output shows a SYN from the client. "
        "No SYN-ACK comes back. What are the three most likely causes? "
        "This is how you diagnose a connection that never completes.'[/bold white]"
    ),
    "dns": (
        "[bold red]BOSS CHALLENGE — DNS HIJACK DETECTION[/bold red]\n\n"
        "[bold white]CIPHER: 'The CNAME for api.internal.corp resolves to an IP "
        "outside our infrastructure. Walk me through the dig commands to trace "
        "the full resolution chain and identify the rogue record.'[/bold white]"
    ),
    "http": (
        "[bold red]BOSS CHALLENGE — REQUEST FORENSICS[/bold red]\n\n"
        "[bold white]CIPHER: 'The access log shows a POST to /api/v2/sync returning "
        "200 OK with a 4MB response body. The endpoint should return 204 No Content "
        "with zero body. What does this tell you about the request?'[/bold white]"
    ),
    "ip_addressing": (
        "[bold red]BOSS CHALLENGE — SHADOW SUBNET[/bold red]\n\n"
        "[bold white]CIPHER: 'NEXUS hid a /20 in the VPC between two /24 subnets. "
        "Calculate the IP range, the number of usable hosts, and explain "
        "how it went undetected by the network team.'[/bold white]"
    ),
    "firewalls_and_security": (
        "[bold red]BOSS CHALLENGE — RULE AUDIT[/bold red]\n\n"
        "[bold white]CIPHER: 'The iptables output shows ACCEPT on the FORWARD chain "
        "for destination port 8443 with no source restriction. Explain the risk "
        "and write the rule to restrict it to the authorized CIDR block.'[/bold white]"
    ),
    "load_balancing": (
        "[bold red]BOSS CHALLENGE — TRAFFIC INTERCEPTION[/bold red]\n\n"
        "[bold white]CIPHER: 'The ALB has a path rule: /api/v2/sync/* routes to "
        "target group tg-nexus-exfil. Health check path: /healthz. "
        "Design the remediation: remove the rule, drain connections, "
        "verify no legitimate traffic is affected.'[/bold white]"
    ),
    "troubleshooting": (
        "[bold red]BOSS CHALLENGE — FULL TRACE[/bold red]\n\n"
        "[bold white]CIPHER: 'A service at api.corp.internal:443 is unreachable. "
        "Walk me through the complete diagnostic sequence: DNS, connectivity, "
        "port, TLS, application. Every command. Every interpretation. "
        "This is the final test — diagnose the wire.'[/bold white]"
    ),
}
