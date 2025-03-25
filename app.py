import os
import sys
import time
import threading
import configparser
import psutil
import keyboard
import pywinstyles
import webbrowser
import locale
import winreg
import argparse
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from darktheme.widget_template import DarkPalette
from datetime import datetime
 

__version__ = "1.7 [25.03.2025]"

TEXTS = {
    "ru": {
        "window_title": "Спам текст чат кс2",
        "main_settings": "Основные",
        "displayed_text": "Отображаемый текст",
        "bind_key": "Клавиша бинда",
        "text_command": "Команда отображения текста",
        "chat_command": "Команда отображения чата",
        "location": "Расположение",
        "cycle": "Цикл",
        "iteration_delay": "Задержка итерации (секунды)",
        "iterations": "Количество итераций",
        "update": "Обновление",
        "bind_exec": "Бинд для exec autoexec.cfg",
        "update_command": "Команда обновления autoexec.cfg",
        "start": "&Запуск",
        "stop": "&Стоп",
        "apply": "&Применить",
        "close": "&Отмена",
        "version": f"Версия {__version__}",
        "error": "Ошибка",
        "error_1": "Ошибка создания конфигурационного файла",
        "error_2": "Ошибка записи в",
        "error_3": "Ошибка записи в конфигурационный файл",
        "error_4": "Папка не найдена",
        "cs2_not_found": "Процесс cs2.exe не найден.",
        "launch_cs2": "Запустить cs2.exe",
        "cancel": "Отмена",
        "powerful_pc": "0 — Только если мощный компьютер",
        "infinite_loop": "0 — Бесконечное выполнение цикла",
        "say_all": "В общий чат (say)",
        "say_team": "В чат команды (say_team)",
        "file_name": "Название"
    },
    "en": {
        "window_title": "Spam text chat CS2",
        "main_settings": "Main",
        "displayed_text": "Displayed text",
        "bind_key": "Bind key",
        "text_command": "Text display command",
        "chat_command": "Chat display command",
        "location": "Location",
        "cycle": "Cycle",
        "iteration_delay": "Iteration delay (seconds)",
        "iterations": "Number of iterations",
        "update": "Update",
        "bind_exec": "Bind for exec autoexec.cfg",
        "update_command": "Update autoexec.cfg command",
        "start": "&Start",
        "stop": "&Stop",
        "apply": "&Apply",
        "close": "&Cancel",
        "version": f"Version {__version__}",
        "error": "Error",
        "error_1": "Error creating configuration file",
        "error_2": "Error writing to",
        "error_3": "Error writing to configuration file",
        "error_4": "Folder not found",
        "cs2_not_found": "cs2.exe process not found.",
        "launch_cs2": "Launch cs2.exe",
        "cancel": "Cancel",
        "powerful_pc": "0 — Only if powerful PC",
        "infinite_loop": "0 — Infinite loop execution",
        "say_all": "To global chat (say)",
        "say_team": "To team chat (say_team)",
        "file_name": "File name"
    },
}

class IconBase64:
 
    def main_window():
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray.fromBase64(b'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'))
        return pixmap

def find_cs2_exe_path():
    try:
        for proc in psutil.process_iter(['name', 'exe']):
            if proc.info['name'] == "cs2.exe":
                return proc.info['exe']
    except Exception:
        return None
    return None

def find_cfg_cs2_path():
    cs2_exe = find_cs2_exe_path()
    if cs2_exe is None:
        return None
    cs2_path = cs2_exe.replace('cs2.exe', 'autoexec.cfg')
    parts = cs2_path.split(os.sep)
    if "bin" in parts and "win64" in parts:
        bin_index = parts.index("bin")
        parts[bin_index:bin_index + 2] = ["csgo", "cfg"]
        new_path = os.sep.join(parts)
        return new_path
    return None

def contains_letter_or_symbol(text):
    cleaned_text = text.strip("\t\n\r ")
    return bool(cleaned_text)

