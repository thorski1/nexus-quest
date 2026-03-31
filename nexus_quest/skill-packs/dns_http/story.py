"""
story.py — Narrative for Protocol Deep Dive (dns_http skill pack).
Theme: Every click starts a chain reaction across the internet. Understand every hop.
"""

INTRO_STORY = """
[bold red]NEXUS TERMINAL — PROTOCOL FORENSICS DIVISION[/bold red]

The intercepted traffic logs are 40 gigabytes of raw packet captures.
NEXUS routed their exfiltration through seven DNS rebinding hops,
TLS-encrypted tunnels with pinned certificates, and HTTP/2 multiplexed
streams disguised as CDN prefetch traffic.

CIPHER pulls up a packet trace: [bold cyan]"Look at this. A single click on a
compromised internal wiki page triggers 47 DNS queries, 12 TLS handshakes,
and 200 HTTP/2 frames — all in under 800 milliseconds. NEXUS embedded
their command channel inside legitimate protocol behavior."[/bold cyan]

The trace scrolls: stub resolver to recursive resolver to root to TLD
to authoritative — and then a CNAME chain four aliases deep, each with
a 30-second TTL. The final target rotates every minute.

[bold white]"They're using the protocol stack as camouflage."[/bold white]

[bold cyan]"Exactly. DNS resolution, record types, DNSSEC validation, HTTP/2
multiplexing, TLS certificate chains, caching headers — every layer of
the protocol stack is a potential hiding place. And NEXUS knows every
layer better than most engineers."[/bold cyan]

A pause. Then: [bold cyan]"Every click starts a chain reaction across the internet.
If you want to find NEXUS in the noise, you need to understand every hop.
From the first DNS query to the last byte of the HTTP response. Every.
Single. Hop."[/bold cyan]

[italic]Resolving nexus-c2.ephemeral.link... CNAME → CNAME → CNAME → A 198.51.100.∎∎[/italic]
"""

ZONE_INTROS = {
    "dns_resolution": (
        "[bold cyan]ZONE 1 — THE RESOLUTION CHAIN[/bold cyan]\n\n"
        "[bold white]CIPHER: 'A single domain lookup touches four different server types "
        "before you get an IP address. Stub resolver, recursive resolver, root nameserver, "
        "TLD, authoritative. NEXUS hid a rogue hop in this chain — a poisoned cache entry "
        "at the recursive resolver that redirects the last step. You need to understand "
        "every link to find where the chain was broken.'[/bold white]"
    ),
    "dns_records_deep": (
        "[bold cyan]ZONE 2 — THE RECORD VAULT[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The zone file for their shadow domain has 14 record types. "
        "A, AAAA, CNAME chains, MX pointing to a mail relay in a non-cooperating jurisdiction, "
        "SRV records for their C2 service discovery, TXT records carrying base64-encoded "
        "configuration payloads. If you can't read every record type, you're reading "
        "the zone file with one eye closed.'[/bold white]"
    ),
    "dns_security": (
        "[bold cyan]ZONE 3 — THE INTEGRITY LAYER[/bold cyan]\n\n"
        "[bold white]CIPHER: 'NEXUS disabled DNSSEC validation on the internal resolver — "
        "that's how the cache poisoning worked. No signature verification means any forged "
        "response gets accepted. Meanwhile, their own C2 queries go through DNS-over-HTTPS "
        "to Cloudflare — encrypted, authenticated, invisible to our network monitoring. "
        "You need to understand both the defenses and the attack vectors.'[/bold white]"
    ),
    "http2_http3": (
        "[bold cyan]ZONE 4 — THE NEXT PROTOCOL[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The exfil channel uses HTTP/2 multiplexing to blend C2 commands "
        "with legitimate API traffic — 200 streams on one connection, and only three of them "
        "carry NEXUS data. The new backup channel? HTTP/3 over QUIC with 0-RTT resumption — "
        "the connection is established before we even see the handshake. "
        "You need to understand the protocol evolution to spot what doesn't belong.'[/bold white]"
    ),
    "tls_deep": (
        "[bold cyan]ZONE 5 — THE CERTIFICATE CHAIN[/bold cyan]\n\n"
        "[bold white]CIPHER: 'NEXUS got a valid TLS certificate for their C2 domain through "
        "Let's Encrypt — automated, free, and legitimate-looking. The certificate chain "
        "validates perfectly. They've even set up OCSP stapling and HSTS. From the outside, "
        "it looks like a model HTTPS deployment. The trust infrastructure of the web "
        "is working exactly as designed — and that's the problem.'[/bold white]"
    ),
    "caching_headers": (
        "[bold cyan]ZONE 6 — THE CACHE BOUNDARY[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The C2 responses come with Cache-Control: no-store — NEXUS "
        "doesn't want their commands cached anywhere. But the exfiltrated data? "
        "max-age=31536000 with content-hashed URLs. They're abusing CDN caching to "
        "distribute stolen data globally. Understanding cache headers isn't just about "
        "performance — it's about knowing where data lives and for how long.'[/bold white]"
    ),
    "debugging_http": (
        "[bold cyan]ZONE 7 — THE WIRE INSPECTOR[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Theory time is over. Now you need the tools. curl -v to replay "
        "the exact requests. Wireshark to inspect the raw frames. DevTools to trace the "
        "waterfall. httpie for rapid API probing. These are your instruments — "
        "and NEXUS's traffic is the specimen on the table. Read every header, "
        "every timing phase, every TLS parameter. The wire doesn't lie.'[/bold white]"
    ),
}

