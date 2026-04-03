"""
story.py — Narrative for The Identity Matrix (auth skill pack).
Theme: Identity is the new perimeter. Every gate needs a gatekeeper who can't be fooled.
"""

INTRO_STORY = """
[bold red]NEXUS TERMINAL — IDENTITY OPERATIONS DIVISION[/bold red]

The breach vector was elegant in its simplicity. A service account with a
hardcoded API key — committed to a public repository eighteen months ago.
No rotation. No MFA. No scope limits. One key unlocked everything.

NEXUS didn't hack the system. NEXUS logged in.

CIPHER's voice cuts through the static: [bold cyan]"They didn't pick the lock.
They walked through the front door wearing a badge nobody thought to revoke.
A badge that granted access to every room in the building — because nobody
scoped the permissions. A badge that never expired — because nobody built
a rotation policy."[/bold cyan]

Your identity dashboard is a graveyard of bad decisions. Passwords hashed
with MD5. Session tokens that live forever. OAuth scopes set to wildcard.
JWTs signed with 'none'. API keys in environment variables committed to
version control. A SAML assertion that nobody validates.

[bold white]"Identity was supposed to be the perimeter."[/bold white]

[bold cyan]"It still is. But a perimeter only works if the gates are real.
Passwords, sessions, tokens, certificates, passkeys — every layer of
identity verification you'll learn here is a gate. Your job is to make
sure none of them can be walked through, forged, or replayed."[/bold cyan]

A pause. Then: [bold cyan]"Authentication isn't a checkbox. It's a discipline.
And right now, every identity in this system is compromised until you
prove otherwise."[/bold cyan]

[italic]Initializing identity operations framework... 5 sectors to secure.[/italic]
"""

ZONE_INTROS = {
    "authentication_basics": (
        "[bold cyan]ZONE 1 — THE FRONT GATE[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The breach database contained 2.3 million passwords. "
        "Fourteen percent were stored in plaintext. Another thirty percent were "
        "unsalted MD5 — cracked in under an hour with a consumer GPU. The remaining "
        "passwords used SHA-256 without a salt — rainbow tables handled those in a "
        "day. Not one used bcrypt. Not one used Argon2. Start at the foundation: "
        "how passwords should be stored, why hashing isn't enough without salting, "
        "and why speed is the enemy when it comes to password security.'[/bold white]"
    ),
    "session_management": (
        "[bold cyan]ZONE 2 — THE SESSION VAULT[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The stolen session token was a JWT with no expiration "
        "claim. It had been valid for eleven months. Eleven months of unrestricted "
        "access from a single authentication event. The cookie had no Secure flag — "
        "intercepted on a coffee shop network. No HttpOnly flag — exfiltrated by "
        "an XSS payload in a comment field. Session management is the bridge between "
        "a single login and continuous access. Cookies, JWTs, refresh tokens, CSRF "
        "protection — if you get sessions wrong, authentication is meaningless.'[/bold white]"
    ),
    "oauth2_oidc": (
        "[bold cyan]ZONE 3 — THE TRUST BROKER[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The third-party integration used the Implicit flow. "
        "Access tokens in URL fragments. Logged by the CDN. Cached by the browser. "
        "Leaked via Referer headers to an analytics provider. NEXUS didn't even "
        "need to intercept traffic — the tokens were already in the logs. OAuth 2.0 "
        "is a delegation framework, not an identity protocol — until you add OpenID "
        "Connect. Flows, scopes, PKCE, ID tokens — the trust broker only works "
        "when every party validates every step.'[/bold white]"
    ),
    "api_authentication": (
        "[bold cyan]ZONE 4 — THE MACHINE GATE[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Humans aren't the only identities in your system. "
        "Service accounts, CI/CD pipelines, IoT devices, third-party integrations — "
        "machine identity is 45x the volume of human identity in a modern "
        "architecture. The leaked API key had no IP restriction, no rate limit, "
        "no expiration, and full administrative scope. API keys, bearer tokens, "
        "mutual TLS, HMAC signatures — machine authentication requires the same "
        "rigor as human authentication. More, actually — machines don't notice "
        "when they've been impersonated.'[/bold white]"
    ),
    "zero_trust_modern_auth": (
        "[bold cyan]ZONE 5 — THE IDENTITY NEXUS[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The old model was simple: inside the firewall, you're "
        "trusted. Outside, you're not. That model died the day the first employee "
        "worked from a coffee shop. Zero Trust means every request proves identity — "
        "every time, from everywhere. Passkeys replace passwords with cryptographic "
        "proof that can't be phished. FIDO2 binds credentials to origins. SSO "
        "centralizes identity. MFA layers factors. The future of authentication "
        "isn't about building higher walls — it's about making identity unforgeable.'[/bold white]"
    ),
}

