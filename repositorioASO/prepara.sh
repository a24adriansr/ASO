#!/bin/bash

#Descargamos archivo pdf
wget -P /tmp https://www.debian.org/doc/manuals/debian-reference/debian-reference.es.pdf
#Damos de alta los grupos
groupadd asir
groupadd daw
groupadd proxecto1
groupadd proxecto2
groupadd proxecto3
groupadd proxecto4

#Damos de alta los usuarios
useradd -d /home/lara -m -g asir -G proxecto1,proxecto2 -s /bin/bash lara
useradd -d /home/sara -m -g asir -G proxecto1,proxecto2 -s /bin/bash sara
useradd -d /home/clara -m -g asir -G proxecto1,proxecto2,proxecto3 -s /bin/bash clara
useradd -d /home/pepe -m -g asir -G proxecto1,proxecto2,proxecto3 -s /bin/bash pepe
useradd -d /home/maria -m -g asir -G proxecto1,proxecto2,proxecto3 -s /bin/bash maria
useradd -d /home/fabricioBRASIL -m -g asir -G proxecto1,proxecto2,proxecto3 -s /bin/bash fabricioBRASIL
cp /tmp/debian-reference.es.pdf /home/clara/
useradd -d /home/juan -m -g daw -G proxecto3,proxecto4 -s /bin/bash juan
useradd -d /home/tino -m -g daw -G proxecto3 -s /bin/bash tino
useradd -d /home/carlos -m -g daw -s /bin/bash carlos
useradd -d /home/nemo -m -g daw -s /bin/bash nemo
useradd -d /home/dorito -m -g daw -s /bin/bash dorito
cp /tmp/debian-reference.es.pdf /home/carlos/