ZONE_COMPLETIONS = {
    "dns_resolution": (
        "[bold green]ZONE CLEAR — THE RESOLUTION CHAIN[/bold green]\n\n"
        "Stub to recursive to root to TLD to authoritative — the full chain is mapped. "
        "You found the poisoned cache entry at the recursive layer: a forged A record "
        "with a 30-second TTL, refreshed by a script before it expires. "
        "CIPHER: 'Good. You can trace a DNS query from the first syscall to the final answer.'"
    ),
    "dns_records_deep": (
        "[bold green]ZONE CLEAR — THE RECORD VAULT[/bold green]\n\n"
        "A, AAAA, CNAME, MX, NS, TXT, SRV, SOA, PTR — every record type decoded. "
        "The shadow zone file is an open book now. "
        "CIPHER: 'The SRV records gave us the C2 service ports. The TXT records "
        "contained their configuration data in base64. You just read their playbook.'"
    ),
    "dns_security": (
        "[bold green]ZONE CLEAR — THE INTEGRITY LAYER[/bold green]\n\n"
        "DNSSEC, DoH, DoT, poisoning vectors, split-horizon — you know the attack "
        "surface and the defenses. "
        "CIPHER: 'We've re-enabled DNSSEC validation and deployed DoT for internal resolvers. "
        "NEXUS can't poison the cache anymore. Their encrypted C2 channel is identified. "
        "The integrity layer holds.'"
    ),
    "http2_http3": (
        "[bold green]ZONE CLEAR — THE NEXT PROTOCOL[/bold green]\n\n"
        "Multiplexing, HPACK, server push, QUIC, 0-RTT — the modern protocol stack decoded. "
        "CIPHER: 'You identified the three rogue HTTP/2 streams in a connection carrying 200. "
        "Stream IDs 47, 113, and 201 — all carrying binary payloads to the C2 endpoint. "
        "The QUIC backup channel is flagged. Protocol camouflage no longer works.'"
    ),
    "tls_deep": (
        "[bold green]ZONE CLEAR — THE CERTIFICATE CHAIN[/bold green]\n\n"
        "Certificate chains, OCSP, HSTS, pinning, Let's Encrypt, mTLS — "
        "the trust infrastructure is transparent. "
        "CIPHER: 'The C2 certificate was issued 72 hours ago via ACME HTTP-01 challenge. "
        "We've submitted a revocation request. Their OCSP response will show revoked "
        "within the hour. The chain of trust works — when we use it.'"
    ),
    "caching_headers": (
        "[bold green]ZONE CLEAR — THE CACHE BOUNDARY[/bold green]\n\n"
        "Cache-Control, ETags, Vary, stale-while-revalidate, CDN invalidation — "
        "you own the caching layer. "
        "CIPHER: 'The CDN-cached exfil payloads have been identified across 14 edge nodes. "
        "Content-hashed filenames made them look like static assets. "
        "Purge requests sent. The cache boundary is secured.'"
    ),
    "debugging_http": (
        "[bold green]ZONE CLEAR — THE WIRE INSPECTOR[/bold green]\n\n"
        "curl, httpie, DevTools, Wireshark — every tool in the diagnostic kit is sharp. "
        "CIPHER: 'You just replayed the full C2 conversation with curl -v, captured the "
        "raw frames in Wireshark, and mapped every timing phase in the DevTools waterfall. "
        "Every hop from DNS query to HTTP response body — visible. "
        "NEXUS has nowhere left to hide in the protocol stack.'"
    ),
}

