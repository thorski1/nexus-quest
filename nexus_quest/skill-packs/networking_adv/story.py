"""
story.py — Narrative for The Network Core (networking_adv skill pack).
Theme: CIPHER cyberpunk. Deeper into the protocol stack — where the real tradecraft lives.
"""

INTRO_STORY = """
[bold red]NEXUS TERMINAL — NETWORK CORE DIVISION[/bold red]

You cleared the fundamentals. You can read the OSI model, trace DNS,
parse HTTP headers, and run tcpdump without flinching. CIPHER signed off
on your network ops clearance.

But the adversary adapted.

CIPHER's voice comes through encrypted sideband, no static this time —
the channel itself is running QUIC over a custom port:

[bold cyan]"The exfil pipeline evolved. They migrated to HTTP/3 — multiplexed
streams over QUIC, zero-RTT resumption, encrypted headers. Our old
packet captures are useless. The TLS 1.3 handshake finishes before our
IDS even sees the ClientHello."[/bold cyan]

A new topology map loads. The nodes are the same, but the edges glow
with protocol annotations you haven't seen before: HPACK-compressed
headers, mTLS client certificates, eBPF hooks in the kernel, GSLB
failover chains spanning three continents.

[bold white]"They upgraded. So do we."[/bold white]

[bold cyan]"Exactly. TCP internals — congestion windows, selective ACK, keepalive
timers. HTTP/2 and HTTP/3 multiplexing. TLS certificate chains and cipher
negotiation. Advanced load balancing — L4 vs L7, GSLB, consistent
hashing. And the debugging tools that see through all of it: tcpdump
filters, Wireshark dissectors, eBPF tracing."[/bold cyan]

A pause. Then: [bold cyan]"This is the network core. The protocols beneath
the protocols. Master them — or NEXUS stays one layer ahead."[/bold cyan]

[italic]Initiating QUIC handshake to nexus-core-01.darknet... 0-RTT accepted.[/italic]
"""

ZONE_INTROS = {
    "tcp_deep_dive": (
        "[bold cyan]ZONE 1 — TCP DEEP DIVE[/bold cyan]\n\n"
        "[bold white]CIPHER: 'You know the three-way handshake. Now learn what happens "
        "after. Congestion windows that expand and collapse. Selective ACKs that "
        "recover from loss without retransmitting everything. Keepalive probes "
        "that detect dead connections. Window scaling that lets TCP fill a "
        "trans-oceanic pipe. This is where TCP actually lives.'[/bold white]"
    ),
    "http2_http3": (
        "[bold cyan]ZONE 2 — HTTP/2 & HTTP/3[/bold cyan]\n\n"
        "[bold white]CIPHER: 'NEXUS switched to HTTP/2 multiplexing six months ago. "
        "Last week they jumped to HTTP/3 — QUIC transport, UDP underneath, "
        "0-RTT resumption. No more head-of-line blocking. Server push preloads "
        "assets before you request them. HPACK compresses headers so tight our "
        "signature matching can't read them. You need to understand every stream, "
        "every frame, every evolution from HTTP/1.1.'[/bold white]"
    ),
    "tls_certificates": (
        "[bold cyan]ZONE 3 — TLS & CERTIFICATES[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The mTLS layer is where NEXUS authenticates their nodes. "
        "Client certs signed by a private CA — if you don't understand the "
        "certificate chain, you can't forge, intercept, or even detect them. "
        "TLS 1.3 handshake, cipher suite negotiation, OCSP stapling, certificate "
        "transparency logs. The encryption isn't the barrier — understanding it is.'[/bold white]"
    ),
    "load_balancing_adv": (
        "[bold cyan]ZONE 4 — ADVANCED LOAD BALANCING[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The exfil infrastructure runs behind a GSLB that routes "
        "by geography, then hits an L4 load balancer for raw throughput, then an "
        "L7 reverse proxy for path-based routing. Consistent hashing pins sessions. "
        "Health checks run every 5 seconds with a 3-strike deregistration policy. "
        "You need to understand every layer of this traffic distribution stack.'[/bold white]"
    ),
    "network_debugging": (
        "[bold cyan]ZONE 5 — NETWORK DEBUGGING[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Theory is worthless if you can't see the wire. tcpdump "
        "with BPF filters to isolate the exact flow. Wireshark dissectors to "
        "decode QUIC streams. dig with +trace to walk the DNS delegation chain. "
        "netstat and ss to map every socket. And eBPF — hooks in the kernel "
        "that trace packets without copying them to userspace. This is how "
        "you see what NEXUS doesn't want you to see.'[/bold white]"
    ),
}

