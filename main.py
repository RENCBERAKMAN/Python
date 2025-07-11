def about_me():
    print("👋 Merhaba! Ben Rençber Akman. Unreal Engine ile oyun geliştiriyorum. Bilgisayar programcılığı okuyorum. Backend tarafına merakım var ")

def fahrenheit_converter():
    celsius = float(input("Celsius değeri: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

def factorial_calc():
    num = int(input("Faktöriyeli hesaplanacak sayı: "))
    result = 1
    for i in range(1, num + 1):
        result *= i
    print(f"{num}! = {result}")

def grade_calc():
    score = float(input("Sınav notunu gir: "))
    if score >= 90:
        grade = "A"
    elif score >= 80:  grade = "B"
    elif score >= 70:  grade = "C"
    elif score >= 60:  grade = "D"
    else:
        grade = "F"
    print(f"Not: {grade}")

while True:
    print("-------------------------------------")
    print("To access About Me       : 1")
    print("To calculate Fahrenheit  : 2")
    print("To calculate Factorial   : 3")
    print("To calculate Grade       : 4")
    print("Exit                     : q")
    print("-------------------------------------")
    
    choice = input("Seçiminiz nedir: ")

    if choice == "1":
        about_me()
    elif choice == "2":
        fahrenheit_converter()
    elif choice == "3":
        factorial_calc()
    elif choice == "4":
        grade_calc()
    elif choice.lower() == "q":
        print("Program kapnıyor...")
        break
    else:
        print("⚠️ Geçersiz seçim. Lütfen 1-4 ya da 'q' tuşlayın.")