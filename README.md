#  👾⌨️ Keylogger em Python ⌨️👾

## 🔐 Aviso Legal
* Este script é um exemplo para entender como capturar eventos do teclado em Python e manipular janelas no Windows. O uso de keyloggers pode violar a privacidade e a lei.
Este projeto **Keylogger em Python** é fornecido **exclusivamente para fins educacionais**.

*  ⚠ **O uso deste código para atividades ilegais, invasão de privacidade ou qualquer outra prática não autorizada é estritamente proibido e pode acarretar consequências legais.**
Ao utilizar este projeto, você se compromete a agir de forma ética e responsável. Use apenas para fins éticos e com autorização.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📄 Descrição
Este projeto é um script em Python que captura as teclas digitadas no teclado do usuário e salva essas informações em um arquivo texto. Além disso, o programa registra:

* Qual janela do computador estava ativa no momento da digitação (exemplo: navegador, editor de texto, sites, etc).

* O local exato em que cada tecla foi pressionada.

* O status da tecla Caps Lock para saber se as letras devem ser registradas como maiúsculas ou minúsculas.

* Algumas teclas especiais são identificadas e registradas de forma legível (ex: [ENTER], [BACKSPACE], [ESPACO], [TAB], [ESC], [SHIFT], [CTRL], [ALT], [CAPS LOCK]).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🎯 Objetivo do Projeto

* Este projeto foi criado com a finalidade de **estudar a defesa cibernética por meio do entendimento profundo de ataques**, como keyloggers. Compreender como esses ataques funcionam é essencial para desenvolver estratégias eficazes de proteção e segurança digital, sendo uma prática legítima e ética dentro da área de cibersegurança.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 💡 Motivação

* A motivação para criar este projeto veio do interesse em aprender na prática sobre técnicas de ataque e defesa, ampliando meus conhecimentos em segurança da informação. Além disso, quero contribuir para a conscientização sobre os riscos desses ataques e a importância de medidas preventivas.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  
## 🔧 Funcionalidades 

* Registro das teclas digitadas em tempo real.

* Detecção da janela ativa no sistema Windows usando a biblioteca win32gui.

* Monitoramento do estado da tecla Caps Lock para registrar corretamente letras maiúsculas e minúsculas.

* Tratamento de teclas especiais para melhor legibilidade no arquivo de log.

* Encerramento do keylogger com a tecla ESC.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 📱 Tecnologias e Bibliotecas Utilizadas 

* Python 3.x (Versão utilizada no projeto: Python 3.12.5 )

* pynput: Biblioteca para monitorar eventos do teclado. (Versão utilizada no projeto: pynput==1.8.1 )

* pywin32 (win32gui): Biblioteca para manipular janelas no Windows e obter a janela ativa. (Versão utilizada no projeto: pywin32==310 )

* datetime: Para registrar o horário das teclas pressionadas.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 🛠️ Como Executar
* 1 - Certifique-se de ter o Python 3 instalado no seu computador 
  
* 2 - Instale as dependências necessárias com:
 
       pip install pynput pywin32
  
* 3 - Execute o script Python.

* 4 - O keylogger começará a capturar as teclas digitadas, salvando no arquivo captura_teclas.txt no mesmo diretório.

* 5 - Para encerrar o keylogger, pressione a tecla ESC.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📁 Estrutura do Código

    • get_janela_ativa():
  
  * Função responsável por retornar o título da janela que está ativa no momento da digitação. Isso permite identificar em qual programa ou site o usuário estava digitando.
<br>

        • on_press(key):
   Função executada sempre que uma tecla é pressionada. Ela:
   
* Registra a nova janela ativa, caso tenha mudado;
  
* Verifica o estado da tecla Caps Lock;
  
* Salva no arquivo de log a tecla pressionada (com tratamento para letras maiúsculas/minúsculas e teclas especiais).
  
<br>

      • on_release(key):
  * Função chamada ao soltar uma tecla. Encerra o keylogger quando a tecla ESC é detectada.

<br>

### Dicionário teclas_especiais:

  * Estrutura que mapeia teclas especiais para representações mais compreensíveis no arquivo de log:

        • Dicionário que mapeia teclas especiais para uma representação mais legível:
    
                                            Tecla (código)	 |      Representação no log
                                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                          Key.space	         |         [ESPAÇO]
                                          Key.enter	         |         [ENTER]
                                          Key.tab	         |         [TAB]
                                          Key.backspace	         |         [BACKSPACE]
                                          Key.esc	         |         [ESC]
                                          Key.shift	         |         [SHIFT]
                                          Key.ctrl_l	         |         [CTRL]
                                          Key.ctrl_r	         |         [CTRL]
                                          Key.alt_l	         |         [ALT]
                                          Key.alt_r	         |         [ALT]
                                          Key.alt_gr	         |         [ALT GR]
                                          Key.caps_lock	         |         [CAPSLOCK]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 💻 Execução do Projeto (Testes)

    • Keylogger iniciado "Vamos capturar algumas teclas meu pequeno hacker." Precione ESC para encerrar.


      [14:53:57] Janela ativa: Nova guia - Google Chrome
      keylogger[ENTER]
      
      
      [14:54:08] Janela ativa: YouTube - Google Chrome
      [CAPSLOCK]E[CAPSLOCK]minem[ENTER]
      
      
      [14:54:21] Janela ativa: Prompt de Comando
      cd[ENTER]
      
      
      [14:54:27] Janela ativa: keylogger.py - Keylogger - Visual Studio Code
      [CAPSLOCK]E
      
      [14:54:29] Janela ativa: â— keylogger.py - Keylogger - Visual Studio Code
      AI[ESPAÇO]PESSOAL[ESPAÇO]DO[ESPAÇO]GITHUB[ENTER]
      NOTAS[ESPAÇO]PARA[ESPAÇO]ESTE[ESPAÇO]PROJETO[ESC]










