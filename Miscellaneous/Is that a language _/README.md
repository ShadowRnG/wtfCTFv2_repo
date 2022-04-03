This CTF is Combination of forensic and cryptography concept.
This CTF also contains confusing extensions for the name of files and photos which must be studied before opening

MOTIVE: The motive of this CTF is to provide user with the extension identification and extravtion processes.This CTF also provide user to get to know about steghide tool(how can we store data in image file) and atlast about OK! encryption.

##SOource

-[lang.tar](./lang.tar) 

WRITEUP COMMANDS TO FOLLOW:-

 -> file *
 
 ->mv lang.tar lang.zip
 
 -> unzip lang.zip
 
 -> file *
 
 -> tar -xvf lang.tar
 
 -> file *
 
 -> mv car.pcap doggstyle.jpeg
 
 -> steghide --extract -sf car.jpeg -xf secret.txt
 
 -> cat secret.txt
 // Now copy the data of the file and open decode.fr where you will search for Ook! and get the Ook type of encryption paste the data there and decrypt
 you will get the flag
	
 	wtfCTF{D0_Y0U_KN0W_AB0U7_E50LAN6_LANGU4G3}

 
