"""
zones.py - All zone and challenge data for The Cache Matrix (Redis Quest)
Challenge types: quiz (with options list), text (options=[])
"""

ZONE_ORDER = [
    "redis_basics",
    "data_structures",
    "pubsub_streams",
    "caching_patterns",
    "redis_production",
]

ZONES = {
    "redis_basics": {
        "id": "redis_basics",
        "name": "The Key-Value Substrate",
        "subtitle": "GET, SET, DEL — The Atomic Layer",
        "color": "red",
        "icon": "🔑",
        "commands": ["SET", "GET", "DEL", "EXISTS", "EXPIRE", "TTL", "KEYS", "MSET"],
        "challenges": [
            {
                "id": "rb_1",
                "type": "quiz",
                "question": "What Redis command stores a key-value pair?",
                "options": ["GET", "SET", "PUT", "INSERT"],
                "answer": "b",
                "lesson": (
                    "SET — stores a string value at a given key.\n\n"
                    "Syntax: SET key value [EX seconds] [PX milliseconds] [NX|XX]\n\n"
                    "  EX seconds  — set expiration in seconds\n"
                    "  PX ms       — set expiration in milliseconds\n"
                    "  NX          — only set if key does NOT exist\n"
                    "  XX          — only set if key ALREADY exists\n\n"
                    "Example: SET session:abc123 '{\"user\":\"ghost\"}' EX 3600\n"
                    "  → stores the session with a 1-hour TTL"
                ),
                "xp": 50,
            },
            {
                "id": "rb_2",
                "type": "text",
                "question": "What Redis command retrieves the value stored at a given key?",
                "options": [],
                "answer": "GET",
                "lesson": (
                    "GET — retrieves the string value at a key.\n\n"
                    "Syntax: GET key\n\n"
                    "Returns the value if the key exists, or nil if it does not.\n"
                    "GET only works with string values. For other data structures,\n"
                    "use the type-specific commands (HGET, LRANGE, SMEMBERS, etc.).\n\n"
                    "Example: GET session:abc123\n"
                    "  → '{\"user\":\"ghost\"}'"
                ),
                "xp": 50,
            },
            {
                "id": "rb_3",
                "type": "quiz",
                "question": "You run DEL mykey. What happens if mykey does not exist?",
                "options": [
                    "Redis throws an error",
                    "Redis returns 0 (no keys were removed)",
                    "Redis returns nil",
                    "Redis creates the key with an empty value",
                ],
                "answer": "b",
                "lesson": (
                    "DEL — removes one or more keys.\n\n"
                    "Syntax: DEL key [key ...]\n\n"
                    "Returns an integer: the number of keys that were removed.\n"
                    "If none of the specified keys exist, it returns 0 — no error.\n"
                    "DEL is synchronous and blocks until the key is freed from memory.\n"
                    "For large keys, consider UNLINK (async deletion).\n\n"
                    "Example: DEL session:abc123 session:def456\n"
                    "  → (integer) 2  (both keys existed and were removed)"
                ),
                "xp": 50,
            },
            {
                "id": "rb_4",
                "type": "text",
                "question": "What Redis command checks whether a key exists without retrieving its value? Returns 1 if the key exists, 0 otherwise.",
                "options": [],
                "answer": "EXISTS",
                "lesson": (
                    "EXISTS — checks if one or more keys exist.\n\n"
                    "Syntax: EXISTS key [key ...]\n\n"
                    "Returns the count of keys that exist. For a single key: 1 or 0.\n"
                    "Useful for conditional logic without transferring the value.\n\n"
                    "Example: EXISTS session:abc123\n"
                    "  → (integer) 1"
                ),
                "xp": 50,
            },
            {
                "id": "rb_5",
                "type": "quiz",
                "question": "What does the EXPIRE command do in Redis?",
                "options": [
                    "Permanently deletes a key",
                    "Sets a time-to-live (TTL) in seconds on a key",
                    "Refreshes the value of a key",
                    "Moves a key to a different database",
                ],
                "answer": "b",
                "lesson": (
                    "EXPIRE — sets a timeout on a key, after which it is automatically deleted.\n\n"
                    "Syntax: EXPIRE key seconds\n\n"
                    "The key will be deleted after the specified seconds elapse.\n"
                    "Use PEXPIRE for millisecond precision.\n"
                    "Use PERSIST to remove an expiration.\n"
                    "Use TTL to check remaining time.\n\n"
                    "Example: EXPIRE session:abc123 3600\n"
                    "  → key auto-deletes in 1 hour"
                ),
                "xp": 75,
            },
            {
                "id": "rb_6",
                "type": "text",
                "question": "What Redis command returns the remaining time-to-live (in seconds) of a key that has an expiration set?",
                "options": [],
                "answer": "TTL",
                "lesson": (
                    "TTL — returns the remaining time to live of a key in seconds.\n\n"
                    "Syntax: TTL key\n\n"
                    "Returns:\n"
                    "  -2  if the key does not exist\n"
                    "  -1  if the key exists but has no associated expire\n"
                    "  n   the remaining TTL in seconds\n\n"
                    "Use PTTL for millisecond precision.\n\n"
                    "Example: TTL session:abc123  →  (integer) 3542"
                ),
                "xp": 50,
            },
            {
                "id": "rb_7",
                "type": "quiz",
                "question": "You need to set a key ONLY if it does not already exist (to implement a lock). Which SET option achieves this?",
                "options": [
                    "SET key value XX",
                    "SET key value NX",
                    "SET key value EX 10",
                    "SET key value KEEPTTL",
                ],
                "answer": "b",
                "lesson": (
                    "SET key value NX — the NX flag means 'Not eXists'.\n\n"
                    "The SET only succeeds if the key does not already exist.\n"
                    "Returns OK on success, nil if the key already exists.\n\n"
                    "This is the foundation of distributed locking in Redis:\n"
                    "  SET lock:resource xyz NX EX 30\n"
                    "  → acquires a lock for 30 seconds, only if no one else holds it.\n\n"
                    "XX is the opposite: only set if the key ALREADY exists."
                ),
                "xp": 75,
            },
            {
                "id": "rb_boss",
                "type": "quiz",
                "question": "You need to atomically set multiple keys at once. Which command sets key1=val1 and key2=val2 in a single operation?",
                "options": [
                    "SET key1 val1; SET key2 val2",
                    "MULTI SET key1 val1 SET key2 val2 EXEC",
                    "MSET key1 val1 key2 val2",
                    "SETALL key1 val1 key2 val2",
                ],
                "answer": "c",
                "lesson": (
                    "MSET — sets multiple keys to multiple values in a single atomic operation.\n\n"
                    "Syntax: MSET key1 value1 key2 value2 ...\n\n"
                    "MSET is atomic: all keys are set at once, never leaving a partial state.\n"
                    "There is no MSET NX equivalent — use MSETNX instead (sets all keys\n"
                    "only if NONE of them exist).\n\n"
                    "Similarly, MGET retrieves multiple keys at once:\n"
                    "  MGET key1 key2 key3\n"
                    "  → returns an array of values (nil for missing keys)"
                ),
                "xp": 200,
                "is_boss": True,
            },
        ],
    },
    "data_structures": {
        "id": "data_structures",
        "name": "The Structure Nexus",
        "subtitle": "Lists, Sets, Hashes, Sorted Sets",
        "color": "green",
        "icon": "🧬",
        "commands": ["LPUSH", "RPUSH", "LRANGE", "SADD", "SMEMBERS", "HSET", "HGET", "ZADD"],
        "challenges": [
            {
                "id": "ds_1",
                "type": "quiz",
                "question": "Which Redis command pushes an element to the LEFT (head) of a list?",
                "options": ["RPUSH", "LPUSH", "LADD", "PREPEND"],
                "answer": "b",
                "lesson": (
                    "LPUSH — inserts one or more values at the head (left) of a list.\n\n"
                    "Syntax: LPUSH key value [value ...]\n\n"
                    "If the key does not exist, an empty list is created before pushing.\n"
                    "Multiple values are inserted left-to-right, so:\n"
                    "  LPUSH mylist a b c  → list is [c, b, a]\n\n"
                    "RPUSH inserts at the tail (right) instead."
                ),
                "xp": 50,
            },
            {
                "id": "ds_2",
                "type": "text",
                "question": "What Redis command returns a range of elements from a list? For example, to get all elements: ___ mylist 0 -1",
                "options": [],
                "answer": "LRANGE",
                "lesson": (
                    "LRANGE — returns a range of elements from a list.\n\n"
                    "Syntax: LRANGE key start stop\n\n"
                    "Indices are zero-based. -1 means the last element.\n"
                    "  LRANGE mylist 0 -1   → returns all elements\n"
                    "  LRANGE mylist 0 4    → returns first 5 elements\n\n"
                    "LRANGE does NOT modify the list. It is a read-only operation.\n"
                    "Time complexity: O(S+N) where S is the offset and N is the range."
                ),
                "xp": 50,
            },
            {
                "id": "ds_3",
                "type": "quiz",
                "question": "What is the key difference between a Redis SET and a LIST?",
                "options": [
                    "Sets are ordered, lists are not",
                    "Sets contain only unique members, lists allow duplicates",
                    "Lists are limited to 100 elements, sets are unlimited",
                    "Sets support TTL, lists do not",
                ],
                "answer": "b",
                "lesson": (
                    "Redis Sets store unique, unordered string members.\n\n"
                    "Key commands:\n"
                    "  SADD key member [member ...]  — add members\n"
                    "  SMEMBERS key                  — return all members\n"
                    "  SISMEMBER key member           — check membership (O(1))\n"
                    "  SCARD key                     — count members\n\n"
                    "Set operations:\n"
                    "  SUNION, SINTER, SDIFF — union, intersection, difference\n\n"
                    "Use sets for: tags, unique visitors, permissions, online users."
                ),
                "xp": 50,
            },
            {
                "id": "ds_4",
                "type": "text",
                "question": "What Redis command adds one or more members to a set?",
                "options": [],
                "answer": "SADD",
                "lesson": (
                    "SADD — adds one or more members to a set.\n\n"
                    "Syntax: SADD key member [member ...]\n\n"
                    "Returns the number of members that were added (ignoring duplicates).\n"
                    "If the key does not exist, a new set is created.\n\n"
                    "Example: SADD online:users user:42 user:99 user:7\n"
                    "  → (integer) 3"
                ),
                "xp": 50,
            },
            {
                "id": "ds_5",
                "type": "quiz",
                "question": "You need to store structured data about a user (name, email, role) under one key. Which Redis data type is best suited?",
                "options": [
                    "String (JSON-encoded)",
                    "List",
                    "Hash",
                    "Sorted Set",
                ],
                "answer": "c",
                "lesson": (
                    "Redis Hashes — maps of field-value pairs stored under a single key.\n\n"
                    "Key commands:\n"
                    "  HSET key field value [field value ...]  — set fields\n"
                    "  HGET key field                          — get one field\n"
                    "  HMGET key field [field ...]             — get multiple fields\n"
                    "  HGETALL key                             — get all field-value pairs\n"
                    "  HDEL key field                          — delete a field\n\n"
                    "Hashes are memory-efficient for objects with many fields.\n"
                    "Each hash can store up to 2^32 - 1 field-value pairs.\n\n"
                    "Example: HSET user:42 name Ghost email ghost@nexus.io role admin"
                ),
                "xp": 75,
            },
            {
                "id": "ds_6",
                "type": "text",
                "question": "What Redis command retrieves the value of a specific field from a hash?",
                "options": [],
                "answer": "HGET",
                "lesson": (
                    "HGET — returns the value of a field in a hash.\n\n"
                    "Syntax: HGET key field\n\n"
                    "Returns the value, or nil if the key or field does not exist.\n\n"
                    "Example: HGET user:42 email  →  'ghost@nexus.io'\n\n"
                    "Use HGETALL to retrieve all fields and values at once.\n"
                    "Use HMGET to retrieve multiple specific fields in one call."
                ),
                "xp": 50,
            },
            {
                "id": "ds_7",
                "type": "quiz",
                "question": "A leaderboard needs members ranked by score, with O(log N) inserts and range queries by rank. Which Redis data type?",
                "options": [
                    "List with LINSERT",
                    "Hash with score field",
                    "Sorted Set (ZSET)",
                    "Stream",
                ],
                "answer": "c",
                "lesson": (
                    "Sorted Sets (ZSETs) — sets where each member has an associated score.\n\n"
                    "Members are unique. Scores are floating-point numbers.\n"
                    "Elements are ordered by score (ascending by default).\n\n"
                    "Key commands:\n"
                    "  ZADD key score member [score member ...]  — add/update members\n"
                    "  ZRANGE key start stop [WITHSCORES]        — range by rank\n"
                    "  ZRANGEBYSCORE key min max                 — range by score\n"
                    "  ZRANK key member                          — get rank of member\n"
                    "  ZREM key member                           — remove member\n\n"
                    "All rank operations are O(log N). Perfect for leaderboards,\n"
                    "rate limiters, priority queues, and time-series indexes."
                ),
                "xp": 75,
            },
            {
                "id": "ds_boss",
                "type": "quiz",
                "question": "You call ZADD leaderboard 100 alice 200 bob 150 charlie. What does ZRANGE leaderboard 0 -1 return?",
                "options": [
                    "alice, bob, charlie (insertion order)",
                    "bob, charlie, alice (descending score)",
                    "alice, charlie, bob (ascending score)",
                    "charlie, alice, bob (alphabetical)",
                ],
                "answer": "c",
                "lesson": (
                    "ZRANGE returns members ordered by score ascending.\n\n"
                    "After ZADD leaderboard 100 alice 200 bob 150 charlie:\n"
                    "  alice   → score 100\n"
                    "  charlie → score 150\n"
                    "  bob     → score 200\n\n"
                    "ZRANGE leaderboard 0 -1  →  alice, charlie, bob\n\n"
                    "For descending order, use ZREVRANGE or ZRANGE ... REV.\n"
                    "Add WITHSCORES to include the scores in the output."
                ),
                "xp": 200,
                "is_boss": True,
            },
        ],
    },
    "pubsub_streams": {
        "id": "pubsub_streams",
        "name": "The Signal Grid",
        "subtitle": "Pub/Sub & Streams — Real-Time Messaging",
        "color": "magenta",
        "icon": "📡",
        "commands": ["PUBLISH", "SUBSCRIBE", "XADD", "XREAD", "XRANGE", "XGROUP", "XACK", "XLEN"],
        "challenges": [
            {
                "id": "ps_1",
                "type": "quiz",
                "question": "In Redis Pub/Sub, what command sends a message to a channel?",
                "options": ["SEND", "PUBLISH", "EMIT", "BROADCAST"],
                "answer": "b",
                "lesson": (
                    "PUBLISH — sends a message to a channel.\n\n"
                    "Syntax: PUBLISH channel message\n\n"
                    "Returns the number of subscribers that received the message.\n"
                    "If no subscribers are listening, the message is lost — Pub/Sub\n"
                    "has no persistence or message queue semantics.\n\n"
                    "Example: PUBLISH alerts:critical 'Server node-7 unreachable'\n"
                    "  → (integer) 3  (3 subscribers received it)"
                ),
                "xp": 50,
            },
            {
                "id": "ps_2",
                "type": "text",
                "question": "What Redis command subscribes a client to one or more channels to receive messages?",
                "options": [],
                "answer": "SUBSCRIBE",
                "lesson": (
                    "SUBSCRIBE — subscribes the client to one or more channels.\n\n"
                    "Syntax: SUBSCRIBE channel [channel ...]\n\n"
                    "Once subscribed, the client enters a special mode where it can\n"
                    "only receive messages or unsubscribe. No other commands are\n"
                    "allowed on the same connection.\n\n"
                    "Use PSUBSCRIBE for pattern-based subscriptions:\n"
                    "  PSUBSCRIBE alerts:*   → matches alerts:critical, alerts:warning, etc."
                ),
                "xp": 50,
            },
            {
                "id": "ps_3",
                "type": "quiz",
                "question": "What is the biggest limitation of Redis Pub/Sub compared to a message queue like Kafka?",
                "options": [
                    "Pub/Sub is slower than Kafka",
                    "Pub/Sub can only have one subscriber per channel",
                    "Messages are fire-and-forget — if no subscriber is listening, the message is lost",
                    "Pub/Sub does not support pattern matching",
                ],
                "answer": "c",
                "lesson": (
                    "Redis Pub/Sub is fire-and-forget — no persistence, no replay.\n\n"
                    "If a subscriber disconnects and reconnects, it misses all messages\n"
                    "published during the gap. There is no acknowledgment mechanism.\n"
                    "There is no message queue — messages go directly to subscribers.\n\n"
                    "For durable messaging with replay, use Redis Streams instead.\n"
                    "Streams persist messages, support consumer groups, and allow\n"
                    "reading from any point in the stream history."
                ),
                "xp": 75,
            },
            {
                "id": "ps_4",
                "type": "text",
                "question": "What Redis command appends a new entry to a stream? Syntax: ___ mystream * field1 value1 field2 value2",
                "options": [],
                "answer": "XADD",
                "lesson": (
                    "XADD — appends a new entry to a stream.\n\n"
                    "Syntax: XADD key [NOMKSTREAM] [MAXLEN|MINID [=|~] threshold] *|id field value [field value ...]\n\n"
                    "The * auto-generates a unique ID (timestamp-sequence).\n"
                    "Each entry is a set of field-value pairs (like a hash).\n\n"
                    "Example: XADD events:clicks * user_id 42 page /dashboard\n"
                    "  → '1680000000000-0'  (auto-generated ID)\n\n"
                    "Use MAXLEN to cap the stream length:\n"
                    "  XADD events:clicks MAXLEN ~ 10000 * user_id 42 page /home"
                ),
                "xp": 50,
            },
            {
                "id": "ps_5",
                "type": "quiz",
                "question": "What does the * argument mean in XADD mystream * field value?",
                "options": [
                    "Wildcard — match all existing entries",
                    "Auto-generate a unique entry ID based on timestamp",
                    "Append to the end of the stream (like RPUSH)",
                    "Create the stream if it does not exist",
                ],
                "answer": "b",
                "lesson": (
                    "The * in XADD auto-generates a unique entry ID.\n\n"
                    "Format: <millisecondsTimestamp>-<sequenceNumber>\n"
                    "  Example: 1680000000000-0\n\n"
                    "The timestamp is the server time. The sequence number handles\n"
                    "multiple entries within the same millisecond.\n\n"
                    "You can specify a custom ID instead of *, but it must be\n"
                    "greater than the last entry's ID (streams are append-only)."
                ),
                "xp": 50,
            },
            {
                "id": "ps_6",
                "type": "quiz",
                "question": "To read stream entries between two IDs (inclusive), which command do you use?",
                "options": [
                    "XREAD",
                    "XRANGE",
                    "XGET",
                    "XSCAN",
                ],
                "answer": "b",
                "lesson": (
                    "XRANGE — returns entries within a range of IDs.\n\n"
                    "Syntax: XRANGE key start end [COUNT count]\n\n"
                    "  XRANGE mystream - +        → all entries (- is minimum ID, + is maximum)\n"
                    "  XRANGE mystream 1680000000000-0 1680000001000-0  → specific range\n\n"
                    "XRANGE is O(log N) to seek + O(M) for M returned entries.\n\n"
                    "XREVRANGE is the reverse — latest entries first.\n\n"
                    "XREAD is different: it blocks and waits for new entries\n"
                    "(like SUBSCRIBE but for streams)."
                ),
                "xp": 75,
            },
            {
                "id": "ps_7",
                "type": "text",
                "question": "In Redis Streams, what command creates a consumer group for distributed processing of stream entries?",
                "options": [],
                "answer": "XGROUP",
                "lesson": (
                    "XGROUP — manages consumer groups on a stream.\n\n"
                    "Create a group:\n"
                    "  XGROUP CREATE mystream mygroup $ MKSTREAM\n"
                    "  → $ means 'only new entries from now on'\n"
                    "  → 0 means 'all existing entries'\n\n"
                    "Read as a consumer in the group:\n"
                    "  XREADGROUP GROUP mygroup consumer1 COUNT 10 BLOCK 2000 STREAMS mystream >\n\n"
                    "Acknowledge processed entries:\n"
                    "  XACK mystream mygroup entry-id\n\n"
                    "Consumer groups guarantee each entry is delivered to exactly\n"
                    "one consumer in the group — enabling parallel processing."
                ),
                "xp": 75,
            },
            {
                "id": "ps_boss",
                "type": "quiz",
                "question": "A consumer in group 'processors' reads entries with XREADGROUP but crashes before calling XACK. What happens to those entries?",
                "options": [
                    "They are lost forever",
                    "They remain in the consumer's Pending Entries List (PEL) and can be claimed by another consumer",
                    "They are automatically re-delivered after 5 seconds",
                    "They are moved to a dead-letter queue",
                ],
                "answer": "b",
                "lesson": (
                    "Unacknowledged entries stay in the Pending Entries List (PEL).\n\n"
                    "When a consumer reads with XREADGROUP but does not XACK,\n"
                    "the entry remains pending. It will not be delivered to other\n"
                    "consumers in the group unless explicitly claimed.\n\n"
                    "Recovery:\n"
                    "  XPENDING mystream mygroup    → see pending entries\n"
                    "  XCLAIM mystream mygroup consumer2 3600000 entry-id\n"
                    "  → claim entries idle for >1 hour to consumer2\n\n"
                    "  XAUTOCLAIM mystream mygroup consumer2 3600000 0-0\n"
                    "  → automatically claim all idle entries (Redis 6.2+)\n\n"
                    "This guarantees at-least-once delivery without message loss."
                ),
                "xp": 200,
                "is_boss": True,
            },
        ],
    },
    "caching_patterns": {
        "id": "caching_patterns",
        "name": "The Temporal Cache",
        "subtitle": "Write-Through, Write-Behind, TTL Strategies",
        "color": "yellow",
        "icon": "⚡",
        "commands": ["SET EX", "GET", "SETEX", "TTL", "PERSIST", "WATCH", "MULTI", "EXEC"],
        "challenges": [
            {
                "id": "cp_1",
                "type": "quiz",
                "question": "In a cache-aside (lazy loading) pattern, when does data get loaded into the cache?",
                "options": [
                    "When the application starts up",
                    "On a cache miss — the app reads from the DB and writes to the cache",
                    "When the database record is updated",
                    "At a fixed interval by a background job",
                ],
                "answer": "b",
                "lesson": (
                    "Cache-Aside (Lazy Loading) — the most common caching pattern.\n\n"
                    "Flow:\n"
                    "  1. App checks cache (GET key)\n"
                    "  2. Cache HIT → return cached value\n"
                    "  3. Cache MISS → query database\n"
                    "  4. Write result to cache (SET key value EX ttl)\n"
                    "  5. Return result\n\n"
                    "Pros: only caches data that is actually requested.\n"
                    "Cons: first request is always a miss (cold start).\n"
                    "Cache can become stale if the DB is updated directly."
                ),
                "xp": 50,
            },
            {
                "id": "cp_2",
                "type": "quiz",
                "question": "In a write-through caching pattern, when is the cache updated?",
                "options": [
                    "Only when a cache miss occurs",
                    "At every write — data is written to both cache and database synchronously",
                    "After a background job detects stale entries",
                    "Only when the TTL expires",
                ],
                "answer": "b",
                "lesson": (
                    "Write-Through — every write goes to both cache and database.\n\n"
                    "Flow:\n"
                    "  1. App writes data\n"
                    "  2. Write to cache AND database (synchronously)\n"
                    "  3. Subsequent reads always hit the cache\n\n"
                    "Pros: cache is always consistent with the database.\n"
                    "Cons: write latency increases (two writes per operation).\n"
                    "Can fill cache with data that is never read.\n\n"
                    "Pair with TTL to evict unread data."
                ),
                "xp": 50,
            },
            {
                "id": "cp_3",
                "type": "text",
                "question": "In a write-behind (write-back) pattern, writes go to the cache first and are asynchronously flushed to the database later. What is the main risk of this pattern?",
                "options": [],
                "answer": "data loss",
                "lesson": (
                    "Write-Behind (Write-Back) — writes go to cache first, DB later.\n\n"
                    "Flow:\n"
                    "  1. App writes to cache\n"
                    "  2. Return success immediately\n"
                    "  3. Background process flushes to database asynchronously\n\n"
                    "Pros: fastest write performance. Batches DB writes.\n"
                    "Cons: if the cache node crashes before flushing, data is lost.\n"
                    "Complex to implement correctly. Requires durable queue or\n"
                    "replication to mitigate data loss risk."
                ),
                "xp": 75,
            },
            {
                "id": "cp_4",
                "type": "quiz",
                "question": "A 'thundering herd' (cache stampede) occurs when a popular key expires and many requests simultaneously hit the database. Which Redis feature helps prevent this?",
                "options": [
                    "WATCH/MULTI for transactions",
                    "SET key value NX EX (locking with NX to let only one request rebuild the cache)",
                    "OBJECT ENCODING to compress the value",
                    "SUBSCRIBE to listen for eviction events",
                ],
                "answer": "b",
                "lesson": (
                    "Cache Stampede Prevention — use SET NX as a distributed lock.\n\n"
                    "When a popular key expires:\n"
                    "  1. First request: SET rebuild-lock:key 1 NX EX 10 → OK\n"
                    "  2. First request rebuilds the cache from DB\n"
                    "  3. Other requests: SET NX returns nil → they wait or use stale data\n\n"
                    "Other strategies:\n"
                    "  - Probabilistic early expiration (refresh before TTL expires)\n"
                    "  - Background refresh (never let popular keys expire)\n"
                    "  - Stale-while-revalidate (serve stale, refresh async)"
                ),
                "xp": 75,
            },
            {
                "id": "cp_5",
                "type": "quiz",
                "question": "What Redis eviction policy removes the least recently used keys when maxmemory is reached?",
                "options": [
                    "volatile-lru",
                    "allkeys-lru",
                    "allkeys-random",
                    "noeviction",
                ],
                "answer": "b",
                "lesson": (
                    "Redis eviction policies — what happens when maxmemory is reached.\n\n"
                    "  noeviction      — return errors on writes (default)\n"
                    "  allkeys-lru     — evict least recently used keys (any key)\n"
                    "  volatile-lru    — evict LRU keys that have an expire set\n"
                    "  allkeys-lfu     — evict least frequently used keys\n"
                    "  volatile-lfu    — evict LFU keys with an expire\n"
                    "  allkeys-random  — evict random keys\n"
                    "  volatile-random — evict random keys with an expire\n"
                    "  volatile-ttl    — evict keys with the shortest TTL\n\n"
                    "For a pure cache: allkeys-lru or allkeys-lfu.\n"
                    "For mixed use (cache + persistent data): volatile-lru."
                ),
                "xp": 75,
            },
            {
                "id": "cp_6",
                "type": "text",
                "question": "What Redis command sets a key with a value AND an expiration in seconds, in a single atomic call? Syntax: ___ key seconds value",
                "options": [],
                "answer": "SETEX",
                "lesson": (
                    "SETEX — sets a key with a value and an expiration atomically.\n\n"
                    "Syntax: SETEX key seconds value\n\n"
                    "Equivalent to: SET key value EX seconds\n\n"
                    "SETEX is atomic — the value and TTL are set together.\n"
                    "There is no window where the key exists without a TTL.\n\n"
                    "For millisecond precision, use PSETEX.\n\n"
                    "Note: SET key value EX seconds is the modern preferred form,\n"
                    "but SETEX is still widely used and fully supported."
                ),
                "xp": 50,
            },
            {
                "id": "cp_7",
                "type": "quiz",
                "question": "You want to ensure that a cached value is only updated if no other client has modified it since you read it. Which Redis mechanism provides this optimistic locking?",
                "options": [
                    "SETNX",
                    "WATCH / MULTI / EXEC (optimistic locking with CAS semantics)",
                    "LOCK command",
                    "EXPIRE with a very short TTL",
                ],
                "answer": "b",
                "lesson": (
                    "WATCH / MULTI / EXEC — optimistic locking in Redis.\n\n"
                    "  WATCH key         → start watching the key\n"
                    "  val = GET key     → read current value\n"
                    "  MULTI             → start transaction\n"
                    "  SET key new_val   → queue write\n"
                    "  EXEC              → execute (returns nil if key changed since WATCH)\n\n"
                    "If another client modifies the watched key between WATCH and EXEC,\n"
                    "the transaction is aborted (EXEC returns nil).\n"
                    "This provides check-and-set (CAS) semantics without true locks.\n\n"
                    "Retry pattern: loop until EXEC succeeds."
                ),
                "xp": 75,
            },
            {
                "id": "cp_boss",
                "type": "quiz",
                "question": "Your application uses cache-aside with a 60-second TTL. A database update happens at T=30s. For the next 30 seconds, the cache serves stale data. What pattern eliminates this staleness?",
                "options": [
                    "Increase the TTL to 5 minutes",
                    "Use write-through: update the cache at the same time as the database",
                    "Switch to allkeys-random eviction",
                    "Use SUBSCRIBE to listen for database changes",
                ],
                "answer": "b",
                "lesson": (
                    "Write-Through eliminates the stale window in cache-aside.\n\n"
                    "Cache-aside problem: the cache has no idea the DB was updated.\n"
                    "It serves the old value until the TTL expires.\n\n"
                    "Write-through solution: every DB write also updates the cache.\n"
                    "The cache is always in sync with the database.\n\n"
                    "Hybrid approach (most common in production):\n"
                    "  - Write-through for frequently read keys\n"
                    "  - Cache-aside for everything else\n"
                    "  - TTL as a safety net (catches bugs, handles edge cases)\n"
                    "  - Cache invalidation (DEL key) on DB write as a simpler alternative"
                ),
                "xp": 200,
                "is_boss": True,
            },
        ],
    },
    "redis_production": {
        "id": "redis_production",
        "name": "The Replication Spine",
        "subtitle": "Clustering, Persistence, Sentinel",
        "color": "red",
        "icon": "🏗",
        "commands": ["CLUSTER", "SENTINEL", "BGSAVE", "BGREWRITEAOF", "INFO", "SLAVEOF", "CONFIG", "DEBUG"],
        "challenges": [
            {
                "id": "rp_1",
                "type": "quiz",
                "question": "Redis supports two persistence mechanisms. RDB creates point-in-time snapshots. What is the other one?",
                "options": [
                    "WAL (Write-Ahead Log)",
                    "AOF (Append Only File)",
                    "Binlog (Binary Log)",
                    "Journaling",
                ],
                "answer": "b",
                "lesson": (
                    "Redis Persistence: RDB vs AOF.\n\n"
                    "RDB (Redis Database):\n"
                    "  - Point-in-time snapshots at configured intervals\n"
                    "  - Compact binary format, fast restarts\n"
                    "  - Data loss between snapshots (e.g., last 5 minutes)\n"
                    "  - BGSAVE triggers a manual snapshot\n\n"
                    "AOF (Append Only File):\n"
                    "  - Logs every write operation\n"
                    "  - Three fsync policies: always, everysec (default), no\n"
                    "  - More durable (at most 1 second of data loss with everysec)\n"
                    "  - Larger files, slower restarts\n"
                    "  - BGREWRITEAOF compacts the AOF file\n\n"
                    "Production recommendation: enable BOTH RDB + AOF."
                ),
                "xp": 50,
            },
            {
                "id": "rp_2",
                "type": "quiz",
                "question": "With AOF persistence, the appendfsync everysec policy means:",
                "options": [
                    "Every command is fsynced to disk before returning to the client",
                    "The AOF buffer is fsynced to disk once per second by a background thread",
                    "The OS decides when to flush (no explicit fsync)",
                    "The AOF is rewritten every second",
                ],
                "answer": "b",
                "lesson": (
                    "AOF fsync policies:\n\n"
                    "  appendfsync always   — fsync after every write command\n"
                    "    Slowest. Most durable. Zero data loss.\n\n"
                    "  appendfsync everysec — fsync once per second (DEFAULT)\n"
                    "    Good balance. At most ~1 second of data loss.\n"
                    "    The fsync runs on a background thread.\n\n"
                    "  appendfsync no       — let the OS flush when it wants\n"
                    "    Fastest. Up to 30 seconds of data loss (OS buffer).\n\n"
                    "For most production workloads: everysec is the right choice."
                ),
                "xp": 50,
            },
            {
                "id": "rp_3",
                "type": "text",
                "question": "What Redis command triggers a background RDB snapshot to disk?",
                "options": [],
                "answer": "BGSAVE",
                "lesson": (
                    "BGSAVE — triggers a background RDB snapshot.\n\n"
                    "Redis forks a child process that writes the snapshot to disk.\n"
                    "The parent process continues serving requests.\n\n"
                    "SAVE (without BG) blocks the server until the snapshot completes.\n"
                    "Never use SAVE in production.\n\n"
                    "RDB snapshots are configured with the 'save' directive:\n"
                    "  save 900 1      → snapshot if 1+ keys changed in 900 seconds\n"
                    "  save 300 10     → snapshot if 10+ keys changed in 300 seconds\n"
                    "  save 60 10000   → snapshot if 10000+ keys changed in 60 seconds"
                ),
                "xp": 50,
            },
            {
                "id": "rp_4",
                "type": "quiz",
                "question": "Redis Sentinel provides high availability. What does Sentinel do when the master node fails?",
                "options": [
                    "Restarts the master process automatically",
                    "Promotes a replica to master and reconfigures other replicas to follow the new master",
                    "Switches to AOF persistence mode",
                    "Pauses all writes until the master recovers",
                ],
                "answer": "b",
                "lesson": (
                    "Redis Sentinel — automatic failover and monitoring.\n\n"
                    "Sentinel runs as a separate process (typically 3+ instances).\n\n"
                    "Responsibilities:\n"
                    "  1. Monitoring — checks if master and replicas are healthy\n"
                    "  2. Notification — alerts administrators via API\n"
                    "  3. Automatic failover — promotes replica to master\n"
                    "  4. Configuration provider — clients ask Sentinel for current master\n\n"
                    "Failover process:\n"
                    "  - Sentinel detects master failure (quorum vote)\n"
                    "  - Selects the best replica (most data, lowest lag)\n"
                    "  - Promotes replica to master (REPLICAOF NO ONE)\n"
                    "  - Reconfigures other replicas to follow new master\n"
                    "  - Notifies clients of the new master address"
                ),
                "xp": 75,
            },
            {
                "id": "rp_5",
                "type": "quiz",
                "question": "Redis Cluster automatically shards data across multiple nodes. How does it determine which node holds a given key?",
                "options": [
                    "Consistent hashing ring",
                    "Hash slots — CRC16(key) mod 16384 maps to one of 16384 slots distributed across nodes",
                    "Round-robin across nodes",
                    "The client chooses the node",
                ],
                "answer": "b",
                "lesson": (
                    "Redis Cluster uses hash slots for data partitioning.\n\n"
                    "  - 16384 hash slots total\n"
                    "  - Each key maps to a slot: CRC16(key) mod 16384\n"
                    "  - Each master node owns a subset of slots\n\n"
                    "Example with 3 masters:\n"
                    "  Node A: slots 0-5460\n"
                    "  Node B: slots 5461-10922\n"
                    "  Node C: slots 10923-16383\n\n"
                    "If a client sends a command to the wrong node, it receives\n"
                    "a MOVED redirect: -MOVED 3999 127.0.0.1:6380\n\n"
                    "Multi-key operations only work if all keys are in the same slot.\n"
                    "Use hash tags {tag} to force keys to the same slot:\n"
                    "  user:{42}:profile and user:{42}:session → same slot"
                ),
                "xp": 75,
            },
            {
                "id": "rp_6",
                "type": "text",
                "question": "In Redis Cluster, to force multiple keys to the same hash slot for multi-key operations, you use hash tags. What characters wrap the hash tag? Example: user:{id}:profile",
                "options": [],
                "answer": "{}",
                "lesson": (
                    "Hash tags — curly braces {} force keys to the same hash slot.\n\n"
                    "Redis Cluster hashes only the content between the first { and\n"
                    "the first } to determine the slot.\n\n"
                    "  user:{42}:profile  → hashes '42'\n"
                    "  user:{42}:session  → hashes '42'\n"
                    "  → both keys land on the same slot\n\n"
                    "This enables multi-key operations (MGET, MSET, pipelines)\n"
                    "across related keys in a cluster.\n\n"
                    "Without hash tags, user:42:profile and user:42:session\n"
                    "would likely land on different nodes."
                ),
                "xp": 50,
            },
            {
                "id": "rp_7",
                "type": "quiz",
                "question": "You have a Redis instance using 8GB of a 10GB maxmemory limit. INFO memory shows high fragmentation ratio (mem_fragmentation_ratio: 2.5). What does this indicate?",
                "options": [
                    "Redis is using swap space",
                    "The OS has allocated ~2.5x more memory than Redis logically needs — heavy fragmentation",
                    "Redis is compressing data at a 2.5x ratio",
                    "25% of keys have expired but not been freed",
                ],
                "answer": "b",
                "lesson": (
                    "mem_fragmentation_ratio = RSS / used_memory\n\n"
                    "  Ratio > 1.5 → significant fragmentation\n"
                    "    The OS allocator has allocated much more memory than Redis\n"
                    "    logically uses. Caused by many small allocations/deallocations.\n\n"
                    "  Ratio ≈ 1.0 → healthy\n\n"
                    "  Ratio < 1.0 → Redis is using swap (CRITICAL — severe performance hit)\n\n"
                    "Fix fragmentation:\n"
                    "  - CONFIG SET activedefrag yes (Redis 4.0+)\n"
                    "  - Restart the Redis process (clean allocation)\n"
                    "  - Use jemalloc (default allocator, handles this well)\n\n"
                    "Monitor with: INFO memory"
                ),
                "xp": 75,
            },
            {
                "id": "rp_boss",
                "type": "quiz",
                "question": "Your Redis Cluster has 3 masters (A, B, C), each with one replica. Master B goes down. What happens?",
                "options": [
                    "The entire cluster stops accepting writes",
                    "B's replica is promoted to master; cluster continues operating on all slots",
                    "Slots owned by B become read-only until B returns",
                    "A and C split B's hash slots between them",
                ],
                "answer": "b",
                "lesson": (
                    "Redis Cluster automatic failover:\n\n"
                    "When a master fails:\n"
                    "  1. Other masters detect the failure (PFAIL → FAIL)\n"
                    "  2. The failed master's replica triggers an election\n"
                    "  3. A majority of masters vote to approve the failover\n"
                    "  4. The replica promotes itself to master\n"
                    "  5. It takes ownership of the failed master's hash slots\n"
                    "  6. The cluster continues with full coverage\n\n"
                    "If no replica is available for the failed master,\n"
                    "the cluster enters a FAIL state for those slots\n"
                    "(controlled by cluster-require-full-coverage config).\n\n"
                    "This is why production clusters use at least 1 replica per master."
                ),
                "xp": 200,
                "is_boss": True,
            },
        ],
    },
}
