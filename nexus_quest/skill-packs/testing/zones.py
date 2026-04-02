"""
zones.py - All zone and challenge data for The Verification Engine
Challenge types: quiz (options list + answer letter), text (options=[], answer string)
"""

ZONES = {
    "unit_testing_fundamentals": {
        "id": "unit_testing_fundamentals",
        "name": "Unit Testing Fundamentals",
        "subtitle": "pytest, Assertions, First Tests",
        "color": "cyan",
        "icon": "🧪",
        "commands": ["pytest", "assert", "test_", "pytest.raises", "conftest"],
        "challenges": [
            {
                "id": "utf_1",
                "type": "quiz",
                "question": "What naming convention must Python test files follow for pytest to automatically discover them?",
                "options": [
                    "Files must start with 'check_'",
                    "Files must start with 'test_' or end with '_test.py'",
                    "Files must be named 'unittest.py'",
                    "Files can have any name if they contain test functions",
                ],
                "answer": "b",
                "lesson": (
                    "pytest discovers tests by searching for files matching test_*.py or *_test.py.\n\n"
                    "Inside those files, it collects:\n"
                    "  - Functions starting with test_\n"
                    "  - Classes starting with Test (no __init__)\n"
                    "  - Methods starting with test_ inside those classes\n\n"
                    "Example:\n"
                    "  # test_auth.py\n"
                    "  def test_login_success():\n"
                    "      assert authenticate('admin', 'pass123') is True"
                ),
                "xp": 50,
            },
            {
                "id": "utf_2",
                "type": "quiz",
                "question": "Which command runs all tests in a project directory recursively with verbose output?",
                "options": [
                    "python -m unittest discover -v",
                    "pytest -v",
                    "pytest --all --recursive",
                    "python test_runner.py -v",
                ],
                "answer": "b",
                "lesson": (
                    "pytest -v runs all discovered tests with verbose output.\n\n"
                    "Common pytest flags:\n"
                    "  pytest -v           Verbose — shows each test name and result\n"
                    "  pytest -x           Stop on first failure\n"
                    "  pytest -k 'auth'    Run only tests matching 'auth'\n"
                    "  pytest --tb=short   Shorter traceback output\n"
                    "  pytest -q           Quiet — minimal output"
                ),
                "xp": 50,
            },
            {
                "id": "utf_3",
                "type": "text",
                "question": "In pytest, what single keyword is used to verify that a condition is true inside a test function? (One word, lowercase.)",
                "options": [],
                "answer": "assert",
                "lesson": (
                    "assert — pytest's core assertion mechanism. No special API needed.\n\n"
                    "Unlike unittest's self.assertEqual(), pytest uses plain assert statements\n"
                    "and provides detailed introspection on failure.\n\n"
                    "Examples:\n"
                    "  assert result == 42\n"
                    "  assert 'error' in response.text\n"
                    "  assert len(users) > 0\n"
                    "  assert user.is_active is True\n\n"
                    "On failure, pytest rewrites the assert to show the actual values."
                ),
                "xp": 50,
            },
            {
                "id": "utf_4",
                "type": "quiz",
                "question": "How do you test that a function raises a specific exception in pytest?",
                "options": [
                    "try/except inside the test and assert on the exception",
                    "with pytest.raises(ExceptionType):",
                    "assert raises(func, ExceptionType)",
                    "@pytest.expect_error(ExceptionType)",
                ],
                "answer": "b",
                "lesson": (
                    "pytest.raises() is a context manager for testing expected exceptions.\n\n"
                    "Usage:\n"
                    "  def test_divide_by_zero():\n"
                    "      with pytest.raises(ZeroDivisionError):\n"
                    "          result = 1 / 0\n\n"
                    "You can also inspect the exception:\n"
                    "  with pytest.raises(ValueError) as exc_info:\n"
                    "      int('not_a_number')\n"
                    "  assert 'invalid literal' in str(exc_info.value)"
                ),
                "xp": 75,
            },
            {
                "id": "utf_5",
                "type": "text",
                "question": "What is the name of the special pytest configuration file (placed in test directories) that can define shared fixtures? Filename only, with extension.",
                "options": [],
                "answer": "conftest.py",
                "lesson": (
                    "conftest.py — pytest's shared fixture and plugin configuration file.\n\n"
                    "Fixtures defined in conftest.py are automatically available\n"
                    "to all tests in the same directory and subdirectories.\n\n"
                    "  # conftest.py\n"
                    "  @pytest.fixture\n"
                    "  def db_connection():\n"
                    "      conn = create_connection()\n"
                    "      yield conn\n"
                    "      conn.close()\n\n"
                    "No import needed — pytest injects conftest fixtures automatically."
                ),
                "xp": 50,
            },
            {
                "id": "utf_6",
                "type": "quiz",
                "question": "What does the -x flag do when running pytest?",
                "options": [
                    "Enables extra verbose output",
                    "Excludes slow tests from the run",
                    "Stops the test run on the first failure",
                    "Runs tests in parallel across CPUs",
                ],
                "answer": "c",
                "lesson": (
                    "pytest -x stops after the first test failure.\n\n"
                    "Related flags for controlling failure behavior:\n"
                    "  pytest -x              Stop on first failure\n"
                    "  pytest --maxfail=3     Stop after 3 failures\n"
                    "  pytest --lf            Re-run only last failed tests\n"
                    "  pytest --ff            Run failures first, then the rest\n\n"
                    "Useful for fast feedback during development."
                ),
                "xp": 50,
            },
            {
                "id": "utf_7",
                "type": "quiz",
                "question": "Which assertion style does pytest natively use, compared to unittest?",
                "options": [
                    "self.assertEqual() and self.assertTrue()",
                    "Plain Python assert statements with automatic introspection",
                    "expect() chains like JavaScript testing frameworks",
                    "Custom assertion functions from the pytest.assert module",
                ],
                "answer": "b",
                "lesson": (
                    "pytest rewrites plain assert statements to provide rich failure messages.\n\n"
                    "Instead of:\n"
                    "  self.assertEqual(a, b)    # unittest\n"
                    "  self.assertIn(x, lst)     # unittest\n\n"
                    "You write:\n"
                    "  assert a == b\n"
                    "  assert x in lst\n\n"
                    "On failure, pytest shows:\n"
                    "  AssertionError: assert 3 == 4\n"
                    "  where 3 = func()\n\n"
                    "This is called assertion introspection / rewriting."
                ),
                "xp": 50,
            },
            {
                "id": "utf_boss",
                "type": "quiz",
                "question": "A test needs to verify that process_payment(amount=-50) raises a ValueError with the message 'Amount must be positive'. Which approach correctly validates BOTH the exception type AND the message?",
                "options": [
                    "assert process_payment(-50) == ValueError('Amount must be positive')",
                    "with pytest.raises(ValueError, match='Amount must be positive'): process_payment(-50)",
                    "try: process_payment(-50) except: pass",
                    "pytest.expect(ValueError, process_payment, -50)",
                ],
                "answer": "b",
                "lesson": (
                    "pytest.raises() accepts a match parameter for regex matching on the message.\n\n"
                    "  with pytest.raises(ValueError, match='Amount must be positive'):\n"
                    "      process_payment(amount=-50)\n\n"
                    "The match parameter is a regex, so you can use patterns:\n"
                    "  match=r'Amount must be \\w+'   # regex pattern\n"
                    "  match='positive'               # substring match\n\n"
                    "This is the idiomatic way to assert both exception type and message."
                ),
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "pytest.raises can take a 'match' keyword for regex matching on the exception message.",
                    "The match parameter accepts a regular expression pattern.",
                ],
            },
        ],
    },

    "mocking_and_test_doubles": {
        "id": "mocking_and_test_doubles",
        "name": "Mocking & Test Doubles",
        "subtitle": "unittest.mock, Patching, Fakes, Stubs",
        "color": "magenta",
        "icon": "🎭",
        "commands": ["Mock", "patch", "MagicMock", "side_effect", "return_value"],
        "challenges": [
            {
                "id": "mtd_1",
                "type": "quiz",
                "question": "What is the primary purpose of mocking in unit tests?",
                "options": [
                    "To speed up tests by skipping slow code paths",
                    "To isolate the unit under test by replacing its dependencies with controlled substitutes",
                    "To generate random test data automatically",
                    "To run tests in parallel without shared state conflicts",
                ],
                "answer": "b",
                "lesson": (
                    "Mocking replaces real dependencies with controlled substitutes.\n\n"
                    "Why mock?\n"
                    "  - Isolate the unit under test from external systems\n"
                    "  - Control what dependencies return (deterministic tests)\n"
                    "  - Avoid slow operations (network, DB, filesystem)\n"
                    "  - Verify interactions (was this method called?)\n\n"
                    "Test doubles: mock, stub, fake, spy, dummy — each serves a different purpose."
                ),
                "xp": 50,
            },
            {
                "id": "mtd_2",
                "type": "quiz",
                "question": "Which module in the Python standard library provides Mock and patch?",
                "options": [
                    "pytest.mock",
                    "unittest.mock",
                    "mock (third-party package)",
                    "testing.doubles",
                ],
                "answer": "b",
                "lesson": (
                    "unittest.mock is part of Python's standard library (3.3+).\n\n"
                    "Key imports:\n"
                    "  from unittest.mock import Mock, MagicMock, patch\n\n"
                    "Note: pytest-mock is a popular wrapper that provides a 'mocker' fixture,\n"
                    "but the underlying implementation is still unittest.mock.\n\n"
                    "  # with pytest-mock\n"
                    "  def test_fetch(mocker):\n"
                    "      mocker.patch('app.requests.get')"
                ),
                "xp": 50,
            },
            {
                "id": "mtd_3",
                "type": "text",
                "question": "When using @patch, you should patch the target where it is LOOKED UP, not where it is DEFINED. If module app.service imports requests and calls requests.get(), and your test file tests app.service, what string do you pass to @patch? (Full dotted path.)",
                "options": [],
                "answer": "app.service.requests.get",
                "lesson": (
                    "The golden rule of patching: patch where the object is LOOKED UP.\n\n"
                    "If app/service.py does:\n"
                    "  import requests\n"
                    "  def fetch(): return requests.get(url)\n\n"
                    "You patch 'app.service.requests.get' — NOT 'requests.get'.\n\n"
                    "Why? Because app.service has its own reference to requests.\n"
                    "Patching the original module doesn't affect that reference.\n\n"
                    "  @patch('app.service.requests.get')\n"
                    "  def test_fetch(mock_get):\n"
                    "      mock_get.return_value.json.return_value = {'ok': True}"
                ),
                "xp": 75,
            },
            {
                "id": "mtd_4",
                "type": "quiz",
                "question": "What is the difference between Mock() and MagicMock()?",
                "options": [
                    "MagicMock is faster; Mock is deprecated",
                    "MagicMock supports magic/dunder methods (__len__, __iter__, etc.); Mock does not",
                    "Mock is for functions; MagicMock is for classes",
                    "There is no difference; they are aliases",
                ],
                "answer": "b",
                "lesson": (
                    "MagicMock is a subclass of Mock with default implementations\n"
                    "of most magic (dunder) methods.\n\n"
                    "  m = MagicMock()\n"
                    "  len(m)      # returns 0 (MagicMock provides __len__)\n"
                    "  iter(m)     # works (MagicMock provides __iter__)\n\n"
                    "  m = Mock()\n"
                    "  len(m)      # TypeError — Mock doesn't provide __len__\n\n"
                    "Use MagicMock by default. Use Mock when you need to be strict\n"
                    "about which magic methods are supported."
                ),
                "xp": 50,
            },
            {
                "id": "mtd_5",
                "type": "quiz",
                "question": "How do you make a Mock raise an exception when called?",
                "options": [
                    "mock.raises(ValueError('bad input'))",
                    "mock.side_effect = ValueError('bad input')",
                    "mock.return_value = ValueError('bad input')",
                    "mock.exception = ValueError('bad input')",
                ],
                "answer": "b",
                "lesson": (
                    "side_effect controls what happens when a mock is called.\n\n"
                    "Raise an exception:\n"
                    "  mock.side_effect = ValueError('bad input')\n\n"
                    "Return different values on successive calls:\n"
                    "  mock.side_effect = [1, 2, 3]\n\n"
                    "Call a custom function:\n"
                    "  mock.side_effect = lambda x: x * 2\n\n"
                    "return_value sets a fixed return; side_effect overrides it."
                ),
                "xp": 75,
            },
            {
                "id": "mtd_6",
                "type": "text",
                "question": "What Mock attribute do you check to verify a mock was called exactly once with specific arguments? (Format: mock.method_name)",
                "options": [],
                "answer": "mock.assert_called_once_with",
                "lesson": (
                    "Mock assertion methods verify call behavior:\n\n"
                    "  mock.assert_called()              # called at least once\n"
                    "  mock.assert_called_once()         # called exactly once\n"
                    "  mock.assert_called_with(arg)      # last call had these args\n"
                    "  mock.assert_called_once_with(arg) # called once with these args\n"
                    "  mock.assert_not_called()          # never called\n\n"
                    "  mock.call_count                   # number of times called\n"
                    "  mock.call_args                    # args from last call\n"
                    "  mock.call_args_list               # args from all calls"
                ),
                "xp": 50,
            },
            {
                "id": "mtd_7",
                "type": "quiz",
                "question": "What is a 'spy' in testing terminology?",
                "options": [
                    "A mock that records calls but also executes the real implementation",
                    "A mock that only works in integration tests",
                    "A test that monitors production systems",
                    "A fixture that watches for test failures",
                ],
                "answer": "a",
                "lesson": (
                    "A spy wraps the real object — calls pass through to the real\n"
                    "implementation, but interactions are recorded.\n\n"
                    "In pytest-mock:\n"
                    "  spy = mocker.spy(obj, 'method_name')\n"
                    "  obj.method_name()  # real method executes\n"
                    "  spy.assert_called_once()  # but we can verify it was called\n\n"
                    "Test double hierarchy:\n"
                    "  Dummy — passed but never used\n"
                    "  Stub  — returns canned values\n"
                    "  Spy   — records calls + runs real code\n"
                    "  Mock  — records calls + returns configured values\n"
                    "  Fake  — working implementation (e.g., in-memory DB)"
                ),
                "xp": 50,
            },
            {
                "id": "mtd_boss",
                "type": "quiz",
                "question": "Your function send_alert() calls requests.post() to send a Slack notification and returns the status code. You need to test that send_alert('server down') calls requests.post with the correct payload WITHOUT making a real HTTP request. Which approach is correct?",
                "options": [
                    "Call send_alert() normally and check Slack for the message",
                    "@patch('myapp.alerts.requests.post') then configure mock_post.return_value.status_code = 200 and assert mock_post.assert_called_once_with(url, json={'text': 'server down'})",
                    "Set requests.post = None before the test and restore it after",
                    "Use pytest.skip() to skip network-dependent tests",
                ],
                "answer": "b",
                "lesson": (
                    "Complete mock pattern for HTTP calls:\n\n"
                    "  @patch('myapp.alerts.requests.post')\n"
                    "  def test_send_alert(mock_post):\n"
                    "      mock_post.return_value.status_code = 200\n"
                    "      result = send_alert('server down')\n"
                    "      mock_post.assert_called_once_with(\n"
                    "          SLACK_URL,\n"
                    "          json={'text': 'server down'}\n"
                    "      )\n"
                    "      assert result == 200\n\n"
                    "This tests behavior (correct call) and result (status code)\n"
                    "without any network dependency."
                ),
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Patch where requests.post is looked up, not where it's defined.",
                    "Configure mock_post.return_value to simulate the Response object.",
                ],
            },
        ],
    },

    "integration_and_e2e": {
        "id": "integration_and_e2e",
        "name": "Integration & E2E Testing",
        "subtitle": "API Testing, Database Tests, End-to-End",
        "color": "green",
        "icon": "🔗",
        "commands": ["httpx", "TestClient", "factory_boy", "selenium", "playwright"],
        "challenges": [
            {
                "id": "ie_1",
                "type": "quiz",
                "question": "What is the key difference between unit tests and integration tests?",
                "options": [
                    "Unit tests are faster; integration tests are slower",
                    "Unit tests verify isolated components; integration tests verify that components work together correctly",
                    "Unit tests use mocks; integration tests never use mocks",
                    "Unit tests are written by developers; integration tests are written by QA",
                ],
                "answer": "b",
                "lesson": (
                    "The testing pyramid:\n\n"
                    "  Unit tests       — test individual functions/classes in isolation\n"
                    "  Integration tests — test that components interact correctly\n"
                    "  E2E tests        — test complete user workflows through the full stack\n\n"
                    "Integration tests might:\n"
                    "  - Hit a real database (but a test database)\n"
                    "  - Call real API endpoints (but a test server)\n"
                    "  - Test multiple modules working together\n\n"
                    "Speed matters but correctness of boundaries matters more."
                ),
                "xp": 50,
            },
            {
                "id": "ie_2",
                "type": "quiz",
                "question": "When testing a FastAPI/Starlette application, which tool provides an in-process HTTP client that doesn't require a running server?",
                "options": [
                    "requests.Session()",
                    "httpx.AsyncClient with app=app (or Starlette's TestClient)",
                    "urllib3.PoolManager()",
                    "aiohttp.ClientSession()",
                ],
                "answer": "b",
                "lesson": (
                    "TestClient (Starlette) or httpx.AsyncClient test HTTP endpoints\n"
                    "without starting a real server.\n\n"
                    "  from fastapi.testclient import TestClient\n"
                    "  from myapp import app\n\n"
                    "  client = TestClient(app)\n"
                    "  response = client.get('/users/1')\n"
                    "  assert response.status_code == 200\n"
                    "  assert response.json()['name'] == 'Ghost'\n\n"
                    "For async endpoints:\n"
                    "  async with httpx.AsyncClient(app=app) as client:\n"
                    "      resp = await client.get('/users/1')"
                ),
                "xp": 50,
            },
            {
                "id": "ie_3",
                "type": "quiz",
                "question": "What is the recommended approach for integration tests that need a database?",
                "options": [
                    "Use the production database with read-only access",
                    "Mock all database calls — it's still an integration test",
                    "Use a dedicated test database, reset state between tests with transactions or fixtures",
                    "Test only the ORM models without connecting to any database",
                ],
                "answer": "c",
                "lesson": (
                    "Database integration testing best practices:\n\n"
                    "  1. Dedicated test database (never production!)\n"
                    "  2. Reset state between tests:\n"
                    "     - Transaction rollback (fast): begin transaction, run test, rollback\n"
                    "     - Truncate tables between tests\n"
                    "     - Fresh database per test run\n\n"
                    "  @pytest.fixture\n"
                    "  def db_session():\n"
                    "      session = TestSession()\n"
                    "      session.begin_nested()  # savepoint\n"
                    "      yield session\n"
                    "      session.rollback()\n"
                    "      session.close()"
                ),
                "xp": 75,
            },
            {
                "id": "ie_4",
                "type": "text",
                "question": "In the 'testing pyramid' (or 'testing trophy'), which layer has the FEWEST tests and the HIGHEST cost per test? (Two words, no hyphen.)",
                "options": [],
                "answer": "end to end",
                "lesson": (
                    "The testing pyramid (bottom to top):\n\n"
                    "         /  E2E  \\         — Few, slow, expensive, brittle\n"
                    "        /  Integ  \\        — Medium count, moderate speed\n"
                    "       / Unit Tests \\      — Many, fast, cheap, isolated\n\n"
                    "E2E tests (end-to-end) simulate real user behavior:\n"
                    "  - Browser automation (Playwright, Selenium)\n"
                    "  - Full stack running (DB + API + frontend)\n"
                    "  - Highest confidence but slowest feedback\n\n"
                    "Kent C. Dodds' 'testing trophy' puts integration tests at the widest\n"
                    "point, arguing they give the best confidence-to-cost ratio."
                ),
                "xp": 50,
            },
            {
                "id": "ie_5",
                "type": "quiz",
                "question": "Which Python library is the modern, recommended choice for browser-based E2E testing with auto-wait and multi-browser support?",
                "options": [
                    "Selenium WebDriver",
                    "Playwright (playwright-python)",
                    "Puppeteer",
                    "Cypress",
                ],
                "answer": "b",
                "lesson": (
                    "Playwright (by Microsoft) is the modern standard for browser E2E tests.\n\n"
                    "  from playwright.sync_api import sync_playwright\n\n"
                    "  with sync_playwright() as p:\n"
                    "      browser = p.chromium.launch()\n"
                    "      page = browser.new_page()\n"
                    "      page.goto('http://localhost:3000')\n"
                    "      page.fill('#username', 'ghost')\n"
                    "      page.click('button[type=submit]')\n"
                    "      assert page.text_content('.welcome') == 'Hello, Ghost'\n\n"
                    "Advantages over Selenium:\n"
                    "  - Auto-wait (no explicit waits/sleeps)\n"
                    "  - Multi-browser (Chromium, Firefox, WebKit)\n"
                    "  - Better async support, network interception, tracing"
                ),
                "xp": 50,
            },
            {
                "id": "ie_6",
                "type": "quiz",
                "question": "What is 'factory_boy' used for in Python testing?",
                "options": [
                    "Creating mock HTTP servers for API testing",
                    "Generating test fixtures — model instances with sensible defaults for database tests",
                    "Building Docker containers for test environments",
                    "Compiling test reports in multiple output formats",
                ],
                "answer": "b",
                "lesson": (
                    "factory_boy generates test data for ORM models with sensible defaults.\n\n"
                    "  import factory\n"
                    "  from myapp.models import User\n\n"
                    "  class UserFactory(factory.Factory):\n"
                    "      class Meta:\n"
                    "          model = User\n"
                    "      name = factory.Faker('name')\n"
                    "      email = factory.Faker('email')\n"
                    "      is_active = True\n\n"
                    "  # Usage:\n"
                    "  user = UserFactory()           # random name, email\n"
                    "  user = UserFactory(name='Ghost')  # override specific fields\n\n"
                    "Eliminates brittle test data setup and keeps tests focused."
                ),
                "xp": 50,
            },
            {
                "id": "ie_7",
                "type": "text",
                "question": "What testing technique records real HTTP responses and replays them in subsequent test runs, avoiding live API calls? (One word, often associated with VCR.py or responses library.)",
                "options": [],
                "answer": "recording",
                "lesson": (
                    "HTTP recording / cassette-based testing captures real API responses\n"
                    "and replays them in tests.\n\n"
                    "VCR.py:\n"
                    "  @vcr.use_cassette('cassettes/github_api.yaml')\n"
                    "  def test_get_repos():\n"
                    "      resp = requests.get('https://api.github.com/user/repos')\n"
                    "      assert resp.status_code == 200\n\n"
                    "First run: real HTTP call, response saved to cassette file.\n"
                    "Subsequent runs: cassette replayed, no network call.\n\n"
                    "Alternatives: responses library, respx (for httpx), pytest-recording."
                ),
                "xp": 75,
            },
            {
                "id": "ie_boss",
                "type": "quiz",
                "question": "You need to test an endpoint POST /orders that creates an order, charges a payment via Stripe API, and sends a confirmation email. The database must be real but Stripe and email must be mocked. Which test architecture is correct?",
                "options": [
                    "Mock everything including the database — it's faster",
                    "Use a test database + @patch the Stripe client and email service at the module where they're imported, then assert the endpoint returns 201 and the order exists in DB",
                    "Skip the test — it's too complex to test reliably",
                    "Use E2E browser testing with Playwright to submit the form and check the email inbox",
                ],
                "answer": "b",
                "lesson": (
                    "Integration test with selective mocking:\n\n"
                    "  @patch('app.orders.stripe_client.charge')\n"
                    "  @patch('app.orders.email_service.send')\n"
                    "  def test_create_order(mock_email, mock_stripe, db_session):\n"
                    "      mock_stripe.return_value = {'id': 'ch_123', 'status': 'succeeded'}\n"
                    "      mock_email.return_value = True\n\n"
                    "      resp = client.post('/orders', json={'item': 'widget', 'amount': 2999})\n\n"
                    "      assert resp.status_code == 201\n"
                    "      assert db_session.query(Order).count() == 1\n"
                    "      mock_stripe.assert_called_once_with(amount=2999)\n"
                    "      mock_email.assert_called_once()\n\n"
                    "Real DB (tests data layer) + mocked externals (isolated, fast)."
                ),
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Integration tests should use real infrastructure where the boundary under test lives (DB), but mock external services (Stripe, email).",
                    "Patch at the import location, not the definition location.",
                ],
            },
        ],
    },

    "test_architecture": {
        "id": "test_architecture",
        "name": "Test Architecture",
        "subtitle": "Fixtures, Parametrize, Coverage, Structure",
        "color": "yellow",
        "icon": "🏗️",
        "commands": ["@pytest.fixture", "@pytest.mark.parametrize", "coverage", "conftest", "markers"],
        "challenges": [
            {
                "id": "ta_1",
                "type": "quiz",
                "question": "What decorator creates a reusable test fixture in pytest?",
                "options": [
                    "@pytest.setup",
                    "@pytest.fixture",
                    "@pytest.before_each",
                    "@pytest.provider",
                ],
                "answer": "b",
                "lesson": (
                    "@pytest.fixture defines reusable test setup/teardown logic.\n\n"
                    "  @pytest.fixture\n"
                    "  def sample_user():\n"
                    "      return User(name='Ghost', role='operative')\n\n"
                    "  def test_user_role(sample_user):  # injected by name!\n"
                    "      assert sample_user.role == 'operative'\n\n"
                    "Fixtures can:\n"
                    "  - Return values (setup only)\n"
                    "  - Use yield for setup + teardown\n"
                    "  - Have scope: function, class, module, session\n"
                    "  - Depend on other fixtures (composition)"
                ),
                "xp": 50,
            },
            {
                "id": "ta_2",
                "type": "quiz",
                "question": "What fixture scope means the fixture is created once and shared across ALL tests in the entire test session?",
                "options": [
                    "scope='function'",
                    "scope='module'",
                    "scope='class'",
                    "scope='session'",
                ],
                "answer": "d",
                "lesson": (
                    "Fixture scopes control how often the fixture is created:\n\n"
                    "  scope='function'  — new instance per test (default)\n"
                    "  scope='class'     — shared within a test class\n"
                    "  scope='module'    — shared within a test file\n"
                    "  scope='session'   — shared across the entire test run\n\n"
                    "  @pytest.fixture(scope='session')\n"
                    "  def database():\n"
                    "      db = create_test_db()\n"
                    "      yield db\n"
                    "      db.drop()\n\n"
                    "Higher scopes = faster tests but shared state risks."
                ),
                "xp": 50,
            },
            {
                "id": "ta_3",
                "type": "text",
                "question": "What pytest decorator runs the same test function with multiple sets of inputs and expected outputs? Write the full decorator name with the @ symbol.",
                "options": [],
                "answer": "@pytest.mark.parametrize",
                "lesson": (
                    "@pytest.mark.parametrize runs one test with many inputs.\n\n"
                    "  @pytest.mark.parametrize('input,expected', [\n"
                    "      (1, 1),\n"
                    "      (2, 4),\n"
                    "      (3, 9),\n"
                    "      (-1, 1),\n"
                    "  ])\n"
                    "  def test_square(input, expected):\n"
                    "      assert square(input) == expected\n\n"
                    "This generates 4 separate test cases.\n"
                    "Each appears as a distinct test in the output:\n"
                    "  test_square[1-1] PASSED\n"
                    "  test_square[2-4] PASSED\n"
                    "  ..."
                ),
                "xp": 75,
            },
            {
                "id": "ta_4",
                "type": "quiz",
                "question": "What does 'test coverage' measure?",
                "options": [
                    "The number of tests in your test suite",
                    "The percentage of source code lines/branches executed by your tests",
                    "How many developers have reviewed the test code",
                    "The execution time of the test suite",
                ],
                "answer": "b",
                "lesson": (
                    "Test coverage measures what percentage of your code is exercised by tests.\n\n"
                    "  pip install pytest-cov\n"
                    "  pytest --cov=myapp --cov-report=html\n\n"
                    "Coverage types:\n"
                    "  Line coverage   — was this line executed?\n"
                    "  Branch coverage — were both if/else paths taken?\n"
                    "  Path coverage   — were all possible execution paths taken?\n\n"
                    "100% line coverage ≠ bug-free code.\n"
                    "A line can execute without testing all edge cases.\n"
                    "Branch coverage is more meaningful than line coverage."
                ),
                "xp": 50,
            },
            {
                "id": "ta_5",
                "type": "quiz",
                "question": "How do you mark a test to be skipped unless a condition is true?",
                "options": [
                    "@pytest.mark.skip(reason='...')",
                    "@pytest.mark.skipif(condition, reason='...')",
                    "@pytest.mark.unless(condition)",
                    "@pytest.mark.conditional(condition)",
                ],
                "answer": "b",
                "lesson": (
                    "Conditional test skipping:\n\n"
                    "  @pytest.mark.skip(reason='Not implemented yet')\n"
                    "  def test_future_feature(): ...\n\n"
                    "  @pytest.mark.skipif(\n"
                    "      sys.platform == 'win32',\n"
                    "      reason='Unix-only test'\n"
                    "  )\n"
                    "  def test_unix_permissions(): ...\n\n"
                    "  @pytest.mark.xfail(reason='Known bug #123')\n"
                    "  def test_known_bug(): ...\n\n"
                    "xfail = expected failure. Test runs but failure is not reported as error."
                ),
                "xp": 50,
            },
            {
                "id": "ta_6",
                "type": "text",
                "question": "In a pytest fixture that uses 'yield', code after the yield statement serves as what? (One word.)",
                "options": [],
                "answer": "teardown",
                "lesson": (
                    "yield in fixtures splits setup and teardown:\n\n"
                    "  @pytest.fixture\n"
                    "  def temp_file():\n"
                    "      # SETUP — runs before the test\n"
                    "      path = Path('/tmp/test_data.txt')\n"
                    "      path.write_text('test content')\n"
                    "      yield path\n"
                    "      # TEARDOWN — runs after the test (even if it fails)\n"
                    "      path.unlink()\n\n"
                    "The yield value is what gets injected into the test.\n"
                    "Code after yield always executes — like a finally block.\n"
                    "This guarantees cleanup regardless of test outcome."
                ),
                "xp": 50,
            },
            {
                "id": "ta_7",
                "type": "quiz",
                "question": "What is the purpose of pytest markers like @pytest.mark.slow or @pytest.mark.integration?",
                "options": [
                    "They change the execution order of tests",
                    "They categorize tests so you can selectively run subsets with -m",
                    "They automatically generate test documentation",
                    "They set timeout limits for individual tests",
                ],
                "answer": "b",
                "lesson": (
                    "Custom markers categorize tests for selective execution.\n\n"
                    "Define in pytest.ini or pyproject.toml:\n"
                    "  [tool.pytest.ini_options]\n"
                    "  markers = [\n"
                    "      'slow: marks tests as slow',\n"
                    "      'integration: integration tests',\n"
                    "  ]\n\n"
                    "Apply:\n"
                    "  @pytest.mark.slow\n"
                    "  def test_large_dataset(): ...\n\n"
                    "Run:\n"
                    "  pytest -m 'not slow'         # skip slow tests\n"
                    "  pytest -m 'integration'      # only integration tests\n"
                    "  pytest -m 'slow and not db'  # boolean expressions"
                ),
                "xp": 50,
            },
            {
                "id": "ta_boss",
                "type": "quiz",
                "question": "You need to test a function calculate_tax(amount, country) across 12 country/rate combinations AND mock an external tax API. The tests must share one database connection. What's the optimal architecture?",
                "options": [
                    "Write 12 separate test functions, each with its own DB connection and @patch decorator",
                    "Use @pytest.mark.parametrize for the 12 cases, a session-scoped fixture for DB, and a function-scoped fixture that patches the tax API",
                    "Use a single test with a for-loop over the 12 cases",
                    "Create 12 conftest.py files, one per country",
                ],
                "answer": "b",
                "lesson": (
                    "Combining pytest features for complex test scenarios:\n\n"
                    "  @pytest.fixture(scope='session')\n"
                    "  def db():\n"
                    "      conn = create_connection()\n"
                    "      yield conn\n"
                    "      conn.close()\n\n"
                    "  @pytest.fixture\n"
                    "  def mock_tax_api(mocker):\n"
                    "      return mocker.patch('app.tax.external_api.get_rate')\n\n"
                    "  @pytest.mark.parametrize('country,rate,amount,expected', [\n"
                    "      ('US', 0.08, 100, 108.00),\n"
                    "      ('DE', 0.19, 100, 119.00),\n"
                    "      # ... 10 more\n"
                    "  ])\n"
                    "  def test_tax(db, mock_tax_api, country, rate, amount, expected):\n"
                    "      mock_tax_api.return_value = rate\n"
                    "      assert calculate_tax(amount, country) == expected"
                ),
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "Parametrize eliminates 12 duplicate functions. Fixture scopes control resource sharing.",
                    "Session scope for expensive resources (DB), function scope for per-test mocks.",
                ],
            },
        ],
    },

    "tdd_and_testing_culture": {
        "id": "tdd_and_testing_culture",
        "name": "TDD & Testing Culture",
        "subtitle": "Red-Green-Refactor, Test Smells, Strategy",
        "color": "red",
        "icon": "🔴",
        "commands": ["red-green-refactor", "FIRST", "arrange-act-assert", "test-smells", "shift-left"],
        "challenges": [
            {
                "id": "tdd_1",
                "type": "quiz",
                "question": "What are the three steps of the TDD (Test-Driven Development) cycle, in order?",
                "options": [
                    "Write code, write tests, refactor",
                    "Red (write failing test), Green (make it pass), Refactor (clean up)",
                    "Plan, implement, verify",
                    "Unit test, integration test, E2E test",
                ],
                "answer": "b",
                "lesson": (
                    "TDD cycle: Red → Green → Refactor\n\n"
                    "  1. RED    — Write a test that fails (test doesn't pass yet)\n"
                    "  2. GREEN  — Write the minimum code to make the test pass\n"
                    "  3. REFACTOR — Clean up the code while keeping tests green\n\n"
                    "Key principle: never write production code without a failing test first.\n\n"
                    "Benefits:\n"
                    "  - Forces you to think about the API before implementation\n"
                    "  - Guarantees test coverage by construction\n"
                    "  - Small, incremental steps reduce debugging time"
                ),
                "xp": 50,
            },
            {
                "id": "tdd_2",
                "type": "quiz",
                "question": "What does the 'Arrange-Act-Assert' (AAA) pattern describe?",
                "options": [
                    "The three phases of a CI/CD pipeline",
                    "The structure of a well-organized test: setup data, execute the code, verify the result",
                    "The three types of test doubles: arrange (mock), act (stub), assert (spy)",
                    "The review process: arrange a meeting, act on feedback, assert quality",
                ],
                "answer": "b",
                "lesson": (
                    "Arrange-Act-Assert (AAA) is the standard test structure:\n\n"
                    "  def test_user_creation():\n"
                    "      # ARRANGE — set up test data and dependencies\n"
                    "      name = 'Ghost'\n"
                    "      role = 'operative'\n\n"
                    "      # ACT — execute the code under test\n"
                    "      user = create_user(name, role)\n\n"
                    "      # ASSERT — verify the result\n"
                    "      assert user.name == 'Ghost'\n"
                    "      assert user.role == 'operative'\n"
                    "      assert user.id is not None\n\n"
                    "Also known as Given-When-Then in BDD (Behavior-Driven Development)."
                ),
                "xp": 50,
            },
            {
                "id": "tdd_3",
                "type": "text",
                "question": "In TDD, what color represents the first step where you write a test that fails? (One word, lowercase.)",
                "options": [],
                "answer": "red",
                "lesson": (
                    "Red = failing test. The first step in every TDD cycle.\n\n"
                    "Why start with a failing test?\n"
                    "  1. Proves the test actually tests something (not a false positive)\n"
                    "  2. Defines the expected behavior before you code it\n"
                    "  3. Gives you a clear goal: make this specific test pass\n\n"
                    "If your new test passes immediately, something is wrong:\n"
                    "  - The test might not test what you think\n"
                    "  - The feature might already be implemented\n"
                    "  - The assertion might be too weak"
                ),
                "xp": 50,
            },
            {
                "id": "tdd_4",
                "type": "quiz",
                "question": "Which of these is a 'test smell' (anti-pattern) that indicates poor test quality?",
                "options": [
                    "Each test function tests exactly one behavior",
                    "Tests are independent and can run in any order",
                    "A single test function contains multiple unrelated assertions testing different behaviors",
                    "Tests use descriptive names like test_login_fails_with_wrong_password",
                ],
                "answer": "c",
                "lesson": (
                    "Common test smells (anti-patterns):\n\n"
                    "  1. Giant test — tests multiple behaviors in one function\n"
                    "  2. Mystery guest — test depends on hidden external state\n"
                    "  3. Fragile test — breaks when implementation changes (not behavior)\n"
                    "  4. Slow test — unnecessarily slow (use mocks, fixtures)\n"
                    "  5. Hidden dependency — tests must run in specific order\n"
                    "  6. Over-mocking — mocks everything, tests nothing real\n"
                    "  7. Assertion-free — runs code but never asserts anything\n\n"
                    "Good tests: fast, isolated, repeatable, self-validating, timely (FIRST)."
                ),
                "xp": 75,
            },
            {
                "id": "tdd_5",
                "type": "quiz",
                "question": "What does 'shift left' mean in the context of testing strategy?",
                "options": [
                    "Move tests to the left side of the CI pipeline configuration file",
                    "Find and fix defects earlier in the development lifecycle, not in production",
                    "Prioritize left-side (client-side) testing over server-side testing",
                    "Use left-join queries in database tests instead of inner joins",
                ],
                "answer": "b",
                "lesson": (
                    "'Shift left' means moving quality activities earlier in development.\n\n"
                    "Traditional: Code → Build → Test → Deploy → Find bugs\n"
                    "Shift left:  Test → Code → Test → Build → Test → Deploy\n\n"
                    "Shift-left practices:\n"
                    "  - TDD (write tests before code)\n"
                    "  - Pre-commit hooks (lint, type-check, unit tests)\n"
                    "  - PR-level test requirements\n"
                    "  - Static analysis in IDE (not just CI)\n\n"
                    "The earlier you find a bug, the cheaper it is to fix.\n"
                    "A bug in production costs 100x more than one caught in a unit test."
                ),
                "xp": 50,
            },
            {
                "id": "tdd_6",
                "type": "quiz",
                "question": "What does the FIRST acronym stand for in test quality principles?",
                "options": [
                    "Fast, Isolated, Repeatable, Self-validating, Timely",
                    "Functional, Integrated, Robust, Scalable, Tested",
                    "Frequent, Incremental, Reliable, Simple, Thorough",
                    "Focused, Independent, Readable, Small, Testable",
                ],
                "answer": "a",
                "lesson": (
                    "FIRST principles for good tests:\n\n"
                    "  F — Fast: tests should run in milliseconds, not seconds\n"
                    "  I — Isolated: no shared state, no order dependency\n"
                    "  R — Repeatable: same result every time, in any environment\n"
                    "  S — Self-validating: pass or fail, no manual interpretation\n"
                    "  T — Timely: written close to the code they test (ideally before, via TDD)\n\n"
                    "If a test violates FIRST, it will eventually be:\n"
                    "  - Skipped (too slow)\n"
                    "  - Flaky (not repeatable)\n"
                    "  - Ignored (confusing output)"
                ),
                "xp": 50,
            },
            {
                "id": "tdd_7",
                "type": "text",
                "question": "What is the term for a test that sometimes passes and sometimes fails without any code changes? (One word, lowercase.)",
                "options": [],
                "answer": "flaky",
                "lesson": (
                    "Flaky tests pass and fail non-deterministically.\n\n"
                    "Common causes:\n"
                    "  - Race conditions / timing dependencies\n"
                    "  - Shared mutable state between tests\n"
                    "  - External service dependencies\n"
                    "  - Time-dependent logic (dates, timestamps)\n"
                    "  - Order-dependent tests\n\n"
                    "Flaky tests destroy trust in the test suite.\n"
                    "Teams start ignoring failures → bugs reach production.\n\n"
                    "Fixes: isolate state, mock time, use deterministic seeds,\n"
                    "quarantine flaky tests, fix root causes immediately."
                ),
                "xp": 75,
            },
            {
                "id": "tdd_boss",
                "type": "quiz",
                "question": "Your team has 2,000 tests. 15 are flaky. The suite takes 20 minutes. Developers skip running tests locally. Coverage is 40%. PRs frequently break main. What is the HIGHEST-IMPACT first action?",
                "options": [
                    "Increase coverage to 80% by writing more tests",
                    "Fix or quarantine the 15 flaky tests to restore trust in the suite, then optimize speed",
                    "Rewrite the entire test suite using TDD",
                    "Add E2E tests to catch the bugs PRs are introducing",
                ],
                "answer": "b",
                "lesson": (
                    "Test suite health triage (priority order):\n\n"
                    "  1. FIX FLAKY TESTS — restore trust. If the suite is unreliable,\n"
                    "     no one runs it. Quarantine immediately, fix root causes.\n\n"
                    "  2. SPEED UP THE SUITE — if tests take 20min, devs won't run them\n"
                    "     locally. Parallelize (pytest-xdist), mock slow deps, fix scope.\n\n"
                    "  3. ENFORCE IN CI — make tests a required PR check on main.\n"
                    "     No merge without green tests.\n\n"
                    "  4. INCREASE COVERAGE — but targeted. Cover the code that breaks,\n"
                    "     not just the easy code.\n\n"
                    "Trust → Speed → Enforcement → Coverage. In that order."
                ),
                "xp": 150,
                "difficulty": "boss",
                "is_boss": True,
                "hints": [
                    "If developers don't trust the test suite, nothing else matters.",
                    "Flaky tests are the #1 killer of testing culture.",
                ],
            },
        ],
    },
}

ZONE_ORDER = [
    "unit_testing_fundamentals",
    "mocking_and_test_doubles",
    "integration_and_e2e",
    "test_architecture",
    "tdd_and_testing_culture",
]


def get_zone(zone_id: str) -> dict:
    return ZONES.get(zone_id, {})


def get_all_zones() -> list:
    return [ZONES[z] for z in ZONE_ORDER if z in ZONES]


def get_zone_challenges(zone_id: str) -> list:
    zone = get_zone(zone_id)
    return zone.get("challenges", [])
