"""
zones.py — TypeScript zones and challenges for Type Forge.

8 zones, ~45 challenges. All challenges use "type": "quiz" with
multiple-choice options (a/b/c/d) and two hints each.
"""

ZONE_ORDER = [
    "ts_basics",
    "interfaces_types",
    "generics",
    "unions_narrowing",
    "enums_literals",
    "advanced_types",
    "ts_with_react",
    "tooling",
]

ZONES = {
    # ── ZONE 1: TS BASICS ──────────────────────────────────────────────
    "ts_basics": {
        "id": "ts_basics",
        "name": "The Type Foundation",
        "subtitle": "Type Annotations, Primitives, Inference & any vs unknown",
        "color": "cyan",
        "icon": "🔷",
        "commands": ["tsc", "ts-node", "string", "number", "boolean"],
        "challenges": [
            {
                "id": "tsb_1",
                "type": "quiz",
                "title": "First Annotation",
                "question": (
                    "How do you declare a variable with an explicit type annotation in TypeScript?\n\n"
                    "  ___ age: number = 30;"
                ),
                "lesson": (
                    "TypeScript adds type annotations to JavaScript using a colon syntax:\n\n"
                    "  let age: number = 30;\n"
                    "  const name: string = 'Ghost';\n"
                    "  let active: boolean = true;\n\n"
                    "The keyword `let` or `const` precedes the variable name,\n"
                    "followed by a colon and the type."
                ),
                "options": [
                    "var",
                    "let",
                    "type",
                    "declare",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It's the same keyword you'd use in modern JavaScript for a mutable variable.",
                    "let age: number = 30; — the annotation goes between the name and the value.",
                ],
            },
            {
                "id": "tsb_2",
                "type": "quiz",
                "title": "Primitive Types",
                "question": (
                    "Which of the following is NOT a primitive type in TypeScript?\n\n"
                    "  let a: string = 'hello';\n"
                    "  let b: number = 42;\n"
                    "  let c: boolean = true;\n"
                    "  let d: integer = 10;"
                ),
                "lesson": (
                    "TypeScript's primitive types:\n"
                    "  string   — text data\n"
                    "  number   — all numeric values (no int/float distinction)\n"
                    "  boolean  — true or false\n"
                    "  null     — intentional absence\n"
                    "  undefined — uninitialized\n"
                    "  symbol   — unique identifier\n"
                    "  bigint   — arbitrary-precision integers\n\n"
                    "There is no `integer` type. All numbers are `number`."
                ),
                "options": [
                    "string",
                    "number",
                    "boolean",
                    "integer",
                ],
                "answer": "d",
                "xp": 25,
                "hints": [
                    "TypeScript doesn't distinguish between integers and floats.",
                    "There's one numeric type that covers all numbers.",
                ],
            },
            {
                "id": "tsb_3",
                "type": "quiz",
                "title": "Type Inference",
                "question": (
                    "What type does TypeScript infer for `x`?\n\n"
                    "  const x = 'NEXUS';"
                ),
                "lesson": (
                    "TypeScript infers types from initializers:\n\n"
                    "  const x = 'NEXUS';    // type: \"NEXUS\" (literal type)\n"
                    "  let y = 'NEXUS';      // type: string\n\n"
                    "`const` narrows to the literal type because the value can never change.\n"
                    "`let` widens to `string` because reassignment is allowed."
                ),
                "options": [
                    "string",
                    "\"NEXUS\" (string literal type)",
                    "any",
                    "String (object wrapper)",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "const means the value can never be reassigned.",
                    "TypeScript uses literal narrowing for const declarations.",
                ],
            },
            {
                "id": "tsb_4",
                "type": "quiz",
                "title": "any vs unknown",
                "question": (
                    "What is the key difference between `any` and `unknown`?\n\n"
                    "  let a: any = getData();\n"
                    "  a.foo();               // compiles fine\n\n"
                    "  let b: unknown = getData();\n"
                    "  b.foo();               // ???"
                ),
                "lesson": (
                    "any — disables type checking entirely. Any operation is allowed.\n"
                    "unknown — type-safe counterpart. You must narrow before using.\n\n"
                    "  let a: any = 'hello';\n"
                    "  a.toFixed();  // no error (but will crash at runtime!)\n\n"
                    "  let b: unknown = 'hello';\n"
                    "  b.toFixed();  // ERROR: Object is of type 'unknown'\n"
                    "  if (typeof b === 'string') b.toUpperCase();  // OK after narrowing"
                ),
                "options": [
                    "any is for functions, unknown is for variables",
                    "They are identical — unknown is just an alias for any",
                    "unknown requires type narrowing before use; any does not",
                    "any is deprecated in TypeScript 5+",
                ],
                "answer": "c",
                "xp": 35,
                "hints": [
                    "One lets you do anything without checks. The other forces you to check first.",
                    "unknown is the type-safe version — you must narrow it before operating on it.",
                ],
            },
            {
                "id": "tsb_5",
                "type": "quiz",
                "title": "Type Assertion",
                "question": (
                    "Which syntax asserts that `value` is a string?\n\n"
                    "  const value: unknown = getPayload();\n"
                    "  const len = (value ___ string).length;"
                ),
                "lesson": (
                    "Type assertions tell TypeScript: 'I know the type — trust me.'\n\n"
                    "Two syntaxes:\n"
                    "  (value as string).length    // 'as' syntax (preferred)\n"
                    "  (<string>value).length      // angle bracket syntax\n\n"
                    "Assertions don't perform runtime checks — they're compile-time only.\n"
                    "Use them sparingly. Prefer type guards for safety."
                ),
                "options": [
                    "is",
                    "as",
                    "instanceof",
                    "to",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The keyword reads naturally: 'value as string'.",
                    "It's a compile-time assertion, not a runtime cast.",
                ],
            },
            {
                "id": "tsb_6",
                "type": "quiz",
                "title": "Void Return",
                "question": (
                    "What return type annotation indicates a function returns nothing?\n\n"
                    "  function logMessage(msg: string): ___ {\n"
                    "      console.log(msg);\n"
                    "  }"
                ),
                "lesson": (
                    "void — indicates a function does not return a meaningful value.\n\n"
                    "  function log(msg: string): void {\n"
                    "      console.log(msg);\n"
                    "  }\n\n"
                    "void is not the same as undefined. A void function may\n"
                    "implicitly return undefined, but the intent is 'no return value'.\n"
                    "never — for functions that never return (throws or infinite loop)."
                ),
                "options": [
                    "null",
                    "undefined",
                    "void",
                    "never",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "It's the same keyword used in C and Java for no-return functions.",
                    "void means 'this function doesn't return anything useful'.",
                ],
            },
        ],
    },

    # ── ZONE 2: INTERFACES & TYPES ──────────────────────────────────────
    "interfaces_types": {
        "id": "interfaces_types",
        "name": "The Interface Layer",
        "subtitle": "Interfaces, Type Aliases, Extending & Readonly",
        "color": "green",
        "icon": "📐",
        "commands": ["interface", "type", "extends", "readonly", "?"],
        "challenges": [
            {
                "id": "it_1",
                "type": "quiz",
                "title": "Interface Declaration",
                "question": (
                    "What keyword declares a contract for object shapes in TypeScript?\n\n"
                    "  ___ User {\n"
                    "      name: string;\n"
                    "      id: number;\n"
                    "  }"
                ),
                "lesson": (
                    "Interfaces define the shape of an object:\n\n"
                    "  interface User {\n"
                    "      name: string;\n"
                    "      id: number;\n"
                    "  }\n\n"
                    "Any object matching the shape satisfies the interface.\n"
                    "This is structural typing — the structure matters, not the name."
                ),
                "options": [
                    "class",
                    "type",
                    "interface",
                    "struct",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "It's a keyword borrowed from Java and C# for defining contracts.",
                    "interface User { ... } — declares the shape an object must match.",
                ],
            },
            {
                "id": "it_2",
                "type": "quiz",
                "title": "Interface vs Type",
                "question": (
                    "Which statement is TRUE about `interface` vs `type` in TypeScript?\n\n"
                    "  interface User { name: string; }\n"
                    "  type User = { name: string; };"
                ),
                "lesson": (
                    "Key differences:\n"
                    "  interface — can be extended, can be merged (declaration merging)\n"
                    "  type     — can represent unions, intersections, primitives, tuples\n\n"
                    "  interface A { x: number; }\n"
                    "  interface A { y: number; }  // merged: { x: number; y: number }\n\n"
                    "  type B = { x: number };\n"
                    "  type B = { y: number };     // ERROR: duplicate identifier\n\n"
                    "Rule of thumb: use interface for objects, type for everything else."
                ),
                "options": [
                    "They are completely identical in every way",
                    "Interfaces support declaration merging; type aliases do not",
                    "Type aliases can be extended; interfaces cannot",
                    "Interfaces can represent union types",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "One of them lets you declare the same name twice and it merges.",
                    "Declaration merging is unique to interfaces.",
                ],
            },
            {
                "id": "it_3",
                "type": "quiz",
                "title": "Optional Properties",
                "question": (
                    "How do you mark a property as optional in an interface?\n\n"
                    "  interface Config {\n"
                    "      host: string;\n"
                    "      port___ number;\n"
                    "  }"
                ),
                "lesson": (
                    "Optional properties use a question mark before the colon:\n\n"
                    "  interface Config {\n"
                    "      host: string;\n"
                    "      port?: number;   // optional — may be undefined\n"
                    "  }\n\n"
                    "  const cfg: Config = { host: 'localhost' };  // OK, port omitted"
                ),
                "options": [
                    "port | undefined: number",
                    "port?: number",
                    "port = undefined: number",
                    "optional port: number",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "A single character after the property name makes it optional.",
                    "The question mark: port?: number",
                ],
            },
            {
                "id": "it_4",
                "type": "quiz",
                "title": "Readonly Properties",
                "question": (
                    "Which modifier prevents a property from being reassigned after creation?\n\n"
                    "  interface Agent {\n"
                    "      ___ id: string;\n"
                    "      name: string;\n"
                    "  }"
                ),
                "lesson": (
                    "readonly prevents reassignment after initialization:\n\n"
                    "  interface Agent {\n"
                    "      readonly id: string;\n"
                    "      name: string;\n"
                    "  }\n\n"
                    "  const a: Agent = { id: 'A-001', name: 'Ghost' };\n"
                    "  a.name = 'Phantom';  // OK\n"
                    "  a.id = 'A-002';      // ERROR: Cannot assign to 'id'"
                ),
                "options": [
                    "const",
                    "final",
                    "immutable",
                    "readonly",
                ],
                "answer": "d",
                "xp": 25,
                "hints": [
                    "It's a modifier keyword, not a JavaScript keyword.",
                    "readonly id: string — the property can't be changed after init.",
                ],
            },
            {
                "id": "it_5",
                "type": "quiz",
                "title": "Extending Interfaces",
                "question": (
                    "How does one interface inherit properties from another?\n\n"
                    "  interface Base { id: string; }\n"
                    "  interface Admin ___ Base {\n"
                    "      level: number;\n"
                    "  }"
                ),
                "lesson": (
                    "Interfaces extend other interfaces with `extends`:\n\n"
                    "  interface Base { id: string; }\n"
                    "  interface Admin extends Base {\n"
                    "      level: number;\n"
                    "  }\n"
                    "  // Admin has: { id: string; level: number; }\n\n"
                    "Multiple extension:\n"
                    "  interface Admin extends Base, Auditable { ... }"
                ),
                "options": [
                    "implements",
                    "extends",
                    "inherits",
                    "includes",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Same keyword used in class inheritance.",
                    "interface Admin extends Base { ... }",
                ],
            },
            {
                "id": "it_6",
                "type": "quiz",
                "title": "Index Signatures",
                "question": (
                    "What syntax allows an interface to accept any string key?\n\n"
                    "  interface EnvVars {\n"
                    "      [key: string]: string;\n"
                    "  }\n\n"
                    "What is the `[key: string]: string` called?"
                ),
                "lesson": (
                    "Index signatures define the type for dynamic keys:\n\n"
                    "  interface EnvVars {\n"
                    "      [key: string]: string;\n"
                    "  }\n\n"
                    "  const env: EnvVars = {\n"
                    "      NODE_ENV: 'production',\n"
                    "      PORT: '3000',\n"
                    "      // any string key with a string value is valid\n"
                    "  };"
                ),
                "options": [
                    "Mapped type",
                    "Generic constraint",
                    "Index signature",
                    "Computed property",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "It uses bracket notation with a key type inside the interface.",
                    "Index signature — [key: string]: ValueType",
                ],
            },
        ],
    },

    # ── ZONE 3: GENERICS ───────────────────────────────────────────────
    "generics": {
        "id": "generics",
        "name": "The Generic Forge",
        "subtitle": "Generic Functions, Types, Constraints & Utility Types",
        "color": "magenta",
        "icon": "🔮",
        "commands": ["<T>", "extends", "Partial", "Pick", "Omit", "Record"],
        "challenges": [
            {
                "id": "gen_1",
                "type": "quiz",
                "title": "Generic Function",
                "question": (
                    "What does `<T>` represent in this function signature?\n\n"
                    "  function identity<T>(arg: T): T {\n"
                    "      return arg;\n"
                    "  }"
                ),
                "lesson": (
                    "Generics let you write code that works with any type:\n\n"
                    "  function identity<T>(arg: T): T {\n"
                    "      return arg;\n"
                    "  }\n\n"
                    "  identity<string>('Ghost');  // T = string\n"
                    "  identity(42);               // T inferred as number\n\n"
                    "<T> is a type parameter — a placeholder that gets filled in at call time."
                ),
                "options": [
                    "A template literal",
                    "A type parameter (generic placeholder)",
                    "A JSX element",
                    "A TypeScript decorator",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "It's a placeholder for a type that gets determined at usage time.",
                    "T is a type parameter — the caller provides the actual type.",
                ],
            },
            {
                "id": "gen_2",
                "type": "quiz",
                "title": "Generic Constraints",
                "question": (
                    "How do you constrain a generic type to objects with a `.length` property?\n\n"
                    "  function logLength<T ___ { length: number }>(arg: T): void {\n"
                    "      console.log(arg.length);\n"
                    "  }"
                ),
                "lesson": (
                    "Generic constraints use `extends` to restrict what types are allowed:\n\n"
                    "  function logLength<T extends { length: number }>(arg: T) {\n"
                    "      console.log(arg.length);\n"
                    "  }\n\n"
                    "  logLength('hello');    // OK — string has .length\n"
                    "  logLength([1, 2, 3]); // OK — array has .length\n"
                    "  logLength(42);        // ERROR — number has no .length"
                ),
                "options": [
                    "implements",
                    "satisfies",
                    "extends",
                    "requires",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "Same keyword used for interface inheritance.",
                    "T extends { length: number } constrains T to types with .length.",
                ],
            },
            {
                "id": "gen_3",
                "type": "quiz",
                "title": "Partial Utility",
                "question": (
                    "What does `Partial<User>` produce?\n\n"
                    "  interface User {\n"
                    "      name: string;\n"
                    "      email: string;\n"
                    "  }\n\n"
                    "  function update(user: User, fields: Partial<User>) { ... }"
                ),
                "lesson": (
                    "Partial<T> makes all properties of T optional:\n\n"
                    "  Partial<User> = {\n"
                    "      name?: string;\n"
                    "      email?: string;\n"
                    "  }\n\n"
                    "Useful for update functions where only some fields may change.\n"
                    "Counterpart: Required<T> — makes all properties required."
                ),
                "options": [
                    "A type with all properties removed",
                    "A type with all properties made optional",
                    "A type with all properties made readonly",
                    "A type with only string properties",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The name 'Partial' means 'part of' — not all fields required.",
                    "Partial<T> wraps every property with ?: making them optional.",
                ],
            },
            {
                "id": "gen_4",
                "type": "quiz",
                "title": "Pick Utility",
                "question": (
                    "What type does `Pick<User, 'name' | 'id'>` produce?\n\n"
                    "  interface User {\n"
                    "      id: number;\n"
                    "      name: string;\n"
                    "      email: string;\n"
                    "      role: string;\n"
                    "  }"
                ),
                "lesson": (
                    "Pick<T, Keys> extracts a subset of properties:\n\n"
                    "  Pick<User, 'name' | 'id'> = {\n"
                    "      id: number;\n"
                    "      name: string;\n"
                    "  }\n\n"
                    "The inverse is Omit<T, Keys> — removes specified keys."
                ),
                "options": [
                    "{ id: number; name: string; }",
                    "{ email: string; role: string; }",
                    "{ name: string; }",
                    "User",
                ],
                "answer": "a",
                "xp": 30,
                "hints": [
                    "Pick selects the listed keys from the original type.",
                    "You're picking 'name' and 'id', so you get those two properties.",
                ],
            },
            {
                "id": "gen_5",
                "type": "quiz",
                "title": "Omit Utility",
                "question": (
                    "What is the result of `Omit<Config, 'secret'>`?\n\n"
                    "  interface Config {\n"
                    "      host: string;\n"
                    "      port: number;\n"
                    "      secret: string;\n"
                    "  }"
                ),
                "lesson": (
                    "Omit<T, Keys> removes specified properties from T:\n\n"
                    "  Omit<Config, 'secret'> = {\n"
                    "      host: string;\n"
                    "      port: number;\n"
                    "  }\n\n"
                    "Useful for creating 'safe' types without sensitive fields.\n"
                    "Pick and Omit are inverses of each other."
                ),
                "options": [
                    "{ secret: string; }",
                    "{ host: string; port: number; }",
                    "{ host: string; port: number; secret: string; }",
                    "{ host: string; }",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Omit removes the listed key. What's left?",
                    "Remove 'secret' from three properties — two remain.",
                ],
            },
            {
                "id": "gen_6",
                "type": "quiz",
                "title": "Record Utility",
                "question": (
                    "What does `Record<string, number>` represent?\n\n"
                    "  const scores: Record<string, number> = {\n"
                    "      alice: 95,\n"
                    "      bob: 87,\n"
                    "  };"
                ),
                "lesson": (
                    "Record<Keys, Value> creates a type with specified key/value types:\n\n"
                    "  Record<string, number>\n"
                    "  // equivalent to: { [key: string]: number }\n\n"
                    "  Record<'admin' | 'user', boolean>\n"
                    "  // equivalent to: { admin: boolean; user: boolean; }\n\n"
                    "Record is a utility for creating mapped object types cleanly."
                ),
                "options": [
                    "An array of string-number pairs",
                    "An object with string keys and number values",
                    "A Map<string, number>",
                    "A tuple of [string, number]",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "Record creates an object type, not a data structure.",
                    "Record<K, V> means: keys of type K, values of type V.",
                ],
            },
        ],
    },

    # ── ZONE 4: UNIONS & NARROWING ──────────────────────────────────────
    "unions_narrowing": {
        "id": "unions_narrowing",
        "name": "The Narrowing Chamber",
        "subtitle": "Union Types, Discriminated Unions, Type Guards & Exhaustive Checks",
        "color": "yellow",
        "icon": "🔀",
        "commands": ["|", "typeof", "instanceof", "in", "is", "never"],
        "challenges": [
            {
                "id": "un_1",
                "type": "quiz",
                "title": "Union Types",
                "question": (
                    "What does the `|` operator mean in a type position?\n\n"
                    "  function format(input: string | number): string {\n"
                    "      return String(input);\n"
                    "  }"
                ),
                "lesson": (
                    "Union types allow a value to be one of several types:\n\n"
                    "  string | number — either a string or a number\n\n"
                    "  function format(input: string | number): string {\n"
                    "      return String(input);\n"
                    "  }\n\n"
                    "  format('hello');  // OK\n"
                    "  format(42);       // OK\n"
                    "  format(true);     // ERROR"
                ),
                "options": [
                    "Bitwise OR",
                    "Logical OR — one of the listed types",
                    "Intersection — both types combined",
                    "Pipe operator for chaining",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "In type position, | means 'or' — the value can be either type.",
                    "string | number means the value is a string OR a number.",
                ],
            },
            {
                "id": "un_2",
                "type": "quiz",
                "title": "typeof Narrowing",
                "question": (
                    "After the typeof check, what type is `value` inside the if block?\n\n"
                    "  function process(value: string | number) {\n"
                    "      if (typeof value === 'string') {\n"
                    "          // value is ___ here\n"
                    "          console.log(value.toUpperCase());\n"
                    "      }\n"
                    "  }"
                ),
                "lesson": (
                    "typeof narrows union types inside conditional blocks:\n\n"
                    "  function process(value: string | number) {\n"
                    "      if (typeof value === 'string') {\n"
                    "          value.toUpperCase();  // value: string\n"
                    "      } else {\n"
                    "          value.toFixed(2);     // value: number\n"
                    "      }\n"
                    "  }\n\n"
                    "TypeScript tracks the type through control flow analysis."
                ),
                "options": [
                    "string | number",
                    "string",
                    "unknown",
                    "any",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "The typeof check eliminated number from the union.",
                    "After typeof value === 'string', only string remains.",
                ],
            },
            {
                "id": "un_3",
                "type": "quiz",
                "title": "Discriminated Unions",
                "question": (
                    "What makes this a discriminated union?\n\n"
                    "  type Success = { status: 'ok'; data: string };\n"
                    "  type Failure = { status: 'error'; message: string };\n"
                    "  type Result = Success | Failure;"
                ),
                "lesson": (
                    "A discriminated union has a common literal property (discriminant):\n\n"
                    "  type Result = Success | Failure;\n\n"
                    "  function handle(r: Result) {\n"
                    "      if (r.status === 'ok') {\n"
                    "          r.data;     // TypeScript knows this is Success\n"
                    "      } else {\n"
                    "          r.message;  // TypeScript knows this is Failure\n"
                    "      }\n"
                    "  }\n\n"
                    "The `status` field is the discriminant — its literal type\n"
                    "tells TypeScript which variant you're working with."
                ),
                "options": [
                    "Both types have different numbers of properties",
                    "The union uses the | operator",
                    "A shared property with literal types distinguishes the variants",
                    "The types use the 'type' keyword instead of 'interface'",
                ],
                "answer": "c",
                "xp": 35,
                "hints": [
                    "Look for a property that appears in both types with different literal values.",
                    "status: 'ok' vs status: 'error' — the shared literal field discriminates.",
                ],
            },
            {
                "id": "un_4",
                "type": "quiz",
                "title": "Custom Type Guard",
                "question": (
                    "What is the return type of a custom type guard function?\n\n"
                    "  function isString(value: unknown): value ___ string {\n"
                    "      return typeof value === 'string';\n"
                    "  }"
                ),
                "lesson": (
                    "Custom type guards use the `is` keyword in the return type:\n\n"
                    "  function isString(value: unknown): value is string {\n"
                    "      return typeof value === 'string';\n"
                    "  }\n\n"
                    "  const x: unknown = getData();\n"
                    "  if (isString(x)) {\n"
                    "      x.toUpperCase();  // x narrowed to string\n"
                    "  }\n\n"
                    "The return type `value is string` is a type predicate."
                ),
                "options": [
                    "as",
                    "instanceof",
                    "is",
                    "typeof",
                ],
                "answer": "c",
                "xp": 35,
                "hints": [
                    "It's a type predicate syntax: paramName is Type.",
                    "value is string — the `is` keyword connects the parameter to the type.",
                ],
            },
            {
                "id": "un_5",
                "type": "quiz",
                "title": "Exhaustive Check",
                "question": (
                    "Why assign to `never` in the default case?\n\n"
                    "  type Shape = 'circle' | 'square';\n"
                    "  function area(s: Shape) {\n"
                    "      switch (s) {\n"
                    "          case 'circle': return Math.PI;\n"
                    "          case 'square': return 1;\n"
                    "          default:\n"
                    "              const _exhaustive: never = s;\n"
                    "      }\n"
                    "  }"
                ),
                "lesson": (
                    "Exhaustive checking ensures all union members are handled:\n\n"
                    "  const _exhaustive: never = s;\n\n"
                    "If all cases are handled, `s` is narrowed to `never` (impossible state).\n"
                    "If a new variant is added to Shape but not handled, TypeScript\n"
                    "will error because the new variant can't be assigned to `never`.\n\n"
                    "This catches unhandled cases at compile time — not runtime."
                ),
                "options": [
                    "It improves runtime performance",
                    "It's required syntax for switch statements",
                    "If a union member isn't handled, the assignment to never fails at compile time",
                    "It converts the value to undefined",
                ],
                "answer": "c",
                "xp": 40,
                "hints": [
                    "never means 'this code should be unreachable'.",
                    "If you add a new variant but forget a case, never catches it at compile time.",
                ],
            },
        ],
    },

    # ── ZONE 5: ENUMS & LITERALS ────────────────────────────────────────
    "enums_literals": {
        "id": "enums_literals",
        "name": "The Literal Vault",
        "subtitle": "String Enums, Numeric Enums, Const Assertions & Template Literals",
        "color": "blue",
        "icon": "🏷️",
        "commands": ["enum", "const", "as const", "template literal"],
        "challenges": [
            {
                "id": "el_1",
                "type": "quiz",
                "title": "String Enums",
                "question": (
                    "What is the runtime value of `Direction.Up`?\n\n"
                    "  enum Direction {\n"
                    "      Up = 'UP',\n"
                    "      Down = 'DOWN',\n"
                    "      Left = 'LEFT',\n"
                    "      Right = 'RIGHT',\n"
                    "  }"
                ),
                "lesson": (
                    "String enums have explicit string values:\n\n"
                    "  enum Direction {\n"
                    "      Up = 'UP',\n"
                    "      Down = 'DOWN',\n"
                    "  }\n\n"
                    "  Direction.Up === 'UP'  // true at runtime\n\n"
                    "String enums are fully opaque — no reverse mapping.\n"
                    "They serialize cleanly to JSON and are readable in logs."
                ),
                "options": [
                    "0",
                    "'Up'",
                    "'UP'",
                    "undefined",
                ],
                "answer": "c",
                "xp": 25,
                "hints": [
                    "The value is what's assigned after the = sign.",
                    "Up = 'UP' — the runtime value is the string 'UP'.",
                ],
            },
            {
                "id": "el_2",
                "type": "quiz",
                "title": "Numeric Enums",
                "question": (
                    "What is the value of `Status.Active` and `Status.Inactive`?\n\n"
                    "  enum Status {\n"
                    "      Pending,\n"
                    "      Active,\n"
                    "      Inactive,\n"
                    "  }"
                ),
                "lesson": (
                    "Numeric enums auto-increment from 0:\n\n"
                    "  enum Status {\n"
                    "      Pending,    // 0\n"
                    "      Active,     // 1\n"
                    "      Inactive,   // 2\n"
                    "  }\n\n"
                    "  Status.Active === 1      // true\n"
                    "  Status[1] === 'Active'   // reverse mapping (numeric only)"
                ),
                "options": [
                    "1 and 2",
                    "0 and 1",
                    "'Active' and 'Inactive'",
                    "undefined and undefined",
                ],
                "answer": "a",
                "xp": 25,
                "hints": [
                    "Numeric enums start at 0 and auto-increment.",
                    "Pending=0, Active=1, Inactive=2.",
                ],
            },
            {
                "id": "el_3",
                "type": "quiz",
                "title": "Const Assertion",
                "question": (
                    "What effect does `as const` have on this object?\n\n"
                    "  const config = {\n"
                    "      host: 'localhost',\n"
                    "      port: 3000,\n"
                    "  } as const;"
                ),
                "lesson": (
                    "`as const` makes all properties readonly and narrows to literal types:\n\n"
                    "  const config = { host: 'localhost', port: 3000 } as const;\n"
                    "  // type: { readonly host: 'localhost'; readonly port: 3000; }\n\n"
                    "Without as const:\n"
                    "  // type: { host: string; port: number; }\n\n"
                    "as const is a zero-cost assertion — no runtime effect."
                ),
                "options": [
                    "Freezes the object at runtime (like Object.freeze)",
                    "Makes all properties readonly with literal types (compile-time only)",
                    "Converts the object to a Map",
                    "Makes the object immutable and adds runtime validation",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "It's a compile-time assertion — no runtime effect.",
                    "as const = readonly + literal types for all properties.",
                ],
            },
            {
                "id": "el_4",
                "type": "quiz",
                "title": "Literal Types",
                "question": (
                    "What type is inferred for `direction`?\n\n"
                    "  let direction: 'left' | 'right' = 'left';\n"
                    "  direction = 'up';  // ???"
                ),
                "lesson": (
                    "Literal types restrict a variable to exact values:\n\n"
                    "  let direction: 'left' | 'right' = 'left';\n"
                    "  direction = 'right';  // OK\n"
                    "  direction = 'up';     // ERROR: Type '\"up\"' is not assignable\n\n"
                    "Literal types work with strings, numbers, and booleans:\n"
                    "  type Bit = 0 | 1;\n"
                    "  type YesNo = true | false;"
                ),
                "options": [
                    "No error — 'up' is a valid string",
                    "Error — direction can only be 'left' or 'right'",
                    "Error — let variables cannot have literal types",
                    "Runtime error — invalid assignment",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "The type explicitly restricts the value to two options.",
                    "'left' | 'right' means only those two strings are valid.",
                ],
            },
            {
                "id": "el_5",
                "type": "quiz",
                "title": "Template Literal Types",
                "question": (
                    "What type does `EventName` represent?\n\n"
                    "  type Entity = 'user' | 'post';\n"
                    "  type Action = 'create' | 'delete';\n"
                    "  type EventName = `${Entity}_${Action}`;"
                ),
                "lesson": (
                    "Template literal types combine literal types with string templates:\n\n"
                    "  type EventName = `${Entity}_${Action}`;\n"
                    "  // = 'user_create' | 'user_delete' | 'post_create' | 'post_delete'\n\n"
                    "TypeScript computes the cartesian product of all combinations.\n"
                    "Powerful for creating type-safe event names, CSS classes, API routes."
                ),
                "options": [
                    "string",
                    "'user_create' | 'user_delete' | 'post_create' | 'post_delete'",
                    "'Entity_Action'",
                    "'user' | 'post' | 'create' | 'delete'",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "TypeScript expands all combinations of the union members.",
                    "2 entities x 2 actions = 4 possible string literal types.",
                ],
            },
            {
                "id": "el_6",
                "type": "quiz",
                "title": "Enum vs Union",
                "question": (
                    "Which approach is preferred in modern TypeScript for a set of constants?\n\n"
                    "  // Option A:\n"
                    "  enum Color { Red = 'RED', Blue = 'BLUE' }\n\n"
                    "  // Option B:\n"
                    "  type Color = 'RED' | 'BLUE';"
                ),
                "lesson": (
                    "Enums vs union literals — trade-offs:\n\n"
                    "  enum — generates runtime code, reverse mapping, namespace\n"
                    "  union — zero runtime cost, simpler, tree-shakeable\n\n"
                    "Modern TypeScript increasingly favors union literals:\n"
                    "  type Color = 'RED' | 'BLUE';\n\n"
                    "Union literals are erased at compile time — no runtime overhead.\n"
                    "Enums still useful for reverse mapping and computed members."
                ),
                "options": [
                    "Enums, because they're the only type-safe option",
                    "Union literals, because they have zero runtime cost",
                    "They're identical — choose either",
                    "Neither — use plain strings without types",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "One generates JavaScript code at runtime. The other is erased entirely.",
                    "Union literals are zero-cost at runtime — preferred in modern TS.",
                ],
            },
        ],
    },

    # ── ZONE 6: ADVANCED TYPES ──────────────────────────────────────────
    "advanced_types": {
        "id": "advanced_types",
        "name": "The Type Architect's Lab",
        "subtitle": "Mapped Types, Conditional Types, infer, keyof & Indexed Access",
        "color": "red",
        "icon": "🧬",
        "commands": ["keyof", "typeof", "in", "infer", "extends", "?:"],
        "challenges": [
            {
                "id": "at_1",
                "type": "quiz",
                "title": "keyof Operator",
                "question": (
                    "What does `keyof User` produce?\n\n"
                    "  interface User {\n"
                    "      id: number;\n"
                    "      name: string;\n"
                    "      email: string;\n"
                    "  }\n\n"
                    "  type UserKeys = keyof User;"
                ),
                "lesson": (
                    "keyof produces a union of all property names as literal types:\n\n"
                    "  keyof User = 'id' | 'name' | 'email'\n\n"
                    "Useful for creating type-safe property access:\n"
                    "  function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {\n"
                    "      return obj[key];\n"
                    "  }"
                ),
                "options": [
                    "['id', 'name', 'email'] (an array)",
                    "'id' | 'name' | 'email' (union of literal types)",
                    "{ id: number; name: string; email: string; }",
                    "string",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "keyof extracts the property names, not the property values.",
                    "The result is a union of string literal types.",
                ],
            },
            {
                "id": "at_2",
                "type": "quiz",
                "title": "Indexed Access Types",
                "question": (
                    "What is the type of `UserName`?\n\n"
                    "  interface User {\n"
                    "      id: number;\n"
                    "      name: string;\n"
                    "      email: string;\n"
                    "  }\n\n"
                    "  type UserName = User['name'];"
                ),
                "lesson": (
                    "Indexed access types use bracket notation to extract property types:\n\n"
                    "  User['name']           // string\n"
                    "  User['id' | 'name']    // number | string\n"
                    "  User[keyof User]       // number | string\n\n"
                    "This is the type-level equivalent of obj['key'] at runtime."
                ),
                "options": [
                    "'name'",
                    "string",
                    "number",
                    "User",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "You're looking up the type of the 'name' property.",
                    "User['name'] resolves to the type of the name field: string.",
                ],
            },
            {
                "id": "at_3",
                "type": "quiz",
                "title": "Mapped Types",
                "question": (
                    "What does this mapped type produce?\n\n"
                    "  type Readonly<T> = {\n"
                    "      readonly [K in keyof T]: T[K];\n"
                    "  };"
                ),
                "lesson": (
                    "Mapped types iterate over keys to transform a type:\n\n"
                    "  type Readonly<T> = {\n"
                    "      readonly [K in keyof T]: T[K];\n"
                    "  };\n\n"
                    "  [K in keyof T] — iterate over each key K\n"
                    "  T[K]          — preserve the original value type\n"
                    "  readonly      — add readonly modifier\n\n"
                    "This is how Partial, Required, Readonly are built internally."
                ),
                "options": [
                    "A type with all properties removed",
                    "A type with all properties made readonly",
                    "A type with all properties made optional",
                    "An exact copy of the original type",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "The readonly modifier is added to each property.",
                    "[K in keyof T]: T[K] iterates keys; readonly is prepended.",
                ],
            },
            {
                "id": "at_4",
                "type": "quiz",
                "title": "Conditional Types",
                "question": (
                    "What does `IsString<number>` resolve to?\n\n"
                    "  type IsString<T> = T extends string ? 'yes' : 'no';\n\n"
                    "  type A = IsString<string>;  // ?\n"
                    "  type B = IsString<number>;  // ?"
                ),
                "lesson": (
                    "Conditional types use ternary syntax at the type level:\n\n"
                    "  T extends U ? X : Y\n\n"
                    "  IsString<string> = 'yes'   // string extends string — true\n"
                    "  IsString<number> = 'no'    // number extends string — false\n\n"
                    "When T is a union, the condition distributes over each member."
                ),
                "options": [
                    "'yes'",
                    "'no'",
                    "boolean",
                    "never",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "Does number extend string? No — so it takes the false branch.",
                    "number is not a string, so the result is 'no'.",
                ],
            },
            {
                "id": "at_5",
                "type": "quiz",
                "title": "infer Keyword",
                "question": (
                    "What does `ReturnType<typeof fn>` extract using `infer`?\n\n"
                    "  type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;\n\n"
                    "  function fn(): string { return 'hello'; }\n"
                    "  type Result = ReturnType<typeof fn>;"
                ),
                "lesson": (
                    "infer declares a type variable inside a conditional type:\n\n"
                    "  type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;\n\n"
                    "  infer R — 'capture whatever the return type is into R'\n\n"
                    "  ReturnType<() => string> = string\n"
                    "  ReturnType<() => number> = number\n\n"
                    "infer is like pattern matching for types."
                ),
                "options": [
                    "The function's parameter types",
                    "The function's return type (string)",
                    "The function's name",
                    "never",
                ],
                "answer": "b",
                "xp": 40,
                "hints": [
                    "infer R captures the return type position.",
                    "fn returns string, so ReturnType<typeof fn> = string.",
                ],
            },
            {
                "id": "at_6",
                "type": "quiz",
                "title": "typeof in Type Position",
                "question": (
                    "What does `typeof` do when used in a TYPE position (not a value position)?\n\n"
                    "  const config = { host: 'localhost', port: 3000 };\n"
                    "  type Config = typeof config;"
                ),
                "lesson": (
                    "typeof in type position extracts the type of a value:\n\n"
                    "  const config = { host: 'localhost', port: 3000 };\n"
                    "  type Config = typeof config;\n"
                    "  // Config = { host: string; port: number; }\n\n"
                    "Two different typeof:\n"
                    "  typeof x === 'string'    // runtime typeof (JavaScript)\n"
                    "  type T = typeof x;       // compile-time typeof (TypeScript)"
                ),
                "options": [
                    "Returns 'object' as a string",
                    "Checks the runtime type and returns a string",
                    "Extracts the compile-time TypeScript type of a value",
                    "Creates a new instance of the value's class",
                ],
                "answer": "c",
                "xp": 35,
                "hints": [
                    "In type position, typeof works at compile time, not runtime.",
                    "It extracts the TypeScript type from a JavaScript value.",
                ],
            },
        ],
    },

    # ── ZONE 7: TS WITH REACT ───────────────────────────────────────────
    "ts_with_react": {
        "id": "ts_with_react",
        "name": "The React Interface",
        "subtitle": "Props Types, useState, Event Handlers, Refs & Children",
        "color": "cyan",
        "icon": "⚛️",
        "commands": ["FC", "useState<T>", "React.MouseEvent", "useRef", "PropsWithChildren"],
        "challenges": [
            {
                "id": "tr_1",
                "type": "quiz",
                "title": "Typing Props",
                "question": (
                    "What is the standard way to type a React component's props?\n\n"
                    "  interface ButtonProps {\n"
                    "      label: string;\n"
                    "      onClick: () => void;\n"
                    "  }\n\n"
                    "  function Button(___ : ButtonProps) {\n"
                    "      return <button>{props.label}</button>;\n"
                    "  }"
                ),
                "lesson": (
                    "Type props using an interface and annotate the parameter:\n\n"
                    "  interface ButtonProps {\n"
                    "      label: string;\n"
                    "      onClick: () => void;\n"
                    "  }\n\n"
                    "  function Button(props: ButtonProps) {\n"
                    "      return <button onClick={props.onClick}>{props.label}</button>;\n"
                    "  }\n\n"
                    "  // Or with destructuring:\n"
                    "  function Button({ label, onClick }: ButtonProps) { ... }"
                ),
                "options": [
                    "props: any",
                    "props: ButtonProps",
                    "props: React.Props",
                    "props: object",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "Annotate the parameter with the interface you defined.",
                    "props: ButtonProps — use the specific interface, not any or object.",
                ],
            },
            {
                "id": "tr_2",
                "type": "quiz",
                "title": "useState Generic",
                "question": (
                    "How do you type a useState hook for a value that starts as null?\n\n"
                    "  const [user, setUser] = useState___(null);"
                ),
                "lesson": (
                    "useState accepts a generic type parameter:\n\n"
                    "  const [user, setUser] = useState<User | null>(null);\n\n"
                    "Without the generic, TypeScript infers the type from the initial value.\n"
                    "  useState(0)        // type: number\n"
                    "  useState('')       // type: string\n"
                    "  useState(null)     // type: null (too narrow!)\n\n"
                    "Provide the generic when the initial value doesn't represent all states."
                ),
                "options": [
                    "(null)",
                    "<User>(null)",
                    "<User | null>(null)",
                    "<null>(null)",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "The state can be a User or null, so include both in the generic.",
                    "useState<User | null>(null) — the generic describes all possible states.",
                ],
            },
            {
                "id": "tr_3",
                "type": "quiz",
                "title": "Event Handler Types",
                "question": (
                    "What type should the event parameter be for an onClick handler on a button?\n\n"
                    "  function handleClick(e: ___) {\n"
                    "      e.preventDefault();\n"
                    "  }\n\n"
                    "  <button onClick={handleClick}>Click</button>"
                ),
                "lesson": (
                    "React provides specific event types for each handler:\n\n"
                    "  React.MouseEvent<HTMLButtonElement>  — onClick, onMouseEnter\n"
                    "  React.ChangeEvent<HTMLInputElement>  — onChange for inputs\n"
                    "  React.FormEvent<HTMLFormElement>     — onSubmit\n"
                    "  React.KeyboardEvent<HTMLInputElement> — onKeyDown, onKeyUp\n\n"
                    "The generic parameter is the HTML element type that fires the event."
                ),
                "options": [
                    "MouseEvent",
                    "Event",
                    "React.MouseEvent<HTMLButtonElement>",
                    "React.ClickEvent<HTMLButtonElement>",
                ],
                "answer": "c",
                "xp": 30,
                "hints": [
                    "React has its own event types, not the native DOM ones.",
                    "React.MouseEvent<HTMLButtonElement> — React event + element type.",
                ],
            },
            {
                "id": "tr_4",
                "type": "quiz",
                "title": "useRef Typing",
                "question": (
                    "How do you type a ref for an HTML input element?\n\n"
                    "  const inputRef = useRef___;"
                ),
                "lesson": (
                    "useRef takes a generic and initial value:\n\n"
                    "  const inputRef = useRef<HTMLInputElement>(null);\n\n"
                    "  <input ref={inputRef} />\n\n"
                    "  // Later:\n"
                    "  inputRef.current?.focus();  // .current is HTMLInputElement | null\n\n"
                    "Pass null as the initial value for DOM refs.\n"
                    "TypeScript knows .current may be null until the element mounts."
                ),
                "options": [
                    "<HTMLInputElement>()",
                    "<HTMLInputElement>(null)",
                    "<Input>(null)",
                    "(document.querySelector('input'))",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "DOM refs start as null before the component mounts.",
                    "useRef<HTMLInputElement>(null) — generic + null initial value.",
                ],
            },
            {
                "id": "tr_5",
                "type": "quiz",
                "title": "Children Type",
                "question": (
                    "What type represents any valid React child (elements, strings, numbers, etc.)?\n\n"
                    "  interface LayoutProps {\n"
                    "      children: ___;\n"
                    "  }"
                ),
                "lesson": (
                    "React.ReactNode is the broadest type for children:\n\n"
                    "  React.ReactNode = \n"
                    "      ReactElement | string | number | boolean | null | undefined\n"
                    "      | ReactFragment | ReactPortal\n\n"
                    "  interface LayoutProps {\n"
                    "      children: React.ReactNode;\n"
                    "  }\n\n"
                    "For single element children: React.ReactElement\n"
                    "For text-only children: string"
                ),
                "options": [
                    "React.ReactElement",
                    "React.ReactNode",
                    "JSX.Element",
                    "React.Component",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "You need the broadest type that accepts strings, numbers, and elements.",
                    "React.ReactNode — the universal children type.",
                ],
            },
            {
                "id": "tr_6",
                "type": "quiz",
                "title": "Generic Component",
                "question": (
                    "How do you type a generic list component that works with any item type?\n\n"
                    "  function List<T>(props: { items: T[]; render: (item: T) => React.ReactNode }) {\n"
                    "      return <>{props.items.map(props.render)}</>;\n"
                    "  }\n\n"
                    "What is `<T>` in this context?"
                ),
                "lesson": (
                    "Generic components use type parameters just like generic functions:\n\n"
                    "  function List<T>({ items, render }: {\n"
                    "      items: T[];\n"
                    "      render: (item: T) => React.ReactNode;\n"
                    "  }) { ... }\n\n"
                    "  <List items={users} render={(user) => <span>{user.name}</span>} />\n"
                    "  // T is inferred as User from the items prop\n\n"
                    "Generic components enable type-safe reusable UI patterns."
                ),
                "options": [
                    "A JSX tag name",
                    "A generic type parameter inferred from the items prop",
                    "A React component reference",
                    "A TypeScript decorator",
                ],
                "answer": "b",
                "xp": 35,
                "hints": [
                    "It's the same generic syntax used in regular functions: <T>.",
                    "T is inferred from usage — pass User[] and T becomes User.",
                ],
            },
        ],
    },

    # ── ZONE 8: TOOLING ────────────────────────────────────────────────
    "tooling": {
        "id": "tooling",
        "name": "The Compiler Core",
        "subtitle": "tsconfig.json, Strict Mode, Declarations, Modules & Runtime",
        "color": "white",
        "icon": "⚙️",
        "commands": ["tsc", "tsconfig.json", "ts-node", "tsx", ".d.ts"],
        "challenges": [
            {
                "id": "tl_1",
                "type": "quiz",
                "title": "tsconfig.json",
                "question": (
                    "What file configures the TypeScript compiler for a project?\n\n"
                    "  $ tsc --init\n"
                    "  // creates ___ in the project root"
                ),
                "lesson": (
                    "tsconfig.json is the TypeScript project configuration file:\n\n"
                    "  {\n"
                    "    \"compilerOptions\": {\n"
                    "      \"target\": \"ES2022\",\n"
                    "      \"module\": \"commonjs\",\n"
                    "      \"strict\": true,\n"
                    "      \"outDir\": \"./dist\"\n"
                    "    },\n"
                    "    \"include\": [\"src/**/*\"]\n"
                    "  }\n\n"
                    "`tsc --init` generates a default tsconfig.json."
                ),
                "options": [
                    "typescript.config.js",
                    "tsconfig.json",
                    ".tsrc",
                    "tsc.yaml",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It's a JSON file named after TypeScript config.",
                    "tsconfig.json — the standard TypeScript project configuration.",
                ],
            },
            {
                "id": "tl_2",
                "type": "quiz",
                "title": "Strict Mode",
                "question": (
                    "What does `\"strict\": true` enable in tsconfig.json?\n\n"
                    "  {\n"
                    "    \"compilerOptions\": {\n"
                    "      \"strict\": true\n"
                    "    }\n"
                    "  }"
                ),
                "lesson": (
                    "strict: true enables all strict type-checking flags:\n\n"
                    "  strictNullChecks     — null/undefined not assignable to other types\n"
                    "  strictFunctionTypes  — stricter function type checking\n"
                    "  strictBindCallApply  — check bind/call/apply arguments\n"
                    "  noImplicitAny        — error on implicit 'any' types\n"
                    "  noImplicitThis       — error on 'this' with implicit 'any'\n"
                    "  alwaysStrict         — emit 'use strict' in output\n\n"
                    "Always use strict: true. It catches real bugs."
                ),
                "options": [
                    "JavaScript strict mode ('use strict') only",
                    "All strict type-checking flags (strictNullChecks, noImplicitAny, etc.)",
                    "Disables all JavaScript features not in TypeScript",
                    "Enforces ESLint rules",
                ],
                "answer": "b",
                "xp": 30,
                "hints": [
                    "It's a shorthand that enables multiple strict checking flags.",
                    "strict: true = strictNullChecks + noImplicitAny + several others.",
                ],
            },
            {
                "id": "tl_3",
                "type": "quiz",
                "title": "Declaration Files",
                "question": (
                    "What file extension is used for TypeScript type declaration files?\n\n"
                    "  // These ship types for JavaScript libraries\n"
                    "  // e.g., @types/react contains react/___.ts"
                ),
                "lesson": (
                    "Declaration files (.d.ts) contain only type information:\n\n"
                    "  // math.d.ts\n"
                    "  declare function add(a: number, b: number): number;\n"
                    "  declare const PI: number;\n\n"
                    "They don't contain implementation — just type signatures.\n"
                    "@types/xxx packages on npm provide .d.ts files for JS libraries.\n\n"
                    "  npm install @types/react  // installs react type declarations"
                ),
                "options": [
                    ".ts",
                    ".d.ts",
                    ".types.ts",
                    ".typedef",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "The 'd' stands for 'declaration'.",
                    ".d.ts — declaration TypeScript files contain only types.",
                ],
            },
            {
                "id": "tl_4",
                "type": "quiz",
                "title": "Module Resolution",
                "question": (
                    "What does `\"moduleResolution\": \"node\"` tell the TypeScript compiler?\n\n"
                    "  {\n"
                    "    \"compilerOptions\": {\n"
                    "      \"moduleResolution\": \"node\"\n"
                    "    }\n"
                    "  }"
                ),
                "lesson": (
                    "moduleResolution controls how TypeScript finds imported modules:\n\n"
                    "  'node'       — mimics Node.js resolution (node_modules, index.ts)\n"
                    "  'node16'     — Node.js ESM + CJS resolution\n"
                    "  'bundler'    — for bundlers (Vite, webpack, esbuild)\n"
                    "  'classic'    — legacy TypeScript resolution (rarely used)\n\n"
                    "  import { foo } from './bar';\n"
                    "  // node resolution: ./bar.ts → ./bar/index.ts → node_modules/bar"
                ),
                "options": [
                    "Use Node.js module resolution algorithm (node_modules, index files)",
                    "Only allow importing .node binary files",
                    "Compile to Node.js native modules",
                    "Enable server-side rendering",
                ],
                "answer": "a",
                "xp": 30,
                "hints": [
                    "It tells the compiler how to find files when you write import statements.",
                    "Node resolution = check relative paths, then node_modules.",
                ],
            },
            {
                "id": "tl_5",
                "type": "quiz",
                "title": "ts-node vs tsx",
                "question": (
                    "What does `ts-node` do?\n\n"
                    "  $ ts-node script.ts\n"
                    "  $ tsx script.ts"
                ),
                "lesson": (
                    "ts-node and tsx run TypeScript directly without a separate compile step:\n\n"
                    "  ts-node — uses the TypeScript compiler (tsc) under the hood.\n"
                    "            Slower startup, full type checking optional.\n\n"
                    "  tsx     — uses esbuild for fast transpilation.\n"
                    "            Much faster, but no type checking.\n\n"
                    "  $ ts-node script.ts   // compile + run\n"
                    "  $ tsx script.ts        // fast transpile + run\n\n"
                    "For production, compile with tsc first, then run the JS output."
                ),
                "options": [
                    "A TypeScript linter",
                    "A TypeScript runtime that compiles and executes .ts files directly",
                    "A TypeScript-to-Python transpiler",
                    "A test runner for TypeScript",
                ],
                "answer": "b",
                "xp": 25,
                "hints": [
                    "It runs .ts files without a manual compile step.",
                    "ts-node = compile + execute TypeScript in one command.",
                ],
            },
        ],
    },
}
