from textual.app import App, ComposeResult
from textual.widgets import Footer, Header


class StopwatchApp(App):
    """Manage stopwatches in the terminal."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the stopwatch app."""
        yield Header()
        yield Footer()

    def action_toogle_dark(self) -> None:
        """Action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()
