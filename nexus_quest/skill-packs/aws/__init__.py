"""
AWS skill pack — The Cloud Layer
IAM, EC2, S3, VPC, RDS, and Lambda.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  __ ___      ____
 / _` \ \ /\ / /\ \
| (_| |\ V  V /  > >
 \__,_| \_/\_/  /_/
"""

SKILL_PACK = SkillPack(
    id="aws",
    title="The Cloud Layer",
    subtitle="◈  Navigate the AWS Infrastructure Behind the Fraud  ◈",
    save_file_name="aws_quest",
    intro_story=INTRO_STORY,
    quit_message="The AWS session is suspended. Credentials cached.",
    name_prompt="[bold red]Operative handle:[/bold red]",
    default_player_name="Operative",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "iam_and_security": "identity_mapper",
        "ec2_and_compute": "fleet_analyst",
        "s3_and_storage": "bucket_inspector",
        "vpc_and_networking": "network_cartographer",
        "rds_and_databases": "archive_extractor",
        "lambda_and_serverless": "function_forensics",
        "cloudwatch_and_monitoring": "signal_analyst",
        "cloudformation_and_iac": "blueprint_reader",
        "ecs_and_containers": "container_investigator",
        "elb_and_autoscaling": "load_balancer_ace",
        "route53_and_cdn": "edge_navigator",
    },
    achievements={
        "identity_mapper": ("Identity Mapper", "Mapped the IAM misconfiguration chain!"),
        "fleet_analyst": ("Fleet Analyst", "Investigated the undeclared EC2 instances!"),
        "bucket_inspector": ("Bucket Inspector", "Recovered versioned S3 evidence!"),
        "network_cartographer": ("Network Cartographer", "Traced the VPC backdoor!"),
        "archive_extractor": ("Archive Extractor", "Restored the primary financial database!"),
        "function_forensics": ("Function Forensics", "Traced the Lambda money-movement trail!"),
        "signal_analyst": ("Signal Analyst", "Reconstructed the fraud timeline from CloudWatch logs!"),
        "blueprint_reader": ("Blueprint Reader", "Found the evidence trail in CloudFormation drift!"),
        "container_investigator": ("Container Investigator", "Followed the ECS task roles to the source!"),
        "load_balancer_ace": ("Load Balancer Ace", "Mastered ALB routing and Auto Scaling groups!"),
        "edge_navigator": ("Edge Navigator", "Mapped the Route 53 DNS and CloudFront CDN layer!"),
        "no_hints": ("Ghost Protocol", "Completed a zone without any hints!"),
        "speed_reader": ("Neural Spike", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1, "Rookie"),
        (6, "Analyst"),
        (11, "Operator"),
        (16, "Specialist"),
        (21, "Expert"),
        (26, "Specter"),
    ],
)
