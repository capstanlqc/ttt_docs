---
tags:
  - Audience꞉Tech
---

# Creating a signed OmegaT installer

## Getting started

The following working environment is recommended:

1. A Linux machine (recommended Debian-based) that runs `systemctl`.
	
	> A virtual machine or WSL could be a valid substitute. This guide is based on building on MX Linux (Linux 5.10.0-22-amd64) and `apt` is used for package installation commands.

2. Install dependencies:
    ```
    $ sudo apt install libxrender1 libxtst6 libxi6 libfreetype6 fontconfig \
	gnutls-bin p11tool software-properties-common softhsm2 \
	libengine-pkcs11-openssl osslsigncode icedtea-netx pcsclite pcsc-tools \
	pcscd procertum-cardreader gh
    ```

3. Install docker:
    ```
    $ sudo apt install docker
    ```
4. Adjust the group membership of your user, so that you can run docker images:
    ```
    $ sudo groupadd docker
    $ sudo usermod -aG docker $USER # or: sudo groupadd docker
    ```
5. Restart or log out.

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
### Setting up Java and Gradle

> There are other ways to do this, what follows is just our recommended approach.

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

### Activating the certificate

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

### Windows installation wizard

A few tweaks were done in the [innosetup file](https://github.com/capstanlqc/omegat/commits/69e87fb6e1bdce3a4fdd4fca3c0b0e716288e4c2/release/win32-specific/OmegaT.iss) to customize the installation wizard on Windows machines. 

> These changes are permanent and don't need to be applied again (this section is just for the record).

- [OmegaT is set to install in English in all cases (user can only choose the setup language)](https://github.com/capstanlqc/omegat/commit/46ba9e9e45f15f0a7917ce88ed8e80b6789eae52)

- [It has the Create Desktop icon option turned on by default](https://github.com/capstanlqc/omegat/commit/46ba9e9e45f15f0a7917ce88ed8e80b6789eae52)

- [Changed location where desktop shortcut icon must be created](https://github.com/capstanlqc/omegat/commit/4996974dfdd25a014cddef3189863dbc01b95beb) (so that it's instsalled for the current user only)

- [Removed the need for elevated permissions to install](https://github.com/capstanlqc/omegat/commit/50b70816b4070eaab478000ac59069d130030c9b)

One important implication is that the installation path has been modified to use `C:\Users\USER\AppData\Local\Programs\OmegaT\OmegaT.exe` by default.


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
	$ gh repo clone capstanlqc/omegat
	```
4. Change directory to the `omegat` folder:
	```
	$ cd omegat
	```
5. Check out the `main-capstan` branch:
	```
	$ git checkout main-capstan
	```
6. Create your `local.properties` file:
	```
	$ cp local.properties.example local.properties
	```
7. Add your certificate details to the `local.properties` file:
	```
	pkcs11module=/usr/lib64/crypto3PKCS/sc30pkcs11-3.0.6.68-MS.so
	winCodesignPassword=**** # your PIN number
	winCodesignCert=/path/to/omegat-installer/cert/be737b17c8d3f3f0d7bbfae716b0ee1a.cer
	```
Defining `pkcs11cert` and `winCodesignTimestampUrl` is not necessary.

8. Kindly ask Gradle to build OmegaT from source and bundle it with the JRE you downloaded into a Windows setup package:
	```
	$ ./gradlew winJRE64Signed
	``` 
> The above command would be `./gradlew winJRE64` without code signing.

> The above command would be `./gradlew macDistZip` to create a mac installer (see short [howto](https://gist.github.com/msoutopico/6717f6608e90d2c9fca86d3b5970aa43)) 
<!-- original https://gist.github.com/kosivantsov/03321b29a8a2be242221e12572885079 -->

### Result

If the process works, the installer will be saved in folder `./build/distributions`, e.g.
	```
	$ cd /path/to/omegat-installer/omegat
	$ find . -name "*.exe"
	./build/distributions/OmegaT_5.7.3_Windows_64_Signed.exe
	```

### Signing the executable on Windows (alternative approach)

If for any reason the signing could not be done during building, it's also possible to sign the Windows executable after creating it. In that case, you could skip section **Activating the certificate** above and steps 1, 6 and 7 in section **Getting down to building**.

Also, step 8 in section **Getting down to building** would be simply:
```
$ ./gradlew winJRE64
```

Following steps: 

1. Install the certificate in the smartcard on Windows:
	
	- open the card in the proCertum CardManager application and go to the Common profile
	- open the certificate
	- click on Install

	> It's not clear the first step is a mandatory step, but just in case.

2. Download one of the Windows SDK's (e.g. the Windows 11 one from the Visual Studio Installer): you need just one single executable called `signtool.exe`.

3. Sign the executable, e.g. `OmegaT_5.7.3_Windows_64.exe`, with SHA1 timestamp:
	```
	signtool.exe sign /n "cApStAn" /t http://time.certum.pl/ /fd sha1 /v OmegaT_5.7.3_Windows_64.exe
	```
4. Sign the same executable now with SHA2 timestamp as well (dual signing - seems to be a requirement):
	```
	signtool.exe sign /n "cApStAn" /tr http://time.certum.pl/ /td sha256 /fd sha256 /as /v OmegaT_5.7.3_Windows_64.exe
	```
Notes:

* `OmegaT_5.7.3_Windows_64.exe` is both the input file and the output file, so if you'd like to keep an unsigned version, make a copy first.
* "cApStAn" is the name of the certificate.


## References

- [OmegaT 4.3.1 - User's Guide > Building OmegaT From Source](https://omegat.sourceforge.io/manual-latest/en/chapter.installing.and.running.html#building.OmegaT.from.source)
- [OmegaT 6.0.0 - User Manual > Build OmegaT](https://omegat.sourceforge.io/manual-standard/en/chapter.how.to.html)
- [omegat-org > omegat > docs_devel > Building OmegaT](https://github.com/omegat-org/omegat/blob/master/docs_devel/docs/02.HowToBuild.md)
- [omegat-org > omegat > docs_devel > Building and testing the installer package](https://github.com/omegat-org/omegat/blob/master/docs_devel/docs/93.BuildingInstallerPackage.md)
- [Open Source Code Signing - set](https://shop.certum.eu/open-source-code-signing.html)
- [omegat-org > omegat > docs_devel > Code signing how-to](https://github.com/omegat-org/omegat/blob/master/docs_devel/docs/92.CodeSigning.md)
- [amake/innosetup-docker](https://github.com/amake/innosetup-docker)

<!-- source: https://rentry.org/build_omegat_jre11_win64 -->