class MyString:
    def __init__(self, value=""):
        # use the setter so validation runs on init
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")
            self._value = ""

    def is_sentence(self):
        """Return True if the string ends with a period."""
        return self.value.endswith(".")

    def is_question(self):
        """Return True if the string ends with a question mark."""
        return self.value.endswith("?")

    def is_exclamation(self):
        """Return True if the string ends with an exclamation mark."""
        return self.value.endswith("!")

    def count_sentences(self):
        """Return the number of sentences (split on ., ?, !)."""
        import re
        # split by ., ?, ! one or more times
        parts = re.split(r"[.!?]+", self.value)
        # filter out empty strings
        sentences = [p for p in parts if p.strip()]
        return len(sentences)
