#მომხმარებელს შემოატანინეთ რიცხვი და შეამოწმეთ, თუ რიცხვი მეტია 90-ზე, დაბეჭდეთ "A", თუ რიცხვი ნაკლებია 90-ზე და მეტია 70-ზე, დაბეჭდეთ "B", თუ რიცხვი ნაკლებია 70-ზე და მეტია 50-ზე, დაბეჭდეთ "C", სხვა შემთხვევაში დაბეჭდეთ "D"


number = int(input("Enter a number: "))
if number > 90:
    print("A")
elif number < 90 and number > 70:
    print("B")
elif number < 70 and number > 50:
    print("C")
else:
    print("D")
