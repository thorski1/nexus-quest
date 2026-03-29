"""
zones.py — API Design zones and challenges for API Forge.

7 zones, ~40 challenges. All challenges use "type": "quiz" with
multiple-choice options (a/b/c/d) and two hints each.
"""

ZONE_ORDER = [
    "rest_fundamentals",
    "url_design",
    "request_response",
    "authentication_apis",
    "graphql_basics",
    "api_documentation",
    "api_testing",
]

ZONES = {
    # ── ZONE 1: REST FUNDAMENTALS ─────────────────────────────────────
    "rest_fundamentals": {
        "id": "rest_fundamentals",
        "name": "The REST Protocol",
        "subtitle": "REST Principles, Resources, HTTP Methods, Status Codes & Idempotency",
        "color": "cyan",
        "icon": "🔗",
        "commands": ["GET", "POST", "PUT", "DELETE", "PATCH"],
        "challenges": [
            {
                "id": "rest_1",
                "type": "quiz",
                "title": "What REST Stands For",
                "question": (
                    "REST is the dominant architectural style for web APIs.\n"
                    "What does REST stand for?"
                ),
                "lesson": (
                    "REST = Representational State Transfer.\n\n"
                    "Defined by Roy Fielding in his 2000 doctoral dissertation, REST is an\n"
                    "architectural style — not a protocol. It describes how clients and\n"
                    "servers should communicate over HTTP using stateless requests,\n"
                    "uniform interfaces, and resource-based URIs.\n\n"
                    "A RESTful API exposes resources (nouns) and uses HTTP methods (verbs)\n"
                    "to perform operations on them."
                ),
                "options": [
                    "Remote Execution Service Transfer",
                    "Representational State Transfer",
                    "Resource Endpoint Structured Transactions",
                    "Reliable Encrypted Secure Transport",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It was defined by Roy Fielding and deals with how state is represented.",
                    "The 'S' stands for State, and the 'T' stands for Transfer.",
                ],
            },
            {
                "id": "rest_2",
                "type": "quiz",
                "title": "Resources as Nouns",
                "question": (
                    "In REST, what does a URL identify?\n\n"
                    "  GET /users/42\n\n"
                    "What is '/users/42' in REST terminology?"
                ),
                "lesson": (
                    "In REST, a URL identifies a resource.\n\n"
                    "A resource is any named piece of information: a user, an order, a document.\n"
                    "The URL is the resource's address. The HTTP method is the action.\n\n"
                    "  /users        → the collection of all users\n"
                    "  /users/42     → a specific user (resource)\n"
                    "  /users/42/orders → orders belonging to user 42\n\n"
                    "URLs should be nouns, not verbs. Use HTTP methods for actions."
                ),
                "options": [
                    "A remote procedure call",
                    "A resource",
                    "A database query",
                    "A server endpoint function",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "REST is resource-oriented. The URL points to a thing, not an action.",
                    "It's a noun — a specific entity or collection the API exposes.",
                ],
            },
            {
                "id": "rest_3",
                "type": "quiz",
                "title": "The Right Method",
                "question": (
                    "You need to create a new user in the system.\n"
                    "Which HTTP method should you use?"
                ),
                "lesson": (
                    "HTTP methods map to CRUD operations:\n\n"
                    "  POST   → Create a new resource\n"
                    "  GET    → Read / retrieve a resource\n"
                    "  PUT    → Update (full replacement) of a resource\n"
                    "  PATCH  → Partial update of a resource\n"
                    "  DELETE → Remove a resource\n\n"
                    "POST is used when the server decides the new resource's URI.\n"
                    "  POST /users  → server creates /users/43 and returns it."
                ),
                "options": [
                    "GET",
                    "PUT",
                    "POST",
                    "PATCH",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "Creating something new — you're sending data to the server to create.",
                    "This method is not idempotent. Calling it twice creates two resources.",
                ],
            },
            {
                "id": "rest_4",
                "type": "quiz",
                "title": "Status Code: Not Found",
                "question": (
                    "A client requests GET /users/999 but that user doesn't exist.\n"
                    "What status code should the server return?"
                ),
                "lesson": (
                    "HTTP status codes communicate the result of a request:\n\n"
                    "  2xx — Success\n"
                    "    200 OK            → request succeeded\n"
                    "    201 Created       → resource created (POST)\n"
                    "    204 No Content    → success, no body (DELETE)\n\n"
                    "  4xx — Client Error\n"
                    "    400 Bad Request   → malformed request\n"
                    "    401 Unauthorized  → not authenticated\n"
                    "    403 Forbidden     → authenticated but not authorized\n"
                    "    404 Not Found     → resource doesn't exist\n"
                    "    409 Conflict      → state conflict\n\n"
                    "  5xx — Server Error\n"
                    "    500 Internal Server Error → unhandled server failure"
                ),
                "options": [
                    "200 OK",
                    "400 Bad Request",
                    "404 Not Found",
                    "500 Internal Server Error",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "The resource was not found. It's a 4xx error — client asked for something missing.",
                    "This is the most well-known 4xx code. You see it in browsers constantly.",
                ],
            },
            {
                "id": "rest_5",
                "type": "quiz",
                "title": "Idempotency",
                "question": (
                    "An idempotent HTTP method produces the same result whether you\n"
                    "call it once or ten times. Which method is NOT idempotent?"
                ),
                "lesson": (
                    "Idempotency means: calling the same request multiple times produces\n"
                    "the same server state as calling it once.\n\n"
                    "Idempotent methods:\n"
                    "  GET    → reading doesn't change state\n"
                    "  PUT    → replacing a resource with the same data is stable\n"
                    "  DELETE → deleting something already deleted is a no-op\n"
                    "  HEAD   → same as GET without a body\n\n"
                    "NOT idempotent:\n"
                    "  POST   → each call may create a new resource\n\n"
                    "Idempotency matters for retries. If a network timeout occurs,\n"
                    "you can safely retry an idempotent request."
                ),
                "options": [
                    "GET",
                    "PUT",
                    "POST",
                    "DELETE",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "Which method creates a new resource each time it's called?",
                    "POST /orders — calling it twice creates two orders, not one.",
                ],
            },
            {
                "id": "rest_6",
                "type": "quiz",
                "title": "Statelessness",
                "question": (
                    "One of REST's core constraints is statelessness.\n"
                    "What does this mean for the server?"
                ),
                "lesson": (
                    "Statelessness: each request from client to server must contain\n"
                    "all the information needed to understand and process the request.\n\n"
                    "The server does not store session state between requests.\n"
                    "Authentication tokens, pagination cursors, filter parameters —\n"
                    "everything travels with the request.\n\n"
                    "Benefits:\n"
                    "  - Any server instance can handle any request (horizontal scaling)\n"
                    "  - No server-side session storage to manage\n"
                    "  - Requests are self-contained and cacheable\n\n"
                    "The client holds the state. The server processes the request."
                ),
                "options": [
                    "The server stores each client's session in memory",
                    "Each request must contain all information needed to process it",
                    "The server caches all previous responses automatically",
                    "Clients must send requests in a specific order",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The server doesn't remember anything between requests.",
                    "Every request is self-contained — it carries everything the server needs.",
                ],
            },
        ],
    },

    # ── ZONE 2: URL DESIGN ────────────────────────────────────────────
    "url_design": {
        "id": "url_design",
        "name": "The Path Matrix",
        "subtitle": "Path Structure, Query Params, Versioning, Plural Nouns & Nesting",
        "color": "green",
        "icon": "🛤️",
        "commands": ["/v1/", "?key=value", "/resources/{id}", "/resources/{id}/sub"],
        "challenges": [
            {
                "id": "url_1",
                "type": "quiz",
                "title": "Plural Resources",
                "question": (
                    "You're designing an endpoint to list all users.\n"
                    "Which URL follows REST naming conventions?"
                ),
                "lesson": (
                    "REST convention: use plural nouns for resource collections.\n\n"
                    "  /users      → collection of users (plural)\n"
                    "  /users/42   → a specific user\n\n"
                    "Why plural?\n"
                    "  GET /users     → returns a list  (consistent with plural)\n"
                    "  GET /users/42  → returns one user (subset of the plural collection)\n"
                    "  POST /users    → creates a new user in the collection\n\n"
                    "Avoid:\n"
                    "  /user       → inconsistent when listing\n"
                    "  /getUsers   → verb in URL (HTTP method handles the verb)\n"
                    "  /user-list  → redundant; the plural already implies a list"
                ),
                "options": [
                    "/user",
                    "/users",
                    "/getUsers",
                    "/user-list",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "REST uses nouns, not verbs. And collections are plural.",
                    "GET /___  should return all users. What's the plural of user?",
                ],
            },
            {
                "id": "url_2",
                "type": "quiz",
                "title": "API Versioning",
                "question": (
                    "Your API has breaking changes. Existing clients still need\n"
                    "the old behavior. What is the most common URL-based versioning strategy?"
                ),
                "lesson": (
                    "URL path versioning is the most common and visible approach:\n\n"
                    "  /v1/users   → version 1\n"
                    "  /v2/users   → version 2 (breaking changes)\n\n"
                    "Other strategies:\n"
                    "  Header:  Accept: application/vnd.myapi.v2+json\n"
                    "  Query:   /users?version=2\n\n"
                    "Path versioning is popular because:\n"
                    "  - It's visible and explicit in every request\n"
                    "  - Easy to route at the load balancer level\n"
                    "  - No ambiguity about which version is being called\n"
                    "  - Easy to document and test separately"
                ),
                "options": [
                    "Add ?version=2 as a query parameter",
                    "Use a custom X-API-Version header",
                    "Include the version in the URL path: /v2/users",
                    "Append the version to the resource: /users-v2",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "The most common approach puts the version right in the URL path.",
                    "Think: /v1/users and /v2/users — the version is a path prefix.",
                ],
            },
            {
                "id": "url_3",
                "type": "quiz",
                "title": "Query Parameters",
                "question": (
                    "You want to filter users by role without changing the resource path.\n"
                    "Where should the filter go?\n\n"
                    "  GET /users ___"
                ),
                "lesson": (
                    "Query parameters are used for filtering, sorting, and pagination.\n\n"
                    "  GET /users?role=admin          → filter by role\n"
                    "  GET /users?sort=created_at      → sort by field\n"
                    "  GET /users?page=2&limit=20      → paginate\n"
                    "  GET /users?role=admin&active=true → multiple filters\n\n"
                    "The path identifies the resource. Query params modify the result set.\n\n"
                    "Convention:\n"
                    "  Path   → identifies WHAT you're accessing\n"
                    "  Query  → modifies HOW the result is returned"
                ),
                "options": [
                    "In the request body as JSON",
                    "In a query string: ?role=admin",
                    "In the URL path: /users/role/admin",
                    "In a custom header: X-Filter-Role: admin",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Filters don't change the resource — they narrow the result set.",
                    "It goes after the ? in the URL. Key=value pairs.",
                ],
            },
            {
                "id": "url_4",
                "type": "quiz",
                "title": "Nested Resources",
                "question": (
                    "You need an endpoint for the orders belonging to user 42.\n"
                    "Which URL correctly represents this nested relationship?"
                ),
                "lesson": (
                    "Nested (sub-resource) URLs express parent-child relationships:\n\n"
                    "  /users/42/orders       → orders belonging to user 42\n"
                    "  /users/42/orders/7     → order 7 of user 42\n\n"
                    "Rules of thumb:\n"
                    "  - Nest only one level deep when possible\n"
                    "  - If the child resource has a global ID, also expose a flat route:\n"
                    "      /orders/7          → same order, accessed directly\n"
                    "  - Deep nesting (/a/1/b/2/c/3) becomes hard to maintain\n\n"
                    "The nested URL makes the ownership relationship explicit."
                ),
                "options": [
                    "/orders?user_id=42",
                    "/users/42/orders",
                    "/users-orders/42",
                    "/getOrdersByUser/42",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The parent resource comes first, then its ID, then the child collection.",
                    "Pattern: /{parent}/{parent_id}/{child}",
                ],
            },
            {
                "id": "url_5",
                "type": "quiz",
                "title": "URL Anti-Patterns",
                "question": (
                    "Which of the following URLs violates REST naming conventions?"
                ),
                "lesson": (
                    "REST URL anti-patterns to avoid:\n\n"
                    "  /getUsers          → verb in URL (use GET /users)\n"
                    "  /deleteUser/42     → verb in URL (use DELETE /users/42)\n"
                    "  /users/create      → verb as path segment\n"
                    "  /api/v1/Users      → inconsistent casing (use lowercase)\n\n"
                    "Good REST URLs:\n"
                    "  - Use lowercase\n"
                    "  - Use hyphens for multi-word: /user-profiles\n"
                    "  - Never use verbs — the HTTP method IS the verb\n"
                    "  - Use plural nouns for collections\n"
                    "  - Keep paths shallow (1-2 nesting levels max)"
                ),
                "options": [
                    "/v1/users/42",
                    "/v1/users?role=admin",
                    "/v1/deleteUser/42",
                    "/v1/users/42/orders",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "One of these has a verb in the URL path. REST uses HTTP methods, not URL verbs.",
                    "DELETE /users/42 is correct. /deleteUser/42 encodes the action in the path.",
                ],
            },
        ],
    },

    # ── ZONE 3: REQUEST & RESPONSE ────────────────────────────────────
    "request_response": {
        "id": "request_response",
        "name": "The Payload Chamber",
        "subtitle": "Headers, Content Types, JSON Structure, Pagination & Filtering",
        "color": "yellow",
        "icon": "📦",
        "commands": ["Content-Type", "Accept", "JSON", "Link", "X-Total-Count"],
        "challenges": [
            {
                "id": "rr_1",
                "type": "quiz",
                "title": "Content-Type Header",
                "question": (
                    "You're sending a JSON body in a POST request.\n"
                    "What Content-Type header should you set?"
                ),
                "lesson": (
                    "Content-Type tells the server what format the request body is in.\n\n"
                    "Common values:\n"
                    "  application/json                → JSON payload\n"
                    "  application/x-www-form-urlencoded → HTML form data\n"
                    "  multipart/form-data             → file uploads\n"
                    "  text/plain                      → plain text\n\n"
                    "For APIs, application/json is the standard. Most modern APIs\n"
                    "both send and receive JSON exclusively."
                ),
                "options": [
                    "text/html",
                    "application/json",
                    "application/xml",
                    "text/plain",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "You're sending JSON. The content type should reflect that.",
                    "The MIME type for JSON is application/json.",
                ],
            },
            {
                "id": "rr_2",
                "type": "quiz",
                "title": "Accept Header",
                "question": (
                    "The Accept header tells the server what response format the client\n"
                    "can handle. What is this process called?"
                ),
                "lesson": (
                    "Content Negotiation: the client tells the server what formats\n"
                    "it accepts, and the server responds accordingly.\n\n"
                    "  Accept: application/json       → client wants JSON\n"
                    "  Accept: application/xml        → client wants XML\n"
                    "  Accept: text/html, application/json → client prefers HTML, accepts JSON\n\n"
                    "If the server can't provide any of the requested formats,\n"
                    "it returns 406 Not Acceptable.\n\n"
                    "Modern APIs typically only support JSON, but the Accept header\n"
                    "remains important for API versioning and format negotiation."
                ),
                "options": [
                    "Content negotiation",
                    "Header forwarding",
                    "MIME encoding",
                    "Request serialization",
                ],
                "answer": "a",
                "xp": 25,
                "hints": [
                    "The client and server are negotiating about the response format.",
                    "It's called content ___. They're agreeing on the content format.",
                ],
            },
            {
                "id": "rr_3",
                "type": "quiz",
                "title": "JSON Envelope",
                "question": (
                    "Which JSON response structure is considered best practice\n"
                    "for returning a list of users?\n\n"
                    "  a) [{...}, {...}]\n"
                    "  b) {\"data\": [{...}, {...}], \"meta\": {...}}\n"
                    "  c) {\"users\": [{...}, {...}]}\n"
                    "  d) \"[{...}, {...}]\""
                ),
                "lesson": (
                    "Wrapping responses in an envelope object is best practice:\n\n"
                    '  {\n'
                    '    "data": [{...}, {...}],\n'
                    '    "meta": {\n'
                    '      "total": 142,\n'
                    '      "page": 1,\n'
                    '      "per_page": 20\n'
                    '    }\n'
                    '  }\n\n'
                    "Why not a bare array?\n"
                    "  - Can't add metadata (pagination, totals) without breaking clients\n"
                    "  - JSON arrays at the top level are vulnerable to certain attacks\n"
                    "  - Harder to extend without breaking backward compatibility\n\n"
                    'The "data" + "meta" pattern is used by most mature APIs.'
                ),
                "options": [
                    "A bare JSON array: [{...}, {...}]",
                    "An envelope: {\"data\": [...], \"meta\": {...}}",
                    "A named key: {\"users\": [...]}",
                    "A JSON string of the array",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Best practice wraps the data in an object with metadata alongside.",
                    "The pattern is called an envelope — data plus meta in a single object.",
                ],
            },
            {
                "id": "rr_4",
                "type": "quiz",
                "title": "Offset Pagination",
                "question": (
                    "Your API returns 10,000 users. You want clients to request\n"
                    "page 3 with 20 results per page. Which query parameters\n"
                    "represent offset-based pagination?"
                ),
                "lesson": (
                    "Offset pagination: page + limit (or offset + limit).\n\n"
                    "  GET /users?page=3&limit=20\n"
                    "  → skips 40 users, returns users 41-60\n\n"
                    "  GET /users?offset=40&limit=20\n"
                    "  → same result, explicit offset\n\n"
                    "Pros: simple, allows jumping to any page\n"
                    "Cons: slow for large offsets (DB must skip N rows)\n\n"
                    "Alternative: Cursor-based pagination\n"
                    "  GET /users?after=cursor_abc&limit=20\n"
                    "  → uses an opaque cursor instead of page number\n"
                    "  → more efficient for large datasets"
                ),
                "options": [
                    "?start=41&end=60",
                    "?page=3&limit=20",
                    "?cursor=abc&count=20",
                    "?range=41-60",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Offset pagination uses a page number and a results-per-page limit.",
                    "page=3 with limit=20 means 'give me the third page of 20 results.'",
                ],
            },
            {
                "id": "rr_5",
                "type": "quiz",
                "title": "Error Response Body",
                "question": (
                    "A 400 Bad Request response should include a body that helps the\n"
                    "client fix the problem. What should that body contain?"
                ),
                "lesson": (
                    "A well-structured error response includes:\n\n"
                    '  {\n'
                    '    "error": {\n'
                    '      "code": "VALIDATION_ERROR",\n'
                    '      "message": "email field is required",\n'
                    '      "details": [\n'
                    '        {"field": "email", "issue": "required"}\n'
                    '      ]\n'
                    '    }\n'
                    '  }\n\n'
                    "Key principles:\n"
                    "  - Machine-readable error code (not just the HTTP status)\n"
                    "  - Human-readable message\n"
                    "  - Field-level details for validation errors\n"
                    "  - Consistent structure across all error responses\n\n"
                    "Never expose stack traces or internal details in production."
                ),
                "options": [
                    "Just the HTTP status code — the body should be empty",
                    "A stack trace so the developer can debug",
                    "A structured error object with code, message, and details",
                    "A plain text string describing the error",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "The error body should be structured, machine-readable, and helpful.",
                    "Include an error code, a message, and field-level details when applicable.",
                ],
            },
            {
                "id": "rr_6",
                "type": "quiz",
                "title": "201 Created",
                "question": (
                    "After successfully creating a resource with POST, the server\n"
                    "should return 201 Created. What header should accompany it?"
                ),
                "lesson": (
                    "When a server creates a resource, best practice is:\n\n"
                    "  HTTP/1.1 201 Created\n"
                    "  Location: /users/43\n"
                    "  Content-Type: application/json\n\n"
                    '  {"id": 43, "name": "Ghost", ...}\n\n'
                    "The Location header tells the client the URL of the newly created\n"
                    "resource. This allows the client to immediately GET the resource\n"
                    "without guessing its URL.\n\n"
                    "The response body should contain the full created resource,\n"
                    "including any server-generated fields (id, timestamps, etc.)."
                ),
                "options": [
                    "X-Created-At with the timestamp",
                    "Location with the URL of the new resource",
                    "X-Resource-Id with the new ID",
                    "Content-Length with the body size",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The server should tell the client WHERE the new resource lives.",
                    "It's a standard HTTP header that provides the URI of the created resource.",
                ],
            },
        ],
    },

    # ── ZONE 4: AUTHENTICATION & API SECURITY ─────────────────────────
    "authentication_apis": {
        "id": "authentication_apis",
        "name": "The Auth Gateway",
        "subtitle": "API Keys, OAuth2, Bearer Tokens, Rate Limiting & CORS",
        "color": "red",
        "icon": "🔐",
        "commands": ["Authorization", "Bearer", "API-Key", "OAuth2", "CORS"],
        "challenges": [
            {
                "id": "auth_1",
                "type": "quiz",
                "title": "API Key Placement",
                "question": (
                    "Your API uses API keys for authentication.\n"
                    "Where is the most secure place to send the key?"
                ),
                "lesson": (
                    "API keys can be sent in three places:\n\n"
                    "  1. Header (recommended):\n"
                    "     Authorization: ApiKey sk-abc123\n"
                    "     X-API-Key: sk-abc123\n\n"
                    "  2. Query parameter (NOT recommended):\n"
                    "     GET /users?api_key=sk-abc123\n"
                    "     → Logged in server access logs, browser history, referrer headers\n\n"
                    "  3. Request body (uncommon):\n"
                    "     Only works for POST/PUT, not GET\n\n"
                    "Headers are the safest: not logged in URLs, not cached by browsers,\n"
                    "not leaked in referrer headers."
                ),
                "options": [
                    "In the URL as a query parameter",
                    "In a request header",
                    "In the URL path segment",
                    "In a browser cookie",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Query parameters end up in logs and browser history. Not secure.",
                    "Headers are not logged in URLs and not leaked through referrer headers.",
                ],
            },
            {
                "id": "auth_2",
                "type": "quiz",
                "title": "OAuth2 Grant Type",
                "question": (
                    "A web application needs to access a user's GitHub data on their\n"
                    "behalf. Which OAuth2 flow is designed for this?"
                ),
                "lesson": (
                    "OAuth2 defines several grant types (flows):\n\n"
                    "  Authorization Code — for server-side apps acting on behalf of a user.\n"
                    "    1. App redirects user to GitHub's authorization page\n"
                    "    2. User approves access\n"
                    "    3. GitHub redirects back with an authorization code\n"
                    "    4. App exchanges the code for an access token (server-to-server)\n\n"
                    "  Client Credentials — machine-to-machine (no user involved)\n"
                    "  Implicit — deprecated (was for SPAs, replaced by PKCE)\n"
                    "  Device Code — for devices without browsers (smart TVs, CLIs)\n\n"
                    "Authorization Code is the most common and most secure for\n"
                    "user-facing applications."
                ),
                "options": [
                    "Client Credentials grant",
                    "Authorization Code grant",
                    "Implicit grant",
                    "Device Code grant",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The user must authorize the app. The app receives a code, then exchanges it for a token.",
                    "This flow involves a redirect to the provider, user consent, and a code exchange.",
                ],
            },
            {
                "id": "auth_3",
                "type": "quiz",
                "title": "Bearer Token",
                "question": (
                    "After OAuth2 authentication, the client sends requests with:\n\n"
                    "  Authorization: Bearer eyJhbGciOi...\n\n"
                    "What does 'Bearer' mean in this context?"
                ),
                "lesson": (
                    "Bearer authentication: whoever bears (holds) the token gets access.\n\n"
                    "  Authorization: Bearer <token>\n\n"
                    "The token is opaque to the client — it doesn't need to understand\n"
                    "its contents. The server validates it on each request.\n\n"
                    "Security implications:\n"
                    "  - Anyone who has the token can use it (no proof of identity)\n"
                    "  - Tokens must be transmitted over HTTPS only\n"
                    "  - Tokens should expire (short-lived: minutes to hours)\n"
                    "  - Refresh tokens provide long-lived access without exposing\n"
                    "    the access token for extended periods"
                ),
                "options": [
                    "The token is encrypted with the client's private key",
                    "Whoever possesses (bears) this token is granted access",
                    "The token was issued by a bearer authority",
                    "The client must bear the cost of token validation",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Think of a bearer bond — whoever holds it can use it.",
                    "'Bearer' means 'whoever has this token gets access.' Possession is proof.",
                ],
            },
            {
                "id": "auth_4",
                "type": "quiz",
                "title": "Rate Limiting",
                "question": (
                    "Your API returns this header:\n\n"
                    "  X-RateLimit-Remaining: 0\n"
                    "  Retry-After: 60\n\n"
                    "What HTTP status code accompanies this response?"
                ),
                "lesson": (
                    "Rate limiting protects APIs from abuse and overuse.\n\n"
                    "  429 Too Many Requests — the client has exceeded the rate limit.\n\n"
                    "Common rate limit headers:\n"
                    "  X-RateLimit-Limit: 100       → max requests per window\n"
                    "  X-RateLimit-Remaining: 0     → requests left in this window\n"
                    "  X-RateLimit-Reset: 1625097600 → when the window resets (epoch)\n"
                    "  Retry-After: 60              → seconds until client can retry\n\n"
                    "Strategies:\n"
                    "  Fixed window  — 100 requests per minute\n"
                    "  Sliding window — 100 requests in any 60-second span\n"
                    "  Token bucket — steady refill rate with burst allowance"
                ),
                "options": [
                    "403 Forbidden",
                    "429 Too Many Requests",
                    "503 Service Unavailable",
                    "408 Request Timeout",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The client hit the rate limit. There's a specific 4xx code for this.",
                    "429 — Too Many Requests. The Retry-After header tells you when to try again.",
                ],
            },
            {
                "id": "auth_5",
                "type": "quiz",
                "title": "CORS Preflight",
                "question": (
                    "A browser-based app at app.example.com calls api.example.com.\n"
                    "The browser sends an OPTIONS request before the actual request.\n"
                    "What is this called?"
                ),
                "lesson": (
                    "CORS (Cross-Origin Resource Sharing) preflight request:\n\n"
                    "When a browser makes a cross-origin request that isn't 'simple'\n"
                    "(e.g., has custom headers, uses PUT/DELETE), the browser first sends\n"
                    "an OPTIONS request — the preflight — asking the server:\n"
                    "  'Will you accept this request from this origin?'\n\n"
                    "The server responds with:\n"
                    "  Access-Control-Allow-Origin: https://app.example.com\n"
                    "  Access-Control-Allow-Methods: GET, POST, PUT\n"
                    "  Access-Control-Allow-Headers: Authorization, Content-Type\n\n"
                    "If the server approves, the browser sends the real request.\n"
                    "If not, the browser blocks it — the request never leaves.\n\n"
                    "CORS is a browser security mechanism. Server-to-server calls\n"
                    "are not affected."
                ),
                "options": [
                    "A CORS preflight request",
                    "A TLS handshake",
                    "A DNS lookup",
                    "A proxy redirect",
                ],
                "answer": "a",
                "xp": 30,
                "hints": [
                    "The browser checks with the server before making the real cross-origin request.",
                    "It's an OPTIONS request sent automatically — called a preflight.",
                ],
            },
            {
                "id": "auth_6",
                "type": "quiz",
                "title": "401 vs 403",
                "question": (
                    "What is the difference between 401 Unauthorized and 403 Forbidden?"
                ),
                "lesson": (
                    "These two status codes are commonly confused:\n\n"
                    "  401 Unauthorized — actually means UNAUTHENTICATED.\n"
                    "    The server doesn't know who you are.\n"
                    "    Fix: provide valid credentials (login, send a token).\n\n"
                    "  403 Forbidden — means UNAUTHORIZED.\n"
                    "    The server knows who you are, but you don't have permission.\n"
                    "    Fix: request elevated permissions or use a different account.\n\n"
                    "The naming is historically misleading:\n"
                    "  401 = 'I don't know who you are' (authentication)\n"
                    "  403 = 'I know who you are, and the answer is no' (authorization)"
                ),
                "options": [
                    "401 means bad request; 403 means server error",
                    "401 means not authenticated; 403 means authenticated but not authorized",
                    "401 means not found; 403 means method not allowed",
                    "They are interchangeable — both mean access denied",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "One is about identity (who are you?), the other is about permission (can you do this?).",
                    "401 = unknown identity. 403 = known identity, insufficient permissions.",
                ],
            },
        ],
    },

    # ── ZONE 5: GRAPHQL BASICS ────────────────────────────────────────
    "graphql_basics": {
        "id": "graphql_basics",
        "name": "The Query Nexus",
        "subtitle": "Schema, Queries, Mutations, Resolvers, N+1 Problem & REST Tradeoffs",
        "color": "magenta",
        "icon": "◆",
        "commands": ["query", "mutation", "schema", "resolver", "type"],
        "challenges": [
            {
                "id": "gql_1",
                "type": "quiz",
                "title": "GraphQL Core Concept",
                "question": (
                    "In GraphQL, the client specifies exactly which fields it wants\n"
                    "in the response. What problem does this solve compared to REST?"
                ),
                "lesson": (
                    "GraphQL solves two key REST problems:\n\n"
                    "  Over-fetching: REST returns all fields, even if the client only\n"
                    "    needs two. GET /users/42 returns name, email, address, avatar,\n"
                    "    preferences — even if you only need the name.\n\n"
                    "  Under-fetching: getting related data requires multiple REST calls.\n"
                    "    GET /users/42, then GET /users/42/orders, then GET /orders/7/items.\n\n"
                    "GraphQL query:\n"
                    "  query {\n"
                    "    user(id: 42) {\n"
                    "      name\n"
                    "      orders { id, total }\n"
                    "    }\n"
                    "  }\n\n"
                    "One request. Exact fields. No wasted bandwidth."
                ),
                "options": [
                    "Over-fetching and under-fetching",
                    "SQL injection vulnerabilities",
                    "Cross-origin request blocking",
                    "Server-side caching",
                ],
                "answer": "a",
                "xp": 25,
                "hints": [
                    "REST returns too much data or requires too many requests.",
                    "Over-fetching = too many fields. Under-fetching = too many round trips.",
                ],
            },
            {
                "id": "gql_2",
                "type": "quiz",
                "title": "Schema Definition",
                "question": (
                    "In GraphQL, what defines the types, fields, and relationships\n"
                    "that clients can query?"
                ),
                "lesson": (
                    "The GraphQL schema is the contract between client and server.\n\n"
                    "  type User {\n"
                    "    id: ID!\n"
                    "    name: String!\n"
                    "    email: String\n"
                    "    orders: [Order!]!\n"
                    "  }\n\n"
                    "  type Query {\n"
                    "    user(id: ID!): User\n"
                    "    users: [User!]!\n"
                    "  }\n\n"
                    "Key concepts:\n"
                    "  ! = non-nullable (field is guaranteed to exist)\n"
                    "  [Type!]! = non-nullable list of non-nullable items\n"
                    "  Query type = entry point for all read operations\n\n"
                    "The schema is strongly typed and introspectable — clients can\n"
                    "discover what's available automatically."
                ),
                "options": [
                    "The resolver functions",
                    "The schema",
                    "The endpoint URL",
                    "The database tables",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It's the type system that defines what clients can ask for.",
                    "The ___ defines types, fields, and their relationships. It's the contract.",
                ],
            },
            {
                "id": "gql_3",
                "type": "quiz",
                "title": "Mutations",
                "question": (
                    "In GraphQL, what operation type is used to create, update,\n"
                    "or delete data?"
                ),
                "lesson": (
                    "GraphQL operations:\n\n"
                    "  query    → read data (like GET)\n"
                    "  mutation → write data (like POST/PUT/DELETE)\n"
                    "  subscription → real-time updates (WebSocket)\n\n"
                    "Example mutation:\n"
                    "  mutation {\n"
                    "    createUser(input: {name: \"Ghost\", email: \"g@x.com\"}) {\n"
                    "      id\n"
                    "      name\n"
                    "    }\n"
                    "  }\n\n"
                    "Mutations return data just like queries — you specify which fields\n"
                    "of the result you want. This avoids a follow-up query after writes."
                ),
                "options": [
                    "query",
                    "mutation",
                    "subscription",
                    "action",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Writes that mutate (change) the data.",
                    "query reads. ___ writes. The name describes what it does to the data.",
                ],
            },
            {
                "id": "gql_4",
                "type": "quiz",
                "title": "Resolvers",
                "question": (
                    "In a GraphQL server, what component is responsible for\n"
                    "fetching the actual data for each field in the schema?"
                ),
                "lesson": (
                    "Resolvers: functions that populate each field in the schema.\n\n"
                    "  const resolvers = {\n"
                    "    Query: {\n"
                    "      user: (parent, { id }) => db.users.findById(id),\n"
                    "    },\n"
                    "    User: {\n"
                    "      orders: (user) => db.orders.findByUserId(user.id),\n"
                    "    },\n"
                    "  };\n\n"
                    "Each field in the schema has a resolver. When a client queries\n"
                    "a field, the corresponding resolver is called to fetch data.\n\n"
                    "Resolver chain: Query.user → User.name, User.orders → Order.total\n"
                    "The parent's result is passed to child resolvers."
                ),
                "options": [
                    "Middleware",
                    "Controllers",
                    "Resolvers",
                    "Adapters",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "Each field in the schema has one. It resolves the query to actual data.",
                    "They're called ___ because they resolve a field to its concrete value.",
                ],
            },
            {
                "id": "gql_5",
                "type": "quiz",
                "title": "The N+1 Problem",
                "question": (
                    "You query 50 users and their orders. The user resolver runs once,\n"
                    "but the orders resolver runs 50 times — one per user.\n"
                    "What is this called, and what solves it?"
                ),
                "lesson": (
                    "The N+1 problem:\n"
                    "  1 query for the list of users\n"
                    "  + N queries for each user's orders (one per user)\n"
                    "  = N+1 database queries for what should be 2\n\n"
                    "Solution: DataLoader (batching + caching)\n\n"
                    "  Instead of:\n"
                    "    SELECT * FROM orders WHERE user_id = 1\n"
                    "    SELECT * FROM orders WHERE user_id = 2\n"
                    "    ... (50 queries)\n\n"
                    "  DataLoader batches into:\n"
                    "    SELECT * FROM orders WHERE user_id IN (1, 2, ..., 50)\n\n"
                    "DataLoader collects all resolver calls in a single tick,\n"
                    "batches them into one query, and distributes results back."
                ),
                "options": [
                    "The N+1 problem, solved by DataLoader batching",
                    "The race condition problem, solved by mutexes",
                    "The circular dependency problem, solved by lazy loading",
                    "The deadlock problem, solved by connection pooling",
                ],
                "answer": "a",
                "xp": 35,
                "hints": [
                    "1 query for the parent + N queries for each child = N+1.",
                    "DataLoader batches the N individual queries into a single batch query.",
                ],
            },
            {
                "id": "gql_6",
                "type": "quiz",
                "title": "REST vs GraphQL",
                "question": (
                    "When is REST a better choice than GraphQL?"
                ),
                "lesson": (
                    "REST advantages over GraphQL:\n\n"
                    "  - Simple CRUD with well-defined resources → REST is simpler\n"
                    "  - HTTP caching works natively (each URL is cacheable)\n"
                    "  - File uploads are straightforward\n"
                    "  - Monitoring: each endpoint has distinct metrics\n"
                    "  - Simpler to rate-limit (per endpoint)\n\n"
                    "GraphQL advantages:\n"
                    "  - Complex, nested data in a single request\n"
                    "  - Client-driven queries (mobile gets less data than web)\n"
                    "  - Strong typing and introspection\n"
                    "  - Eliminates API versioning (add fields, deprecate old ones)\n\n"
                    "Neither is universally better. The choice depends on the data shape,\n"
                    "client diversity, and team expertise."
                ),
                "options": [
                    "When clients need deeply nested data in one request",
                    "When different clients need different fields from the same resource",
                    "When the API serves simple CRUD and HTTP caching is important",
                    "When the API needs to avoid over-fetching",
                ],
                "answer": "c",
                "xp": 35,
                "hints": [
                    "REST is simpler for straightforward resources and benefits from HTTP-level caching.",
                    "Simple CRUD + caching = REST. Complex nested queries = GraphQL.",
                ],
            },
        ],
    },

    # ── ZONE 6: API DOCUMENTATION ─────────────────────────────────────
    "api_documentation": {
        "id": "api_documentation",
        "name": "The Spec Vault",
        "subtitle": "OpenAPI/Swagger, Endpoint Docs, Examples, SDKs & Developer Experience",
        "color": "blue",
        "icon": "📜",
        "commands": ["openapi", "swagger", "paths", "components", "examples"],
        "challenges": [
            {
                "id": "doc_1",
                "type": "quiz",
                "title": "OpenAPI Specification",
                "question": (
                    "What is the industry standard format for describing REST APIs\n"
                    "in a machine-readable way?"
                ),
                "lesson": (
                    "OpenAPI Specification (formerly Swagger):\n\n"
                    "A standard, language-agnostic format for describing REST APIs.\n"
                    "Written in YAML or JSON, it defines:\n"
                    "  - Endpoints (paths and methods)\n"
                    "  - Request/response schemas\n"
                    "  - Authentication methods\n"
                    "  - Parameters, headers, and examples\n\n"
                    "  openapi: 3.0.0\n"
                    "  info:\n"
                    "    title: User API\n"
                    "    version: 1.0.0\n"
                    "  paths:\n"
                    "    /users:\n"
                    "      get:\n"
                    "        summary: List all users\n"
                    "        responses:\n"
                    "          '200':\n"
                    "            description: Success\n\n"
                    "Tools like Swagger UI render it into interactive documentation."
                ),
                "options": [
                    "WSDL",
                    "OpenAPI (Swagger)",
                    "RAML",
                    "API Blueprint",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It was originally called Swagger. Now it has a more generic name.",
                    "The ___ Specification is the most widely adopted API description format.",
                ],
            },
            {
                "id": "doc_2",
                "type": "quiz",
                "title": "Try-It-Out",
                "question": (
                    "Swagger UI renders an OpenAPI spec into interactive documentation.\n"
                    "What key feature makes it more than just static docs?"
                ),
                "lesson": (
                    "Swagger UI's killer feature: 'Try it out'\n\n"
                    "Developers can make real API calls directly from the documentation\n"
                    "page — no curl, no Postman, no code required.\n\n"
                    "Interactive docs:\n"
                    "  1. Developer reads the endpoint description\n"
                    "  2. Clicks 'Try it out'\n"
                    "  3. Fills in parameters\n"
                    "  4. Sees the real response\n\n"
                    "This reduces time-to-first-call dramatically. A developer who can\n"
                    "make a working API call in under 5 minutes is far more likely to\n"
                    "adopt your API."
                ),
                "options": [
                    "Automatic SDK generation",
                    "Built-in rate limit monitoring",
                    "Interactive 'Try it out' to make live API calls",
                    "Automatic API versioning",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "It lets developers test the API without leaving the documentation page.",
                    "You can make real requests from the browser. 'Try it ___.'",
                ],
            },
            {
                "id": "doc_3",
                "type": "quiz",
                "title": "Request Examples",
                "question": (
                    "What is the single most important element of API documentation\n"
                    "for developer adoption?"
                ),
                "lesson": (
                    "Working code examples are the #1 factor in API adoption.\n\n"
                    "Developers don't read documentation linearly — they scan for\n"
                    "an example they can copy, modify, and run.\n\n"
                    "Best practices:\n"
                    "  - Show a complete curl command for every endpoint\n"
                    "  - Include the full request AND response\n"
                    "  - Show examples in multiple languages (curl, Python, JS)\n"
                    "  - Use realistic data, not 'foo' and 'bar'\n"
                    "  - Show error responses too, not just happy paths\n\n"
                    "Stripe, Twilio, and GitHub are gold standards for API docs\n"
                    "because every endpoint has copy-pasteable examples."
                ),
                "options": [
                    "A comprehensive changelog",
                    "Working code examples with real requests and responses",
                    "UML diagrams of the data model",
                    "A formal API specification in WSDL",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Developers want to copy, paste, and run. What enables that?",
                    "Working code ___ that show real requests and responses.",
                ],
            },
            {
                "id": "doc_4",
                "type": "quiz",
                "title": "SDK Generation",
                "question": (
                    "An OpenAPI spec can be used to automatically generate client\n"
                    "libraries in multiple languages. What are these called?"
                ),
                "lesson": (
                    "SDKs (Software Development Kits) — client libraries that wrap\n"
                    "your API in language-native code.\n\n"
                    "  Instead of:\n"
                    "    response = requests.get('/users/42',\n"
                    "        headers={'Authorization': 'Bearer tok'})\n\n"
                    "  SDK provides:\n"
                    "    user = client.users.get(42)\n\n"
                    "Tools like openapi-generator can auto-generate SDKs from your\n"
                    "OpenAPI spec in Python, JavaScript, Java, Go, Ruby, and more.\n\n"
                    "Benefits:\n"
                    "  - Type safety and IDE autocomplete\n"
                    "  - Handles auth, retries, and serialization\n"
                    "  - Reduces time-to-integration for developers"
                ),
                "options": [
                    "Middleware plugins",
                    "API gateways",
                    "SDKs (Software Development Kits)",
                    "Service meshes",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "Client libraries generated from the spec. They wrap HTTP calls in native code.",
                    "SDK stands for Software Development ___.",
                ],
            },
            {
                "id": "doc_5",
                "type": "quiz",
                "title": "Developer Experience",
                "question": (
                    "What term describes the overall quality of a developer's experience\n"
                    "when integrating with your API — including docs, errors, SDKs,\n"
                    "and onboarding?"
                ),
                "lesson": (
                    "DX (Developer Experience) — the API equivalent of UX.\n\n"
                    "Great DX includes:\n"
                    "  - Clear, accurate documentation with examples\n"
                    "  - Helpful error messages with actionable details\n"
                    "  - Consistent naming and predictable behavior\n"
                    "  - Quick time-to-first-call (< 5 minutes)\n"
                    "  - SDKs in popular languages\n"
                    "  - A sandbox/test environment\n"
                    "  - Clear rate limit communication\n\n"
                    "Companies like Stripe have built their market position largely\n"
                    "on superior DX. The API that's easiest to integrate with wins,\n"
                    "even if it's not the most feature-rich."
                ),
                "options": [
                    "API governance",
                    "Developer Experience (DX)",
                    "Service Level Agreement (SLA)",
                    "Technical debt management",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "It's like UX but for developers. The overall quality of the integration experience.",
                    "DX — Developer ___. How pleasant and efficient is it to use your API?",
                ],
            },
        ],
    },

    # ── ZONE 7: API TESTING ───────────────────────────────────────────
    "api_testing": {
        "id": "api_testing",
        "name": "The Test Grid",
        "subtitle": "Postman, curl, Integration Tests, Contract Testing & Mocking",
        "color": "white",
        "icon": "🧪",
        "commands": ["curl", "postman", "newman", "pact", "mock"],
        "challenges": [
            {
                "id": "test_1",
                "type": "quiz",
                "title": "curl Basics",
                "question": (
                    "What curl flag sets the HTTP method for a request?\n\n"
                    "  curl ___ DELETE https://api.example.com/users/42"
                ),
                "lesson": (
                    "curl — command-line tool for making HTTP requests.\n\n"
                    "Key flags:\n"
                    "  -X METHOD    → set the HTTP method (GET, POST, PUT, DELETE)\n"
                    "  -H 'Header'  → add a request header\n"
                    "  -d 'data'    → send request body data\n"
                    "  -i           → include response headers in output\n"
                    "  -v           → verbose mode (shows full request/response)\n"
                    "  -o file      → save response to file\n\n"
                    "Examples:\n"
                    "  curl -X POST -H 'Content-Type: application/json' \\\n"
                    "    -d '{\"name\": \"Ghost\"}' https://api.example.com/users\n\n"
                    "Note: GET is the default method, so -X GET is optional."
                ),
                "options": [
                    "-H",
                    "-d",
                    "-X",
                    "-o",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "It specifies which HTTP method to use. Think: reQuest method.",
                    "The flag is -X, followed by the method name: -X DELETE, -X POST.",
                ],
            },
            {
                "id": "test_2",
                "type": "quiz",
                "title": "Postman Collections",
                "question": (
                    "Postman allows you to group related API requests into a\n"
                    "reusable, shareable set. What is this called?"
                ),
                "lesson": (
                    "Postman Collections: groups of saved API requests.\n\n"
                    "A collection can contain:\n"
                    "  - Multiple requests organized in folders\n"
                    "  - Pre-request scripts (set variables, generate tokens)\n"
                    "  - Test scripts (assert status codes, validate response bodies)\n"
                    "  - Environment variables (swap between dev/staging/prod)\n\n"
                    "Collections can be:\n"
                    "  - Shared with team members\n"
                    "  - Version controlled\n"
                    "  - Run via Newman (Postman's CLI runner) in CI/CD\n"
                    "  - Published as API documentation"
                ),
                "options": [
                    "A workspace",
                    "A collection",
                    "A suite",
                    "A manifest",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It's a group of requests you can save, share, and run together.",
                    "Postman ___ — the term for a saved group of API requests.",
                ],
            },
            {
                "id": "test_3",
                "type": "quiz",
                "title": "Integration Testing",
                "question": (
                    "You want to test that your API endpoint returns the correct\n"
                    "status code, headers, and response body against a real running\n"
                    "server. What type of test is this?"
                ),
                "lesson": (
                    "Integration tests verify that components work together correctly.\n\n"
                    "For APIs, integration tests:\n"
                    "  - Hit real endpoints (not mocks)\n"
                    "  - Verify status codes, headers, and response bodies\n"
                    "  - Test the full request/response cycle\n"
                    "  - May use a test database or staging environment\n\n"
                    "Example (Python / pytest):\n"
                    "  def test_create_user():\n"
                    "      response = client.post('/users',\n"
                    "          json={'name': 'Ghost'})\n"
                    "      assert response.status_code == 201\n"
                    "      assert response.json()['name'] == 'Ghost'\n"
                    "      assert 'id' in response.json()\n\n"
                    "Integration tests catch issues that unit tests miss:\n"
                    "serialization bugs, auth middleware, database constraints."
                ),
                "options": [
                    "Unit test",
                    "Integration test",
                    "Load test",
                    "Smoke test",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "It tests the integration between client and server — the full cycle.",
                    "Not a unit test (too isolated) or a load test (not about performance).",
                ],
            },
            {
                "id": "test_4",
                "type": "quiz",
                "title": "Contract Testing",
                "question": (
                    "Team A builds the frontend. Team B builds the API. They need\n"
                    "to ensure the API response structure doesn't break the frontend.\n"
                    "What testing approach verifies this agreement?"
                ),
                "lesson": (
                    "Contract testing: verifying that a provider (API) and a consumer\n"
                    "(frontend/client) agree on the interface.\n\n"
                    "Tools: Pact, Spring Cloud Contract\n\n"
                    "How Pact works:\n"
                    "  1. Consumer defines expected interactions (contracts)\n"
                    "     'When I call GET /users/42, I expect {id, name, email}'\n"
                    "  2. Contracts are published to a Pact broker\n"
                    "  3. Provider runs the contracts against its actual implementation\n"
                    "  4. If the provider breaks a contract, the test fails\n\n"
                    "Contract tests catch breaking changes before deployment.\n"
                    "They're especially valuable in microservice architectures where\n"
                    "multiple teams own different services."
                ),
                "options": [
                    "End-to-end testing",
                    "Contract testing",
                    "Regression testing",
                    "Acceptance testing",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "It tests the contract — the agreed-upon interface between producer and consumer.",
                    "Pact is the most well-known tool for this type of testing.",
                ],
            },
            {
                "id": "test_5",
                "type": "quiz",
                "title": "API Mocking",
                "question": (
                    "The backend API isn't built yet, but the frontend team needs\n"
                    "to start development. What technique lets them work against\n"
                    "a fake API that returns realistic responses?"
                ),
                "lesson": (
                    "API mocking: creating a fake API server that returns predefined\n"
                    "responses, allowing parallel development.\n\n"
                    "Tools:\n"
                    "  - Postman mock servers\n"
                    "  - WireMock (Java ecosystem)\n"
                    "  - MSW (Mock Service Worker — browser/Node.js)\n"
                    "  - Prism (generates mocks from OpenAPI specs)\n"
                    "  - json-server (instant REST API from a JSON file)\n\n"
                    "Benefits:\n"
                    "  - Frontend and backend develop in parallel\n"
                    "  - Tests run without external dependencies\n"
                    "  - Simulate error conditions and edge cases\n"
                    "  - No network latency in test suites\n\n"
                    "A mock derived from the OpenAPI spec guarantees the fake\n"
                    "responses match the real API's structure."
                ),
                "options": [
                    "API mocking",
                    "API proxying",
                    "API caching",
                    "API throttling",
                ],
                "answer": "a",
                "xp": 30,
                "hints": [
                    "A fake API that returns realistic but predetermined responses.",
                    "___ lets you simulate an API that doesn't exist yet.",
                ],
            },
            {
                "id": "test_6",
                "type": "quiz",
                "title": "Newman CLI",
                "question": (
                    "You want to run your Postman collection as part of your CI/CD\n"
                    "pipeline. What tool runs Postman collections from the command line?"
                ),
                "lesson": (
                    "Newman: Postman's command-line collection runner.\n\n"
                    "  npx newman run collection.json \\\n"
                    "    --environment staging.json \\\n"
                    "    --reporters cli,junit\n\n"
                    "Newman enables:\n"
                    "  - Running Postman tests in CI/CD (GitHub Actions, Jenkins, etc.)\n"
                    "  - Automated regression testing of APIs\n"
                    "  - JUnit/HTML reports for test results\n"
                    "  - Environment variable injection for different stages\n\n"
                    "Workflow:\n"
                    "  1. Create and test requests in Postman GUI\n"
                    "  2. Export the collection as JSON\n"
                    "  3. Run with Newman in your pipeline\n"
                    "  4. Fail the build if any test assertions fail"
                ),
                "options": [
                    "Postman CLI",
                    "Newman",
                    "Insomnia",
                    "HTTPie",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "It's Postman's official CLI runner, named after a certain mail carrier.",
                    "The tool is called ___. It runs Postman collections from the terminal.",
                ],
            },
        ],
    },
}
