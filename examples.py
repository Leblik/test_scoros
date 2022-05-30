with open('test.txt', 'wt', encoding='utf-8') as inFile: # Открытие файла
    words = input() # Получение данных от пользователя
    inFile.write (words) # Запись данных