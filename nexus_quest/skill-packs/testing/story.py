"""
story.py - Narrative text for The Verification Engine
"""

INTRO_STORY = """
The deployment went clean. Green across the board.

Fourteen microservices. Two hundred and thirty-one endpoints. Every health check
returning 200. Every dashboard showing nominal. The release notes went to stakeholders
at 5:47 PM on a Friday. Routine.

At 5:52 PM, the first ticket came in.

By 6:30 PM, forty-seven users had reported data corruption. Transaction amounts
doubled. Account balances negative. An edge case in the currency conversion service
that [bold red]no test had ever exercised[/bold red].

The post-mortem was damning. Not because the bug existed — bugs always exist.
Because [bold white]the test suite had passed[/bold white]. Two thousand tests. Every one green.
Every one worthless against the failure that actually mattered.

CIPHER's audit of the test infrastructure revealed the truth:
the tests weren't testing behavior. They were testing implementation details.
Mocking everything. Asserting nothing meaningful. Coverage metrics painted
a comforting lie — 87% line coverage that missed every critical path.

[bold magenta]You are Ghost.[/bold magenta] You've traced the infrastructure. You've read the code.
You've mapped the data flows. Now you need to build what NEXUS never had:
[bold white]a verification engine that actually catches failures before they reach production[/bold white].

The testing framework is open. pytest is loaded. The cursor is blinking.

[bold cyan]Write the tests that would have prevented all of it. Begin.[/bold cyan]
"""

