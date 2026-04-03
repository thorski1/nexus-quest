"""
Message Queues skill pack — The Signal Highway
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

SKILL_PACK = SkillPack(
    id="message_queues",
    title="The Signal Highway",
    subtitle="◈  Route the Signals Through the Grid  ◈",
    save_file_name="message_queues_quest",
    intro_story=INTRO_STORY,
    quit_message="The queues persist... messages will wait.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "messaging_fundamentals": "signal_initiate",
        "rabbitmq": "rabbit_wrangler",
        "apache_kafka": "stream_rider",
        "cloud_messaging": "cloud_courier",
        "patterns_best_practices": "pattern_master",
    },
    achievements={
        "signal_initiate": ("Signal Initiate", "Mastered messaging fundamentals"),
        "rabbit_wrangler": ("Rabbit Wrangler", "Conquered RabbitMQ exchanges and queues"),
        "stream_rider": ("Stream Rider", "Navigated Kafka partitions and consumer groups"),
        "cloud_courier": ("Cloud Courier", "Deployed cloud messaging across providers"),
        "pattern_master": ("Pattern Master", "Applied advanced messaging patterns in production"),
    },
    kids_mode=False,
    level_titles=[
        (1, "Listener"),
        (6, "Publisher"),
        (11, "Broker"),
        (16, "Architect"),
        (21, "Signal Master"),
        (26, "Grid Sovereign"),
    ],
)