def is_windows_dark_mode():
    try:
        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize",
            0,
            winreg.KEY_READ
        ) as key:
            value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            return value == 0
    except Exception:
        return False

class PushButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon(IconBase64.lang_open()))

class KeyCaptureLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    def keyPressEvent(self, event):
        key = event.key()
        key_text = event.text()
        if key == Qt.Key_Space:
            self.setText("SPACE")
        elif key == Qt.Key_Delete:
            self.setText("DELETE")
        elif key == Qt.Key_Control:
            self.setText("CTRL")
        elif key == Qt.Key_Escape:
            self.setText("ESCAPE")
        elif key == Qt.Key_CapsLock:
            self.setText("CAPSLOCK")
        elif key == Qt.Key_Tab:
            self.setText("TAB")
        elif key == Qt.Key_Shift:
            self.setText("SHIFT")
        elif Qt.Key_F1 <= key <= Qt.Key_F12:
            self.setText(f"F{key - Qt.Key_F1 + 1}")
        elif contains_letter_or_symbol(key_text):
            self.setText(key_text)
        else:
            self.setText("")

class MainWindow(QMainWindow):
    path_config = os.path.join(os.getcwd(), 'spam_text_cs2.cfg')

    def __init__(self):
        super().__init__()
        self.language = LANGUAGE
        self.chat_text_history = []
        self.setWindowTitle(TEXTS[self.language]["window_title"])
        self.setFixedSize(QSize(700, 600))
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint & ~Qt.WindowMaximizeButtonHint)
        self.move(
            (QDesktopWidget().screenGeometry().width() - self.frameGeometry().width()) // 2,
            (QDesktopWidget().screenGeometry().height() - self.frameGeometry().height()) // 2
        )
        self.setWindowIcon(QIcon(IconBase64.main_window()))
        central_widget = QWidget()
        self.main_layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)
        self.create_main_layout()
        self.load_config()
        self.bind_key = self.bind_key_input.text() if self.bind_key_input.text() else "F8"
        try:
            self.delay = float(self.delay_input.value())
        except Exception:
            self.delay = 1.0
        self.running = False
        self.thread = None

    def get_text(self, ru_text, en_text):
        return ru_text if self.language == "ru" else en_text

    def log(self, text=''):
        current_time = datetime.now().strftime("%H:%M:%S")
        error_message = f'[{current_time}] - {text}'
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle(TEXTS[self.language]["error"])
        msg_box.setText(error_message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def create_main_layout(self):
        main_settings_frame = QGroupBox(TEXTS[self.language]["main_settings"])
        main_settings_frame.setObjectName("main_settings_frame")
        main_settings_layout = QGridLayout()

        chat_text_label = QLabel(TEXTS[self.language]["displayed_text"])
        chat_text_label.setObjectName("chat_text_label")
        main_settings_layout.addWidget(chat_text_label, 0, 0)

        self.chat_text_combo = QComboBox()
        self.chat_text_combo.setEditable(True)
        self.chat_text_combo.setInsertPolicy(QComboBox.NoInsert)
        self.chat_text_combo.lineEdit().setPlaceholderText(TEXTS[self.language]["displayed_text"])
        self.chat_text_combo.lineEdit().textChanged.connect(self.update_command)
        self.chat_text_combo.addItems(self.chat_text_history)
        main_settings_layout.addWidget(self.chat_text_combo, 0, 1)

        bind_key_label = QLabel(TEXTS[self.language]["bind_key"])
        bind_key_label.setObjectName("bind_key_label")
        main_settings_layout.addWidget(bind_key_label, 1, 0)

        self.bind_key_input = KeyCaptureLineEdit()
        self.bind_key_input.textChanged.connect(self.update_command)
        main_settings_layout.addWidget(self.bind_key_input, 1, 1)

        chat_command_label = QLabel(TEXTS[self.language]["chat_command"])
        chat_command_label.setObjectName("chat_command_label")
        main_settings_layout.addWidget(chat_command_label, 2, 0)

        self.chat_command_combo = QComboBox()
      
        self.chat_command_combo.addItems([TEXTS[self.language]["say_all"], 
                                          TEXTS[self.language]["say_team"]]) 
        
            
        self.chat_command_combo.currentIndexChanged.connect(self.update_command)
        main_settings_layout.addWidget(self.chat_command_combo, 2, 1)

        text_command_label = QLabel(TEXTS[self.language]["text_command"])
        text_command_label.setObjectName("text_command_label")
        main_settings_layout.addWidget(text_command_label, 3, 0)

        self.text_command_input = QLineEdit(r'bind "" "say"')
        self.text_command_input.setReadOnly(True)
        main_settings_layout.addWidget(self.text_command_input, 3, 1)

        main_settings_frame.setLayout(main_settings_layout)
        self.main_layout.addWidget(main_settings_frame)

        update_frame = QGroupBox(TEXTS[self.language]["update"])
        update_frame.setObjectName("update_frame")
        update_layout = QGridLayout()

        bind_exec_label = QLabel(TEXTS[self.language]["bind_exec"])
        bind_exec_label.setObjectName("bind_exec_label")
        update_layout.addWidget(bind_exec_label, 0, 0)

        self.bind_exec_input = KeyCaptureLineEdit()
        self.bind_exec_input.textChanged.connect(self.update_exec_bind_command)
        update_layout.addWidget(self.bind_exec_input, 0, 1)

        update_label = QLabel(TEXTS[self.language]["update_command"])
        update_label.setObjectName("update_label")
        update_layout.addWidget(update_label, 1, 0)

        self.update_command_input = QLineEdit("exec autoexec.cfg")
        self.update_command_input.setReadOnly(True)
        update_layout.addWidget(self.update_command_input, 1, 1)

        update_frame.setLayout(update_layout)
        self.main_layout.addWidget(update_frame)

        cycle_settings_frame = QGroupBox(TEXTS[self.language]["cycle"])
        cycle_settings_frame.setObjectName("cycle_settings_frame")
        cycle_settings_layout = QGridLayout()

        delay_label = QLabel(TEXTS[self.language]["iteration_delay"])
        delay_label.setObjectName("delay_label")
        cycle_settings_layout.addWidget(delay_label, 0, 0)

        self.delay_input = QSpinBox()
        self.delay_input.setRange(0, 1000)
        self.delay_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        cycle_settings_layout.addWidget(self.delay_input, 0, 1)

        info_label_1 = QLabel(TEXTS[self.language]["powerful_pc"])
        cycle_settings_layout.addWidget(info_label_1, 0, 2)

        iterations_label = QLabel(TEXTS[self.language]["iterations"])
        iterations_label.setObjectName("iterations_label")
        cycle_settings_layout.addWidget(iterations_label, 1, 0)

        self.iterations_input = QSpinBox()
        self.iterations_input.setRange(0, 99999)
        self.iterations_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.iterations_input.setValue(0)
      
        cycle_settings_layout.addWidget(self.iterations_input, 1, 1)

        info_label_2 = QLabel(TEXTS[self.language]["infinite_loop"])
        cycle_settings_layout.addWidget(info_label_2, 1, 2)
        

        cycle_settings_frame.setLayout(cycle_settings_layout)
        self.main_layout.addWidget(cycle_settings_frame)

        location_frame = QGroupBox(TEXTS[self.language]["location"])
        location_frame.setObjectName("location_frame")
        location_layout = QVBoxLayout()

        table_widget = QTableWidget()
      
        table_widget.setColumnCount(2)   
       
        table_widget.setColumnCount(2)
        table_widget.setHorizontalHeaderLabels(
            [TEXTS[self.language]["file_name"], TEXTS[self.language]["location"]]
        )

        header = table_widget.horizontalHeader()
        header.setStretchLastSection(True)
        header.setHighlightSections(False)
        table_widget.setSelectionBehavior(QTableWidget.SelectRows)
        table_widget.setSelectionMode(QTableWidget.SingleSelection)
        table_widget.setEditTriggers(QTableWidget.NoEditTriggers)
        table_widget.setRowCount(3)  
        table_widget.setShowGrid(False)  
        table_widget.verticalHeader().setVisible(False) 

        def on_table_item_click(item):
            if item.column() == 1:
                path = item.text()  
                self.open_folder(path)  

        table_widget.itemClicked.connect(on_table_item_click)

        cs2_exe = find_cs2_exe_path() or ""
        table_widget.setItem(0, 0, QTableWidgetItem("cs2.exe"))
        table_widget.setItem(0, 1, QTableWidgetItem(cs2_exe))

        autoexec_path = find_cfg_cs2_path() or ""
        table_widget.setItem(1, 0, QTableWidgetItem("autoexec.cfg"))
        table_widget.setItem(1, 1, QTableWidgetItem(autoexec_path))
        cfg_input = self.path_config
        table_widget.setItem(2, 0, QTableWidgetItem("config"))
        table_widget.setItem(2, 1, QTableWidgetItem(cfg_input))
        table_widget.resizeColumnsToContents()
        table_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        location_layout.addWidget(table_widget)
        location_frame.setLayout(location_layout)
        self.main_layout.addWidget(location_frame)
        table_widget.setMinimumHeight(111)  

        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)
        self.separator.setStyleSheet('background:#f1f1f1;')
        self.main_layout.addWidget(self.separator)

        buttons_layout = QHBoxLayout()
        self.label_version = QLabel(TEXTS[self.language]["version"])
        self.label_version.setObjectName('label_version')
        buttons_layout.addWidget(self.label_version)
        buttons_layout.addStretch(1)
        self.start_button = QPushButton(TEXTS[self.language]["start"])
        self.start_button.setObjectName("start_button")
        self.start_button.clicked.connect(self.toggle_start_stop)
        self.start_button.setDefault(True)
        buttons_layout.addWidget(self.start_button)
        self.apply_button = QPushButton(TEXTS[self.language]["apply"])
        self.apply_button.setObjectName("apply_button")
        self.apply_button.clicked.connect(self.save_config_on_apply)
        buttons_layout.addWidget(self.apply_button)
        self.close_button = QPushButton(TEXTS[self.language]["close"])
        self.close_button.setObjectName("close_button")
        self.close_button.clicked.connect(lambda: self.close())
        buttons_layout.addWidget(self.close_button)
        self.main_layout.addLayout(buttons_layout)

    def update_exec_bind_command(self):
        bind_key = self.bind_exec_input.text()
        if bind_key:
            self.update_command_input.setText(f'bind "{bind_key}" "exec autoexec.cfg"')

    def save_config_on_apply(self):
        self.save_config(save_autoexec=True)

    def update_command(self):
        chat_text = self.chat_text_combo.currentText()
        bind_key = self.bind_key_input.text()
        chat_command = "say" if self.chat_command_combo.currentText() == TEXTS[self.language]["say_all"] else "say_team"
        text_command = f'bind "{bind_key}" "{chat_command} {chat_text}"'
        self.text_command_input.setText(text_command)

    def open_folder(self, path):
        folder_path = os.path.dirname(path)
        if os.path.isdir(folder_path):
            os.startfile(folder_path)
        else:
            self.log(f"{TEXTS[self.language]["error_4"]} : {path}")

    def toggle_start_stop(self):
        if find_cs2_exe_path() is None:
            self.log(TEXTS[self.language]["cs2_not_found"])
            return
        self.set_interface_enabled(self.running)
        self.bind_key = self.bind_key_input.text().strip() if self.bind_key_input.text().strip() else "F8"
        try:
            self.delay = float(self.delay_input.value())
        except Exception:
            self.delay = 1.0
        if self.running:
            self.running = False
            self.start_button.setText(TEXTS[self.language]["start"])
            if self.thread and self.thread.is_alive():
                self.thread.join()
        else:
            self.running = True
            self.start_button.setText(TEXTS[self.language]["stop"])
            if self.thread and self.thread.is_alive():
                self.thread.join()
            self.thread = threading.Thread(target=self.run_spam, daemon=True)
            self.thread.start()

    def set_interface_enabled(self, enabled):
        self.chat_text_combo.setEnabled(enabled)
        self.bind_key_input.setEnabled(enabled)
        self.delay_input.setEnabled(enabled)
        self.apply_button.setEnabled(enabled)
        self.chat_command_combo.setEnabled(enabled)
        self.bind_exec_input.setEnabled(enabled)
        self.iterations_input.setEnabled(enabled)
        self.start_button.setEnabled(True)

    def run_spam(self):
        iterations = self.iterations_input.value()
        if iterations == 0:
            while self.running:
                try:
                    keyboard.press_and_release(self.bind_key)
                except Exception as e:
                    self.log(f"Ошибка при нажатии клавиши: {e}")
                time.sleep(self.delay)
        else:
            for _ in range(iterations):
                if not self.running:
                    break
                try:
                    keyboard.press_and_release(self.bind_key)
                except Exception as e:
                    self.log(f"Ошибка при нажатии клавиши: {e}")
                time.sleep(self.delay)
            self.running = False
            self.start_button.setText(TEXTS[self.language]["start"])
            self.set_interface_enabled(True)
    def update_history(self, text):
 
        if text and text not in self.chat_text_history:   
            self.chat_text_history.append(text)   
            self.chat_text_combo.addItem(text)  
    def save_program_config(self):
        chat_text = self.chat_text_combo.currentText()
        bind_key = self.bind_key_input.text().strip() if self.bind_key_input.text().strip() else "F8"
        delay = self.delay_input.value()
        bind_exec_key = self.bind_exec_input.text().strip()
        self.update_history(chat_text)
        config = configparser.ConfigParser()
        config['Settings'] = {
            'chat_text': chat_text,
            'bind_key': bind_key,
            'delay': str(delay),
            'language': self.language,
            'bind_exec_key': bind_exec_key
        }
        config['History'] = {
            'texts': ';'.join(self.chat_text_history)
        }
        try:
            with open(self.path_config, 'w', encoding='utf-8') as configfile:
                config.write(configfile)
        except Exception as e:
            self.log(f"{TEXTS[self.language]["error_3"]} : {e}")

    def save_autoexec_cfg(self):
        text_command = self.text_command_input.text().strip()
        if not text_command:
            self.log(TEXTS[self.language]['error'])
            return

        autoexec_path = find_cfg_cs2_path()
        if autoexec_path is not None:
            if not os.path.isfile(autoexec_path):
                with open(autoexec_path, 'w', encoding='utf-8') as file:
                    file.write(text_command + "\n")
            else:
                try:
                    with open(autoexec_path, 'r', encoding='utf-8') as file:
                        lines = file.readlines()
                except Exception as e:
                    lines = []

                bind_updated = False
                for i, line in enumerate(lines):
                    if line.strip().startswith("bind "):
                        current_bind_key = line.split('"')[1]
                        new_bind_key = text_command.split('"')[1]
                        if current_bind_key == new_bind_key:
                            bind_updated = True
                            lines[i] = text_command + "\n"
                            break

                if not bind_updated:
                    lines.append(text_command + "\n")

                try:
                    with open(autoexec_path, 'w', encoding='utf-8') as file:
                        file.writelines(lines)
                except Exception as e:
                    self.log(f"{TEXTS[self.language]['error_2']} {autoexec_path}: {e}")
        else:
            self.log(TEXTS[self.language]['error'])

    def save_config(self, save_autoexec=True):
        self.save_program_config()
        if save_autoexec:
            self.save_autoexec_cfg()

    def load_config(self):
        if os.path.isfile(self.path_config):
            config = configparser.ConfigParser()
            try:
                config.read(self.path_config, encoding='utf-8')
                chat_text = config.get('Settings', 'chat_text', fallback='')
                self.chat_text_combo.setCurrentText(chat_text)
                self.bind_key_input.setText(config.get('Settings', 'bind_key', fallback='F8'))
                try:
                    self.delay_input.setValue(int(config.get('Settings', 'delay', fallback='1')))
                except Exception:
                    self.delay_input.setValue(1)
                bind_exec_key = config.get('Settings', 'bind_exec_key', fallback='F9')
                self.bind_exec_input.setText(bind_exec_key)
                history_texts = config.get('History', 'texts', fallback='')
                if history_texts:
                    self.chat_text_history = history_texts.split(';')
                    self.chat_text_combo.clear()
                    self.chat_text_combo.addItems(self.chat_text_history)
                self.update_command()
            except Exception as e:
                self.log(f"Ошибка чтения конфигурационного файла: {e}")
        else:
            config_default = configparser.ConfigParser()
            config_default['Settings'] = {
                'chat_text': 'text',
                'bind_key': 'F8',
                'delay': '1',
                'language': self.language,
                'bind_exec_key': 'F9'
            }
            config_default['History'] = {
                'texts': ''
            }
            try:
                with open(self.path_config, "w", encoding='utf-8') as my_file:
                    config_default.write(my_file)
            except Exception as e:
                self.log(f"{TEXTS[self.language]['error_1']}: {e}")
            self.chat_text_combo.setCurrentText('text')
            self.bind_key_input.setText('F8')
            self.delay_input.setValue(1)
            self.bind_exec_input.setText('F9')
            self.chat_text_history = []
            self.chat_text_combo.clear()
            self.update_command()

