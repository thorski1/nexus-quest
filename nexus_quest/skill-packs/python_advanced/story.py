"""story.py — Narrative for the Python Advanced skill pack."""

INTRO_STORY = """
[bold yellow]THE NEXUS FILES[/bold yellow]
[bold yellow]Chapter: Python Dark Arts[/bold yellow]

CIPHER's voice crackled through static.

[bold cyan]"You know Python. But do you [italic]know[/italic] Python?"[/bold cyan]

A terminal flickered, showing code that seemed to write itself —
decorators wrapping decorators, generators yielding infinite sequences,
metaclasses creating classes that created other classes.

[bold cyan]"The dark arts aren't dark because they're dangerous.
They're dark because most people never go deep enough to find them.
Decorators. Generators. Metaclasses. Async. Type hints.
The tools that separate scripts from systems."[/bold cyan]

[bold white]Time to go beyond the basics.[/bold white]
"""

ZONE_INTROS = {
    "decorators": "[bold cyan]\"Decorators,\"[/bold cyan] CIPHER said, [bold cyan]\"are functions that eat other functions and return something better.\"[/bold cyan]\n\n[bold white]Let's unwrap the @ symbol.[/bold white]",
    "generators_iterators": "[bold cyan]\"Why compute everything at once when you can compute it one piece at a time?\"[/bold cyan]\n\n[bold white]Welcome to lazy evaluation.[/bold white]",
    "context_managers": "[bold cyan]\"Resources that clean up after themselves. The 'with' statement is civilization.\"[/bold cyan]\n\n[bold white]Let's manage some contexts.[/bold white]",
    "metaclasses_descriptors": "[bold cyan]\"Classes are objects. Objects are instances of classes. Classes are instances of metaclasses. Welcome to the rabbit hole.\"[/bold cyan]\n\n[bold white]The deepest layer of Python.[/bold white]",
    "async_python": "[bold cyan]\"One thread. Many tasks. No waiting. That's async.\"[/bold cyan]\n\n[bold white]Let's make Python concurrent.[/bold white]",
    "type_hints": "[bold cyan]\"Python is dynamically typed. Type hints don't change that. They just make your IDE smarter and your code clearer.\"[/bold cyan]\n\n[bold white]Types as documentation.[/bold white]",
    "testing_advanced": "[bold cyan]\"Tests aren't overhead. Tests are the safety net that lets you move fast.\"[/bold cyan]\n\n[bold white]Beyond basic assertions.[/bold white]",
    "packaging": "[bold cyan]\"You wrote great code. Now ship it.\"[/bold cyan]\n\n[bold white]From script to package to PyPI.[/bold white]",
}

ZONE_COMPLETIONS = {
    "decorators": "[bold green]Decorators mastered![/bold green] You can wrap, chain, and parameterize with confidence.",
    "generators_iterators": "[bold green]Generators unlocked![/bold green] Lazy evaluation is now your default thinking.",
    "context_managers": "[bold green]Context managers conquered![/bold green] Resources will always be properly managed.",
    "metaclasses_descriptors": "[bold green]Metaclasses understood![/bold green] You've seen the deepest layer of Python's object model.",
    "async_python": "[bold green]Async mastered![/bold green] Concurrent Python without threads.",
    "type_hints": "[bold green]Type hints complete![/bold green] Your code is now self-documenting.",
    "testing_advanced": "[bold green]Testing advanced![/bold green] Your test suite is now a fortress.",
    "packaging": "[bold green]Packaging done![/bold green] You can ship Python to the world.",
}

BOSS_INTROS = {
    "decorators": "CIPHER asks: [bold yellow]\"Write a decorator that takes arguments. What's the pattern?\"[/bold yellow]",
    "generators_iterators": "CIPHER asks: [bold yellow]\"What does generator.send() do that next() can't?\"[/bold yellow]",
    "context_managers": "CIPHER asks: [bold yellow]\"How do you make an async context manager?\"[/bold yellow]",
    "metaclasses_descriptors": "CIPHER asks: [bold yellow]\"When __init_subclass__ was added, it replaced most metaclass use cases. Why?\"[/bold yellow]",
    "async_python": "CIPHER asks: [bold yellow]\"What's the difference between asyncio.gather and asyncio.wait?\"[/bold yellow]",
    "type_hints": "CIPHER asks: [bold yellow]\"What's the difference between Protocol and ABC?\"[/bold yellow]",
    "testing_advanced": "CIPHER asks: [bold yellow]\"What is property-based testing and when should you use it?\"[/bold yellow]",
    "packaging": "CIPHER asks: [bold yellow]\"What replaced setup.py in modern Python packaging?\"[/bold yellow]",
}
