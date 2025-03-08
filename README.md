# spam-chat-cs2
![1](https://github.com/user-attachments/assets/f0dd336c-ec38-4e95-b5b3-a2de55e478e2)

# Алгоритм

# Основные 
## Отображаемый текст
Поле ввода текста, который будет заспамлен в чате.<br>
Также можно выбрать последние 10 вводов из списка.<br>

![image](https://github.com/user-attachments/assets/ddbcf9ff-7249-4d43-bb22-7664e6d257f3)


## Клавиша бинда
Желательно не трогать это поле, так как клавиша F8 мало где используется. <br>
Подробнее о том, зачем она нужна, можно посмотреть в <a href="https://github.com/metros-software/spam-chat-cs2/blob/main/README.md#%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC">Алгоритм</a>.<br><br>
![image](https://github.com/user-attachments/assets/416bf8a1-f3ef-4027-b879-c0bd53780f98)

## Команда отображения чата

Здесь нужно выбрать, в какой чат будет идти спам: в общий чат или в чат команды.<br> 

![image](https://github.com/user-attachments/assets/5a459962-4f02-4a1b-940f-50b867143337)
![image](https://github.com/user-attachments/assets/a84d6cff-0b90-44b6-913d-91715b6a4696)


## Команда отображения текста
Это поле отображает, какая команда будет использоваться для спама в чат.<br>
Она будет добавлена в autoexec.cfg.<br>

![image](https://github.com/user-attachments/assets/795b5bfe-75c2-425a-9f60-afdb12e6fc6e)


# Обновление 
## Бинд для exec autoexec.cfg
Нужно выбрать клавишу, которая будет перезагружать autoexec.cfg.<br>
Это необходимо для применения изменений, если текст спама был изменён или были внесены другие настройки.<br><br>
![image](https://github.com/user-attachments/assets/cb1dabd8-e192-498d-b54d-1af14d34cca7)

## Команда обновления autoexec.cfg
Это поле отображает, какая команда будет использоваться для обновления autoexec.cfg<br>
Она будет добавлена в autoexec.cfg.<br>

![image](https://github.com/user-attachments/assets/a5c053fa-7895-4874-b8fb-e28fe2fd7203)


# Цикл
## Задержка итерации
Задержка итерации — это задержка в секундах между отправкой текста в чат.<br>

![image](https://github.com/user-attachments/assets/c07c54e3-697a-493a-a379-594d9241b47e)

> Важно не ставить 0, так как из-за отсутствия задержки текст будет отправляться слишком быстро, и кс, скорее всего, крашнется.

## Количество итерации
Это количество нажатий на клавишу бинда отправки текста.

![image](https://github.com/user-attachments/assets/7da9b1d8-cb13-4d33-a01f-a27e255dcade)

> 0 - Бесконечное выполнение цикла.

# Расположение
