from googletrans import Translator

class TextTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate(self, text):
        result = self.translator.translate(text, dest="en")
        return result.text
try:
    from googletrans import Translator
except Exception as e:
    Translator = None

class TextTranslator:
    def __init__(self):
        if Translator:
            self.translator = Translator()
        else:
            self.translator = None

    def translate(self, text):
        if not self.translator:
            return text  # fallback: return original

        try:
            result = self.translator.translate(text, dest="en")
            return result.text
        except Exception:
            return text
