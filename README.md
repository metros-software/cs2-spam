# spam-chat-cs2
![1](https://github.com/user-attachments/assets/f0dd336c-ec38-4e95-b5b3-a2de55e478e2)

Программа Spam Chat CS2 предназначена для автоматической отправки текстовых сообщений в чат игры Counter-Strike 2 (CS2). <br>
Она позволяет настроить текст, который будет отправляться в чат, а также управлять частотой и количеством отправляемых сообщений. <br>
Программа работает на уровне операционной системы (Windows), имитируя нажатие клавиши, которая привязана к команде отправки сообщения в чат.<br>

## Основные функции программы
### Отправка текста в чат CS2
Программа позволяет настроить текст, который будет отправляться в чат (общий чат или командный чат).<br>
Текст отправляется с определённой задержкой и количеством повторений.<br>

#### Настройка клавиши для отправки сообщения
По умолчанию используется клавиша `F8`, которая не конфликтует с другими командами в CS2 или Windows.<br>
Программа имитирует нажатие этой клавиши, чтобы отправить сообщение в чат.<br>
#### Управление задержкой и количеством сообщений
Можно настроить задержку между отправкой сообщений (в секундах).<br>
Можно указать количество сообщений (или выбрать бесконечный цикл).<br>

### Обновление настроек
При изменении текста или других параметров программа обновляет конфигурационный файл `autoexec.cfg`, который используется в CS2.<br>
Для применения изменений нужно перезагрузить `autoexec.cfg` с помощью команды `exec autoexec.cfg` в консоли CS2.<br>

## Поддержка тем и языков
Программа поддерживает светлую и темную тему интерфейса.<br>
Также можно выбрать язык интерфейса: русский или английский.<br><br>
Программа автоматически устанавливает тему и язык в зависимости от локализации системы и выбранной темы Windows.<br>
Если вам необходимы конкретные настройки, добавьте соответствующие <a href="https://github.com/metros-software/spam-chat-cs2#параметры-запуска">параметры запуска</a>.<br>

## Как это работает
Программа создаёт команду в формате `bind "клавиша" "say текст"` (для общего чата) или `bind "клавиша" "say_team текст"` (для командного чата).<br>
Эта команда добавляется в файл `autoexec.cfg`, который автоматически загружается при запуске CS2.<br>
Программа имитирует нажатие клавиши (по умолчанию `F8`), что приводит к отправке сообщения в чат.<br>
Цикл повторяется с заданной задержкой и количеством итераций.<br>

# Установка
Скачать программу <a href="https://github.com/metros-software/spam-chat-cs2/releases/download/cs2/app.exe">здесь</a>.<br> 
Релиз <a href="https://github.com/metros-software/spam-chat-cs2/releases/tag/cs2">здесь</a>.

<a href="https://github.com/metros-software/spam-chat-cs2/releases/tag/cs2">![image](https://github.com/user-attachments/assets/e7e4f826-2896-4d54-a0f5-9f7c08335863)</a>
 


# Использование
## Первое использование
1. Запустите CS.
2. Введите в поле Отображаемый текст свой текст для спама.
3. Выберите из списка Команда отображения чата вариант, в какой именно чат будет происходить спам: в общий чат или в чат команды.
4. Нажмите на кнопку `Применить`.
5. В cs, во время матча (на карте), введите в консоли команду `exec autoexec.cfg` для перезагрузки файла `autoexec.cfg`.
6. Нажмите на кнопку `Запуск`.

## Последующие запуски (после первой настройки)
1. Запустите CS.
2. Нажмите на кнопку `Запуск`.

> При обновлении данных перезагрузите `autoexec.cfg`, нажав на клавишу `F9`.


# Алгоритм
Алгоритм программы состоит из простой команды: `bind "f8" "say текст"`. Если ввести эту команду в консоль, то при нажатии на клавишу `F8` будет отображаться текст в общем чате (say). Программа имитирует нажатие на эту клавишу. `F8` используется по умолчанию, так как она нигде не взаимодействует с элементами CS или Windows, что позволяет спокойно пользоваться Windows и CS. Если указать другую клавишу, например, `i`, то будет происходить имитация нажатия на эту клавишу, и при открытии чата или консоли она будет вводиться. Поэтому оставьте всё как есть.

При изменении настроек нажмите на кнопку `Применить`, а затем нажмите `F9` для выполнения команды `autoexec.cfg`, чтобы обновить команду `bind "f8" "say текст"`.

Цикл работает в зависимости от задержки и количества итераций. Цикл выполняется именно на уровне Windows.

# Основные 
## Отображаемый текст
Поле ввода текста, который будет заспамлен в чате.<br>
Также можно выбрать последние `10` вводов из списка.<br>

![image](https://github.com/user-attachments/assets/ddbcf9ff-7249-4d43-bb22-7664e6d257f3)


## Клавиша бинда
Желательно не трогать это поле, так как клавиша F8 мало где используется. <br>
Подробнее о том, зачем она нужна, можно посмотреть в <a href="https://github.com/metros-software/spam-chat-cs2#%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC">Алгоритм</a>.<br><br>
![image](https://github.com/user-attachments/assets/416bf8a1-f3ef-4027-b879-c0bd53780f98)

## Команда отображения чата

Здесь нужно выбрать, в какой чат будет идти спам: в общий чат или в чат команды.<br> 

![image](https://github.com/user-attachments/assets/5a459962-4f02-4a1b-940f-50b867143337)
![image](https://github.com/user-attachments/assets/a84d6cff-0b90-44b6-913d-91715b6a4696)


## Команда отображения текста
Это поле отображает, какая команда будет использоваться для спама в чат.<br>
Она будет добавлена в `autoexec.cfg`.<br>

![image](https://github.com/user-attachments/assets/795b5bfe-75c2-425a-9f60-afdb12e6fc6e)


# Обновление 
## Бинд для exec autoexec.cfg
Нужно выбрать клавишу, которая будет перезагружать `autoexec.cfg`.<br>
Это необходимо для применения изменений, если текст спама был изменён или были внесены другие настройки.<br><br>
![image](https://github.com/user-attachments/assets/cb1dabd8-e192-498d-b54d-1af14d34cca7)

## Команда обновления autoexec.cfg
Это поле отображает, какая команда будет использоваться для обновления `autoexec.cfg`<br>
Она будет добавлена в `autoexec.cfg`.<br>

![image](https://github.com/user-attachments/assets/a5c053fa-7895-4874-b8fb-e28fe2fd7203)


# Цикл

Цикл работает в зависимости от клавиши бинда, задержки и количества итераций.<br>
Клавиша бинда будет нажиматься с определённой задержкой, а количество нажатий будет соответствовать количеству итераций.

## Задержка итерации
Задержка итерации — это задержка в секундах между отправкой текста в чат.<br>

![image](https://github.com/user-attachments/assets/c07c54e3-697a-493a-a379-594d9241b47e)

> Важно не ставить 0, так как из-за отсутствия задержки текст будет отправляться слишком быстро, и кс, скорее всего, крашнется.

## Количество итерации
Это количество нажатий на клавишу бинда отправки текста.

![image](https://github.com/user-attachments/assets/7da9b1d8-cb13-4d33-a01f-a27e255dcade)

> 0 - Бесконечное выполнение цикла.

# Расположение
| Файл | Описание |
|-------|------------|
| **cs2.exe** | Местоположение игры CS2 |
| **autoexec.cfg** | Файл конфигурации CS2 |
| **config** | Файл конфигурации программы |


# Параметры запуска

```
usage: app.exe [-h] [--theme {dark,light}] [--locale {ru,en}]

Spam Text Chat CS2

options:
  -h, --help            show this help message and exit
  --theme {dark,light}  Выберите тему: dark (темная) или light (светлая).
  --locale {ru,en}      Выберите язык интерфейса: ru (русский) или en (английский).
```

# Конфиг программы
```
[Settings]
chat_text = text
bind_key = F8
delay = 1
language = ru
bind_exec_key = F9

[History]
texts = text1;text2
```

# Компиляция
```
pyinstaller -y -w -F --icon=app.ico app.py
```
или
```bash
./setup.bat
```
