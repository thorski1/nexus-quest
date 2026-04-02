"""
zones.py — GraphQL zones and challenges for The Query Nexus.

5 zones, 40 challenges. Mix of quiz (multiple-choice) and text challenges.
"""

ZONE_ORDER = [
    "schema_types",
    "queries_mutations",
    "resolvers_dataloading",
    "subscriptions_realtime",
    "graphql_production",
]

ZONES = {
    # ── ZONE 1: SCHEMA & TYPES ───────────────────────────────────────
    "schema_types": {
        "id": "schema_types",
        "name": "The Type Lattice",
        "subtitle": "Schema Definition Language, Scalar Types, Objects, Enums & Interfaces",
        "color": "cyan",
        "icon": "{}",
        "commands": ["type", "scalar", "enum", "interface", "union"],
        "challenges": [
            {
                "id": "schema_1",
                "type": "quiz",
                "title": "Schema Definition Language",
                "question": (
                    "GraphQL APIs are defined by a schema written in a specific language.\n"
                    "What is the name of the language used to define GraphQL schemas?"
                ),
                "lesson": (
                    "SDL — Schema Definition Language — is the syntax used to define\n"
                    "GraphQL schemas. It describes the types, fields, and relationships\n"
                    "that make up your API's contract.\n\n"
                    "  type User {\n"
                    "    id: ID!\n"
                    "    name: String!\n"
                    "    email: String\n"
                    "  }\n\n"
                    "SDL is declarative and language-agnostic. The schema IS the API contract."
                ),
                "options": [
                    "JSON Schema",
                    "Schema Definition Language (SDL)",
                    "Protocol Buffers",
                    "OpenAPI Specification",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It's specific to GraphQL and uses the keyword 'type' to define objects.",
                    "The abbreviation is SDL — it looks like a simplified type system.",
                ],
            },
            {
                "id": "schema_2",
                "type": "quiz",
                "title": "Non-Null Types",
                "question": (
                    "In a GraphQL schema, what does the exclamation mark signify?\n\n"
                    "  type User {\n"
                    "    id: ID!\n"
                    "    name: String!\n"
                    "    bio: String\n"
                    "  }"
                ),
                "lesson": (
                    "The `!` suffix in GraphQL means non-null. The field is guaranteed\n"
                    "to never return null.\n\n"
                    "  id: ID!       → always returns a value\n"
                    "  bio: String   → may return null\n\n"
                    "Non-null is a contract with the client. If a non-null field resolves\n"
                    "to null, GraphQL propagates the null up to the nearest nullable parent.\n"
                    "This can cause entire objects to become null — so use `!` deliberately."
                ),
                "options": [
                    "The field is deprecated",
                    "The field is non-null (required)",
                    "The field is unique",
                    "The field is indexed",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It's a nullability modifier — it constrains what the field can return.",
                    "Fields without it can return null. Fields with it cannot.",
                ],
            },
            {
                "id": "schema_3",
                "type": "quiz",
                "title": "Scalar Types",
                "question": (
                    "GraphQL has five built-in scalar types.\n"
                    "Which of these is NOT a built-in GraphQL scalar?"
                ),
                "lesson": (
                    "The five built-in GraphQL scalars are:\n\n"
                    "  Int      → signed 32-bit integer\n"
                    "  Float    → signed double-precision floating-point\n"
                    "  String   → UTF-8 character sequence\n"
                    "  Boolean  → true or false\n"
                    "  ID       → unique identifier (serialized as String)\n\n"
                    "Date, DateTime, JSON, and URL are NOT built-in. You must define\n"
                    "them as custom scalars: `scalar DateTime`"
                ),
                "options": [
                    "Int",
                    "Boolean",
                    "DateTime",
                    "ID",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "Think about which types need custom serialization/parsing logic.",
                    "Time-related types are not part of the GraphQL specification.",
                ],
            },
            {
                "id": "schema_4",
                "type": "text",
                "title": "Object Type Definition",
                "question": (
                    "In GraphQL SDL, what keyword do you use to define a new object type?\n\n"
                    "For example, to define a Product with fields id and name,\n"
                    "what keyword starts the definition?\n\n"
                    "Answer with the single keyword (lowercase)."
                ),
                "lesson": (
                    "The `type` keyword defines a new object type in GraphQL SDL:\n\n"
                    "  type Product {\n"
                    "    id: ID!\n"
                    "    name: String!\n"
                    "    price: Float!\n"
                    "  }\n\n"
                    "Object types are the building blocks of your schema. They describe\n"
                    "the shape of the data your API exposes. Every field on an object type\n"
                    "has a type of its own — either a scalar, enum, or another object type."
                ),
                "options": [],
                "answer": "type",
                "xp": 30,
                "hints": [
                    "It's the same keyword many typed languages use to define structures.",
                    "In SDL you write: _____ Product { id: ID! }",
                ],
            },
            {
                "id": "schema_5",
                "type": "quiz",
                "title": "Enum Types",
                "question": (
                    "You need to restrict a field to a fixed set of values:\n"
                    "PENDING, SHIPPED, DELIVERED, CANCELLED.\n\n"
                    "Which GraphQL type construct should you use?"
                ),
                "lesson": (
                    "Enums define a type restricted to a fixed set of values:\n\n"
                    "  enum OrderStatus {\n"
                    "    PENDING\n"
                    "    SHIPPED\n"
                    "    DELIVERED\n"
                    "    CANCELLED\n"
                    "  }\n\n"
                    "  type Order {\n"
                    "    id: ID!\n"
                    "    status: OrderStatus!\n"
                    "  }\n\n"
                    "Enums provide type safety and self-documentation. The schema itself\n"
                    "tells clients exactly which values are valid."
                ),
                "options": [
                    "union",
                    "enum",
                    "scalar",
                    "interface",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "This is a closed set of named values — a common pattern in typed languages.",
                    "The construct name is the same as in Java, TypeScript, or Rust.",
                ],
            },
            {
                "id": "schema_6",
                "type": "quiz",
                "title": "Interfaces",
                "question": (
                    "Multiple types share common fields: id, createdAt, updatedAt.\n"
                    "Which GraphQL construct lets you define shared fields that\n"
                    "multiple types must implement?"
                ),
                "lesson": (
                    "An interface defines a set of fields that implementing types must include:\n\n"
                    "  interface Node {\n"
                    "    id: ID!\n"
                    "    createdAt: DateTime!\n"
                    "    updatedAt: DateTime!\n"
                    "  }\n\n"
                    "  type User implements Node {\n"
                    "    id: ID!\n"
                    "    createdAt: DateTime!\n"
                    "    updatedAt: DateTime!\n"
                    "    name: String!\n"
                    "  }\n\n"
                    "Interfaces enable polymorphic queries — you can query a field that\n"
                    "returns a Node and get any implementing type back."
                ),
                "options": [
                    "interface",
                    "union",
                    "abstract type",
                    "mixin",
                ],
                "answer": "a",
                "xp": 30,
                "hints": [
                    "It's the same concept as interfaces in Java or TypeScript.",
                    "Types that share fields 'implement' this construct.",
                ],
            },
            {
                "id": "schema_7",
                "type": "quiz",
                "title": "Union Types",
                "question": (
                    "A search API can return Users, Posts, or Comments.\n"
                    "These types share NO common fields.\n"
                    "Which GraphQL construct represents 'one of these types'?"
                ),
                "lesson": (
                    "A union type represents a value that could be one of several types:\n\n"
                    "  union SearchResult = User | Post | Comment\n\n"
                    "  type Query {\n"
                    "    search(term: String!): [SearchResult!]!\n"
                    "  }\n\n"
                    "Unlike interfaces, union members don't need shared fields.\n"
                    "Clients use inline fragments to select fields per type:\n\n"
                    "  ... on User { name email }\n"
                    "  ... on Post { title body }"
                ),
                "options": [
                    "enum",
                    "interface",
                    "union",
                    "abstract",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "The types share no common fields — interfaces require shared fields.",
                    "This construct uses the | (pipe) operator in SDL syntax.",
                ],
            },
            {
                "id": "schema_8",
                "type": "quiz",
                "title": "Input Types",
                "question": (
                    "You need to pass a complex object as an argument to a mutation.\n"
                    "GraphQL doesn't allow regular object types as arguments.\n"
                    "What special type construct is required for mutation arguments?"
                ),
                "lesson": (
                    "Input types are special object types used for arguments:\n\n"
                    "  input CreateUserInput {\n"
                    "    name: String!\n"
                    "    email: String!\n"
                    "    role: Role\n"
                    "  }\n\n"
                    "  type Mutation {\n"
                    "    createUser(input: CreateUserInput!): User!\n"
                    "  }\n\n"
                    "Regular `type` objects can have resolvers and circular references.\n"
                    "Input types cannot — they must be serializable as JSON arguments.\n"
                    "This separation is intentional: inputs and outputs have different constraints."
                ),
                "options": [
                    "argument type",
                    "input type",
                    "parameter type",
                    "request type",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The keyword in SDL is 'input', not 'type'.",
                    "input CreateUserInput { ... } — a dedicated construct for arguments.",
                ],
            },
        ],
    },

    # ── ZONE 2: QUERIES & MUTATIONS ───────────────────────────────────
    "queries_mutations": {
        "id": "queries_mutations",
        "name": "The Operation Grid",
        "subtitle": "Queries, Mutations, Variables, Fragments & Directives",
        "color": "green",
        "icon": ">_",
        "commands": ["query", "mutation", "fragment", "variable", "directive"],
        "challenges": [
            {
                "id": "qm_1",
                "type": "quiz",
                "title": "Root Operation Types",
                "question": (
                    "Every GraphQL schema has up to three root operation types.\n"
                    "Which of these is NOT a root operation type in GraphQL?"
                ),
                "lesson": (
                    "GraphQL has exactly three root operation types:\n\n"
                    "  Query        → read operations (like GET)\n"
                    "  Mutation     → write operations (like POST/PUT/DELETE)\n"
                    "  Subscription → real-time streaming operations\n\n"
                    "Every GraphQL request starts at one of these root types.\n"
                    "Only Query is required — Mutation and Subscription are optional."
                ),
                "options": [
                    "Query",
                    "Mutation",
                    "Action",
                    "Subscription",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "There are exactly three. One for reading, one for writing, one for streaming.",
                    "'Action' is not a GraphQL concept — it belongs to REST or Redux.",
                ],
            },
            {
                "id": "qm_2",
                "type": "quiz",
                "title": "Query Selection Sets",
                "question": (
                    "What is the key advantage of GraphQL queries over REST endpoints\n"
                    "when it comes to the data returned to the client?"
                ),
                "lesson": (
                    "GraphQL lets clients specify exactly which fields they need:\n\n"
                    "  query {\n"
                    "    user(id: 42) {\n"
                    "      name\n"
                    "      email\n"
                    "    }\n"
                    "  }\n\n"
                    "The server returns only name and email — nothing more.\n"
                    "REST endpoints typically return fixed response shapes, leading to:\n\n"
                    "  Over-fetching: getting fields you don't need\n"
                    "  Under-fetching: needing multiple requests for related data\n\n"
                    "Selection sets eliminate both problems."
                ),
                "options": [
                    "Faster server-side processing",
                    "Clients choose exactly which fields are returned",
                    "Automatic caching of all responses",
                    "Built-in pagination for all queries",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It solves over-fetching and under-fetching.",
                    "The client sends a selection set specifying the exact fields needed.",
                ],
            },
            {
                "id": "qm_3",
                "type": "text",
                "title": "Variable Syntax",
                "question": (
                    "In a GraphQL operation, variables are prefixed with a special character.\n\n"
                    "  query GetUser(___id: ID!) {\n"
                    "    user(id: ___id) { name }\n"
                    "  }\n\n"
                    "What single character prefixes variable names in GraphQL?\n"
                    "Answer with just the character."
                ),
                "lesson": (
                    "The `$` character prefixes all variable names in GraphQL:\n\n"
                    "  query GetUser($id: ID!) {\n"
                    "    user(id: $id) {\n"
                    "      name\n"
                    "      email\n"
                    "    }\n"
                    "  }\n\n"
                    "Variables are defined in the operation signature with their types,\n"
                    "then passed as a separate JSON object:\n\n"
                    "  { \"id\": \"42\" }\n\n"
                    "This separates the query structure from the runtime values,\n"
                    "enabling query caching and preventing injection attacks."
                ),
                "options": [],
                "answer": "$",
                "xp": 30,
                "hints": [
                    "It's a common prefix for variables in shell scripting and PHP too.",
                    "query GetUser($id: ID!) — the character before 'id'.",
                ],
            },
            {
                "id": "qm_4",
                "type": "quiz",
                "title": "Fragments",
                "question": (
                    "You're querying the same set of User fields in multiple places.\n"
                    "Which GraphQL feature lets you define a reusable set of fields?"
                ),
                "lesson": (
                    "Fragments define reusable sets of fields on a specific type:\n\n"
                    "  fragment UserBasic on User {\n"
                    "    id\n"
                    "    name\n"
                    "    email\n"
                    "  }\n\n"
                    "  query {\n"
                    "    currentUser { ...UserBasic }\n"
                    "    adminUsers { ...UserBasic role }\n"
                    "  }\n\n"
                    "Fragments reduce query duplication and keep clients DRY.\n"
                    "They're also the foundation of Relay's container pattern,\n"
                    "where each component declares its own data requirements."
                ),
                "options": [
                    "Aliases",
                    "Fragments",
                    "Directives",
                    "Mixins",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "They use the spread syntax: ...FragmentName",
                    "Defined with 'fragment Name on Type { fields }'",
                ],
            },
            {
                "id": "qm_5",
                "type": "quiz",
                "title": "Aliases",
                "question": (
                    "You need to query the same field twice with different arguments\n"
                    "in a single request. How do you avoid field name collisions?\n\n"
                    "  query {\n"
                    "    ???: user(id: 1) { name }\n"
                    "    ???: user(id: 2) { name }\n"
                    "  }"
                ),
                "lesson": (
                    "Aliases let you rename fields in the response to avoid collisions:\n\n"
                    "  query {\n"
                    "    alice: user(id: 1) { name }\n"
                    "    bob: user(id: 2) { name }\n"
                    "  }\n\n"
                    "Response:\n"
                    "  {\n"
                    "    \"alice\": { \"name\": \"Alice\" },\n"
                    "    \"bob\": { \"name\": \"Bob\" }\n"
                    "  }\n\n"
                    "Without aliases, you can't have two fields with the same name\n"
                    "in one selection set — JSON keys must be unique."
                ),
                "options": [
                    "Aliases",
                    "Fragments",
                    "Variables",
                    "Directives",
                ],
                "answer": "a",
                "xp": 25,
                "hints": [
                    "You prefix the field with a custom name followed by a colon.",
                    "alice: user(id: 1) — 'alice' is the _____ for the user field.",
                ],
            },
            {
                "id": "qm_6",
                "type": "quiz",
                "title": "Built-in Directives",
                "question": (
                    "Which built-in GraphQL directive conditionally includes a field\n"
                    "based on a Boolean variable?\n\n"
                    "  query GetUser($withEmail: Boolean!) {\n"
                    "    user(id: 1) {\n"
                    "      name\n"
                    "      email ???($withEmail)\n"
                    "    }\n"
                    "  }"
                ),
                "lesson": (
                    "GraphQL has three built-in directives:\n\n"
                    "  @include(if: Boolean!) → include field when true\n"
                    "  @skip(if: Boolean!)    → skip field when true\n"
                    "  @deprecated(reason: String) → mark field as deprecated\n\n"
                    "  query GetUser($withEmail: Boolean!) {\n"
                    "    user(id: 1) {\n"
                    "      name\n"
                    "      email @include(if: $withEmail)\n"
                    "    }\n"
                    "  }\n\n"
                    "Directives modify query behavior without changing the schema.\n"
                    "Custom directives (e.g., @auth, @cache) extend this pattern."
                ),
                "options": [
                    "@include(if: $withEmail)",
                    "@when(if: $withEmail)",
                    "@show(if: $withEmail)",
                    "@filter(if: $withEmail)",
                ],
                "answer": "a",
                "xp": 30,
                "hints": [
                    "It's one of three built-in directives: @include, @skip, @deprecated.",
                    "To conditionally include a field, you use @include(if: ...).",
                ],
            },
            {
                "id": "qm_7",
                "type": "quiz",
                "title": "Mutation Conventions",
                "question": (
                    "Which is a best practice for structuring GraphQL mutation responses?"
                ),
                "lesson": (
                    "A well-designed mutation returns enough data for the client\n"
                    "to update its local cache without a follow-up query:\n\n"
                    "  mutation {\n"
                    "    createUser(input: { name: \"Alice\" }) {\n"
                    "      user {\n"
                    "        id\n"
                    "        name\n"
                    "        createdAt\n"
                    "      }\n"
                    "      errors {\n"
                    "        field\n"
                    "        message\n"
                    "      }\n"
                    "    }\n"
                    "  }\n\n"
                    "Returning a payload type with the mutated object AND structured\n"
                    "errors lets clients handle success and failure in one response.\n"
                    "This avoids the need for a refetch after every mutation."
                ),
                "options": [
                    "Return only a success Boolean",
                    "Return the mutated object so the client can update its cache",
                    "Always return the entire database record",
                    "Return a redirect URL to fetch the result",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The goal is to avoid a follow-up query after the mutation.",
                    "If the mutation returns the updated object, the client cache stays fresh.",
                ],
            },
            {
                "id": "qm_8",
                "type": "quiz",
                "title": "Inline Fragments",
                "question": (
                    "A query returns a union type: `SearchResult = User | Post`.\n"
                    "How do you select type-specific fields in the query?"
                ),
                "lesson": (
                    "Inline fragments select fields based on the concrete type:\n\n"
                    "  query {\n"
                    "    search(term: \"alice\") {\n"
                    "      ... on User {\n"
                    "        name\n"
                    "        email\n"
                    "      }\n"
                    "      ... on Post {\n"
                    "        title\n"
                    "        body\n"
                    "      }\n"
                    "    }\n"
                    "  }\n\n"
                    "The `... on Type` syntax is an inline fragment. It tells GraphQL:\n"
                    "'if this result is a User, return these fields; if it's a Post,\n"
                    "return those fields.'\n\n"
                    "You can also request __typename to know which type was returned."
                ),
                "options": [
                    "Type guards with typeof checks",
                    "Inline fragments with ... on Type { }",
                    "Switch statements in the query",
                    "Separate queries for each type",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The syntax uses the spread operator (...) with 'on' and the type name.",
                    "... on User { name } — this is an inline ________.",
                ],
            },
        ],
    },

    # ── ZONE 3: RESOLVERS & DATA LOADING ─────────────────────────────
    "resolvers_dataloading": {
        "id": "resolvers_dataloading",
        "name": "The Resolver Core",
        "subtitle": "Resolver Functions, Context, N+1 Problem, DataLoader & Batching",
        "color": "yellow",
        "icon": "fn",
        "commands": ["resolve", "context", "batch", "dataloader", "parent"],
        "challenges": [
            {
                "id": "res_1",
                "type": "quiz",
                "title": "Resolver Function Signature",
                "question": (
                    "A GraphQL resolver function receives four arguments.\n"
                    "Which is the correct order of parameters?"
                ),
                "lesson": (
                    "Every resolver receives four arguments:\n\n"
                    "  (parent, args, context, info)\n\n"
                    "  parent  → the return value of the parent resolver\n"
                    "  args    → the arguments passed to this field\n"
                    "  context → shared state (auth, DB connections, loaders)\n"
                    "  info    → AST and schema metadata about the query\n\n"
                    "Most resolvers only use 2-3 of these. The `context` argument is\n"
                    "where you inject database connections, authentication state,\n"
                    "and DataLoaders — anything shared across the resolver chain."
                ),
                "options": [
                    "(args, context, parent, info)",
                    "(parent, args, context, info)",
                    "(context, parent, args, info)",
                    "(info, parent, args, context)",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Parent comes first — it's the return value from the level above.",
                    "The mnemonic: 'PACI' — parent, args, context, info.",
                ],
            },
            {
                "id": "res_2",
                "type": "quiz",
                "title": "The N+1 Problem",
                "question": (
                    "A query fetches 50 users, and for each user fetches their profile.\n"
                    "Without optimization, how many database queries are executed?"
                ),
                "lesson": (
                    "The N+1 problem is the most common GraphQL performance issue:\n\n"
                    "  1 query to fetch 50 users\n"
                    "  + 50 queries to fetch each user's profile\n"
                    "  = 51 total queries\n\n"
                    "This happens because each field resolver runs independently.\n"
                    "The user resolver fetches the list, then the profile resolver\n"
                    "fires once per user, each making its own DB call.\n\n"
                    "The solution: DataLoader — batch and cache individual loads\n"
                    "into a single query per tick of the event loop."
                ),
                "options": [
                    "1",
                    "2",
                    "50",
                    "51",
                ],
                "answer": "d",
                "xp": 30,
                "hints": [
                    "One query for the list, then one query per item in the list.",
                    "N items + 1 initial query = N+1. With 50 users, that's 51.",
                ],
            },
            {
                "id": "res_3",
                "type": "text",
                "title": "DataLoader Pattern",
                "question": (
                    "Facebook created a library to solve the N+1 problem by batching\n"
                    "individual loads into a single database query per event loop tick.\n\n"
                    "What is the name of this library/pattern?\n"
                    "Answer with the single word (case-insensitive)."
                ),
                "lesson": (
                    "DataLoader batches and caches individual load calls:\n\n"
                    "  Instead of:\n"
                    "    SELECT * FROM profiles WHERE user_id = 1\n"
                    "    SELECT * FROM profiles WHERE user_id = 2\n"
                    "    ... (50 times)\n\n"
                    "  DataLoader combines them into:\n"
                    "    SELECT * FROM profiles WHERE user_id IN (1, 2, ..., 50)\n\n"
                    "DataLoader collects all load(id) calls within a single tick of\n"
                    "the event loop, then executes one batched query. It also caches\n"
                    "results within the request to avoid duplicate loads.\n\n"
                    "A new DataLoader instance should be created per request to\n"
                    "avoid cross-request cache pollution."
                ),
                "options": [],
                "answer": "dataloader",
                "xp": 35,
                "hints": [
                    "It's a utility from Facebook — the name describes what it does.",
                    "It loads data — batched. Data + Loader.",
                ],
            },
            {
                "id": "res_4",
                "type": "quiz",
                "title": "Context Object",
                "question": (
                    "Where should you store shared resources like database connections,\n"
                    "authenticated user info, and DataLoader instances in a\n"
                    "GraphQL server?"
                ),
                "lesson": (
                    "The context object is the shared state for a single request:\n\n"
                    "  const server = new ApolloServer({\n"
                    "    schema,\n"
                    "    context: ({ req }) => ({\n"
                    "      db: database,\n"
                    "      user: authenticateToken(req.headers.authorization),\n"
                    "      loaders: createLoaders(),\n"
                    "    }),\n"
                    "  });\n\n"
                    "Context is created fresh per request and passed to every resolver.\n"
                    "It's the right place for:\n"
                    "  - Database/ORM connections\n"
                    "  - Authenticated user identity\n"
                    "  - DataLoader instances\n"
                    "  - Request-scoped caches"
                ),
                "options": [
                    "In global variables",
                    "In the GraphQL context object",
                    "In the schema definition",
                    "In resolver closures",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It's the third argument passed to every resolver: (parent, args, ???, info).",
                    "A per-request object created in server setup and shared across resolvers.",
                ],
            },
            {
                "id": "res_5",
                "type": "quiz",
                "title": "Default Resolvers",
                "question": (
                    "If you don't define a resolver for a field on an object type,\n"
                    "what does GraphQL do by default?"
                ),
                "lesson": (
                    "GraphQL has a default resolver that returns `parent[fieldName]`:\n\n"
                    "  // If User type has a 'name' field with no explicit resolver:\n"
                    "  // The default resolver does:\n"
                    "  (parent) => parent.name\n\n"
                    "This means if your database returns objects whose property names\n"
                    "match your schema field names, you don't need to write resolvers\n"
                    "for those fields at all.\n\n"
                    "You only need explicit resolvers for:\n"
                    "  - Computed fields\n"
                    "  - Fields that require database lookups\n"
                    "  - Fields whose names differ from the data source"
                ),
                "options": [
                    "Throws a runtime error",
                    "Returns null for that field",
                    "Returns the matching property from the parent object",
                    "Skips the field entirely",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "The default behavior is intuitive — it looks for a matching key.",
                    "parent['fieldName'] — property access on the parent value.",
                ],
            },
            {
                "id": "res_6",
                "type": "quiz",
                "title": "Resolver Chain",
                "question": (
                    "Consider this query:\n\n"
                    "  query {\n"
                    "    user(id: 1) {\n"
                    "      posts {\n"
                    "        author {\n"
                    "          name\n"
                    "        }\n"
                    "      }\n"
                    "    }\n"
                    "  }\n\n"
                    "What value does the `author` resolver receive as its `parent` argument?"
                ),
                "lesson": (
                    "Resolvers form a chain. Each resolver's return value becomes\n"
                    "the `parent` argument of its child resolvers:\n\n"
                    "  Query.user → returns a User object\n"
                    "    User.posts → parent is the User; returns [Post]\n"
                    "      Post.author → parent is a Post; returns a User\n"
                    "        User.name → parent is the author User\n\n"
                    "The `parent` argument is how data flows down the resolver tree.\n"
                    "Each level receives the result of the level above it."
                ),
                "options": [
                    "The root Query object",
                    "The User object from the user resolver",
                    "A single Post object from the posts array",
                    "The entire query variables",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "The author field is on the Post type. Its parent is a Post.",
                    "Resolvers run per-item in lists — each Post gets its own author resolver.",
                ],
            },
            {
                "id": "res_7",
                "type": "quiz",
                "title": "Batching Strategy",
                "question": (
                    "DataLoader requires a batch function. What constraint must the\n"
                    "batch function's return value satisfy?"
                ),
                "lesson": (
                    "The batch function must return an array of values (or errors)\n"
                    "in the SAME ORDER as the input keys:\n\n"
                    "  const batchUsers = async (ids) => {\n"
                    "    const users = await db.users.findByIds(ids);\n"
                    "    // Must map results back to input order!\n"
                    "    return ids.map(id => \n"
                    "      users.find(u => u.id === id) || new Error(`No user: ${id}`)\n"
                    "    );\n"
                    "  };\n\n"
                    "If you pass [3, 1, 2], you must return [user3, user1, user2].\n"
                    "DataLoader maps results back to callers by index position."
                ),
                "options": [
                    "Results must be sorted alphabetically by ID",
                    "Results must match the input keys array in length and order",
                    "Results must be wrapped in a Promise.all",
                    "Results must include a status code for each item",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "DataLoader uses array index to match results back to callers.",
                    "Same length, same order — one result per input key.",
                ],
            },
            {
                "id": "res_8",
                "type": "text",
                "title": "Per-Request Loaders",
                "question": (
                    "DataLoader caches loaded values within its instance.\n"
                    "To prevent data from one user's request leaking to another,\n"
                    "how often should you create new DataLoader instances?\n\n"
                    "Answer: per ________ (one word)"
                ),
                "lesson": (
                    "DataLoader instances must be created per request:\n\n"
                    "  // In your context factory:\n"
                    "  context: () => ({\n"
                    "    loaders: {\n"
                    "      userLoader: new DataLoader(batchUsers),\n"
                    "      postLoader: new DataLoader(batchPosts),\n"
                    "    }\n"
                    "  })\n\n"
                    "Each DataLoader maintains an in-memory cache. If you share a\n"
                    "DataLoader across requests:\n"
                    "  - User A loads user 42 (cached)\n"
                    "  - User B gets user 42 from cache — even if they lack permission\n\n"
                    "Per-request instances prevent cache pollution and ensure\n"
                    "authorization boundaries are respected."
                ),
                "options": [],
                "answer": "request",
                "xp": 30,
                "hints": [
                    "Each incoming HTTP request should get its own set of loaders.",
                    "The cache lives for exactly one ________ lifecycle.",
                ],
            },
        ],
    },

    # ── ZONE 4: SUBSCRIPTIONS & REAL-TIME ─────────────────────────────
    "subscriptions_realtime": {
        "id": "subscriptions_realtime",
        "name": "The Event Stream",
        "subtitle": "Subscriptions, WebSockets, PubSub, Live Queries & Event-Driven Architecture",
        "color": "magenta",
        "icon": "~~",
        "commands": ["subscribe", "publish", "websocket", "pubsub", "event"],
        "challenges": [
            {
                "id": "sub_1",
                "type": "quiz",
                "title": "Subscription Transport",
                "question": (
                    "GraphQL subscriptions maintain a persistent connection to push\n"
                    "updates to the client. What transport protocol is typically used?"
                ),
                "lesson": (
                    "WebSockets are the standard transport for GraphQL subscriptions:\n\n"
                    "  Client → WebSocket handshake → Server\n"
                    "  Client ← subscription data    ← Server (pushed on events)\n\n"
                    "Unlike HTTP request/response, WebSockets maintain a persistent\n"
                    "bidirectional connection. The server can push data at any time\n"
                    "without the client polling.\n\n"
                    "The graphql-ws protocol (replacing the older subscriptions-transport-ws)\n"
                    "is the modern standard for GraphQL over WebSockets."
                ),
                "options": [
                    "HTTP long polling",
                    "WebSockets",
                    "Server-Sent Events (SSE)",
                    "gRPC streams",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It's a persistent, bidirectional connection protocol.",
                    "The protocol that lets the server push data to the client at any time.",
                ],
            },
            {
                "id": "sub_2",
                "type": "quiz",
                "title": "Subscription Schema",
                "question": (
                    "How do you define a subscription in a GraphQL schema?\n\n"
                    "  type ??? {\n"
                    "    messageCreated(roomId: ID!): Message\n"
                    "  }"
                ),
                "lesson": (
                    "Subscriptions are defined under the `Subscription` root type:\n\n"
                    "  type Subscription {\n"
                    "    messageCreated(roomId: ID!): Message\n"
                    "    orderUpdated(orderId: ID!): Order\n"
                    "  }\n\n"
                    "Each field on the Subscription type represents a distinct event\n"
                    "stream. Clients subscribe to specific fields:\n\n"
                    "  subscription {\n"
                    "    messageCreated(roomId: \"general\") {\n"
                    "      id\n"
                    "      text\n"
                    "      author { name }\n"
                    "    }\n"
                    "  }\n\n"
                    "The server pushes new data whenever the subscribed event fires."
                ),
                "options": [
                    "Subscription",
                    "Stream",
                    "EventSource",
                    "Listener",
                ],
                "answer": "a",
                "xp": 25,
                "hints": [
                    "It's one of the three root operation types in GraphQL.",
                    "Query, Mutation, and __________ — the third root type.",
                ],
            },
            {
                "id": "sub_3",
                "type": "quiz",
                "title": "PubSub Pattern",
                "question": (
                    "In a GraphQL subscription resolver, what mechanism notifies\n"
                    "subscribers when new data is available?"
                ),
                "lesson": (
                    "The Publish/Subscribe (PubSub) pattern connects mutations\n"
                    "to subscriptions:\n\n"
                    "  // Mutation resolver\n"
                    "  createMessage: (_, { input }, { pubsub }) => {\n"
                    "    const message = db.messages.create(input);\n"
                    "    pubsub.publish('MESSAGE_CREATED', { messageCreated: message });\n"
                    "    return message;\n"
                    "  }\n\n"
                    "  // Subscription resolver\n"
                    "  messageCreated: {\n"
                    "    subscribe: (_, { roomId }, { pubsub }) => \n"
                    "      pubsub.asyncIterator('MESSAGE_CREATED')\n"
                    "  }\n\n"
                    "The mutation publishes events. The subscription listens for them.\n"
                    "PubSub is the bridge between writes and real-time updates."
                ),
                "options": [
                    "Polling the database at intervals",
                    "A PubSub (publish/subscribe) system",
                    "Direct WebSocket messages from the mutation",
                    "Database triggers that call the resolver",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The pattern name describes two roles: one publishes, one subscribes.",
                    "Mutations publish events; subscriptions listen via asyncIterator.",
                ],
            },
            {
                "id": "sub_4",
                "type": "quiz",
                "title": "Scaling Subscriptions",
                "question": (
                    "An in-memory PubSub works for a single server instance.\n"
                    "What do you need when running multiple server instances?"
                ),
                "lesson": (
                    "In-memory PubSub only works for a single process. When you\n"
                    "scale to multiple server instances behind a load balancer:\n\n"
                    "  Server A publishes event → only Server A's subscribers get it\n"
                    "  Server B's subscribers miss the event entirely\n\n"
                    "Solution: use an external PubSub backend:\n\n"
                    "  - Redis PubSub (most common)\n"
                    "  - Apache Kafka\n"
                    "  - Google Cloud Pub/Sub\n"
                    "  - RabbitMQ\n\n"
                    "Redis PubSub is the go-to choice: all servers publish and subscribe\n"
                    "to Redis. When Server A publishes, Redis broadcasts to all servers,\n"
                    "and each server pushes to its local WebSocket clients."
                ),
                "options": [
                    "Sticky sessions on the load balancer",
                    "An external PubSub backend like Redis",
                    "Shared memory between server instances",
                    "Database polling instead of subscriptions",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "You need a centralized message broker that all servers connect to.",
                    "Redis PubSub is the most common choice for this.",
                ],
            },
            {
                "id": "sub_5",
                "type": "text",
                "title": "AsyncIterator",
                "question": (
                    "In a GraphQL subscription resolver, the `subscribe` function\n"
                    "must return a special type of iterator that yields values\n"
                    "asynchronously over time.\n\n"
                    "What is this called? (two words, camelCase, e.g., asyncIterator)"
                ),
                "lesson": (
                    "The subscribe function returns an AsyncIterator:\n\n"
                    "  messageCreated: {\n"
                    "    subscribe: (_, args, { pubsub }) =>\n"
                    "      pubsub.asyncIterator(['MESSAGE_CREATED'])\n"
                    "  }\n\n"
                    "An AsyncIterator is a JavaScript protocol for objects that produce\n"
                    "a sequence of values asynchronously. It implements:\n\n"
                    "  { [Symbol.asyncIterator](): { next(): Promise<IteratorResult> } }\n\n"
                    "Each time PubSub fires an event, the AsyncIterator yields the\n"
                    "next value, and GraphQL pushes it to the client over WebSocket."
                ),
                "options": [],
                "answer": "asyncIterator",
                "xp": 35,
                "hints": [
                    "It's an async version of the iterator protocol.",
                    "pubsub.________(['MESSAGE_CREATED']) — the method name.",
                ],
            },
            {
                "id": "sub_6",
                "type": "quiz",
                "title": "Subscription Filtering",
                "question": (
                    "A chat app has hundreds of rooms. A subscriber only wants messages\n"
                    "from room 'general'. How do you filter subscription events?"
                ),
                "lesson": (
                    "Use a `withFilter` wrapper to filter events before they reach\n"
                    "the subscriber:\n\n"
                    "  import { withFilter } from 'graphql-subscriptions';\n\n"
                    "  messageCreated: {\n"
                    "    subscribe: withFilter(\n"
                    "      (_, __, { pubsub }) => pubsub.asyncIterator('MESSAGE_CREATED'),\n"
                    "      (payload, variables) => \n"
                    "        payload.messageCreated.roomId === variables.roomId\n"
                    "    )\n"
                    "  }\n\n"
                    "Without filtering, every subscriber receives every event and\n"
                    "must discard irrelevant ones client-side — wasteful and insecure."
                ),
                "options": [
                    "Filter on the client side after receiving all events",
                    "Use a withFilter function in the subscribe resolver",
                    "Create separate PubSub channels per room",
                    "Use GraphQL directives to filter events",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Filtering should happen server-side before pushing to the client.",
                    "The function wraps the asyncIterator with a predicate function.",
                ],
            },
            {
                "id": "sub_7",
                "type": "quiz",
                "title": "Subscription vs Polling",
                "question": (
                    "When should you prefer GraphQL subscriptions over polling\n"
                    "with periodic queries?"
                ),
                "lesson": (
                    "Use subscriptions when:\n"
                    "  - Events are infrequent and unpredictable (chat messages, alerts)\n"
                    "  - Low latency is critical (real-time dashboards, gaming)\n"
                    "  - Multiple clients need instant updates\n\n"
                    "Use polling when:\n"
                    "  - Data changes frequently and regularly (stock tickers at 1s intervals)\n"
                    "  - WebSocket infrastructure isn't available\n"
                    "  - Simplicity outweighs latency requirements\n\n"
                    "Subscriptions add infrastructure complexity: WebSocket servers,\n"
                    "PubSub backends, connection management, and reconnection logic.\n"
                    "Don't use subscriptions when polling at a reasonable interval works."
                ),
                "options": [
                    "Always — subscriptions are strictly better than polling",
                    "When data changes are infrequent and low-latency updates are needed",
                    "Only for mobile clients",
                    "When the data changes every second",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Subscriptions shine for unpredictable, infrequent events that need instant delivery.",
                    "If data changes every second, polling at 1s is simpler than maintaining WebSockets.",
                ],
            },
            {
                "id": "sub_8",
                "type": "quiz",
                "title": "Connection Lifecycle",
                "question": (
                    "In the graphql-ws protocol, what must the client send first\n"
                    "after the WebSocket connection is established?"
                ),
                "lesson": (
                    "The graphql-ws protocol has a defined handshake:\n\n"
                    "  1. Client establishes WebSocket connection\n"
                    "  2. Client sends ConnectionInit message (with optional auth payload)\n"
                    "  3. Server validates and responds with ConnectionAck\n"
                    "  4. Client can now send Subscribe messages\n\n"
                    "  Client → { type: 'connection_init', payload: { token: '...' } }\n"
                    "  Server → { type: 'connection_ack' }\n"
                    "  Client → { type: 'subscribe', id: '1', payload: { query: '...' } }\n"
                    "  Server → { type: 'next', id: '1', payload: { data: { ... } } }\n\n"
                    "The ConnectionInit message is where authentication happens.\n"
                    "The server can reject the connection before any queries execute."
                ),
                "options": [
                    "A Subscribe message with the query",
                    "A ConnectionInit message",
                    "An authentication HTTP header",
                    "A ping/pong heartbeat",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "It's the initialization step — before any subscriptions can be created.",
                    "ConnectionInit comes first, then ConnectionAck from the server.",
                ],
            },
        ],
    },

    # ── ZONE 5: GRAPHQL IN PRODUCTION ──────────────────────────────────
    "graphql_production": {
        "id": "graphql_production",
        "name": "The Federation Matrix",
        "subtitle": "Federation, Schema Stitching, Caching, Security, Rate Limiting & Performance",
        "color": "red",
        "icon": "!!",
        "commands": ["federate", "cache", "persisted", "depthLimit", "introspection"],
        "challenges": [
            {
                "id": "prod_1",
                "type": "quiz",
                "title": "Apollo Federation",
                "question": (
                    "Your company has 5 teams, each owning a microservice.\n"
                    "Each team wants to contribute types to a single GraphQL API.\n"
                    "What architecture pattern solves this?"
                ),
                "lesson": (
                    "Apollo Federation composes multiple GraphQL services (subgraphs)\n"
                    "into a single unified API (supergraph):\n\n"
                    "  Users Subgraph:    type User { id: ID!, name: String! }\n"
                    "  Orders Subgraph:   type Order { id: ID!, user: User! }\n"
                    "  Products Subgraph: type Product { id: ID!, price: Float! }\n\n"
                    "  → Apollo Gateway combines them into one schema\n"
                    "  → Clients query one endpoint, get data from all services\n\n"
                    "Each team owns their subgraph independently — they deploy,\n"
                    "iterate, and scale their piece of the schema without coordinating\n"
                    "with every other team."
                ),
                "options": [
                    "Schema stitching with manual resolvers",
                    "GraphQL Federation (e.g., Apollo Federation)",
                    "A single monolithic GraphQL server",
                    "REST APIs behind a GraphQL proxy",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Multiple subgraphs composed into a supergraph by a gateway.",
                    "Apollo's architecture for microservice-based GraphQL.",
                ],
            },
            {
                "id": "prod_2",
                "type": "quiz",
                "title": "Query Depth Limiting",
                "question": (
                    "A malicious client sends a deeply nested query:\n"
                    "  { user { friends { friends { friends { friends { ... } } } } } }\n\n"
                    "What server-side protection prevents this attack?"
                ),
                "lesson": (
                    "Query depth limiting restricts how deeply nested a query can be:\n\n"
                    "  // Apollo Server example\n"
                    "  import depthLimit from 'graphql-depth-limit';\n\n"
                    "  const server = new ApolloServer({\n"
                    "    validationRules: [depthLimit(5)],\n"
                    "  });\n\n"
                    "A depth limit of 5 means: Query → user → friends → posts → author → name\n"
                    "is allowed, but going deeper is rejected before execution.\n\n"
                    "Depth limiting is one of several protections:\n"
                    "  - Query depth limiting\n"
                    "  - Query complexity analysis\n"
                    "  - Persisted queries (whitelist)\n"
                    "  - Timeout enforcement"
                ),
                "options": [
                    "Query depth limiting",
                    "Rate limiting by IP address",
                    "CORS restrictions",
                    "Response size limits",
                ],
                "answer": "a",
                "xp": 30,
                "hints": [
                    "The attack vector is depth — the protection targets depth.",
                    "A validation rule that rejects queries exceeding a nesting threshold.",
                ],
            },
            {
                "id": "prod_3",
                "type": "quiz",
                "title": "Persisted Queries",
                "question": (
                    "In production, sending full query strings with every request\n"
                    "wastes bandwidth and exposes your API's query surface.\n"
                    "What technique replaces query strings with hashes?"
                ),
                "lesson": (
                    "Automatic Persisted Queries (APQ) replace query strings with hashes:\n\n"
                    "  1. Client hashes the query: sha256(query) → 'abc123'\n"
                    "  2. Client sends: { extensions: { persistedQuery: { sha256Hash: 'abc123' } } }\n"
                    "  3. Server looks up hash → finds cached query → executes it\n"
                    "  4. If miss: client resends with full query, server caches it\n\n"
                    "Benefits:\n"
                    "  - Smaller request payloads (hash vs. full query string)\n"
                    "  - Allowlisting: only pre-registered queries can execute\n"
                    "  - Prevents arbitrary query attacks in production\n"
                    "  - CDN caching with GET requests using query hash"
                ),
                "options": [
                    "Query minification",
                    "Persisted queries / Automatic Persisted Queries (APQ)",
                    "GraphQL query compression",
                    "Server-side query generation",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "The client sends a hash; the server looks up the full query.",
                    "APQ — Automatic _________ Queries.",
                ],
            },
            {
                "id": "prod_4",
                "type": "quiz",
                "title": "Caching Challenges",
                "question": (
                    "HTTP caching works well with REST because each URL is a unique\n"
                    "resource. Why is caching harder in GraphQL?"
                ),
                "lesson": (
                    "GraphQL typically uses a single endpoint (POST /graphql) for\n"
                    "all operations. This breaks HTTP caching:\n\n"
                    "  REST:    GET /users/42  → cacheable by URL\n"
                    "  GraphQL: POST /graphql  → every request hits the same URL\n\n"
                    "Solutions:\n"
                    "  - Client-side normalized caching (Apollo Client, urql)\n"
                    "  - CDN caching with APQ + GET requests\n"
                    "  - Response-level caching with @cacheControl directives\n"
                    "  - Field-level caching in resolvers (Redis, Memcached)\n\n"
                    "Apollo Client's normalized cache stores entities by type + ID,\n"
                    "so updating a User anywhere updates it everywhere in the UI."
                ),
                "options": [
                    "GraphQL responses are too large to cache",
                    "GraphQL uses a single endpoint, so URL-based HTTP caching doesn't work",
                    "GraphQL doesn't support ETags",
                    "Clients always request different fields",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "REST caches by URL. GraphQL sends everything to POST /graphql.",
                    "When every request goes to the same URL, CDN/proxy caches can't differentiate.",
                ],
            },
            {
                "id": "prod_5",
                "type": "quiz",
                "title": "Introspection in Production",
                "question": (
                    "GraphQL introspection lets clients query the schema itself:\n"
                    "  { __schema { types { name } } }\n\n"
                    "What should you do with introspection in production?"
                ),
                "lesson": (
                    "Introspection exposes your entire API surface — every type,\n"
                    "every field, every argument, every description:\n\n"
                    "  { __schema { types { name fields { name type { name } } } } }\n\n"
                    "In development: essential for tooling (GraphiQL, Apollo Studio).\n"
                    "In production: a reconnaissance goldmine for attackers.\n\n"
                    "Best practice: disable introspection in production.\n\n"
                    "  const server = new ApolloServer({\n"
                    "    introspection: process.env.NODE_ENV !== 'production',\n"
                    "  });\n\n"
                    "Use schema registries (Apollo Studio, Hive) for team access\n"
                    "to the schema without exposing it via introspection."
                ),
                "options": [
                    "Leave it enabled for developer convenience",
                    "Disable it to prevent schema reconnaissance",
                    "Rate limit introspection queries",
                    "Cache introspection responses",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Introspection reveals your entire API surface to anyone.",
                    "Attackers use it to map every type and field before targeting vulnerabilities.",
                ],
            },
            {
                "id": "prod_6",
                "type": "text",
                "title": "Query Complexity",
                "question": (
                    "Beyond depth limiting, you can assign a cost to each field\n"
                    "and reject queries whose total cost exceeds a threshold.\n\n"
                    "What is this technique called?\n"
                    "Answer: query _________ analysis (one word)"
                ),
                "lesson": (
                    "Query complexity analysis assigns a cost to each field:\n\n"
                    "  type Query {\n"
                    "    users(limit: Int): [User]  # cost: limit * 5\n"
                    "    user(id: ID!): User         # cost: 1\n"
                    "  }\n\n"
                    "  type User {\n"
                    "    posts: [Post]  # cost: 10 (list field)\n"
                    "    name: String   # cost: 0 (scalar)\n"
                    "  }\n\n"
                    "Before executing a query, the server calculates total cost.\n"
                    "If cost exceeds the threshold (e.g., 1000), the query is rejected.\n\n"
                    "This catches wide queries that depth limiting misses:\n"
                    "  { users(limit: 1000) { posts { comments { ... } } } }\n"
                    "Depth = 3 (passes depth limit) but cost = astronomical."
                ),
                "options": [],
                "answer": "complexity",
                "xp": 35,
                "hints": [
                    "Each field has a cost. Total cost is the _________ of the query.",
                    "The analysis measures how computationally expensive a query is.",
                ],
            },
            {
                "id": "prod_7",
                "type": "quiz",
                "title": "Federation @key Directive",
                "question": (
                    "In Apollo Federation, how does the Orders subgraph reference\n"
                    "a User type that's defined in the Users subgraph?"
                ),
                "lesson": (
                    "Federation uses the @key directive to define entity identity\n"
                    "and cross-subgraph references:\n\n"
                    "  // Users subgraph\n"
                    "  type User @key(fields: \"id\") {\n"
                    "    id: ID!\n"
                    "    name: String!\n"
                    "  }\n\n"
                    "  // Orders subgraph\n"
                    "  type User @key(fields: \"id\") {\n"
                    "    id: ID!       # minimal representation\n"
                    "  }\n"
                    "  type Order {\n"
                    "    id: ID!\n"
                    "    user: User!   # references the entity\n"
                    "  }\n\n"
                    "The @key directive marks User as an entity. The Orders subgraph\n"
                    "provides a stub with just the key field. The gateway resolves\n"
                    "the full User from the Users subgraph automatically."
                ),
                "options": [
                    "Import the User type directly from the Users subgraph",
                    "Define a stub type with @key(fields: \"id\") and let the gateway resolve it",
                    "Use a shared npm package with the User type definition",
                    "Call the Users subgraph REST API from the Orders resolver",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Federation uses directives to mark entities and their key fields.",
                    "@key(fields: \"id\") — the directive that enables cross-subgraph resolution.",
                ],
            },
            {
                "id": "prod_8",
                "type": "quiz",
                "title": "Error Handling Strategy",
                "question": (
                    "A GraphQL response can contain BOTH `data` and `errors`.\n"
                    "What does it mean when both are present?"
                ),
                "lesson": (
                    "GraphQL supports partial success — some fields resolve,\n"
                    "others fail:\n\n"
                    "  {\n"
                    "    \"data\": {\n"
                    "      \"user\": {\n"
                    "        \"name\": \"Alice\",\n"
                    "        \"email\": null  // resolver failed\n"
                    "      }\n"
                    "    },\n"
                    "    \"errors\": [\n"
                    "      {\n"
                    "        \"message\": \"Not authorized to view email\",\n"
                    "        \"path\": [\"user\", \"email\"]\n"
                    "      }\n"
                    "    ]\n"
                    "  }\n\n"
                    "This is fundamentally different from REST, where a request either\n"
                    "succeeds (2xx) or fails (4xx/5xx). In GraphQL, a single response\n"
                    "can contain successful data AND errors for fields that failed.\n\n"
                    "The `path` field tells you exactly which field errored."
                ),
                "options": [
                    "The entire response should be treated as an error",
                    "Some fields resolved successfully while others failed (partial success)",
                    "The errors are warnings that can be ignored",
                    "The server is returning cached data with stale errors",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "GraphQL allows partial responses — not all-or-nothing like REST.",
                    "Some fields succeeded, some fields failed. Both are in the response.",
                ],
            },
        ],
    },
}
