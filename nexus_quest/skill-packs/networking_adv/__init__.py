"""
Advanced Networking skill pack — The Network Core
Deep protocol internals: TCP congestion control, HTTP/2-3 multiplexing,
TLS certificate chains, advanced load balancing, and network debugging.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _  _ ___ _____    ___ ___  ___ ___
 | \| | __|_   _|  / __/ _ \| _ \ __|
 | .` | _|  | |   | (_| (_) |   / _|
 |_|\_|___| |_|    \___\___/|_|_\___|
"""

SKILL_PACK = SkillPack(
    id="networking_adv",
    title="The Network Core",
    subtitle="◈  Deep Protocol Internals — Where the Real Tradecraft Lives  ◈",
    save_file_name="networking_adv_quest",
    intro_story=INTRO_STORY,
    quit_message="QUIC connection closed. Session state encrypted and cached. Resume when ready.",
    name_prompt="[bold red]Core operator handle:[/bold red]",
    default_player_name="Operator",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "tcp_deep_dive":       "congestion_master",
        "http2_http3":         "stream_analyst",
        "tls_certificates":    "cert_authority",
        "load_balancing_adv":  "traffic_engineer",
        "network_debugging":   "packet_surgeon",
    },
    achievements={
        "congestion_master":  ("Congestion Master",  "Mastered TCP internals: congestion windows, SACK, keepalive, and fast retransmit."),
        "stream_analyst":     ("Stream Analyst",     "Decoded HTTP/2 multiplexing, HPACK compression, QUIC transport, and 0-RTT."),
        "cert_authority":     ("Cert Authority",     "Traced certificate chains, cipher suites, OCSP stapling, and mTLS."),
        "traffic_engineer":   ("Traffic Engineer",   "Engineered L4/L7 load balancing, GSLB, consistent hashing, and DSR."),
        "packet_surgeon":     ("Packet Surgeon",     "Dissected traffic with tcpdump, Wireshark, dig, ss, and eBPF."),
        "no_hints":           ("Dark Tunnel",        "Completed a zone without any hints."),
        "speed_reader":       ("Zero-RTT",           "Answered a challenge in under 10 seconds."),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1,  "Segment"),
        (6,  "Stream"),
        (11, "Cipher"),
        (16, "Balancer"),
        (21, "Surgeon"),
        (26, "Core Master"),
    ],
)
