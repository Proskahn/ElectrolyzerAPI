from typing import List


class MembraneSelector:
    """
    Handles membrane selection logic for the Electrolyzer digital twin.
    """

    def __init__(self):
        self.available_membranes = ["Nafion 115", "Nafion 117", "Nafion 212"]

    def list_membranes(self) -> List[str]:
        """
        Returns a list of supported membrane options.
        """
        return self.available_membranes

    def select_membrane(self, name: str) -> str:
        """
        Select a membrane if it exists in the available list.

        Args:
            name (str): Membrane name.

        Returns:
            str: Confirmation message or error.
        """
        if name in self.available_membranes:
            return f"Membrane '{name}' selected."
        return f"Error: Membrane '{name}' is not supported."
