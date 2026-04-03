"""
Auth skill pack — The Identity Matrix
Passwords, sessions, OAuth, API auth, and Zero Trust —
master every layer of authentication and identity verification.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _____ _   _ _____   ___ ____  _____ _   _ _____ ___ _______   __
 |_   _| | | | ____| |_ _|  _ \| ____| \ | |_   _|_ _|_   _\ \ / /
   | | | |_| |  _|    | || | | |  _| |  \| | | |  | |  | |  \   /
   | | |  _  | |___   | || |_| | |___| |\  | | |  | |  | |   | |
   |_| |_| |_|_____| |___|____/|_____|_| \_| |_| |___| |_|   |_|
  __  __    _  _____ ____  _____  __
 |  \/  |  / \|_   _|  _ \|_ _\ \/ /
 | |\/| | / _ \ | | | |_) || | \  /
 | |  | |/ ___ \| | |  _ < | | /  \
 |_|  |_/_/   \_\_| |_| \_\___/_/\_\
"""

SKILL_PACK = SkillPack(
    id="auth",
    title="The Identity Matrix",
    subtitle="◈  Master Every Layer of Identity  ◈",
    save_file_name="auth_quest",
    intro_story=INTRO_STORY,
    quit_message="Identity perimeter sealed. Session state encrypted and cached. Resume when ready.",
    name_prompt="[bold red]Operative handle:[/bold red]",
    default_player_name="Operative",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "authentication_basics":  "gate_builder",
        "session_management":     "session_warden",
        "oauth2_oidc":            "trust_broker",
        "api_authentication":     "machine_sentinel",
        "zero_trust_modern_auth": "identity_architect",
    },
    achievements={
        "gate_builder":       ("Gate Builder",        "Mastered password hashing, salting, bcrypt, and credential security."),
        "session_warden":     ("Session Warden",      "Secured cookies, JWTs, refresh tokens, and CSRF defenses."),
        "trust_broker":       ("Trust Broker",        "Commanded OAuth 2.0, PKCE, OpenID Connect, and token validation."),
        "machine_sentinel":   ("Machine Sentinel",    "Locked down API keys, bearer tokens, mTLS, and HMAC signatures."),
        "identity_architect": ("Identity Architect",  "Deployed Zero Trust, passkeys, FIDO2, SSO, and modern MFA."),
        "no_hints":           ("Zero Knowledge",      "Completed a zone without any hints."),
        "speed_reader":       ("Rapid Auth",          "Answered a challenge in under 10 seconds."),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1,  "Intern"),
        (6,  "Analyst"),
        (11, "Engineer"),
        (16, "Architect"),
        (21, "Principal"),
        (26, "CISO"),
    ],
)
