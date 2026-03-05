from captcha.image import ImageCaptcha
import random
import string
import webbrowser

def generate_captcha():

    text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

    image = ImageCaptcha(width=280, height=90)
    image.write(text, "captcha.png")

    print("A CAPTCHA image has been generated.")
    print("Open captcha.png and type the text.")

    user_input = input("Enter CAPTCHA: ")

    if user_input == text:
        print("CAPTCHA correct. Redirecting to Google...")
        webbrowser.open("https://www.google.com")
    else:
        print("CAPTCHA incorrect. Try again.")

generate_captcha()