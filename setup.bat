@cls
@color 03
@echo Start %time%
@pip install -r requirements.txt
@pyinstaller -y -w -F --icon=app.ico app.py
@echo End %time%
@pause>nul