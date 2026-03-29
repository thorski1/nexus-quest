"""
story.py - Narrative text for API Forge
Theme: APIs are the contracts between systems. A rogue API gateway is leaking
       data across the corporate mesh. You're the API Architect brought in to
       audit, redesign, and lock down every interface.
"""

INTRO_STORY = """
The incident report landed at [bold cyan]2:47 AM[/bold cyan].

[bold white]Three hundred microservices.[/bold white] Communicating through a mesh of REST endpoints,
GraphQL resolvers, and undocumented internal APIs that nobody mapped. The breach
didn't come through the firewall. It came through an API — a public endpoint with
no rate limiting, no authentication, and a response body that included fields
the frontend never used but the attacker certainly did.

Over-fetching. The API returned everything. The attacker only needed the email
addresses and internal account IDs. They were right there in the JSON, in every
response, because nobody had designed the contract — they'd just exposed the
database and called it an API.

[bold white]You are an API Architect.[/bold white]

[bold magenta]Independent contractor. Interface forensics. You've audited API surfaces for
corps that thought "we have endpoints" meant "we have an API strategy." It doesn't.
An API is a contract. A contract requires design, documentation, versioning,
authentication, and testing. Without those, it's just a hole in the wall
with a JSON response.[/bold magenta]

You've been given access to the full API surface: endpoint manifests, OpenAPI specs
(where they exist), authentication configs, rate limit policies, and the GraphQL
schema that serves the mobile clients. Your job: audit every interface, identify
every design failure, and rebuild the contracts from the ground up.

The engineering leads are watching your recommendations.
Every design decision you make will be reviewed.

[bold cyan]The API surface is live. The contracts are waiting. Start with the fundamentals.[/bold cyan]
"""

