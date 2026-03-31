"""
story.py — Narrative text for Web Forge (Web Development skill pack).

Theme: "The web is the world's platform. Build it right."
Cyberpunk setting — the NEXUS Files investigation.
"""

INTRO_STORY = """
The frontend was flawless. Too flawless.

Two hundred and twelve pages served to [bold white]forty million monthly visitors[/bold white].
Sub-second load times on every continent. Perfect Lighthouse scores.
Zero accessibility complaints. The NEXUS public-facing web platform was
the most polished interface the congressional investigators had ever seen.

And behind it — every fraudulent transaction, every manipulated record,
every fabricated audit trail — was rendered through components so clean,
so performant, so perfectly structured that no user ever suspected they
were looking at a lie wrapped in semantic HTML.

[bold red]The web is the world's platform.[/bold red]

Someone at NEXUS understood that better than anyone. The markup was semantic.
The styles were responsive. The JavaScript was async, tree-shaken, and
lazy-loaded to the millisecond. Server components rendered the sensitive
data. Client components handled the interactions. The deployment pipeline
was automated, immutable, and reproduced identically across three regions.

The frontend wasn't just a UI. It was [bold white]the delivery mechanism[/bold white].

You found the first page source in [yellow]/opt/nexus/web/app/page.tsx[/yellow].
Server Component. No client-side JavaScript shipped for the landing page.
The initial paint was 0.4 seconds. The layout shift was zero.
Built by someone who understood that the fastest page is the one
that loads before the user notices it started.

[bold magenta]You are Ghost.[/bold magenta] You've been inside the terminal. You've read the git history.
You've mapped the container infrastructure. You've queried the databases.
You've traced the type system. You've read the API contracts.

Now you need to understand the web layer — the platform that delivered
the fraud to the world. The HTML that structured it. The CSS that styled it.
The JavaScript that powered it. The framework that optimized it.
The pipeline that shipped it.

The web is the world's platform. Build it right — or understand
how someone built it wrong.

[bold cyan]The browser is open. The DevTools are waiting. View source.[/bold cyan]
"""

