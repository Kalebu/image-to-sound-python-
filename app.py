from PIL import Image
from gtts import gTTS
from pytesseract import image_to_string
clean = lambda text : ' '.join(text.split('\n'))
to_text = lambda image: clean(image_to_string(Image.open(image)))
to_sound = lambda text: gTTS(text, lang='en').save('gene.mp3')
image_to_sound  = lambda image: to_sound(to_text(image))
image_to_sound('image.jpg')
input()