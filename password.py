password = str(input("Please enter a password: ")).encode("utf-8")

encoded = base64.b64encode(password)
print("Here's how your encrypted password looks: ")
print(encoded)

decoded = base64.b64decode(encoded)
print("Here's your decoded password: ")
print(decoded)
