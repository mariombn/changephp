Change PHP Version for Ubuntu
=============================

This script aims to facilitate the exchange of PHP versions.

Once you have more than one version of php installed in your environment, you can use this command to switch the active version with Apache.

To run it is enough to clone this repository with the command:
```
git clone https://github.com/mariombn/changephp.git changephp
cd changephp
sudo chmod +x changephp.py
```

And to make the PHP version change, use the command:
```
./changephp.py <phpversion>
```

Like example:
```
./changephp.py 5.6
```
