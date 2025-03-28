# Sistema Cliente/Servidor para Processamento de Imagens

Este projeto implementa um sistema em três camadas, onde um cliente envia imagens para um servidor via HTTP, o servidor aplica um filtro à imagem e retorna a versão modificada. Além disso, o sistema salva as imagens e seus metadados em um banco de dados SQLite.

##  Funcionalidades

✅ Envio de imagens do cliente para o servidor via HTTP\
✅ Aplicação de filtros de imagem (exemplo: pixelização, troca de cores)\
✅ Retorno da imagem processada ao cliente\
✅ Armazenamento das imagens em disco\
✅ Registro dos metadados da imagem (nome, filtro aplicado, data/hora) no SQLite\
✅ Visualização da imagem original e alterada pelo cliente

##  Tecnologias Utilizadas

- *Python*
- *Flask* – Comunicação HTTP do servidor
- *Tkinter* – Interface gráfica do cliente
- *Pillow* – Processamento e aplicação de filtros às imagens
- *SQLite* – Armazenamento de metadados das imagens

##  Como Executar

###  Configuração do Servidor

1. Navegue até a pasta do servidor:

   bash
   cd servidor-imagem
   

2. Crie um ambiente virtual:

   bash
   python -m venv venv
   

3. Ative o ambiente virtual:

   - *Windows (Prompt de Comando)*
     bash
     venv\Scripts\activate
     
   - *Windows (PowerShell) – Se houver problemas de permissão:*
     powershell
     Get-ExecutionPolicy  # Para verificar a política atual
     Set-ExecutionPolicy Unrestricted -Scope Process  # Permite execução temporária
     venv\Scripts\activate
     

4. Instale as dependências:

   bash
   pip install flask pillow
   

5. Execute o servidor:

   bash
   python server.py
   

O servidor estará rodando em http://localhost:5000

###  Configuração do Cliente

1. No outro computador (ou na mesma máquina), execute:
   bash
   python cliente.py
   
2. A interface gráfica do cliente será aberta para envio de imagens

##  Demonstração

### 🔹 Envio da Imagem

 O cliente seleciona uma imagem e a envia para o servidor

### 🔹 Imagem Recebida com Filtro

 O servidor processa a imagem e retorna a versão alterada

### 🔹 Imagens Salvas

 A imagem original e a modificada são armazenadas no disco

### 🔹 Dados Gravados no Banco

 O nome da imagem, filtro aplicado e data/hora são registrados no SQLite

##VIDEO
[Baixar vídeo](video.mp4)

---
