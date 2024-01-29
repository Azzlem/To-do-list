from service import create_base_if_not_exists, get_values, insert_values, select_values

create_base_if_not_exists()

print("Давайте создадим базу данных наших дел!!")
print("Есть несколько стандартных выборов:\n"
      "1 - выбрать те дела которые вы уже завершили.\n"
      "2 - выбрать те дела которыке требуют завершения.\n")

while True:
    input_name = input("Имя дела не должно быть пустым.\n"
                       "Введите имя дела: ")
    if input_name == "exit":
        break
    if input_name == "1":
        result = select_values(bool(int(input_name)))
        for el in result:
            print(el)
        continue
    if input_name == "0":
        result = select_values(bool(int(input_name)))
        for el in result:
            print(el)
        continue
    input_description = input("Описание дела не более 250 символов!\n"
                              "Введите описнаие: ")
    input_bool = input("Статус выполнения 'да', 'нет' !\n"
                       "Введите статус выполнения дела: ")
    if input_bool.lower() == "да":
        input_bool = True
    else:
        input_bool = False

    insert_values(get_values(input_name, input_description, input_bool))