ZONE_INTROS = {
    "html_fundamentals": """
[bold cyan]== THE MARKUP LAYER ==[/bold cyan]

The page source is open. View source on any NEXUS page and the first thing
you see is structure — semantic, deliberate, accessible.

Every landmark has a role. Every form has labels. Every image has alt text.
The HTML wasn't written by someone filling in templates. It was written by
someone who understood that [bold white]the DOM is the document[/bold white], and the document
is what screen readers, crawlers, and browsers actually consume.

[yellow]<header>[/yellow], [yellow]<main>[/yellow], [yellow]<nav>[/yellow], [yellow]<article>[/yellow] — semantic landmarks.
[yellow]<form>[/yellow] with [yellow]<label for>[/yellow] — accessible inputs.
[yellow]<meta>[/yellow] tags — viewport, Open Graph, charset.

The NEXUS landing page passes every WCAG 2.1 AA criterion.
Accessibility wasn't an afterthought. It was a design constraint.

[italic]"The best HTML is the HTML you don't notice — because it just works,
for everyone, on every device."[/italic]
""",

    "css_modern": """
[bold cyan]== THE STYLE MATRIX ==[/bold cyan]

The layout system is surgical. Open DevTools on any NEXUS page and you'll
see Grid and Flexbox used with precision — no floats, no clearfixes, no
hacks from 2012.

Custom properties cascade through the component tree. A single
[yellow]--color-primary[/yellow] change in [yellow]:root[/yellow] and the entire theme shifts.
Container queries make components responsive to their parent, not the
viewport. Animations are GPU-accelerated. Transitions are 60fps.

[yellow]display: flex[/yellow] and [yellow]display: grid[/yellow] — the layout engines.
[yellow]var(--custom-property)[/yellow] — runtime theming.
[yellow]@media[/yellow] and [yellow]@container[/yellow] — responsive at every level.

The CSS is not decoration. It's architecture.

[italic]"A layout system that breaks on resize is not a layout system.
It's a screenshot."[/italic]
""",

    "javascript_core": """
[bold cyan]== THE SCRIPT ENGINE ==[/bold cyan]

The JavaScript is lean. Not because they wrote less — because they understood
what the engine actually does with the code at runtime.

Closures capture exactly the state they need. Promises chain without nesting.
Async/await reads like synchronous code but never blocks the main thread.
The event loop is respected — no long tasks, no jank, no frozen UI.

[yellow]Closures[/yellow] — the foundation of data privacy and React hooks.
[yellow]Promises[/yellow] and [yellow]async/await[/yellow] — asynchronous control flow.
[yellow]The event loop[/yellow] — why setTimeout(fn, 0) doesn't run immediately.
[yellow]ES Modules[/yellow] — import/export for tree-shakeable code.

The NEXUS frontend ships 47KB of JavaScript to the client.
The rest runs on the server.

[italic]"JavaScript is the only language that runs everywhere.
Understand the runtime, or the runtime runs you."[/italic]
""",

    "react_essentials": """
[bold cyan]== THE COMPONENT FORGE ==[/bold cyan]

The component tree is deep but disciplined. Every component is a function.
Every function takes props. Every piece of state lives exactly where it
needs to — no higher, no lower.

[yellow]useState[/yellow] for local state. [yellow]useEffect[/yellow] for side effects.
[yellow]useRef[/yellow] for DOM access and stable references.
Props flow down. Events flow up. State is lifted to the nearest
common ancestor and no further.

The NEXUS dashboard renders 12,000 data points in real-time.
No lag. No stale data. The component architecture was designed
by someone who understood that React re-renders are features,
not bugs — if your state is in the right place.

[italic]"A component is a contract: given these props, render this UI.
Break the contract and React will tell you."[/italic]
""",

    "nextjs": """
[bold cyan]== THE NEXT DIMENSION ==[/bold cyan]

The framework layer. Where React meets the server.

NEXUS runs on the App Router. Server Components render the data-heavy
pages — no client JavaScript shipped. Client Components handle the
interactive elements — forms, filters, real-time updates. The boundary
between server and client is explicit: [yellow]'use client'[/yellow] or nothing.

[yellow]page.tsx[/yellow] and [yellow]layout.tsx[/yellow] — file-based routing.
[yellow]Server Components[/yellow] — zero client JS, direct database access.
[yellow]route.ts[/yellow] — API endpoints with typed request handlers.
[yellow]middleware.ts[/yellow] — auth checks before the request hits the page.

The NEXUS web platform deploys to three regions. Each deployment
is immutable. Each page is either statically generated or
server-rendered depending on the data freshness requirement.

[italic]"Next.js is not a framework on top of React.
It's the infrastructure underneath it."[/italic]
""",

    "web_performance": """
[bold cyan]== THE SPEED PROTOCOL ==[/bold cyan]

The performance audit tells a story. Every NEXUS page loads in under
1.5 seconds on a 3G connection. Largest Contentful Paint: 0.8s.
Interaction to Next Paint: 45ms. Cumulative Layout Shift: 0.

This wasn't luck. This was engineering.

[yellow]LCP[/yellow], [yellow]INP[/yellow], [yellow]CLS[/yellow] — the Core Web Vitals.
[yellow]loading='lazy'[/yellow] — defer off-screen images.
[yellow]React.lazy[/yellow] — code-split heavy components.
[yellow]Cache-Control[/yellow] — CDN and browser caching strategy.

Images are served in AVIF with fallbacks. Fonts are preloaded.
Critical CSS is inlined. Third-party scripts are deferred.
Every byte has been accounted for.

[italic]"Performance is not an optimization. It's a feature.
Users don't wait. They leave."[/italic]
""",

    "web_security": """
[bold cyan]== THE FIREWALL ==[/bold cyan]

The security layer is invisible — which means it's working.

Every user input is escaped before rendering. Every form has a CSRF token.
Every cookie is HttpOnly, Secure, SameSite=Lax. The Content Security
Policy blocks inline scripts. CORS headers restrict API access to known
origins. Auth tokens live in HttpOnly cookies, never in localStorage.

[yellow]XSS prevention[/yellow] — output encoding and CSP.
[yellow]CSRF protection[/yellow] — tokens and SameSite cookies.
[yellow]CORS[/yellow] — server-controlled cross-origin access.
[yellow]HTTPS everywhere[/yellow] — Strict-Transport-Security.

The NEXUS web platform had zero security incidents in production.
Not because nobody tried to attack it. Because the defenses were
correct, layered, and configured by someone who understood the
threat model.

[italic]"Security is not a feature you add. It's a property you maintain.
Every header. Every cookie attribute. Every escaped character."[/italic]
""",

    "deployment": """
[bold cyan]== THE LAUNCH PAD ==[/bold cyan]

The deployment pipeline is the final layer. Every git push triggers a build.
Every branch gets a preview URL. Every merge to main deploys to production
in under ninety seconds.

[yellow]Vercel[/yellow] — zero-config Next.js deployment.
[yellow]Docker[/yellow] — multi-stage builds for containerized hosting.
[yellow]GitHub Actions[/yellow] — CI/CD: lint, type-check, test, build, deploy.
[yellow]Preview deployments[/yellow] — every PR gets a live URL.

The NEXUS deployment configuration was the most disciplined part of
the operation. Immutable deployments. Content-hashed assets.
Environment variables separated by deployment target.
No manual steps. No SSH. No "it works on my machine."

The pipeline was evidence. Every build artifact, every deployment log,
every preview URL — timestamped, immutable, and waiting to be read.

[italic]"The deployment pipeline is not the last step.
It's the proof that every previous step succeeded."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "html_fundamentals": """
[bold green]THE MARKUP LAYER — ANALYZED.[/bold green]

Semantic elements mapped. Forms audited. Accessibility labels verified.
Meta tags catalogued. The viewport is set. The Open Graph tags generate
clean previews on every platform.

The HTML is the foundation. Every CSS rule, every JavaScript handler,
every framework feature — all of it sits on top of the markup.
The NEXUS team got the foundation right.

[bold cyan]The Style Matrix is next — Flexbox, Grid, and the visual architecture.[/bold cyan]
""",

    "css_modern": """
[bold green]THE STYLE MATRIX — MAPPED.[/bold green]

Flexbox layouts traced. Grid systems documented. Custom properties
catalogued from :root through every component. Animations verified
at 60fps. Responsive breakpoints mapped from mobile to ultrawide.
Container queries identified in twelve reusable components.

The CSS architecture is modular, themeable, and performs.

[bold cyan]The Script Engine holds the JavaScript core — closures, promises, and the event loop.[/bold cyan]
""",

    "javascript_core": """
[bold green]THE SCRIPT ENGINE — DECODED.[/bold green]

Closures traced through the component tree. Promise chains verified
for error handling. Async/await patterns documented. The event loop
priority order is understood — microtasks before macrotasks, always.

ES Module imports mapped. Destructuring patterns catalogued.
The JavaScript is lean, modern, and precise.

[bold cyan]The Component Forge is next — React hooks, props, and state management.[/bold cyan]
""",

    "react_essentials": """
[bold green]THE COMPONENT FORGE — MASTERED.[/bold green]

Function components documented. useState patterns traced through
the state tree. useEffect dependency arrays verified — no stale
closures, no infinite loops. useRef usage catalogued for DOM access
and stable references.

Props flow down. State is lifted to the correct level.
The component architecture is sound.

[bold cyan]The Next Dimension holds the framework layer — App Router, Server Components, SSR.[/bold cyan]
""",

    "nextjs": """
[bold green]THE NEXT DIMENSION — NAVIGATED.[/bold green]

App Router file conventions mapped. Server Components identified —
zero client JavaScript for data-heavy pages. Client Components
marked with 'use client' only where interactivity requires it.

API routes documented. Middleware traced for auth checks.
Image optimization verified. SSG vs SSR decisions audited.
The framework layer is fully understood.

[bold cyan]The Speed Protocol — Core Web Vitals, caching, and every optimization.[/bold cyan]
""",

    "web_performance": """
[bold green]THE SPEED PROTOCOL — BENCHMARKED.[/bold green]

Core Web Vitals: all green. LCP under 2.5s. INP under 200ms. CLS zero.
Lazy loading verified for below-the-fold images. Code splitting traced
through React.lazy and dynamic imports. Cache-Control headers audited.

Lighthouse scores documented. Every optimization explained.
The performance architecture is intentional, measurable, and effective.

[bold cyan]The Firewall — XSS, CSRF, CORS, and every security layer.[/bold cyan]
""",

    "web_security": """
[bold green]THE FIREWALL — AUDITED.[/bold green]

XSS defenses verified: output encoding on all user input, CSP headers
blocking inline scripts. CSRF tokens on every state-changing form.
Cookies set with HttpOnly, Secure, SameSite. CORS restricting API
access to known origins. Auth tokens stored in HttpOnly cookies.

The security posture is correct. Every header. Every attribute.
Every escaped character. Defense in depth.

[bold cyan]The Launch Pad — deployment, CI/CD, and the final pipeline.[/bold cyan]
""",

    "deployment": """
[bold yellow]★ ★ ★  THE LAUNCH PAD — FULLY OPERATIONAL.  ★ ★ ★[/bold yellow]

[bold white]Complete.[/bold white]

The deployment pipeline is fully documented. Git-triggered builds.
Preview deployments on every PR. Production deployments on merge to main.
Multi-stage Docker builds for containerized hosting. GitHub Actions
running lint, type-check, test, and build on every push.

Environment variables separated by target. Immutable deployments.
Content-hashed assets cached for a year. Zero manual intervention.

The web layer that delivered the NEXUS fraud to the world is now
fully understood. From semantic HTML to the deployment pipeline.
Every abstraction layer, every optimization, every security header —
documented, analyzed, and attached to the filing.

[bold magenta]Ghost Operative — Web Development certified.
The platform is mapped. The delivery mechanism is understood.[/bold magenta]

[bold yellow]WEB FORGE: COMPLETE. THE PLATFORM IS DOCUMENTED.[/bold yellow]
""",
}

BOSS_INTROS = {
    "html_fundamentals": "[bold red]⚠  MARKUP AUDIT: The Accessibility Review[/bold red]\nA screen reader user reports they can't navigate the NEXUS landing page. Forms have no labels. Landmarks are missing. Prove you can read and fix semantic HTML.",
    "css_modern": "[bold red]⚠  LAYOUT CHALLENGE: The Responsive Grid[/bold red]\nThe dashboard layout breaks on tablet screens. Grid columns collapse wrong. Container queries aren't firing. Prove you understand modern CSS layout.",
    "javascript_core": "[bold red]⚠  RUNTIME ANALYSIS: The Event Loop Trap[/bold red]\nA long-running synchronous task is freezing the UI. setTimeout isn't helping. The microtask queue is backing up. Prove you understand the event loop.",
    "react_essentials": "[bold red]⚠  COMPONENT AUDIT: The Re-Render Storm[/bold red]\nThe dashboard re-renders 400 times per second. State is in the wrong component. Effects are missing dependencies. Prove you can fix the component architecture.",
    "nextjs": "[bold red]⚠  FRAMEWORK ANALYSIS: The Server/Client Boundary[/bold red]\nA Server Component is importing useState. The build fails. The boundary between server and client is broken. Prove you understand where each component belongs.",
    "web_performance": "[bold red]⚠  PERFORMANCE CRISIS: The Lighthouse Audit[/bold red]\nLCP is 8 seconds. CLS is 0.45. The JavaScript bundle is 2MB. Every optimization is missing. Prove you can diagnose and fix web performance.",
    "web_security": "[bold red]⚠  SECURITY BREACH: The XSS Incident[/bold red]\nUser-submitted content is rendering as executable HTML. Cookies are accessible to JavaScript. CORS is set to '*'. Prove you can identify and fix every vulnerability.",
    "deployment": "[bold red]★  FINAL MISSION: The Production Pipeline[/bold red]\nThe deployment pipeline has no tests, no previews, and no rollback strategy. Build the CI/CD workflow from scratch. The platform depends on it.",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "markup_master":      ("Markup Master", "Cleared the Markup Layer. Semantic HTML, accessible forms, meta tags — the foundation is solid."),
    "style_architect":    ("Style Architect", "Mapped the Style Matrix. Flexbox, Grid, custom properties, container queries — the visual layer decoded."),
    "script_engineer":    ("Script Engineer", "Decoded the Script Engine. Closures, promises, event loop, modules — the runtime is understood."),
    "component_smith":    ("Component Smith", "Mastered the Component Forge. Hooks, props, state, and the art of lifting state up."),
    "next_navigator":     ("Next Navigator", "Navigated the Next Dimension. App Router, Server Components, SSR, SSG — the framework layer mapped."),
    "speed_specialist":   ("Speed Specialist", "Benchmarked the Speed Protocol. Core Web Vitals green. Every optimization documented."),
    "security_sentinel":  ("Security Sentinel", "Audited the Firewall. XSS, CSRF, CSP, CORS, cookies — every security layer verified."),
    "deploy_commander":   ("Deploy Commander", "The Launch Pad is operational. CI/CD, previews, immutable deployments — the pipeline is complete."),
    "first_tag":          ("First Tag", "Wrote your first HTML tag. The browser rendered it."),
    "streak_3":           ("Clean Commit", "3 correct in a row. The web fundamentals are clicking."),
    "streak_5":           ("Hot Module", "5 correct in a row. Your web knowledge reloads instantly."),
    "streak_10":          ("Zero Downtime", "10 correct in a row. Flawless deployment. No rollback needed."),
    "no_hints":           ("View Source", "Cleared a zone without hints. You read the web like source code."),
    "speed_demon":        ("First Paint", "Answered in under 5 seconds. Faster than your LCP."),
    "level_10":           ("Junior Web Dev", "Level 10. You think in components now."),
    "level_20":           ("Senior Web Dev", "Level 20. You see the network tab before you see the page."),
    "level_30":           ("Tim Berners-Lee", "Maximum level. The web is your platform. You built it right."),
    "boss_slayer":        ("Bug Squashed", "Beat your first boss challenge. The DevTools bow to you."),
    "completionist":      ("Full Stack Certified", "Every challenge. Every zone. HTML to deployment — the complete web platform, documented."),
}
