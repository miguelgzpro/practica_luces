Luces encendidas o apagadas
Como primer paso debera clonar el repositorio con el siguiente comando y linea del git ( si no tienes instalado git deberas poner sudo apt-get install git)
git clone https://github.com/miguelgzpro/practica_luces.git

Debera instalar los siguientes puntos desde la consola de ubuntu
 sudo apt-get install mosquitto mosquitto-clients
 sudo apt-get install python3 python3-pip

Debes comprobar que mosquito este activado
systemctl status mosquitto

Para ejecutarlo de manera correcta deberas ejecutar primero el archivo sensor.py
recomendable abrir una nueva terminal en la carpeta donde esta el proyecto y poner:
python3 sensor.py

Luego desde otra terminal que debera estar en la carpeta de proyecto poner:
python3 switch.py

Una vez hecho eso veras como se imprimen mensajes dependiendo el json devuelto que pueden ser
Luces apagadas o encendidas
