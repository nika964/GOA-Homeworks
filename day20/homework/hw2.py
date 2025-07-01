animals = ["Dog", "Elephant", "Fox", "lion", "Cat", "Tiger", "Bear"]

for animal in animals:
    if len(animal) < 5 and animal == animal.capitalize():
        print(animal[:3])
    else:
        print(f"{animal} - ეს სიტყვა გრძელია")
