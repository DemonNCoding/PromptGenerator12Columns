import random

class PromptGenerator12Columns_Empty:
    DEBUG = True

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Column_1": ("STRING", {"multiline": True, "default": ""}),
                "Column_2": ("STRING", {"multiline": True, "default": ""}),
                "Column_3": ("STRING", {"multiline": True, "default": ""}),
                "Column_4": ("STRING", {"multiline": True, "default": ""}),
                "Column_5": ("STRING", {"multiline": True, "default": ""}),
                "Column_6": ("STRING", {"multiline": True, "default": ""}),
                "Column_7": ("STRING", {"multiline": True, "default": ""}),
                "Column_8": ("STRING", {"multiline": True, "default": ""}),
                "Column_9": ("STRING", {"multiline": True, "default": ""}),
                "Column_10": ("STRING", {"multiline": True, "default": ""}),
                "Column_11": ("STRING", {"multiline": True, "default": ""}),
                "Column_12": ("STRING", {"multiline": True, "default": ""}),
                "always_add": ("STRING", {"multiline": True, "default": ""}),
            },
            "optional": {
                "use_commas": ("BOOLEAN", {
                    "default": True,
                    "label_on": "Use Commas",
                    "label_off": "New Lines"
                }),
                "include_always": ("BOOLEAN", {
                    "default": True,
                    "label_on": "Include Always Add",
                    "label_off": "Skip Always Add"
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate"
    CATEGORY = "Random Prompt Generators"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return random.random()

    def _pick_one(self, text_block):
        if not text_block:
            return ""
        lines = [l.strip() for l in str(text_block).splitlines()
                 if l.strip() and not l.strip().startswith('#')]
        return random.choice(lines) if lines else ""

    def generate(self, **kwargs):
        seed = random.randint(0, 0xffffffffffffffff)
        random.seed(seed)

        cols = [kwargs[f"Column_{i}"] for i in range(1, 13)]
        use_commas = kwargs.get("use_commas", True)
        include_always = kwargs.get("include_always", True)
        always_add = kwargs.get("always_add", "").strip()

        # Pick one from each column (skip empty results)
        parts = [self._pick_one(col) for col in cols if self._pick_one(col)]

        # Join the column picks
        if use_commas:
            result = ", ".join(parts)
        else:
            result = "\n".join(parts)

        # Smart always_add handling
        if include_always and always_add:
            if use_commas:
                connector = ", " if result else ""
            else:
                connector = "\n" if result else ""
            result += connector + always_add

        if self.DEBUG:
            print(f"\n[Empty 12-Columns Generator] Seed: {seed}\n→ {result}\n{'─' * 80}")

        return (result,)


NODE_CLASS_MAPPINGS = {
    "PromptGenerator12Columns_Empty": PromptGenerator12Columns_Empty
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptGenerator12Columns_Empty": "(Empty) Prompt Generator 12 Columns"
}