ZONE_COMPLETIONS = {
    "authentication_basics": (
        "[bold green]ZONE CLEAR — THE FRONT GATE[/bold green]\n\n"
        "Plaintext is dead. MD5 is dead. SHA-256 without salt is dead. "
        "Bcrypt with a work factor of 12. Argon2id with memory-hardness. "
        "Unique salts per password. Rate limiting on login attempts. "
        "CIPHER: 'The front gate holds. No password in this system "
        "can be recovered from its hash in any attacker's lifetime.'"
    ),
    "session_management": (
        "[bold green]ZONE CLEAR — THE SESSION VAULT[/bold green]\n\n"
        "Cookies are Secure, HttpOnly, and SameSite. JWTs are short-lived "
        "and properly validated. Refresh tokens are rotatable and revocable. "
        "CSRF tokens protect every state-changing request. Sessions regenerate on login. "
        "CIPHER: 'The session vault is sealed. No token lives forever. "
        "No cookie crosses a boundary it shouldn't. No session survives hijacking.'"
    ),
    "oauth2_oidc": (
        "[bold green]ZONE CLEAR — THE TRUST BROKER[/bold green]\n\n"
        "Authorization Code + PKCE. Scoped tokens with the minimum necessary permissions. "
        "ID tokens validated: signature, issuer, audience, expiration. "
        "The Implicit flow is gone. Token exchange for downstream services. "
        "CIPHER: 'The trust broker is honest. Every delegation is scoped. "
        "Every identity is verified. Every token is validated end-to-end.'"
    ),
    "api_authentication": (
        "[bold green]ZONE CLEAR — THE MACHINE GATE[/bold green]\n\n"
        "API keys are scoped, rotated, and transmitted in headers. "
        "Bearer tokens are short-lived. mTLS authenticates both sides. "
        "HMAC signatures prove integrity and authenticity with replay protection. "
        "CIPHER: 'The machine gate holds. Every service proves its identity. "
        "Every request is signed. Every key has an expiration date.'"
    ),
    "zero_trust_modern_auth": (
        "[bold green]ZONE CLEAR — THE IDENTITY NEXUS[/bold green]\n\n"
        "Zero Trust is the architecture. Passkeys are the credential. "
        "FIDO2 is phishing-resistant. SSO centralizes the identity perimeter. "
        "MFA is layered and fatigue-resistant. Step-up protects sensitive operations. "
        "CIPHER: 'The Identity Matrix is complete. No password to phish. "
        "No token to replay. No session to hijack. Identity isn't a wall — "
        "it's a proof. And proof, unlike walls, doesn't crumble.'"
    ),
}

BOSS_INTROS = {
    "authentication_basics": (
        "[bold red]BOSS CHALLENGE — CREDENTIAL STORE AUDIT[/bold red]\n\n"
        "[bold white]CIPHER: 'A legacy system migration exposes a user table: "
        "40% plaintext, 30% unsalted MD5, 20% SHA-256 with a global salt, "
        "10% bcrypt cost 8. Design the migration strategy — what gets rehashed, "
        "in what order, and how do you handle users who haven't logged in "
        "for a year? Time is critical — the table is already exfiltrated.'[/bold white]"
    ),
    "session_management": (
        "[bold red]BOSS CHALLENGE — SESSION HIJACKING POST-MORTEM[/bold red]\n\n"
        "[bold white]CIPHER: 'An attacker stole a session cookie via XSS in a "
        "user comment field. The cookie had no HttpOnly flag. The session "
        "lasted 30 days with no rotation. The attacker accessed the account "
        "for 3 weeks before detection. Walk me through every failure "
        "and design the session architecture that prevents each one.'[/bold white]"
    ),
    "oauth2_oidc": (
        "[bold red]BOSS CHALLENGE — TOKEN LEAKAGE INVESTIGATION[/bold red]\n\n"
        "[bold white]CIPHER: 'Access tokens from your SPA are appearing in a "
        "third-party analytics provider's logs. The tokens have admin scope "
        "and 24-hour expiration. Trace the leakage path from the OAuth flow "
        "to the analytics logs. Then redesign the flow: which grant type, "
        "what scope, what token lifetime, and how do you prevent "
        "leakage to third-party scripts?'[/bold white]"
    ),
    "api_authentication": (
        "[bold red]BOSS CHALLENGE — API KEY ROTATION UNDER FIRE[/bold red]\n\n"
        "[bold white]CIPHER: 'A production API key was found in a public GitHub "
        "repository. It has admin scope across all services. The key has been "
        "public for 72 hours. You can't just revoke it — 14 services depend "
        "on it with no secondary authentication. Design the emergency response: "
        "contain the blast radius, rotate without downtime, and architect "
        "the system so this can never happen again.'[/bold white]"
    ),
    "zero_trust_modern_auth": (
        "[bold red]BOSS CHALLENGE — ZERO TRUST MIGRATION PLAN[/bold red]\n\n"
        "[bold white]CIPHER: 'A 200-person company uses VPN + LDAP passwords "
        "for everything. No MFA. No SSO. Session cookies live for 90 days. "
        "Service-to-service auth uses shared static credentials. "
        "Design the 6-month migration to Zero Trust: identity provider, "
        "MFA rollout, passkey adoption, service mesh with mTLS, "
        "and step-up authentication for sensitive operations. "
        "What's week 1? What's month 6? Prioritize by risk.'[/bold white]"
    ),
}