ZONE_INTROS = {
    "rest_fundamentals": """
[bold cyan]== THE REST PROTOCOL ==[/bold cyan]

Every API audit starts here — with the fundamentals.

Before you can evaluate whether an API is well-designed, you need to understand
the principles it should follow. REST is not a protocol. It's an architectural
style — a set of constraints that, when followed, produce APIs that are
predictable, scalable, and cacheable.

Resources. HTTP methods. Status codes. Statelessness. Idempotency.
These aren't academic concepts. They're the difference between an API that
scales to a million clients and one that breaks at a hundred.

[yellow]GET[/yellow] — read a resource.
[yellow]POST[/yellow] — create a resource.
[yellow]PUT[/yellow] — replace a resource.
[yellow]DELETE[/yellow] — remove a resource.

[italic]"The API that violates REST principles doesn't fail immediately.
It fails at scale, under load, when you can't afford to redesign it."[/italic]
""",
    "url_design": """
[bold cyan]== THE PATH MATRIX ==[/bold cyan]

URLs are the address system of your API. They tell clients where to find
resources and how those resources relate to each other.

The audit of the compromised API revealed URLs like [yellow]/getActiveUsersByRole[/yellow],
[yellow]/api/deleteItem[/yellow], and [yellow]/v1/data/fetch/all[/yellow]. Verbs embedded in paths.
Inconsistent naming. No clear hierarchy. A client couldn't predict the next
endpoint without reading every line of documentation.

A well-designed URL scheme is self-documenting. A developer who sees
[yellow]/v1/users/42/orders[/yellow] already understands the resource hierarchy
without reading a single doc page.

[yellow]/v1/[/yellow] — version prefix.
[yellow]/resources[/yellow] — plural noun collections.
[yellow]/{id}[/yellow] — specific resource by identifier.
[yellow]?key=value[/yellow] — filters and modifiers.

[italic]"If your URLs need a glossary, your API needs a redesign."[/italic]
""",
    "request_response": """
[bold cyan]== THE PAYLOAD CHAMBER ==[/bold cyan]

The request goes in. The response comes back. Everything between those two
events is the contract — headers, content types, body structure, pagination,
error format.

The compromised API returned [bold white]different error formats from different endpoints[/bold white].
One returned [yellow]{{"error": "not found"}}[/yellow]. Another returned
[yellow]{{"message": "404", "success": false}}[/yellow]. A third returned a raw HTML error page
from the reverse proxy. The frontend team had three different error-handling
code paths. The attacker found a fourth.

Consistency is the contract. Every response — success or failure — should
follow the same structure.

[yellow]Content-Type[/yellow] — what format is this?
[yellow]Accept[/yellow] — what format do I want?
[yellow]pagination[/yellow] — how do I get the next page?
[yellow]error envelope[/yellow] — how do failures communicate?

[italic]"An API that returns different error formats from different endpoints
is not one API. It's several APIs wearing a trenchcoat."[/italic]
""",
    "authentication_apis": """
[bold cyan]== THE AUTH GATEWAY ==[/bold cyan]

Authentication is the door. Authorization is the room you're allowed to enter.
Rate limiting is the bouncer who counts how many times you've walked through.

The audit found [bold white]an API key embedded in a query parameter[/bold white] — visible in server
access logs, cached by proxies, logged by CDN providers, and indexed by the
internal search appliance. Twelve thousand requests a day, each one carrying
the API key in the URL for anyone with log access to read.

The OAuth2 implementation was functional but misconfigured: tokens with
no expiration, refresh tokens stored in localStorage, and CORS headers set
to [yellow]Access-Control-Allow-Origin: *[/yellow] across every endpoint.

[yellow]Authorization: Bearer[/yellow] — token-based access.
[yellow]API keys[/yellow] — static credentials for machine clients.
[yellow]OAuth2[/yellow] — delegated access on behalf of users.
[yellow]CORS[/yellow] — browser security for cross-origin requests.

[italic]"An API key in a URL is not authentication. It's a neon sign
that says 'the key is here, come and get it.'"[/italic]
""",
    "graphql_basics": """
[bold cyan]== THE QUERY NEXUS ==[/bold cyan]

The mobile team requested GraphQL two years ago. They were tired of
over-fetching — every REST endpoint returned the full object even when the
mobile client only needed two fields. Bandwidth costs. Latency costs.
Battery costs. All because the API returned everything, always.

GraphQL solved the over-fetching problem. But it introduced new ones.

The schema grew to [bold white]four hundred types[/bold white]. No one governed which fields were
queryable. A single query could request nested data ten levels deep —
users → orders → items → reviews → authors → profiles → settings.
Each level triggered N+1 resolver calls. One query brought down the
database connection pool.

[yellow]query[/yellow] — read data. Client specifies exact fields.
[yellow]mutation[/yellow] — write data. Returns selected fields.
[yellow]schema[/yellow] — the contract. Types, fields, relationships.
[yellow]resolver[/yellow] — the function behind each field.

[italic]"GraphQL gives clients power. Without guardrails,
that power becomes a denial-of-service vector."[/italic]
""",
    "api_documentation": """
[bold cyan]== THE SPEC VAULT ==[/bold cyan]

The API had [bold white]no documentation[/bold white].

Not "bad documentation." Not "outdated documentation." None. The onboarding
guide was a Slack message from 2023 that said "just look at the code." The
code was in four repositories, three programming languages, and two
different API styles. New developers took three weeks to make their first
successful API call. Most gave up and asked someone to send them a curl command.

The competitors had interactive docs, SDKs in five languages, and a
sandbox environment where developers could make test calls without
signing up. Their API adoption rate was nine times higher.

[yellow]OpenAPI[/yellow] — the spec that makes APIs machine-readable.
[yellow]Swagger UI[/yellow] — interactive docs from an OpenAPI spec.
[yellow]examples[/yellow] — copy-paste code that actually works.
[yellow]SDKs[/yellow] — native client libraries generated from the spec.

[italic]"An undocumented API is a private API, no matter what the
access policy says. If they can't understand it, they can't use it."[/italic]
""",
    "api_testing": """
[bold cyan]== THE TEST GRID ==[/bold cyan]

The API had [bold white]no tests[/bold white].

Not "insufficient tests." Not "flaky tests." None. Every deployment was a
leap of faith. A developer changed a response field from [yellow]user_name[/yellow] to
[yellow]username[/yellow] and deployed on Friday. The mobile app broke for thirty-six hours.
Nobody noticed until Monday because there were no contract tests, no
integration tests, and no monitoring on response schema changes.

The curl commands in the README were three versions behind.
The Postman collection hadn't been updated since the original developer left.
The staging environment returned different data than production.

[yellow]curl[/yellow] — the universal API testing tool.
[yellow]Postman[/yellow] — GUI for building and testing requests.
[yellow]contract tests[/yellow] — verify the interface agreement.
[yellow]mocks[/yellow] — fake APIs for parallel development.

[italic]"An API without tests is a promise without a signature.
It means nothing when the contract breaks."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "rest_fundamentals": """
[bold green]THE REST PROTOCOL — AUDITED.[/bold green]

You know the fundamentals. Resources are nouns. HTTP methods are verbs.
Status codes communicate results. Statelessness enables scaling.
Idempotency enables safe retries.

The compromised API violated three of these principles in a single endpoint:
a POST that was actually a read operation, returned 200 for errors, and
stored session state on the server. You've documented all three.

[bold cyan]The Path Matrix is next. URL design tells you everything about API quality.[/bold cyan]
""",
    "url_design": """
[bold green]THE PATH MATRIX — MAPPED.[/bold green]

Plural nouns. Consistent nesting. Version prefixes. Query parameters for
filtering. No verbs in paths. The URL scheme is now self-documenting.

You rewrote [yellow]/getActiveUsersByRole?r=admin[/yellow] as
[yellow]GET /v1/users?role=admin&active=true[/yellow]. Same data. Predictable address.
Any developer can guess the next endpoint.

[bold cyan]The Payload Chamber. Request and response design.[/bold cyan]
""",
    "request_response": """
[bold green]THE PAYLOAD CHAMBER — STANDARDIZED.[/bold green]

Every response now follows the same envelope: [cyan]{{"data": ..., "meta": ...}}[/cyan].
Every error follows the same structure: [cyan]{{"error": {{"code": ..., "message": ..., "details": ...}}}}[/cyan].
Pagination is consistent. Content-Type headers are enforced.

The frontend team deleted three error-handling code paths.
One path handles everything now.

[bold cyan]The Auth Gateway. Lock down the door.[/bold cyan]
""",
    "authentication_apis": """
[bold green]THE AUTH GATEWAY — SECURED.[/bold green]

API keys moved from query parameters to headers. OAuth2 tokens now expire.
Refresh tokens are stored server-side. Rate limits are enforced with
proper 429 responses and Retry-After headers. CORS is locked to
specific origins.

The twelve thousand daily requests with exposed API keys are now
twelve thousand daily requests with keys safely in headers.
The logs are clean.

[bold cyan]The Query Nexus. GraphQL brings power — and risk.[/bold cyan]
""",
    "graphql_basics": """
[bold green]THE QUERY NEXUS — GOVERNED.[/bold green]

Schema types are documented. Query depth is limited to four levels.
DataLoader handles N+1 problems. Mutations validate inputs.
The resolver chain is optimized.

The query that brought down the connection pool now returns in
forty milliseconds. Not because GraphQL changed — because the
implementation was fixed.

[bold cyan]The Spec Vault. Documentation is the difference between a public API and a private one.[/bold cyan]
""",
    "api_documentation": """
[bold green]THE SPEC VAULT — PUBLISHED.[/bold green]

OpenAPI specs for every endpoint. Swagger UI with interactive testing.
Code examples in Python, JavaScript, and curl. SDKs auto-generated
from the spec. A sandbox environment for safe experimentation.

Time-to-first-call dropped from three weeks to four minutes.
Developer adoption doubled in the first month.

[bold cyan]The Test Grid. Final phase. An API without tests is a liability.[/bold cyan]
""",
    "api_testing": """
[bold yellow]★ ★ ★  THE TEST GRID — COMPLETE. API SURFACE FULLY AUDITED.  ★ ★ ★[/bold yellow]

[bold white]The audit is complete. The contracts are rebuilt.[/bold white]

Every endpoint has integration tests. Contract tests run in CI/CD.
Newman executes the Postman collection on every deploy. Mock servers
enable parallel frontend/backend development. curl examples are
current and tested.

The Friday deployment that broke mobile for thirty-six hours?
It would now fail the CI pipeline in under two minutes.
The contract test would catch the field rename before it reached staging.

[bold magenta]The API surface is locked down. The contracts are signed.
APIs are not endpoints — they are promises.
Now you know how to design promises that hold.[/bold magenta]

[bold yellow]API ARCHITECT STATUS: GATEWAY MASTER.  CONTRACTS: FULLY FORGED.[/bold yellow]
""",
}

BOSS_INTROS = {
    "rest_fundamentals": "[bold red]⚠  REST AUDIT: The Principles Exam[/bold red]\nSix REST constraints. Five HTTP methods. Status codes for every scenario. Prove you understand the foundation.",
    "url_design": "[bold red]⚠  URL AUDIT: The Path Review[/bold red]\nEvery URL in the API surface is being evaluated. Versioning, naming, nesting, parameters. Prove you can design a self-documenting URL scheme.",
    "request_response": "[bold red]⚠  PAYLOAD AUDIT: The Contract Review[/bold red]\nHeaders, envelopes, pagination, error formats. Prove the request/response contract is bulletproof.",
    "authentication_apis": "[bold red]⚠  AUTH AUDIT: The Security Gate[/bold red]\nAPI keys, OAuth2 flows, token handling, rate limits, CORS. Prove the authentication layer is locked down.",
    "graphql_basics": "[bold red]⚠  GRAPHQL AUDIT: The Schema Review[/bold red]\nTypes, queries, mutations, resolvers, and the N+1 problem. Prove you can govern a GraphQL surface.",
    "api_documentation": "[bold red]⚠  DOCUMENTATION AUDIT: The Spec Review[/bold red]\nOpenAPI, interactive docs, examples, SDKs, developer experience. Prove the API is documented for adoption.",
    "api_testing": "[bold red]★  TEST AUDIT: The Final Gate[/bold red]\ncurl, Postman, integration tests, contract tests, mocking. Prove every contract is verified and every edge case is covered.",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "first_blood": ("First Endpoint Audited", "Made your first API design decision. The surface acknowledged your access."),
    "rest_scholar": ("REST Fundamentals Cleared", "Audited the REST protocol layer. Resources, methods, status codes, idempotency — the foundation is solid."),
    "path_architect": ("URL Design Cleared", "Mapped the Path Matrix. Every URL is self-documenting, versioned, and predictable."),
    "payload_master": ("Request/Response Cleared", "Standardized the Payload Chamber. Consistent envelopes, pagination, and error formats across every endpoint."),
    "auth_sentinel": ("Authentication Cleared", "Secured the Auth Gateway. Keys in headers, tokens that expire, rate limits that hold."),
    "query_governor": ("GraphQL Cleared", "Governed the Query Nexus. Schema, resolvers, depth limits, and DataLoader — the graph is optimized."),
    "spec_keeper": ("Documentation Cleared", "Published the Spec Vault. OpenAPI, interactive docs, examples, SDKs — the API is discoverable."),
    "test_warden": ("Testing Cleared", "Locked down the Test Grid. Integration tests, contract tests, mocking, and CI/CD validation — every contract is verified."),
    "streak_3": ("Clean Interface", "3 correct in a row. Your API design instincts are sharpening."),
    "streak_5": ("Consistent Contract", "5 in a row. You design APIs the way they should be consumed — predictably."),
    "streak_10": ("UNBREAKABLE CONTRACT", "10 in a row. Your API contracts are immutable. No breaking changes. No surprises."),
    "no_hints": ("No Docs Needed", "Cleared a zone without hints. The spec is already in your head."),
    "speed_demon": ("Sub-5 Response", "Answered in under 5 seconds. Faster than the API's p99 latency."),
    "level_10": ("Junior Architect", "Level 10. You read API surfaces the way others read error messages."),
    "level_20": ("Senior Architect", "Level 20. You design contracts that don't break. Teams rely on your specs."),
    "level_30": ("API Czar", "Maximum level. You've audited and redesigned API surfaces at enterprise scale. The contracts hold."),
    "completionist": ("Full Surface Audited", "Every zone. Every challenge. Total API architecture mastery achieved."),
    "boss_slayer": ("Design Flaw Found", "Beat your first boss challenge. The API thought its flaws were hidden. They weren't."),
}
