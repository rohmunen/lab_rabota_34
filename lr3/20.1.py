#БСБО-05-19 Салынь Даниил Леонидович
def translate(text: str):
    text = text.replace("А", "")
    text = text.replace("а", "")
    text = text.replace("Е", "")
    text = text.replace("е", "")
    text = text.replace("И", "")
    text = text.replace("и", "")
    text = text.replace("О", "")
    text = text.replace("о", "")
    text = text.replace("Ы", "")
    text = text.replace("ы", "")
    text = text.replace("Э", "")
    text = text.replace("э", "")
    text = text.replace("Ю", "")
    text = text.replace("ю", "")
    text = text.replace("Я", "")
    text = text.replace("я", "")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("!", "")
    text = text.replace("?", "")
    text = text.replace(":", "")
    global translatedText
    translatedText = text


translatedText = ""
translate(input())
print(translatedText)
