## FASTIRC

Es un proyecto "UNIX" que permite extraer valores de energía versus coordenada de reacción desde uno dos archivo(s) de salida generado(s) por el programa Gaussian 16 y a pedido opcional del usuario, extraer datos de posición en coordenadas cartesianas de átomos que provienen de dicho cálculo
## Requerimientos

Requiere python 3.

## Installation

Descarga el proyecto desde Github usando la opción zip o git clone. Mueve el proyecto FASTIRC a una carpeta en tu computador. 

Descomprime el archivo zip mediante consola o usando las herramientas del sistema operativo (click derecho descomprimir)
```
$unzip fastirc.zip
```
También puedes crear un alias en $ .bashrc. (en MAC OS se llama "bash_profile") Utiliza un editor de texto (vi, vim, nano u otro)
```
$ nano ~.bashrc
```
Y agrega esta ultima linea: 
```
alias fastirc='python /home/user/fastirc/fastirc.py'
```
la ruta es donde esta guardado el proyecto en tu computadora

## Ejecución
Debes tener los 3 archivos .log (proyecto FASTIRC), luego ejecutar el programa mediante el comando python

Antes de invocar el codigo fastirc, procure nombrar sus archivos con la terminacion _irc.log en el caso que haya realizado un calculo de coordenada de reacción intrínseca (IRC) único en el programa Gaussian.

Por ejemplo, si tiene un archivo de salida proveniente de un calculo IRC llamado reaccion.log, cambie su nombre a reaccion_irc.log o reaccion-irc.log

Puede también emplear letras mayúsculas: reaccion_IRC.log o reaccion-IRC.log

Pero nunca mezcle mayúsculas con minúsculas: reaccion-Irc.log

Si el calculo IRC lo realizó de manera seccionada, esto es en dos partes, considerando una rama de retroceso (uso de comando reverse en el calculo IRC) y un rama de avance (uso del comando forward en el calculo IRC), asegurese que ambos archivos de salida terminen en _irc-r.log e _irc-f.log


Pero nunca separe la sigla irc de la letra r o f con guion bajo ya que fastirc no reconocerá esos archivos: por ejemplo archivos como proceso-irc_r.log o cambio-quimico-irc_f.log no serán leídos, pero sí serán leídos  proceso-irc-r.log o cambio-quimico-irc-f.log o proceso_irc-r.log o cambio-quimico-irc-f.log


Versión Gráfica:
```
$ python /home/user/fastirc/fastirc.py'
```
Version Linea de Comandos:
```
$ python /home/user/fastirc/fastirc.py' more
```
o simplemente usado el alias fastirc:

Versión Gráfica:
```
$ fastirc
```
![](https://webdesign.s3-us-west-2.amazonaws.com/fastirc/fastirc.png)

Version Linea de Comandos:
```
$ fastirc more
```
![](https://webdesign.s3-us-west-2.amazonaws.com/fastirc/fastircmore.png)
