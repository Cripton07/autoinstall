import os 

ejecutar = input("""
------------------------------------------------------------
|                Hecho por cripton07                       |
|       Mi github https://github.com/Cripton07             |
|--script autoinstall para personalizar tu entorno termux--|
------------------------------------------------------------
deseas ejecutar en autoinstall (y/n):""")

if ejecutar.lower() == "y":
    os.system('pkg update && pkg upgrade -y')
    os.system('git clone --depth=1 https://github.com/mayTermux/myTermux.git')
    os.system('cd myTermux')
    os.system('export COLUMNS LINES')
    os.system('chmod +x ./install.sh')
    os.system('./install.sh')

elif ejecutar.lower() == "n":
    print("hasta luego!!")
