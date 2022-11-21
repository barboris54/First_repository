# Чтобы немедленно прервать цикл while без выполнения оставшегося кода в цикле
# независимо от состояния условия, используйте команду break. Команда break
# управляет ходом выполнения программы; она позволит вам управлять тем, какая
# часть кода выполняется, а какая нет.

prompt = "Tell me city you visited"
prompt += "\n If you want to stop program enter quit"
while True:  # Цикл, который начинается с while True , будет выполняться бесконечно — если только в нем не будет выполнена команда break.
    city = input(prompt).strip()
    if city == 'quit':
        break
    else:
        print(f"I'd like to visit {city.title()}")
