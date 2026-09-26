class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]


raw = "  water,  ginger , lemon ,   cardamom"

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)
