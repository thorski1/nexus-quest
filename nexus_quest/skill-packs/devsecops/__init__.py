"""
DevSecOps skill pack — The Security Pipeline
Secure the pipeline from first commit to runtime: shift-left testing,
secret management, supply chain verification, runtime detection, and
compliance automation.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___  _____   _____ ___ ___ ___  ___  ___
|   \| __\ \ / / __| __/ __/ _ \| _ \/ __|
| |) | _| \ V /\__ \ _| (_| (_) |  _/\__ \
|___/|___| \_/ |___/___\___\___/|_|  |___/
"""

SKILL_PACK = SkillPack(
    id="devsecops",
    title="The Security Pipeline",
    subtitle="◈  Secure the Pipeline, Secure the Product  ◈",
    save_file_name="devsecops_quest",
    intro_story=INTRO_STORY,
    quit_message="Pipeline paused. Security state persisted. Resume when ready, operative.",
    name_prompt="[bold red]Operative handle:[/bold red]",
    default_player_name="Operative",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "shift_left_security":    "shift_left_sentinel",
        "secret_management":      "vault_keeper",
        "supply_chain_security":  "chain_verifier",
        "runtime_security":       "runtime_guardian",
        "compliance_as_code":     "compliance_automator",
    },
    achievements={
        "shift_left_sentinel":  ("Shift-Left Sentinel",  "Integrated SAST, DAST, and SCA into every pipeline — vulnerabilities die at the source."),
        "vault_keeper":         ("Vault Keeper",         "Mastered secret management: Vault, sealed secrets, rotation, and zero-trust credential delivery."),
        "chain_verifier":       ("Chain Verifier",       "Secured the supply chain: SBOMs, Sigstore signatures, SLSA provenance, and admission control."),
        "runtime_guardian":     ("Runtime Guardian",     "Deployed runtime defenses: Falco, eBPF, network policies, and pod security standards."),
        "compliance_automator": ("Compliance Automator", "Codified compliance: CIS benchmarks, SOC 2 controls, and HIPAA safeguards — all automated."),
        "no_hints":             ("Zero Trust",           "Completed a zone without any hints."),
        "speed_reader":         ("Rapid Pipeline",       "Answered a challenge in under 10 seconds."),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1,  "Junior SecEng"),
        (6,  "Security Engineer"),
        (11, "DevSecOps Engineer"),
        (16, "Security Architect"),
        (21, "Principal SecArch"),
        (26, "CISO"),
    ],
)
