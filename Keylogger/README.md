# Keylogger em Python

## Descrição

Este projeto é um script em Python que captura as teclas digitadas no teclado do usuário e salva essas informações em um arquivo texto. Além disso, o programa registra:

Qual janela do computador estava ativa no momento da digitação (exemplo: navegador, editor de texto, etc).

O horário exato em que cada tecla foi pressionada.

O status da tecla Caps Lock para saber se as letras devem ser registradas como maiúsculas ou minúsculas.

Algumas teclas especiais são identificadas e registradas de forma legível (ex: [ENTER], [BACKSPACE], [ESPACO]).

Funcionalidades
Registro das teclas digitadas em tempo real.

Detecção da janela ativa no sistema Windows usando a biblioteca win32gui.

Monitoramento da tecla Caps Lock para registrar letras maiúsculas quando ativada.

Tratamento de teclas especiais para melhor legibilidade no arquivo de log.

Encerramento do keylogger com a tecla ESC.

Tecnologias e Bibliotecas Utilizadas
Python 3.x

pynput: Biblioteca para monitorar eventos do teclado.

pywin32 (win32gui): Biblioteca para manipular janelas no Windows e obter a janela ativa.

datetime: Para registro do horário das teclas pressionadas.
