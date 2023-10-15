from PIL import Image
from gtts import gTTS
from pytesseract import image_to_string


def image_to_sound():
    """
    Function for converting an  image to sound
    """
    try:
        loaded_image = Image.open("./image.jpg")
        decoded_text = image_to_string(loaded_image)
        cleaned_text = " ".join(decoded_text.split("\n"))
        print(cleaned_text)
        sound = gTTS(cleaned_text, lang="en",tld='com')
        sound.save("sound_test_2.mp3")
        return True
    except Exception as bug:
        print("The bug thrown while excuting the code\n", bug)
        return


if __name__ == "__main__":
    image_to_sound()
    input()