ZONE_INTROS = {
    "unit_testing_fundamentals": """
[bold cyan]== THE ASSERTION LAYER ==[/bold cyan]

CIPHER's scan of the test directory is complete. The results are worse than expected.

Half the test files don't follow naming conventions — pytest never discovered them.
The tests that [italic]do[/italic] run are bloated. Fifteen assertions per function.
Setup code duplicated across every file. No fixtures. No parametrization.
Just raw, repetitive, fragile checks that break every time someone renames a variable.

The foundation is rotten. Before you can build a verification engine,
you need to understand the substrate: [yellow]pytest[/yellow]. How it discovers tests.
How it runs them. How [yellow]assert[/yellow] actually works under the hood —
the introspection, the rewriting, the detailed failure messages that
make the difference between a useful test and a waste of time.

[italic]"A test suite is only as strong as its weakest assertion.
Start with the assertions. Make them precise."[/italic]
""",

    "mocking_and_test_doubles": """
[bold cyan]== THE ISOLATION CHAMBER ==[/bold cyan]

CIPHER found the source of the false confidence.

The currency conversion tests mocked [italic]everything[/italic]. The HTTP client. The database.
The config loader. The logger. Every dependency replaced with a stub that returned
exactly what the test expected — which meant the tests only verified that
the mocks were configured correctly. Not that the code worked.

Mocking is a scalpel. NEXUS used it as a sledgehammer.

[yellow]unittest.mock[/yellow]. [yellow]patch[/yellow]. [yellow]MagicMock[/yellow]. [yellow]side_effect[/yellow].
These are precision instruments for isolating the unit under test.
Used correctly, they reveal bugs. Used carelessly, they hide them.

You need to learn when to mock, what to mock, and — critically —
[bold white]what to never mock[/bold white].

[italic]"The most dangerous mock is the one that makes a broken test pass."[/italic]
""",

    "integration_and_e2e": """
[bold cyan]== THE BOUNDARY SCANNER ==[/bold cyan]

The unit tests — even the good ones — never caught the currency bug.

Because the bug lived at the [bold white]boundary[/bold white]. Between the conversion service
and the transaction processor. The data format that one service produced
and the other consumed. A field that was a float in one system and a
string in the other. No unit test could catch it. No mock would reveal it.

Integration tests verify the boundaries. E2E tests verify the user experience.
The currency bug would have been caught by a single integration test that
sent a real conversion through the real pipeline with a real database.

[yellow]TestClient[/yellow]. [yellow]httpx[/yellow]. [yellow]factory_boy[/yellow]. [yellow]Playwright[/yellow].
The tools exist. NEXUS never used them.

[italic]"Unit tests verify that pieces work. Integration tests verify that pieces fit.
The bug is always in the fit."[/italic]
""",

    "test_architecture": """
[bold cyan]== THE STRUCTURAL MATRIX ==[/bold cyan]

CIPHER's analysis goes deeper now. Past the individual tests to the
[bold white]architecture[/bold white] of the test suite itself.

The conftest.py files are empty or missing. Fixtures are redefined
in every test file — the same database setup code copied forty-seven times.
No parametrization. A function that should be tested with twelve inputs
gets tested with one. Coverage reports are generated but never read.
Markers don't exist. The entire suite runs every time — twenty minutes
of tests when a developer only changed one module.

Test architecture is software architecture. The same principles apply:
[yellow]DRY[/yellow], [yellow]separation of concerns[/yellow], [yellow]composition over duplication[/yellow].

[italic]"A test suite that's hard to maintain is a test suite that stops being maintained."[/italic]
""",

    "tdd_and_testing_culture": """
[bold cyan]== THE PROTOCOL CORE ==[/bold cyan]

The final layer. Not tools. Not syntax. [bold white]Philosophy[/bold white].

CIPHER's audit found the root cause beneath all the technical failures:
[bold red]tests were written as an afterthought[/bold red]. After the code. After the review.
After the merge. Sometimes after the bug. Always too late to shape the design.

The currency conversion service was never designed to be testable.
Its constructor required a live database connection. Its methods had
side effects. Its return types were inconsistent. No amount of mocking
could make it reliably testable — because it was never built with testing in mind.

TDD isn't about tests. It's about design. Red-Green-Refactor forces you
to define behavior before implementation. The test becomes the specification.

[italic]"The team that writes tests after the code will always be surprised by production.
The team that writes tests first will be surprised by how rarely production surprises them."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "unit_testing_fundamentals": """
[bold green]THE ASSERTION LAYER — VERIFIED.[/bold green]

pytest discovery. Clean assertions. Exception testing with pytest.raises().
conftest.py for shared fixtures. The -x flag for fast failure feedback.

The foundation is solid. You write tests that test what they claim to test.
The assertion introspection means every failure tells you exactly what went wrong.

[bold cyan]The Isolation Chamber is next — learning to mock with precision.[/bold cyan]
""",

    "mocking_and_test_doubles": """
[bold green]THE ISOLATION CHAMBER — CALIBRATED.[/bold green]

Patch where it's looked up. side_effect for exceptions. return_value for happy paths.
assert_called_once_with for verification. MagicMock for dunder methods.

You know the scalpel from the sledgehammer. Mocking isolates — it doesn't replace
the need for real integration. The mocks are precise now.

[bold cyan]The Boundary Scanner awaits — integration and E2E testing.[/bold cyan]
""",

    "integration_and_e2e": """
[bold green]THE BOUNDARY SCANNER — OPERATIONAL.[/bold green]

TestClient for API endpoints. Real databases with transaction rollback.
Factory_boy for test data. Playwright for browser E2E. The testing pyramid
understood — not as dogma but as a cost/confidence tradeoff.

The currency bug lives at boundaries. Your integration tests guard those boundaries now.

[bold cyan]The Structural Matrix holds the architecture — fixtures, parametrize, coverage.[/bold cyan]
""",

    "test_architecture": """
[bold green]THE STRUCTURAL MATRIX — OPTIMIZED.[/bold green]

Session-scoped fixtures for expensive resources. @pytest.mark.parametrize
for comprehensive input coverage. Markers for selective execution.
Coverage reports that measure branch coverage, not just lines.

The test suite is no longer a monolith. It's modular, fast, and maintainable.

[bold cyan]The Protocol Core is the final layer — TDD and testing culture.[/bold cyan]
""",

    "tdd_and_testing_culture": """
[bold yellow]★ ★ ★  THE VERIFICATION ENGINE — COMPLETE.  ★ ★ ★[/bold yellow]

[bold white]Complete.[/bold white]

Red-Green-Refactor. Arrange-Act-Assert. FIRST principles.
The test smells identified and eliminated. Flaky tests quarantined and fixed.
Shift-left applied — tests before code, quality before deployment.

The currency conversion bug would never have shipped. Not because of one test —
because of a culture that writes tests first, trusts the suite, and treats
every failure as information.

NEXUS had tools. They lacked discipline.
You have both.

[bold magenta]Ghost Operative — Verification Engine certified. Test suite armed.[/bold magenta]
""",
}

BOSS_INTROS = {
    "unit_testing_fundamentals": "[bold red]⚠  ASSERTION GAUNTLET: The Exception Validator[/bold red]\nThe payment processor must reject negative amounts with a ValueError containing a specific message. Prove it — test both the exception type AND the message content in a single pytest construct.",
    "mocking_and_test_doubles": "[bold red]⚠  ISOLATION BREACH: The Slack Alert[/bold red]\nThe alert system calls requests.post() to send Slack notifications. Test the function without making a real HTTP request — patch the right target, configure the mock response, and verify the payload.",
    "integration_and_e2e": "[bold red]⚠  BOUNDARY FAILURE: The Order Pipeline[/bold red]\nPOST /orders creates a record, charges Stripe, and sends an email. The database must be real. Stripe and email must be mocked. Design the test that catches boundary failures while isolating external services.",
    "test_architecture": "[bold red]★  ARCHITECTURE AUDIT: The Tax Calculator[/bold red]\nTwelve country/rate combinations. One shared database connection. One mocked external API. Combine parametrize, fixture scopes, and mocking into a single, elegant test architecture.",
    "tdd_and_testing_culture": "[bold red]★  FINAL PROTOCOL: The Culture Fix[/bold red]\nFifteen flaky tests. Twenty-minute suite. Forty percent coverage. Developers skipping tests. PRs breaking main. Diagnose the highest-impact intervention — the one that restores trust before anything else.",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "assertion_master": ("Assertions Verified", "Cleared Unit Testing Fundamentals. pytest discovered, assertions precise, exceptions tested. The foundation holds."),
    "isolation_expert": ("Isolation Calibrated", "Cleared Mocking & Test Doubles. Patches precise, side_effects controlled, mocks verified. The scalpel, not the sledgehammer."),
    "boundary_guardian": ("Boundaries Guarded", "Cleared Integration & E2E. TestClient deployed, databases tested, factories built. The boundaries are watched."),
    "architecture_engineer": ("Architecture Optimized", "Cleared Test Architecture. Fixtures scoped, tests parametrized, coverage measured. The suite is maintainable."),
    "protocol_master": ("Protocol Mastered", "Cleared TDD & Testing Culture. Red-Green-Refactor internalized. FIRST principles applied. The verification engine is armed."),
    "first_blood": ("First Test", "Executed your first testing challenge. The assertion layer acknowledged you."),
    "streak_3": ("Signal Locked", "3 correct in a row. The test patterns are becoming readable."),
    "streak_5": ("Ghost Protocol", "5 correct in a row. You think in tests now."),
    "streak_10": ("Verification Master", "10 correct in a row. The test suite holds no secrets from you."),
    "no_hints": ("Dark Run", "Cleared a zone without hints. Pure comprehension. No scaffolding."),
    "speed_demon": ("Sub-5 Parse", "Answered in under 5 seconds. The pattern is instinctive now."),
    "level_10": ("Junior Operative", "Level 10. Testing is starting to feel like a first instinct."),
    "level_20": ("Senior Operative", "Level 20. You write tests before you write code."),
    "level_30": ("Ghost: Specter", "Maximum level. The verification engine is fully operational. Ship with confidence."),
    "boss_slayer": ("Boss Bypassed", "Beat your first boss challenge. The hard cases don't slow you down."),
    "completionist": ("Full Verification", "Every challenge. Every zone. The complete verification engine — tested, trusted, deployed."),
}