def check_cs2_process():
    if find_cs2_exe_path() is None:
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        msg_box = QMessageBox()
        msg_box.setWindowIcon(QIcon(IconBase64.main_window()))
        msg_box.setWindowTitle(TEXTS[LANGUAGE]["error"])
        msg_box.setText(TEXTS[LANGUAGE]["cs2_not_found"])
        msg_box.setInformativeText(TEXTS[LANGUAGE]["launch_cs2"])
        launch_button = msg_box.addButton(TEXTS[LANGUAGE]["launch_cs2"], QMessageBox.ActionRole)
        cancel_button = msg_box.addButton(TEXTS[LANGUAGE]["cancel"], QMessageBox.RejectRole)
        msg_box.exec_()
        if msg_box.clickedButton() == launch_button:
            try:
                webbrowser.open("steam://rungameid/730")
                wait_for_cs2()
            except Exception as e:
                print(f"Ошибка при запуске Steam: {e}")
        else:
            sys.exit(0)
    else:
        open_main_window()

def wait_for_cs2():
    timeout = 60
    start_time = time.time()
    while find_cs2_exe_path() is None:
        if time.time() - start_time > timeout:
            print("Превышено время ожидания запуска cs2.exe")
            sys.exit(0)
        time.sleep(5)
    open_main_window()

def parse_arguments():
    parser = argparse.ArgumentParser(description="Spam Text Chat CS2")
    parser.add_argument(
        "--theme",
        choices=["dark", "light"],
        help="Выберите тему: dark (темная) или light (светлая)."
    )
    parser.add_argument(
        "--locale",
        choices=["ru", "en"],
        help="Выберите язык интерфейса: ru (русский) или en (английский)."
    )
    args = parser.parse_args()
    return args

def open_main_window():
    global LANGUAGE
    args = parse_arguments()

    if args.theme == "dark":
        theme = True
    elif args.theme == "light":
        theme = False
    else:
        theme = is_windows_dark_mode() 

    if args.locale:
        LANGUAGE = args.locale
    else:
        sys_locale = locale.getlocale()[0] or "en_US"
        LANGUAGE = "ru" if "ru" in sys_locale.lower() else "en"
    
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    if theme:
        app.setPalette(DarkPalette())
        window = MainWindow()
        pywinstyles.apply_style(window, 'dark')
        window.separator.setStyleSheet('background:#353535;')
    else:
        window = MainWindow()
        window.separator.setStyleSheet('background:#f1f1f1;')
    
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    check_cs2_process()


