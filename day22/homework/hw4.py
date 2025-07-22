text = "Hello World 123"

# ყველა ასო დიდად
print(text.upper())        # "HELLO WORLD 123"

# პირველი ასო დიდად, დანარჩენი პატარად
print(text.capitalize())   # "Hello world 123"

# ყველა ასო პატარად
print(text.lower())        # "hello world 123"

# პოულობს "World"-ს და აბრუნებს მის პირველ ინდექსს
print(text.find("World"))  # 6

# ცვლის "World"-ს სიტყვით "Python"
print(text.replace("World", "Python"))  # "Hello Python 123"

# ცვლის დიდ ასოებს პატარად და პირიქით
print(text.swapcase())     # "hELLO wORLD 123"

# ამოწმებს არის თუ არა ყველა სიმბოლო დიდი
print(text.isupper())      # False

# ამოწმებს არის თუ არა ყველა სიმბოლო პატარა
print(text.islower())      # False

# ამოწმებს შეიცავს თუ არა ტექსტი მხოლოდ ციფრებს
print("123".isdigit())     # True

# ამოწმებს შეიცავს თუ არა ტექსტი მხოლოდ ასოებს
print("Hello".isalpha())   # True

# ამოწმებს შეიცავს თუ არა ტექსტი მხოლოდ ასოებს ან ციფრებს
print("Hello123".isalnum()) # True

# ყოფს სიტყვებად
print(text.split())        # ['Hello', 'World', '123']