ZONE_COMPLETIONS = {
    "tcp_deep_dive": (
        "[bold green]ZONE CLEAR — TCP DEEP DIVE[/bold green]\n\n"
        "Congestion windows, selective ACKs, Nagle's algorithm, keepalive timers — "
        "you own the TCP state machine down to the byte. "
        "CIPHER: 'You can read a congestion collapse before it happens. "
        "NEXUS can't hide behind TCP tuning anymore.'"
    ),
    "http2_http3": (
        "[bold green]ZONE CLEAR — HTTP/2 & HTTP/3[/bold green]\n\n"
        "Multiplexed streams, HPACK compression, QUIC transport, 0-RTT — "
        "the modern HTTP stack is transparent to you now. "
        "CIPHER: 'Their HTTP/3 migration bought them six weeks. "
        "You just took that advantage back.'"
    ),
    "tls_certificates": (
        "[bold green]ZONE CLEAR — TLS & CERTIFICATES[/bold green]\n\n"
        "Handshakes, certificate chains, OCSP, mTLS, cipher suites — "
        "the encryption layer is no longer a black box. "
        "CIPHER: 'We identified their private CA. The client certs "
        "are signed with a 2048-bit RSA key — and we have the fingerprint.'"
    ),
    "load_balancing_adv": (
        "[bold green]ZONE CLEAR — ADVANCED LOAD BALANCING[/bold green]\n\n"
        "GSLB, consistent hashing, connection draining, health check tuning — "
        "the traffic distribution layer is fully mapped. "
        "CIPHER: 'Three continents, seven PoPs, one consistent hash ring. "
        "We know exactly where their traffic lands.'"
    ),
    "network_debugging": (
        "[bold green]ZONE CLEAR — NETWORK DEBUGGING[/bold green]\n\n"
        "tcpdump, Wireshark, dig, ss, eBPF — every tool in the kit, mastered. "
        "CIPHER: 'You just traced a QUIC stream through three proxies, "
        "decoded the 0-RTT payload, and identified the exfil endpoint — "
        "all from a kernel-level eBPF trace. The network core is yours. "
        "NEXUS has nowhere left to hide.'"
    ),
}

BOSS_INTROS = {
    "tcp_deep_dive": (
        "[bold red]BOSS CHALLENGE — CONGESTION COLLAPSE[/bold red]\n\n"
        "[bold white]CIPHER: 'The tcpdump shows the congestion window dropped from "
        "64KB to 1 MSS three times in 10 seconds. Retransmissions are spiking. "
        "Walk me through what is happening inside the TCP state machine "
        "and how the sender will recover.'[/bold white]"
    ),
    "http2_http3": (
        "[bold red]BOSS CHALLENGE — STREAM ANALYSIS[/bold red]\n\n"
        "[bold white]CIPHER: 'The Wireshark capture shows 47 concurrent HTTP/2 streams "
        "on a single TCP connection. Stream 13 carries the exfil payload. "
        "Explain how multiplexing works, why stream 13 isn't blocked by "
        "stream 7's slow response, and what changes with HTTP/3.'[/bold white]"
    ),
    "tls_certificates": (
        "[bold red]BOSS CHALLENGE — CERTIFICATE FORGERY DETECTION[/bold red]\n\n"
        "[bold white]CIPHER: 'A client connects with a certificate claiming CN=node-07.nexus.internal, "
        "signed by an intermediate CA we don't recognize. Walk me through "
        "the verification chain, how to check OCSP revocation status, and "
        "what mTLS enforcement should have caught.'[/bold white]"
    ),
    "load_balancing_adv": (
        "[bold red]BOSS CHALLENGE — FAILOVER STORM[/bold red]\n\n"
        "[bold white]CIPHER: 'The GSLB just failed over traffic from EU to US-EAST, "
        "but the L7 load balancer is returning 503 on 40% of requests. "
        "Health checks pass. Sticky sessions are breaking. "
        "Diagnose the cascade failure and design the remediation.'[/bold white]"
    ),
    "network_debugging": (
        "[bold red]BOSS CHALLENGE — INVISIBLE EXFIL[/bold red]\n\n"
        "[bold white]CIPHER: 'Outbound traffic to 198.51.100.23:443 spikes every 6 hours. "
        "Standard packet capture shows normal TLS. DNS resolves clean. "
        "But something is leaking. Use every tool in your arsenal — "
        "tcpdump filters, Wireshark, dig, ss, eBPF — to find the channel "
        "and prove what data is leaving.'[/bold white]"
    ),
}
