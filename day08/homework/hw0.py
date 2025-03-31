# შემოიტანეთ თქვენი ოჯახის წევრების ასაკი და დაუპრინტეთ თუ რამდენი წლისები იქნებიან 25 წლის შემდეგ(გამოიყენეთ int ფუნქცია).

me = int(input("my age is: "))
mom = int(input("moms age is: "))
dad = int(input("dads age is: "))
brother = int(input("brothers age is: "))
sister = int(input("sisters age is: "))

num = me + 25
num_1 = mom + 25
num_2 = dad + 25
num_3 = brother + 25
num_4 = sister + 25
print("me 25 years later i would be" + " " + str(num) + " " + "my mom 25 years later would be" + " " + str(num_1) + " " + "my dad 25 years later would be" + " " + str(num_2) + " " + "my brother 25 years later would be" + " " + str(num_3) + " " + "my sister 25 years later would be" + " " + str(num_4))
