import json
import os

class PromptStorageNode:
    def __init__(self):
        self.prompts = self.load_prompts()

    def load_prompts(self):
        path = os.path.join(os.path.dirname(__file__), "prompt_storage.json")
        if not os.path.exists(path):
            raise FileNotFoundError(f"Prompt-Datei nicht gefunden: {path}")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("library", [])

    @classmethod
    def INPUT_TYPES(cls):
        prompts = cls().load_prompts()
        choices = ["None"] + [p["name"] for p in prompts]
        return {
            "required": {
                "prompt_choice": (choices,),
                "manual_positive": ("STRING", {"multiline": True}),
                "manual_negative": ("STRING", {"multiline": True})
            }
        }

    RETURN_TYPES = ("STRING", "STRING",)
    RETURN_NAMES = ("positive_prompt", "negative_prompt",)
    FUNCTION = "get_prompt"
    CATEGORY = "🛡 Audit-qwen"

    def get_prompt(self, prompt_choice, manual_positive, manual_negative):
        # Priorität 1: Manuelle Eingabe, wenn nicht leer
        if manual_positive.strip() or manual_negative.strip():
            return (manual_positive, manual_negative)

        # Priorität 2: Auswahl aus Bibliothek
        if prompt_choice == "None":
            return ("", "")

        for p in self.prompts:
            if p["name"] == prompt_choice:
                return (p["positive"], p["negative"])

        return ("", "")

NODE_CLASS_MAPPINGS = {
    "PromptStorageNode": PromptStorageNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptStorageNode": "🛡 Prompt & Szenen Stockproduktion",
}
