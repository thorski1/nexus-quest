"""
zones.py — Networking skill pack zones for NEXUS Quest.
Cover the full network stack: OSI model through troubleshooting.
"""

from engine.zone import Zone
from engine.challenge import Challenge

ZONE_ORDER = [
    "osi_model",
    "tcp_ip",
    "dns",
    "http",
    "ip_addressing",
    "firewalls_and_security",
    "load_balancing",
    "troubleshooting",
]

ZONES = {
    # ──────────────────────────────────────────────
    # ZONE 1 — OSI MODEL
    # ──────────────────────────────────────────────
    "osi_model": Zone(
        id="osi_model",
        title="The Seven Layers",
        description="Understand the OSI reference model — each layer's role, encapsulation, and real-world mapping.",
        challenges=[
            Challenge(
                id="osi_layer_count",
                type="quiz",
                prompt="How many layers does the OSI (Open Systems Interconnection) model define?",
                options=[
                    "4 layers — matching the TCP/IP model",
                    "5 layers — Physical through Session",
                    "7 layers — Physical through Application",
                    "8 layers — including a Security layer",
                ],
                answer="c",
                explanation="The OSI model defines exactly 7 layers: Physical, Data Link, Network, Transport, Session, Presentation, and Application. The mnemonic 'Please Do Not Throw Sausage Pizza Away' maps layers 1-7.",
                xp=25,
            ),
            Challenge(
                id="osi_physical",
                type="quiz",
                prompt="Layer 1 (Physical) is responsible for:",
                options=[
                    "Routing packets between networks using IP addresses",
                    "Transmitting raw bit streams over a physical medium (cables, radio waves, voltage levels)",
                    "Establishing, maintaining, and tearing down sessions between applications",
                    "Encrypting data before transmission",
                ],
                answer="b",
                explanation="Layer 1 deals with raw bits on the wire — voltage levels, cable specs (Cat5e, fibre), radio frequencies (Wi-Fi), connectors (RJ45). It has no concept of addresses or packets, only 1s and 0s.",
                xp=25,
            ),
            Challenge(
                id="osi_data_link",
                type="quiz",
                prompt="Which layer uses MAC addresses and frames to deliver data between devices on the same network segment?",
                options=[
                    "Layer 1 — Physical",
                    "Layer 2 — Data Link",
                    "Layer 3 — Network",
                    "Layer 4 — Transport",
                ],
                answer="b",
                explanation="The Data Link layer (Layer 2) packages bits into frames, adds source and destination MAC addresses, and handles error detection (CRC). Switches operate at this layer. Ethernet and Wi-Fi are Layer 2 protocols.",
                xp=25,
            ),
            Challenge(
                id="osi_network_layer",
                type="quiz",
                prompt="A router makes forwarding decisions based on IP addresses. At which OSI layer does a router primarily operate?",
                options=[
                    "Layer 2 — Data Link",
                    "Layer 3 — Network",
                    "Layer 4 — Transport",
                    "Layer 7 — Application",
                ],
                answer="b",
                explanation="Layer 3 (Network) handles logical addressing (IP) and routing — determining the best path for packets across multiple networks. Routers examine destination IP addresses to make forwarding decisions. IP, ICMP, and OSPF live here.",
                xp=30,
            ),
            Challenge(
                id="osi_encapsulation",
                type="quiz",
                prompt="As data moves down the OSI stack from Application to Physical, each layer adds its own header. This process is called:",
                options=[
                    "Multiplexing — combining multiple signals on one medium",
                    "Encapsulation — wrapping data with layer-specific headers (and sometimes trailers)",
                    "Serialization — converting objects to a byte stream",
                    "Fragmentation — splitting data into smaller pieces",
                ],
                answer="b",
                explanation="Encapsulation wraps each layer's PDU (Protocol Data Unit) inside the next layer down. Application data becomes a segment (L4), then a packet (L3), then a frame (L2), then bits (L1). The reverse — stripping headers — is decapsulation.",
                xp=30,
            ),
            Challenge(
                id="osi_transport_vs_network",
                type="quiz",
                prompt="What is the key difference between Layer 3 (Network) and Layer 4 (Transport)?",
                options=[
                    "Layer 3 handles MAC addresses; Layer 4 handles IP addresses",
                    "Layer 3 handles IP addressing and routing; Layer 4 handles end-to-end delivery, ports, and reliability (TCP/UDP)",
                    "Layer 3 handles encryption; Layer 4 handles compression",
                    "Layer 3 operates on switches; Layer 4 operates on hubs",
                ],
                answer="b",
                explanation="Layer 3 gets packets to the right host via IP routing. Layer 4 gets data to the right application via port numbers and provides reliability (TCP) or speed (UDP). Together they form the core of TCP/IP communication.",
                xp=35,
            ),
        ],
    ),

    # ──────────────────────────────────────────────
    # ZONE 2 — TCP/IP
    # ──────────────────────────────────────────────
    "tcp_ip": Zone(
        id="tcp_ip",
        title="The Transport Grid",
        description="TCP vs UDP, the three-way handshake, ports, sockets, and connection states.",
        challenges=[
            Challenge(
                id="tcp_vs_udp",
                type="quiz",
                prompt="Which statement correctly contrasts TCP and UDP?",
                options=[
                    "TCP is connectionless and fast; UDP is connection-oriented and reliable",
                    "TCP is connection-oriented with guaranteed delivery; UDP is connectionless with no delivery guarantee",
                    "Both TCP and UDP guarantee ordered delivery of packets",
                    "UDP uses a three-way handshake; TCP does not",
                ],
                answer="b",
                explanation="TCP establishes a connection (three-way handshake), guarantees delivery via ACKs and retransmissions, and ensures ordering. UDP fires packets without confirmation — faster, lighter, but no guarantees. DNS queries, video streaming, and gaming often use UDP.",
                xp=25,
            ),
            Challenge(
                id="tcp_handshake",
                type="quiz",
                prompt="The TCP three-way handshake consists of which sequence?",
                options=[
                    "ACK, SYN, FIN",
                    "SYN, SYN-ACK, ACK",
                    "SYN, ACK, FIN",
                    "HELLO, OK, READY",
                ],
                answer="b",
                explanation="Client sends SYN (synchronize), server responds with SYN-ACK (synchronize-acknowledge), client replies with ACK (acknowledge). This establishes sequence numbers and confirms both sides are ready. Only then does data flow.",
                xp=30,
            ),
            Challenge(
                id="tcp_well_known_port",
                type="quiz",
                prompt="Which port number does HTTPS use by default?",
                options=[
                    "Port 22 — used by SSH",
                    "Port 80 — used by HTTP",
                    "Port 443 — used by HTTPS",
                    "Port 3306 — used by MySQL",
                ],
                answer="c",
                explanation="HTTPS (HTTP over TLS) defaults to port 443. HTTP uses 80, SSH uses 22, DNS uses 53. Ports 0-1023 are 'well-known' and typically require root/admin to bind. Memorize the critical ones: 22 (SSH), 53 (DNS), 80 (HTTP), 443 (HTTPS), 5432 (PostgreSQL).",
                xp=25,
            ),
            Challenge(
                id="tcp_socket_definition",
                type="quiz",
                prompt="A 'socket' in networking is defined as:",
                options=[
                    "A physical connector on a network interface card",
                    "The combination of an IP address and a port number that uniquely identifies a connection endpoint",
                    "A software firewall rule that permits traffic",
                    "The name for a UDP datagram",
                ],
                answer="b",
                explanation="A socket = IP address + port number (e.g., 192.168.1.10:8080). A TCP connection is uniquely identified by a 4-tuple: source IP, source port, destination IP, destination port. The socket abstraction is what allows a single server to handle thousands of connections.",
                xp=30,
            ),
            Challenge(
                id="tcp_time_wait",
                type="quiz",
                prompt="After a TCP connection is closed, the socket enters TIME_WAIT state. Why?",
                options=[
                    "To allow the server to restart the connection automatically",
                    "To ensure any delayed packets from the old connection don't corrupt a new connection using the same port",
                    "To keep the connection alive for HTTP keep-alive",
                    "To allow the firewall to log the connection closure",
                ],
                answer="b",
                explanation="TIME_WAIT (typically 2x MSL = 60-120 seconds) ensures late-arriving packets from the closed connection are discarded rather than misinterpreted by a new connection. On high-traffic servers, many TIME_WAIT sockets can exhaust ports — tunable via net.ipv4.tcp_tw_reuse.",
                xp=35,
            ),
            Challenge(
                id="tcp_udp_use_case",
                type="quiz",
                prompt="A live video streaming service chooses UDP over TCP because:",
                options=[
                    "UDP encrypts the video stream automatically",
                    "UDP's lack of retransmission avoids stale-frame delays — a dropped frame is better than a late one",
                    "UDP supports larger packet sizes than TCP",
                    "UDP connections are more secure than TCP connections",
                ],
                answer="b",
                explanation="For real-time media, retransmitting a lost packet arrives too late to display — the moment has passed. UDP accepts occasional loss for lower latency. Protocols like RTP (Real-time Transport Protocol) run over UDP and handle their own minimal error recovery.",
                xp=30,
            ),
        ],
    ),

    # ──────────────────────────────────────────────
    # ZONE 3 — DNS
    # ──────────────────────────────────────────────
    "dns": Zone(
        id="dns",
        title="The Name Authority",
        description="DNS resolution, record types, TTL, caching, and dig.",
        challenges=[
            Challenge(
                id="dns_purpose",
                type="quiz",
                prompt="What is the primary function of DNS?",
                options=[
                    "Encrypting web traffic between browser and server",
                    "Translating human-readable domain names into IP addresses",
                    "Routing packets between networks",
                    "Assigning IP addresses to devices on a network",
                ],
                answer="b",
                explanation="DNS (Domain Name System) is the internet's phone book. When you type 'example.com', DNS resolves it to an IP like 93.184.216.34. Without DNS you'd have to memorize numeric addresses for every site. The resolution chain: browser cache -> OS cache -> resolver -> root -> TLD -> authoritative nameserver.",
                xp=25,
            ),
            Challenge(
                id="dns_a_record",
                type="quiz",
                prompt="An 'A' record in DNS maps:",
                options=[
                    "A domain name to an IPv6 address",
                    "A domain name to an IPv4 address",
                    "A domain name to another domain name (alias)",
                    "A domain to a mail server",
                ],
                answer="b",
                explanation="A record = Address record, mapping a domain to an IPv4 address. AAAA maps to IPv6. CNAME creates an alias (one domain pointing to another). MX defines mail servers. NS specifies authoritative nameservers for a zone.",
                xp=25,
            ),
            Challenge(
                id="dns_cname",
                type="quiz",
                prompt="Your CDN provider says: 'Point www.example.com to cdn-12345.cdnprovider.net.' Which DNS record type creates this alias?",
                options=[
                    "A record — maps to an IP address",
                    "CNAME record — maps one domain name to another domain name",
                    "MX record — maps to a mail server",
                    "NS record — delegates to a nameserver",
                ],
                answer="b",
                explanation="CNAME (Canonical Name) creates an alias from one domain to another. The resolver follows the chain: www.example.com CNAME cdn-12345.cdnprovider.net, then resolves that to an IP. Important: CNAME cannot coexist with other records at the zone apex (bare domain).",
                xp=30,
            ),
            Challenge(
                id="dns_ttl",
                type="quiz",
                prompt="A DNS record has a TTL (Time To Live) of 300. This means:",
                options=[
                    "The record expires permanently after 300 days",
                    "Resolvers can cache the record for 300 seconds before re-querying the authoritative server",
                    "The domain will be unreachable for 300 seconds during a DNS change",
                    "The record can hold a maximum of 300 bytes",
                ],
                answer="b",
                explanation="TTL is measured in seconds. A TTL of 300 = 5 minutes of caching. Before a DNS migration, lower the TTL (e.g., to 60s) so changes propagate fast. After migration, raise it (e.g., 3600s = 1 hour) to reduce query load. Overlooking TTL is a common cause of 'I changed the DNS but nothing happened.'",
                xp=30,
            ),
            Challenge(
                id="dns_dig_command",
                type="quiz",
                prompt="Which command queries DNS records from the command line and shows the full answer section, authority, and additional data?",
                options=[
                    "nslookup example.com — basic lookup, less detail",
                    "dig example.com — full DNS query tool with detailed output sections",
                    "traceroute example.com — traces the network path",
                    "curl example.com — fetches HTTP content",
                ],
                answer="b",
                explanation="dig (Domain Information Groper) is the gold-standard DNS debugging tool. 'dig example.com A' shows the answer section, TTL, authoritative servers. 'dig +short' gives just the IP. 'dig @8.8.8.8 example.com' queries a specific resolver. Essential for troubleshooting DNS propagation issues.",
                xp=30,
            ),
            Challenge(
                id="dns_resolution_chain",
                type="quiz",
                prompt="When a recursive resolver needs to look up 'api.example.com' from scratch, what is the correct resolution order?",
                options=[
                    "Root nameserver -> .com TLD nameserver -> example.com authoritative nameserver",
                    "example.com authoritative nameserver -> .com TLD nameserver -> Root nameserver",
                    "Browser cache -> ISP cache -> Root nameserver only",
                    "The resolver contacts api.example.com directly",
                ],
                answer="a",
                explanation="DNS resolution walks the hierarchy top-down. The recursive resolver asks a root server (.) for .com, gets referred to the .com TLD server, asks it for example.com, gets referred to the authoritative NS, then finally gets the A/AAAA record for api.example.com. Caching short-circuits this at every step.",
                xp=35,
            ),
        ],
    ),

    # ──────────────────────────────────────────────
    # ZONE 4 — HTTP
    # ──────────────────────────────────────────────
    "http": Zone(
        id="http",
        title="The Protocol Layer",
        description="HTTP methods, status codes, headers, TLS, and HTTP/2 vs HTTP/3.",
        challenges=[
            Challenge(
                id="http_get_vs_post",
                type="quiz",
                prompt="What is the fundamental difference between HTTP GET and POST?",
                options=[
                    "GET requests can have a body; POST requests cannot",
                    "GET retrieves a resource without side effects; POST submits data to be processed (often creating or modifying resources)",
                    "GET is encrypted; POST is not",
                    "GET is used only for HTML pages; POST is used only for JSON APIs",
                ],
                answer="b",
                explanation="GET is idempotent and safe — it retrieves data without changing server state. POST sends data to the server (form submissions, API calls that create resources). GET parameters go in the URL query string; POST data goes in the request body. PUT replaces a resource; DELETE removes one; PATCH partially updates.",
                xp=25,
            ),
            Challenge(
                id="http_status_404",
                type="quiz",
                prompt="A server returns HTTP status code 404. This means:",
                options=[
                    "The server is overloaded and cannot handle the request",
                    "The request was successful",
                    "The requested resource was not found on the server",
                    "The client is not authorized to access the resource",
                ],
                answer="c",
                explanation="404 Not Found — the resource doesn't exist at the given URL. The status code families: 2xx = success (200 OK, 201 Created), 3xx = redirection (301 Moved, 304 Not Modified), 4xx = client error (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found), 5xx = server error (500, 502, 503).",
                xp=25,
            ),
            Challenge(
                id="http_status_503",
                type="quiz",
                prompt="During a deployment, your load balancer health checks start returning 503. What does this status code indicate?",
                options=[
                    "502 Bad Gateway — the upstream server sent an invalid response",
                    "503 Service Unavailable — the server is temporarily unable to handle requests (overloaded or in maintenance)",
                    "500 Internal Server Error — an unhandled exception crashed the request",
                    "504 Gateway Timeout — the upstream server didn't respond in time",
                ],
                answer="b",
                explanation="503 Service Unavailable means the server is alive but temporarily can't serve requests — common during deployments, overload, or maintenance. Unlike 500 (unexpected crash), 503 is deliberate and expected to be temporary. Load balancers use this to route traffic away from unhealthy backends.",
                xp=30,
            ),
            Challenge(
                id="http_tls",
                type="quiz",
                prompt="HTTPS uses TLS (Transport Layer Security) to provide:",
                options=[
                    "Faster page load times and compression",
                    "Encryption in transit, server authentication (via certificates), and data integrity",
                    "DNS resolution and IP routing",
                    "Load balancing across multiple servers",
                ],
                answer="b",
                explanation="TLS (successor to SSL) provides three guarantees: confidentiality (encryption prevents eavesdropping), authentication (certificates prove the server is who it claims), and integrity (data can't be tampered with in transit). The TLS handshake negotiates cipher suites and exchanges keys before any HTTP data flows.",
                xp=30,
            ),
            Challenge(
                id="http_put_vs_patch",
                type="quiz",
                prompt="In a RESTful API, what is the difference between PUT and PATCH?",
                options=[
                    "PUT creates a new resource; PATCH deletes an existing one",
                    "PUT replaces the entire resource; PATCH applies a partial update to the resource",
                    "PUT is idempotent; PATCH is not — they are otherwise identical",
                    "There is no difference; they are interchangeable",
                ],
                answer="b",
                explanation="PUT sends the complete new representation — any fields you omit are reset. PATCH sends only the changes (e.g., {\"email\": \"new@example.com\"}). Both can be idempotent in practice. Use PUT when you have the full object; use PATCH when updating one or two fields.",
                xp=30,
            ),
            Challenge(
                id="http_2_vs_3",
                type="quiz",
                prompt="HTTP/3 differs from HTTP/2 primarily because:",
                options=[
                    "HTTP/3 removes encryption; HTTP/2 requires TLS",
                    "HTTP/3 uses QUIC over UDP instead of TCP, eliminating TCP head-of-line blocking",
                    "HTTP/3 replaces JSON with binary encoding",
                    "HTTP/3 only works on IPv6 networks",
                ],
                answer="b",
                explanation="HTTP/2 multiplexes streams over a single TCP connection but still suffers from TCP head-of-line blocking (one lost packet stalls all streams). HTTP/3 replaces TCP with QUIC (built on UDP), giving each stream independent loss recovery. TLS 1.3 is built into QUIC, reducing handshake round-trips.",
                xp=40,
            ),
        ],
    ),

    # ──────────────────────────────────────────────
    # ZONE 5 — IP ADDRESSING
    # ──────────────────────────────────────────────
    "ip_addressing": Zone(
        id="ip_addressing",
        title="The Address Grid",
        description="IPv4, IPv6, subnetting, CIDR, private ranges, and NAT.",
        challenges=[
            Challenge(
                id="ip_private_range",
                type="quiz",
                prompt="Which of the following is a private (RFC 1918) IPv4 address range?",
                options=[
                    "8.8.8.0/24 — Google's public DNS range",
                    "192.168.0.0/16 — private, used in home and office LANs",
                    "203.0.113.0/24 — TEST-NET-3, reserved for documentation",
                    "169.254.0.0/16 — link-local, auto-assigned when DHCP fails",
                ],
                answer="b",
                explanation="RFC 1918 defines three private ranges: 10.0.0.0/8 (16M addresses), 172.16.0.0/12 (1M addresses), 192.168.0.0/16 (65K addresses). These are not routable on the public internet — NAT translates them to a public IP at the gateway. Every home router uses one of these internally.",
                xp=25,
            ),
            Challenge(
                id="ip_cidr_slash_24",
                type="quiz",
                prompt="A subnet defined as 10.0.1.0/24 contains how many usable host addresses?",
                options=[
                    "256 addresses — all available for hosts",
                    "254 addresses — 256 minus network address and broadcast address",
                    "128 addresses — half the range reserved",
                    "24 addresses — one per bit in the mask",
                ],
                answer="b",
                explanation="/24 means 24 bits for network, 8 bits for hosts = 2^8 = 256 total. Subtract the network address (10.0.1.0) and broadcast address (10.0.1.255) = 254 usable host addresses. This is the most common subnet size for a single VLAN or AWS subnet.",
                xp=30,
            ),
            Challenge(
                id="ip_nat_purpose",
                type="quiz",
                prompt="NAT (Network Address Translation) is primarily used to:",
                options=[
                    "Encrypt traffic between two private networks",
                    "Allow multiple devices with private IPs to share a single public IP address for internet access",
                    "Assign domain names to IP addresses",
                    "Route traffic between VLANs on a switch",
                ],
                answer="b",
                explanation="NAT lets an entire LAN (e.g., 192.168.1.0/24) access the internet through one public IP. The router tracks which internal host made each request (using port numbers — PAT/NAPT). This conserves IPv4 addresses and provides a basic layer of obscurity (not security) for internal hosts.",
                xp=30,
            ),
            Challenge(
                id="ip_ipv6_format",
                type="quiz",
                prompt="An IPv6 address is:",
                options=[
                    "32 bits, written in dotted decimal (e.g., 192.168.1.1)",
                    "128 bits, written in eight groups of four hexadecimal digits separated by colons",
                    "64 bits, written in four groups of hexadecimal digits",
                    "48 bits, identical in format to a MAC address",
                ],
                answer="b",
                explanation="IPv6 = 128 bits, e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334. Leading zeros can be dropped and one consecutive run of all-zero groups replaced with :: (e.g., 2001:db8::1). This gives 3.4 x 10^38 addresses — enough that NAT is unnecessary. IPv4 has only 4.3 billion (2^32).",
                xp=30,
            ),
            Challenge(
                id="ip_subnet_splitting",
                type="quiz",
                prompt="You have a /16 network and need to split it into subnets, each supporting at least 250 hosts. The most efficient subnet mask is:",
                options=[
                    "/24 — 254 usable hosts per subnet (just enough)",
                    "/25 — 126 usable hosts per subnet (too few)",
                    "/20 — 4094 usable hosts per subnet (too large, wastes addresses)",
                    "/28 — 14 usable hosts per subnet (way too few)",
                ],
                answer="a",
                explanation="/24 gives 254 usable hosts — the smallest subnet that satisfies >= 250 hosts. /25 only provides 126. Efficient subnetting means choosing the mask that fits your requirement with minimal waste. In AWS, /24 is the standard for most subnets; /28 is the minimum VPC subnet size.",
                xp=35,
            ),
        ],
    ),

    # ──────────────────────────────────────────────
    # ZONE 6 — FIREWALLS AND SECURITY
    # ──────────────────────────────────────────────
    "firewalls_and_security": Zone(
        id="firewalls_and_security",
        title="The Perimeter",
        description="iptables, security groups, WAF, DDoS defense, and zero-trust architecture.",
        challenges=[
            Challenge(
                id="fw_iptables_chains",
                type="quiz",
                prompt="In Linux iptables, which chain handles packets arriving at the machine that are destined for a local process?",
                options=[
                    "OUTPUT — handles outbound packets from local processes",
                    "INPUT — handles inbound packets destined for the local machine",
                    "FORWARD — handles packets being routed through the machine",
                    "PREROUTING — handles packets before routing decisions",
                ],
                answer="b",
                explanation="iptables has three default chains in the filter table: INPUT (inbound to this host), OUTPUT (outbound from this host), FORWARD (passing through to another host). PREROUTING and POSTROUTING are in the nat table. A typical server hardens INPUT to allow only SSH (22), HTTP (80), HTTPS (443) and drops everything else.",
                xp=30,
            ),
            Challenge(
                id="fw_security_groups",
                type="quiz",
                prompt="AWS Security Groups are stateful. This means:",
                options=[
                    "Rules must be defined in both directions — inbound and outbound separately for each flow",
                    "If you allow inbound traffic on a port, the return traffic is automatically allowed regardless of outbound rules",
                    "They remember previous connections and block repeated offenders",
                    "They can only be attached to instances in public subnets",
                ],
                answer="b",
                explanation="Stateful firewalls track connection state. If an inbound rule allows TCP 443, the response packets are automatically permitted — you don't need an explicit outbound rule. NACLs (Network ACLs) are stateless and require rules in both directions. This is a top interview question.",
                xp=30,
            ),
            Challenge(
                id="fw_waf_purpose",
                type="quiz",
                prompt="A WAF (Web Application Firewall) protects against:",
                options=[
                    "Physical theft of server hardware",
                    "Application-layer attacks like SQL injection, XSS, and malicious request patterns",
                    "Low-level network floods at Layer 3/4",
                    "DNS poisoning attacks",
                ],
                answer="b",
                explanation="A WAF inspects HTTP/HTTPS traffic at Layer 7 and blocks malicious requests: SQL injection, cross-site scripting (XSS), request smuggling, path traversal. AWS WAF, Cloudflare WAF, and ModSecurity are common examples. It complements (not replaces) network firewalls and NACLs.",
                xp=30,
            ),
            Challenge(
                id="fw_ddos_mitigation",
                type="quiz",
                prompt="A volumetric DDoS attack overwhelms your service with massive traffic. The primary mitigation strategy is:",
                options=[
                    "Add more iptables rules to block each attacker IP individually",
                    "Absorb and filter traffic at the edge using a DDoS mitigation service or CDN with massive bandwidth capacity",
                    "Increase the server's CPU and RAM",
                    "Switch from HTTP to HTTPS",
                ],
                answer="b",
                explanation="Volumetric DDoS attacks can exceed hundreds of Gbps — far more than any single server or even data center can absorb. Services like AWS Shield, Cloudflare, and Akamai absorb traffic at globally distributed edge nodes, filtering legitimate requests from attack traffic before it reaches your origin.",
                xp=35,
            ),
            Challenge(
                id="fw_zero_trust",
                type="quiz",
                prompt="The zero-trust security model is based on the principle:",
                options=[
                    "Trust everything inside the corporate firewall; verify everything outside",
                    "Never trust, always verify — authenticate and authorize every request regardless of network location",
                    "Trust is established once during VPN connection and lasts for the session",
                    "Only trust traffic from whitelisted IP ranges",
                ],
                answer="b",
                explanation="Zero trust assumes the network is always hostile — even internal traffic. Every request must be authenticated, authorized, and encrypted. No implicit trust based on IP or network segment. Google's BeyondCorp is a famous implementation. This model replaces the castle-and-moat perimeter approach.",
                xp=35,
            ),
            Challenge(
                id="fw_default_deny",
                type="quiz",
                prompt="When configuring a firewall, 'default deny' means:",
                options=[
                    "All traffic is allowed unless explicitly blocked by a rule",
                    "All traffic is blocked unless explicitly allowed by a rule",
                    "The firewall denies traffic only during non-business hours",
                    "Denied packets are logged but still forwarded",
                ],
                answer="b",
                explanation="Default deny (whitelist model) blocks everything by default and only allows explicitly permitted traffic. This is the gold standard for security — if you forgot to add a rule, the traffic is blocked rather than allowed. The opposite, default allow (blacklist model), lets everything through unless blocked — far riskier.",
                xp=25,
            ),
        ],
    ),

    # ──────────────────────────────────────────────
    # ZONE 7 — LOAD BALANCING
    # ──────────────────────────────────────────────
    "load_balancing": Zone(
        id="load_balancing",
        title="The Distribution Matrix",
        description="L4 vs L7 load balancing, algorithms, health checks, sticky sessions, and CDNs.",
        challenges=[
            Challenge(
                id="lb_l4_vs_l7",
                type="quiz",
                prompt="What is the key difference between Layer 4 and Layer 7 load balancing?",
                options=[
                    "L4 is software-based; L7 is hardware-only",
                    "L4 routes based on IP/port (TCP/UDP); L7 routes based on application data (HTTP headers, URL paths, cookies)",
                    "L4 supports HTTPS; L7 does not",
                    "L4 is used for internal services; L7 is used only for public endpoints",
                ],
                answer="b",
                explanation="L4 (Transport layer) sees only IP addresses and ports — fast, low overhead, protocol-agnostic. L7 (Application layer) inspects HTTP content: route /api/* to backend A, /static/* to backend B, sticky sessions via cookies. AWS NLB is L4; ALB is L7. Use L4 for raw TCP/UDP performance, L7 for HTTP-aware routing.",
                xp=30,
            ),
            Challenge(
                id="lb_round_robin",
                type="quiz",
                prompt="Round-robin load balancing distributes requests by:",
                options=[
                    "Sending all traffic to the server with the lowest current load",
                    "Cycling through each backend server in sequential order, one request at a time",
                    "Hashing the client IP to consistently route to the same server",
                    "Randomly selecting a server for each request",
                ],
                answer="b",
                explanation="Round-robin is the simplest algorithm: Server A, B, C, A, B, C... Weighted round-robin assigns proportional shares (e.g., A gets 3x the traffic of C). It's fair but doesn't account for server load — least-connections is better when request processing times vary significantly.",
                xp=25,
            ),
            Challenge(
                id="lb_health_checks",
                type="quiz",
                prompt="A load balancer health check typically:",
                options=[
                    "Monitors CPU usage on each backend server via SSH",
                    "Sends periodic requests (HTTP GET / or TCP connect) to each backend and removes unhealthy ones from rotation",
                    "Checks if the server's SSL certificate has expired",
                    "Pings the server's public IP address",
                ],
                answer="b",
                explanation="Health checks verify backends are alive and responsive. HTTP health checks hit a specific path (e.g., /healthz) and expect a 200 OK. TCP checks just verify the port accepts connections. Unhealthy servers are removed from the pool; once healthy again, they're re-added. Misconfigured health checks are a top cause of outages.",
                xp=30,
            ),
            Challenge(
                id="lb_sticky_sessions",
                type="quiz",
                prompt="Sticky sessions (session affinity) ensure that:",
                options=[
                    "All users are routed to the fastest server",
                    "A specific client is always routed to the same backend server for the duration of their session",
                    "Sessions are encrypted end-to-end",
                    "Server sessions are replicated across all backends",
                ],
                answer="b",
                explanation="Sticky sessions route a client to the same backend (via cookie or IP hash) so session state is preserved. Downside: uneven load distribution and reduced fault tolerance — if that backend dies, the session is lost. The modern solution: externalize session state to Redis or a database, making backends truly stateless.",
                xp=30,
            ),
            Challenge(
                id="lb_cdn_purpose",
                type="quiz",
                prompt="A CDN (Content Delivery Network) improves performance by:",
                options=[
                    "Compressing all database queries",
                    "Caching content at edge locations geographically close to users, reducing latency and origin server load",
                    "Encrypting traffic between microservices",
                    "Replacing the load balancer entirely",
                ],
                answer="b",
                explanation="CDNs (Cloudflare, CloudFront, Akamai) cache static assets (images, JS, CSS) and sometimes dynamic content at edge PoPs worldwide. A user in Tokyo hits the Tokyo edge instead of your US-East origin — reducing latency from ~200ms to ~20ms. CDNs also absorb traffic spikes and DDoS attacks at the edge.",
                xp=30,
            ),
            Challenge(
                id="lb_least_connections",
                type="quiz",
                prompt="The 'least connections' load balancing algorithm sends new requests to:",
                options=[
                    "The server that has been running the longest",
                    "The server currently handling the fewest active connections",
                    "The server with the lowest IP address",
                    "Whichever server responded most recently",
                ],
                answer="b",
                explanation="Least-connections routes traffic to the backend with the fewest active connections, which naturally accounts for varying request processing times. If server A is handling 50 long-running requests and server B only has 10, new requests go to B. This is better than round-robin for uneven workloads.",
                xp=25,
            ),
        ],
    ),

    # ──────────────────────────────────────────────
    # ZONE 8 — TROUBLESHOOTING
    # ──────────────────────────────────────────────
    "troubleshooting": Zone(
        id="troubleshooting",
        title="The Wire",
        description="ping, traceroute, netstat, tcpdump, curl — the operator's diagnostic toolkit.",
        challenges=[
            Challenge(
                id="ts_ping",
                type="quiz",
                prompt="The 'ping' command tests network connectivity by:",
                options=[
                    "Opening a TCP connection to port 80 on the target",
                    "Sending ICMP Echo Request packets and measuring round-trip time for the Echo Reply",
                    "Performing a DNS lookup and reporting the IP address",
                    "Scanning all open ports on the target host",
                ],
                answer="b",
                explanation="ping sends ICMP Echo Requests and listens for Echo Replies. It tells you: is the host reachable? What's the latency? Is there packet loss? Note: many hosts and firewalls block ICMP — a failed ping doesn't always mean the host is down. Always verify with a TCP-level check (curl, telnet, nc).",
                xp=25,
            ),
            Challenge(
                id="ts_traceroute",
                type="quiz",
                prompt="traceroute (tracert on Windows) shows the path packets take to a destination by:",
                options=[
                    "Sending packets with incrementally increasing TTL values and recording each router that responds with ICMP Time Exceeded",
                    "Reading the routing table on the local machine",
                    "Querying DNS for all intermediate servers",
                    "Opening TCP connections to each hop in the path",
                ],
                answer="a",
                explanation="traceroute sends packets with TTL=1 (first router responds), TTL=2 (second router), and so on. Each router decrements TTL and sends ICMP Time Exceeded when it hits 0. This maps every hop on the path, revealing where latency spikes or packet loss occurs. Essential for diagnosing routing issues.",
                xp=30,
            ),
            Challenge(
                id="ts_netstat_ss",
                type="quiz",
                prompt="To see all TCP connections and listening ports on a Linux server, the modern replacement for netstat is:",
                options=[
                    "ifconfig — shows network interface configuration",
                    "ss — socket statistics, faster and more detailed than netstat",
                    "ip route — shows the routing table",
                    "arp — shows the ARP cache",
                ],
                answer="b",
                explanation="ss (socket statistics) is the modern replacement for netstat on Linux. 'ss -tulnp' shows all TCP/UDP listening sockets with process names. It's faster because it reads directly from kernel socket tables. Common usage: 'ss -tnp' (active TCP connections with processes), 'ss -s' (summary statistics).",
                xp=30,
            ),
            Challenge(
                id="ts_tcpdump",
                type="quiz",
                prompt="tcpdump is used to:",
                options=[
                    "Monitor CPU and memory usage of network processes",
                    "Capture and inspect raw network packets on an interface in real time",
                    "Test HTTP endpoints and display response headers",
                    "Display the DNS cache on the local machine",
                ],
                answer="b",
                explanation="tcpdump captures packets at the network interface level — the closest you can get to seeing what's actually on the wire. 'tcpdump -i eth0 port 443' captures all HTTPS traffic. 'tcpdump -w capture.pcap' saves to a file for analysis in Wireshark. It's the ultimate 'what is actually happening on this network?' tool.",
                xp=35,
            ),
            Challenge(
                id="ts_curl_debug",
                type="quiz",
                prompt="To debug an HTTP request including DNS resolution time, TLS handshake, and response headers, the best curl flag is:",
                options=[
                    "curl -s (silent mode — hides progress but also hides debug info)",
                    "curl -v (verbose — shows connection details, TLS negotiation, request/response headers)",
                    "curl -o /dev/null (discards the body — useful but doesn't show debug info alone)",
                    "curl -L (follows redirects — doesn't add debug output)",
                ],
                answer="b",
                explanation="curl -v shows the full conversation: DNS resolution, TCP connect, TLS handshake (cipher suite, certificate chain), request headers sent, response headers received. For timing breakdown, use: curl -w '@curl-format.txt' -o /dev/null -s. For just headers: curl -I. curl is the Swiss Army knife of HTTP debugging.",
                xp=30,
            ),
            Challenge(
                id="ts_dns_not_resolving",
                type="quiz",
                prompt="A service is unreachable. 'ping myservice.example.com' fails, but 'ping 10.0.5.23' (the service's IP) works. The most likely cause is:",
                options=[
                    "The service is down and refusing connections",
                    "A DNS resolution failure — the domain name cannot be resolved to an IP address",
                    "A firewall is blocking ICMP packets",
                    "The server's TLS certificate has expired",
                ],
                answer="b",
                explanation="If the IP works but the hostname doesn't, DNS is the culprit. Debug with: 'dig myservice.example.com' to check if the record exists, 'cat /etc/resolv.conf' to verify resolver config, 'dig @8.8.8.8' to test with an external resolver. Common causes: missing DNS record, wrong NS delegation, local resolver misconfiguration.",
                xp=30,
            ),
        ],
    ),
}