BOSS_INTROS = {
    "dns_resolution": (
        "[bold red]BOSS CHALLENGE — FULL CHAIN TRACE[/bold red]\n\n"
        "[bold white]CIPHER: 'A user reports that internal.corp.example.com resolves to "
        "an IP outside our infrastructure. Walk me through the complete resolution chain, "
        "identify at which layer the poisoning occurred, and explain how the TTL was "
        "used to maintain persistence.'[/bold white]"
    ),
    "dns_records_deep": (
        "[bold red]BOSS CHALLENGE — ZONE FILE ANALYSIS[/bold red]\n\n"
        "[bold white]CIPHER: 'I'm showing you the full zone file for NEXUS's shadow domain. "
        "Fourteen records. Identify the purpose of each one — A, AAAA, CNAME chain, "
        "MX relay, SRV service discovery, TXT config payload. "
        "Read the zone file like a blueprint.'[/bold white]"
    ),
    "dns_security": (
        "[bold red]BOSS CHALLENGE — ATTACK VECTOR IDENTIFICATION[/bold red]\n\n"
        "[bold white]CIPHER: 'Three DNS security failures enabled the breach: "
        "disabled DNSSEC validation, unencrypted resolver traffic, and a split-horizon "
        "misconfiguration. For each one, explain the attack it enabled and "
        "the remediation. This is your security audit.'[/bold white]"
    ),
    "http2_http3": (
        "[bold red]BOSS CHALLENGE — STREAM IDENTIFICATION[/bold red]\n\n"
        "[bold white]CIPHER: 'An HTTP/2 connection carries 200 active streams. "
        "Three are C2 channels. Given the frame headers, stream priorities, "
        "and payload patterns, identify the rogue streams and explain "
        "why QUIC 0-RTT makes the backup channel harder to detect.'[/bold white]"
    ),
    "tls_deep": (
        "[bold red]BOSS CHALLENGE — CERTIFICATE FORENSICS[/bold red]\n\n"
        "[bold white]CIPHER: 'The C2 server presents a valid certificate chain: "
        "leaf signed by R3, R3 signed by ISRG Root X1. The certificate was issued "
        "via ACME HTTP-01 72 hours ago. Design the revocation strategy: "
        "OCSP, CRL, CT log monitoring. How do we ensure no client trusts "
        "this certificate by tomorrow?'[/bold white]"
    ),
    "caching_headers": (
        "[bold red]BOSS CHALLENGE — CACHE PURGE OPERATION[/bold red]\n\n"
        "[bold white]CIPHER: 'Stolen data is cached across 14 CDN edge nodes as "
        "content-hashed static assets with max-age=31536000. The CDN purge API "
        "has a 15-minute propagation delay. Design the full remediation: "
        "purge strategy, origin changes, header updates to prevent re-caching. "
        "Every cached copy must be gone.'[/bold white]"
    ),
    "debugging_http": (
        "[bold red]BOSS CHALLENGE — FULL PROTOCOL REPLAY[/bold red]\n\n"
        "[bold white]CIPHER: 'Using only curl and Wireshark, replay the full C2 conversation: "
        "DNS resolution, TLS handshake, HTTP/2 request with custom headers, "
        "response analysis. Show me every command, every flag, every filter. "
        "This is the final test — read the wire from first query to last byte.'[/bold white]"
    ),
}
