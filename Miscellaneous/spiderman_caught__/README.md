This CTF contains data inside the image,web exploitation methods and cryptography

motive: this CTF provides the user to know about steghide tool and also encourage about web exploration, also bring a know of encryption about base 91

BEFORE YOU START YOU MUST READ THE MESSAGE GIVEN

##Source
- [Spiderman.zip](./spiderman.zip)

Write-up(COMMANDS TO BE USED):-

->  file *
 
 -> unzip spiderman.zip
 
 -> ls -lart
 
 -> file *
 
 -> mv archive.zip archive.tar
 
 -> tar -xvf archive.tar
 
 -> ls -lart
 
 -> file *
 
 -> mv .search search
 
 -> ls -lart
 
 -> file *
 
 -> cat search
 
 -> cat secret.txt

// after reading copy the encrypted text and decrypt it using base 91

// you will get the password for steghide tool --> marryjenson

-> steghide --extract -sf spiderman.jpeg -xf text.txt

// enter the password 

-> ls

-> cat text.txt

after this you will get the url which will take you mine web page where you will have to dive deep
 means you will have to check HTML CSS and JS
 
 you can also download the html file and use cat CTF.html | grep CTF
	
  when you go in css you will find the flag:
  
  CTF{TH1S_I5_S0METH1NG_W3BBY}
	
