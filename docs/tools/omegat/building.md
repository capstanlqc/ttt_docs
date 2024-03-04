---
tags:
  - Audience꞉Tech
---

I would like to mention that we now have the possibility to create our own (cApStAn's) installer of OmegaT 6.1.0, if we need to. Kudos to Adrien and Gergely for all their help! 



That means that if needed we could (as a very exceptional case if case of emergency) add features to our own installer which for any reason are not being included (in time or at all) in the official installer. 

Ideally we should avoid having an independent fork that is not aligned with the official codebase, that would lead to maintenance issues sooner or later. 

well, and there are other inconvenients, like the installer not knowing what is the user's home folder, so custom config files will have to be included in the installation folder, which the problems that this entails if a 







# Creating a signed OmegaT installer

## Getting started

The following working environment is recommended:

1. A Linux machine (recommended Debian-based) that runs `systemctl`.
	> A virtual machine or WSL could be a valid substitute. This guide is based on building on MX Linux (Linux 5.10.0-22-amd64) and `apt` is used for package installation commands.
3. Install dependencies:
    ```
    $ sudo apt install libxrender1 libxtst6 libxi6 libfreetype6 fontconfig gnutls-bin p11tool software-properties-common softhsm2 libengine-pkcs11-openssl osslsigncode icedtea-netx pcsclite pcsc-tools pcscd procertum-cardreader gh
    ```
4. Install docker:
    ```
    $ sudo apt install docker
    ```
3. Adjust the group membership of your user, so that you can run docker images:
    ```
    $ sudo groupadd docker
    $ sudo usermod -aG docker $USER # or: sudo groupadd docker
    ```
4. Restart or log out.

## Before building

### Setting up docker
Follow these steps: 

1. Make sure that `docker` is in your groups:
    ```
    $ groups
    sys wheel rfkill autologin souto foo bar docker
    ```
2. Start docker:
	```
	$ systemctl start docker
	```
3. Check if `docker` works:
	```
	$ docker run hello-world
	```
7.	Create a folder for the building process:
	```
	$ mkdir -p /path/to/omegat-installer
	```

### Setting up Java
> There are other ways to do this, what follows is what I use and my recommended approach.

1. Install sdkman (as explained [here](https://sdkman.io/install)):
	```
	$ curl -s "https://get.sdkman.io" | bash
	$ source "$HOME/.sdkman/bin/sdkman-init.sh"
	```
2. Select the Java version that you need, i.e. `17.0.4-tem` (recommended: make it your default version)
	```
	$ sdk use java 17.0.4-tem
	```
3. Confirm that you have the expected java version:
	```
	$ java -version
	openjdk version "11.0.19" 2023-04-18
	OpenJDK Runtime Environment Temurin-11.0.19+7 (build 11.0.19+7)
	OpenJDK 64-Bit Server VM Temurin-11.0.19+7 (build 11.0.19+7, mixed mode)
	```	
8. Download the zipped JRE bundle for the same version (file called `OpenJDK11U-jre_x64_windows_hotspot_11.0.19_7.zip`) from https://adoptium.net/ for the following criteria:
	- Operating system: Windows
	- Architecture: x64
	- Package type: JRE
	- Version: 11 - LTS
9. Move the zipped JRE bundle to your building folder:
	```
	$ mv ~/Downloads/OpenJDK11U-jre_x64_windows_hotspot_11.0.19_7.zip /path/to/omegat-installer/
	```

### Activate the certificate
The steps in this section only need to be done once. If that has already been done and you already have a valid binary file of the certificate (the file with `.cer` extension) which hasn't expired, you can skip to the next section.

Using Certum certificate, go through the procedure to activate the certificate. Through that process, you will have to define a PIN number for the common profile that is used to access the Certum's cryptographic smart card.

You'll have to run two tools for that: 

- the SmartCard Reader (which you have already installed as a dependency)
	```
	$ cd /opt/proCertumCardManager
	$ proCertumCardManager
	```
-  and a Crypto tool (which the Certum page will ask you download):
	```
	$ javaws CertumCryptoAgent_en.jnlp
	```
At the end of the process when the certificate is activated and available for download, download the binary certificate (with a `.cer` extension) from the Certum page. 

## Getting down to building
Ok, let's build the installer.

1. Move the certificate file to your building folder : 
	```
	$ mkdir /path/to/omegat-installer/cert/
	$ mv ~/Downloads/be737b17c8d3f3f0d7bbfae716b0ee1a.cer /path/to/omegat-installer/cert/
	```
2. Change directory to your building folder: 
	```
	$ cd /path/to/omegat-installer/
	```
3. Clone the OmegaT source code repository:
	```
	$ gh repo clone omegat-org/omegat
	```
4. Change directory to the `omegat` folder:

	```
	$ cd omegat
	```
	Check out any specific branch if the main/master branch is not what you want to use.
	
5. Create your `local.properties` file:

	```
	$ cp local.properties.example local.properties
	```
6. Add your certificate details to the `local.properties` file:
	```
	pkcs11module=/usr/lib64/crypto3PKCS/sc30pkcs11-3.0.6.68-MS.so
	winCodesignPassword=**** # your PIN number
	winCodesignCert=/path/to/omegat-installer/cert/be737b17c8d3f3f0d7bbfae716b0ee1a.cer
	```
Defining `pkcs11cert` and `winCodesignTimestampUrl` is not necessary.

7. Kindly ask Gradle to build OmegaT from source and bundle it with the JRE you downloaded into a Windows setup package:
	```
	$ ./gradlew winJRE64Signed
	```
     
### Result
If the process works, the installer will be saved in folder `./build/distributions`:
	```
	$ cd /path/to/omegat-installer/omegat
	$ find . -name "*.exe"
	./build/distributions/OmegaT_6.1.0_Beta_Windows_64_Signed.exe
	```
### References
- https://omegat.sourceforge.io/manual-standard/en/chapter.installing.and.running.html#building.OmegaT.from.source
- https://github.com/omegat-org/omegat/tree/master/docs_devel
- https://github.com/omegat-org/omegat/blob/master/docs_devel/docs/93.BuildingInstallerPackage.md
- https://shop.certum.eu/open-source-code-signing.html
- https://github.com/omegat-org/omegat/blob/master/docs_devel/docs/92.CodeSigning.md
- https://github.com/amake/innosetup-docker

<!-- source: https://rentry.org/build_omegat_jre11_win64 -->