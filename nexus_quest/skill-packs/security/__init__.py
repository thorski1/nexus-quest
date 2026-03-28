"""
Security skill pack — Security Ops
Defend the digital fortress: CIA triad, authentication, encryption,
web security, containers, cloud, incident response, and security culture.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ ___ ___ _   _ ___ ___ _______   __
 / __| __/ __| | | | _ \_ _|_   _\ \ / /
 \__ \ _| (__| |_| |   /| |  | |  \   /
 |___/___\___|\___/|_|_\___| |_|   |_|
"""

SKILL_PACK = SkillPack(
    id="security",
    title="Security Ops",
    subtitle="◈  Defend the Digital Fortress  ◈",
    save_file_name="security_quest",
    intro_story=INTRO_STORY,
    quit_message="Perimeter secured. Session state encrypted and cached. Resume when ready.",
    name_prompt="[bold red]Operative handle:[/bold red]",
    default_player_name="Operative",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "security_fundamentals": "foundation_builder",
        "authentication":        "gatekeeper",
        "encryption":            "cipher_master",
        "web_security":          "surface_hardener",
        "container_security":    "vault_sealer",
        "cloud_security":        "cloud_sentinel",
        "incident_response":     "first_responder",
        "security_culture":      "culture_architect",
    },
    achievements={
        "foundation_builder": ("Foundation Builder", "Mastered the CIA triad, threat models, and defense in depth."),
        "gatekeeper":         ("Gatekeeper",         "Secured authentication: hashing, MFA, OAuth2, JWTs, and sessions."),
        "cipher_master":      ("Cipher Master",      "Commanded symmetric, asymmetric, TLS, PKI, and forward secrecy."),
        "surface_hardener":   ("Surface Hardener",   "Mitigated the OWASP Top 10: XSS, CSRF, SQLi, CORS, and CSP."),
        "vault_sealer":       ("Vault Sealer",       "Locked down containers: images, privileges, secrets, supply chain."),
        "cloud_sentinel":     ("Cloud Sentinel",     "Secured the cloud perimeter: IAM, security groups, logging, S3."),
        "first_responder":    ("First Responder",    "Executed incident response: detection through post-mortem."),
        "culture_architect":  ("Culture Architect",  "Built security into the SDLC: DevSecOps, shift-left, champions."),
        "no_hints":           ("Zero Trust",         "Completed a zone without any hints."),
        "speed_reader":       ("Rapid Response",     "Answered a challenge in under 10 seconds."),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1,  "Scout"),
        (6,  "Analyst"),
        (11, "Engineer"),
        (16, "Architect"),
        (21, "Guardian"),
        (26, "CISO"),
    ],
)
