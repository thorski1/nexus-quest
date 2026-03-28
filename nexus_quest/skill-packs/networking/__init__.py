"""
Networking skill pack — Network Ops
Master the protocols that connect everything: OSI, TCP/IP, DNS, HTTP,
IP addressing, firewalls, load balancing, and troubleshooting.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _  _ ___ _____      _____  ___ _  __
 | \| | __|_   _|\ \/\ / / _ \| _ \ |/ /
 | .` | _|  | |   \    /| (_) |   / ' <
 |_|\_|___| |_|    \_/\_/ \___/|_|_\_|\_\
"""

SKILL_PACK = SkillPack(
    id="networking",
    title="Network Ops",
    subtitle="◈  Master the Protocols That Connect Everything  ◈",
    save_file_name="networking_quest",
    intro_story=INTRO_STORY,
    quit_message="Connection terminated. Packet state cached. Resume when ready.",
    name_prompt="[bold red]Operative handle:[/bold red]",
    default_player_name="Operative",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "osi_model":               "layer_mapper",
        "tcp_ip":                  "transport_analyst",
        "dns":                     "name_resolver",
        "http":                    "protocol_reader",
        "ip_addressing":           "subnet_architect",
        "firewalls_and_security":  "perimeter_guard",
        "load_balancing":          "traffic_controller",
        "troubleshooting":         "wire_tracer",
    },
    achievements={
        "layer_mapper":       ("Layer Mapper",       "Mapped all seven OSI layers and their protocols."),
        "transport_analyst":  ("Transport Analyst",  "Mastered TCP, UDP, handshakes, and connection states."),
        "name_resolver":      ("Name Resolver",      "Traced DNS resolution chains and decoded every record type."),
        "protocol_reader":    ("Protocol Reader",    "Read HTTP methods, status codes, and TLS like a language."),
        "subnet_architect":   ("Subnet Architect",   "Carved address space with CIDR, mapped NAT, and calculated subnets."),
        "perimeter_guard":    ("Perimeter Guard",    "Audited firewalls, security groups, and WAF rules."),
        "traffic_controller": ("Traffic Controller", "Mastered load balancing algorithms, health checks, and CDNs."),
        "wire_tracer":        ("Wire Tracer",        "Traced the full network path with ping, tcpdump, and curl."),
        "no_hints":           ("Dark Route",         "Completed a zone without any hints."),
        "speed_reader":       ("Speed of Light",     "Answered a challenge in under 10 seconds."),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1,  "Packet"),
        (6,  "Switch"),
        (11, "Router"),
        (16, "Firewall"),
        (21, "Architect"),
        (26, "NetMaster"),
    ],
)
