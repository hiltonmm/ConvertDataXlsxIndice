@echo off
echo Criando ambiente virtual...
python -m venv .venv

echo Ativando ambiente e instalando dependencias...
call .venv\Scripts\activate

echo Instalando bibliotecas necessarias...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Ambiente configurado com sucesso!
echo Voce pode executar seu script com: .venv\Scripts\python.exe convertData.py
pause