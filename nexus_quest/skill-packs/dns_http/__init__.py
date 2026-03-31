"""
DNS & HTTP Deep Dive skill pack — Protocol Deep Dive
Master the full protocol stack: DNS resolution, record types, DNSSEC,
HTTP/2, HTTP/3, TLS, caching headers, and wire-level debugging.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___  _  _ ___    ___   _  _ _____ _____ ___
 |   \| \| / __|  / / | | ||_   _|_   _| _ \
 | |) | .` \__ \ / /| |_| |  | |   | | |  _/
 |___/|_|\_|___//_/  |___|_|  |_|   |_| |_|
"""

SKILL_PACK = SkillPack(
    id="dns_http",
    title="Protocol Deep Dive",
    subtitle="◈  Understand Every Hop  ◈",
    save_file_name="dns_http_quest",
    intro_story=INTRO_STORY,
    quit_message="Connection closed. Protocol state cached. Resume when ready.",
    name_prompt="[bold red]Operative handle:[/bold red]",
    default_player_name="Operative",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "dns_resolution":   "chain_tracer",
        "dns_records_deep": "record_keeper",
        "dns_security":     "integrity_guard",
        "http2_http3":      "stream_analyst",
        "tls_deep":         "cert_forensic",
        "caching_headers":  "cache_master",
        "debugging_http":   "wire_reader",
    },
    achievements={
        "chain_tracer":   ("Chain Tracer",     "Traced the full DNS resolution chain from stub resolver to authoritative answer."),
        "record_keeper":  ("Record Keeper",    "Decoded every DNS record type — A, AAAA, CNAME, MX, NS, TXT, SRV, SOA, PTR."),
        "integrity_guard":("Integrity Guard",  "Mastered DNSSEC, DoH, DoT, and DNS poisoning defense."),
        "stream_analyst": ("Stream Analyst",   "Decoded HTTP/2 multiplexing, QUIC, and 0-RTT connection establishment."),
        "cert_forensic":  ("Cert Forensic",    "Analyzed TLS certificate chains, OCSP, HSTS, and mutual TLS."),
        "cache_master":   ("Cache Master",     "Controlled the caching layer — Cache-Control, ETags, Vary, and CDN invalidation."),
        "wire_reader":    ("Wire Reader",      "Inspected every byte on the wire with curl, httpie, DevTools, and Wireshark."),
        "no_hints":       ("Dark Route",       "Completed a zone without any hints."),
        "speed_reader":   ("Speed of Light",   "Answered a challenge in under 10 seconds."),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1,  "Packet"),
        (6,  "Request"),
        (11, "Connection"),
        (16, "Protocol"),
        (21, "RFC Author"),
        (26, "Vint Cerf"),
    ],
)
