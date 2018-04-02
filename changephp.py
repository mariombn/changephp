#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import commands
import subprocess

output = subprocess.check_output(["php", "-v"]);
phpOld = output[4:7]
phpNew = sys.argv[1]

print("De " + phpOld + " para: " + phpNew)

print("Iniciando troca de versão do PHP")
print

print("Desativando php" + phpOld)
os.system("sudo a2dismod php" + phpOld)

print("Ativando php" + phpNew)
os.system("sudo a2enmod php" + phpNew)

print("Devifindo Atralho do PHP")
os.system("sudo update-alternatives --set php /usr/bin/php" + phpNew)

print("Reiniciando o Apache")
os.system("sudo systemctl restart apache2")

print("Carregando arquivo de Configuração do PHP")
os.system("php -i | grep \"Loaded Configuration File\"")

print
print
print

print(os.system("php -v"))