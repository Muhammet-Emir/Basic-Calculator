# Language-Choose # <-- This section make user to choose a language.
text_lang = str("E") # The program comes with english language.
def text_cho():
    global text_lang
    print("Welcome To The Calculator")
    print("Please choose a language, English or Turkish")
    text_lang = str(input("(E/T)?: ")) # Program asks user the which language prefers to use.
    if text_lang not in ("e" , "E" , "t" , "T"):
        print("Please enter a valid value!"),text_cho()
text_cho()
text_lang = text_lang.upper()
# End-Language-Choose #

# Language-Text-Parts # <-- This section contains texts for both languages.
##>English Language
def eng_lang():
    global text_num1, text_num2, Err_Msg_num, text_calc, Err_Msg_calc_req, Err_Msg_division_twozero, pr_answer
    text_num1 = ("Please input the first number: ")
    text_num2 = ("Please input the second number: ")
    Err_Msg_num = ("Error!: Please input a integer number for calculation!")
    text_calc = ("Please insert a calculation method [+|-|*|/]: ")
    Err_Msg_calc_req = ("Error!: Please enter a valid method!")
    Err_Msg_division_twozero = ("Error!: Zero cannot divide by itself!")
    pr_answer = ("Answer = ")

##>Turkish Language
def tur_lang():
    global text_num1, text_num2, Err_Msg_num, text_calc, Err_Msg_calc_req, Err_Msg_division_twozero, pr_answer
    text_num1 = str("Lütfen birinci sayıyı giriniz: ")
    text_num2 = str("Lütfen ikinci sayıyı giriniz: ")
    Err_Msg_num = ("Hata!:Lütfen hesaplama için bir tam sayı girişi yapınız!")
    text_calc = ("Lütfen bir hesaplama yöntemi yazınız [+|-|*|/]: ")
    Err_Msg_calc_req = ("Hata!: Lütfen geçerli bir yöntem yazınız!")
    Err_Msg_division_twozero = ("Hata!: Sıfır kendisine bölünemez!")
    pr_answer = ("Cevap = ")

if text_lang == "E" : eng_lang()
elif text_lang == "T": tur_lang()
else:
    print("Code Error! Message: There is a error in a language choosing section!")
    quit(0)
# End-Language-Text-Parts #

# Request-numbers # <-- This section asks user for int numbers for calculation.
def input_num1():
    global num1
    num1 = int("1")
    try:
        num1 = int(input(text_num1)) # Asks for the first integer number.
    except ValueError: print(Err_Msg_num), input_num1() # Gives an error message when gets a wrong input and starts the input_num1 def again
input_num1() # Starts the def

def input_num2():
    global num2
    num2 = int("1")
    try:
        num2 = int(input(text_num2)) # Asks for the second integer number.
    except ValueError: print(Err_Msg_num), input_num2() # Gives an error message when gets a wrong input and starts the input_num2 def again
input_num2() # Starts the def
# End-Request-Numbers #

# Request-Calculation-Method #
calc = str("+") # The calculation method comes with addition method.
def calc_cho():
    global calc
    calc = str(input(text_calc))
    if calc not in ("+","-","*","/"):
        print(Err_Msg_calc_req), calc_cho() # Gives an error message when gets an wrong input and start the def again.
calc_cho() # <-Starts the def
# End-Request-Calculation-Method #

# The-Calculation #
def calculation():
    global answer
    try:
        match calc:
            case "+":answer = int(num1 + num2)
            case "-":answer = int(num1 - num2)
            case "*":answer = int(num1 * num2)
            case "/":answer = int(num1 / num2)
    except ZeroDivisionError: print(Err_Msg_division_twozero), quit(0)
calculation()
# End-The-Calculation #

# Print-Answer #
answer = str(answer)
print(pr_answer + answer)
# End-Print-Answer #