# Манько Анна (відкриття файлу для подальшої роботи з ним)
inputFileName = "question-answer.txt"
inputFileOK = False

while not inputFileOK:
    try:
        inputFile = open(inputFileName, "w+", encoding="utf-8")
    except IOError:
        print("Файл: ", inputFileName, "не може бути відкритим")
    else:
        print("Відкриття файлу: ", inputFileName, " для читання та запису інформації.")
        inputFileOK = True
        if inputFileOK:
            print("Успішне зчитання інформації із файлу", inputFileName)
            inputFileName = "question-answer.txt"
            open(inputFileName, "w+", encoding="utf-8").close()
            inputFile = open(inputFileName, "a+", encoding="utf-8")
        else:
            print("Помилка в зчитуванні інформації із файлу! Аварійне завершення програми!", inputFileName)

# Манько Анна (додавання першого запитання)
try:
    pib="Манько Анна Олександрівна"
    question="Дайте відповідь на питання: Змінна в Python і як її створити?"
    inputFile.write(pib+"\n\n")
    inputFile.write(question+"\n\n")
except IOError:
    print("Помилка із додаванням інформації у файл")

# Снаговська Дар'я (додавання відповіді на перше питання та другого запитання)
try:
    pib="Снаговська Дар'я Ярославівна"
    answer= ("Змінна — це іменований контейнер для збереження значення в пам’яті програми.\nЗмінна створюється просто присвоєнням значення до імені; тип визначається автоматично при присвоєнні.\n "
             "Приклад:\n x = 55\n name = 'Алекс'\n pi = 3.1415\nПравила іменування: ім’я може містити літери, цифри та підкреслення, не починається з цифри, не використовує ключові слова Python.\nТипи значень: число, рядок, булеве, список тощо; тип можна перевірити через type(x).")
    inputFile.write(pib+"\n\n")
    inputFile.write(answer+"\n\n")
    question="Дайте відповідь на питання: Яка різниця між list і tuple та коли який використовувати?"
    inputFile.write(question+"\n\n")
except IOError:
    print("Помилка із додаванням інформації у файл")
    
# Манько Анна (завершення роботи з файлом)
print("\nІнформація додана! Завершення програми!", inputFileName)
inputFile.close()
print("Файл закритий", inputFileName)