<h1 align="center">
  <br>
  <a href="https://github.com/gsvprharsha/Br0ther_Ey3"><img src="https://github.com/gsvprharsha/Br0ther_Ey3/blob/main/imgs/Br0ther_Ey3.png" alt="Br0ther Ey3"></a>
  <br>
  Br0ther Ey3
  <br>
</h1>


<h3 align="center">Social Media Discover Tool</h3>

<p align="center">
  <img alt="Maintained" src="https://img.shields.io/maintenance/yes/2022?style=for-the-badge">
  <img alt="Languages" src="https://img.shields.io/github/languages/count/gsvprharsha/Br0ther_Ey3?style=for-the-badge">
  <img alt="Repo Size" src="https://img.shields.io/github/repo-size/gsvprharsha/Br0ther_Ey3?style=for-the-badge">
  <img alt="License" src="https://img.shields.io/github/license/gsvprharsha/Hunter-Framework?color=light&style=for-the-badge">
</p>

![demo](https://github.com/gsvprharsha/Br0ther_Ey3/blob/main/imgs/terminal.png)

## What is Br0ther Ey3?

Br0ther Ey3 is an open-source OSINT tool, that can be used to check for an individual's account on some of the most popular **Social Media websites** on the internet. It uses status codes to determine whether there is an account with the username that is provided to it; on the website.  

## Fun Fact
Most users on the internet use the **same username** for all their social medias. Including Me :)


## Tested On
<p align="center">
  <img alt="Kali Linux" src="https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kali-linux&logoColor=white">
  <img alt="Debian" src="https://img.shields.io/badge/Debian-A81D33?style=for-the-badge&logo=debian&logoColor=white">
  <img alt="Ubuntu" src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white">
  <img alt="Arch Linux" src="https://img.shields.io/badge/Arch_Linux-1793D1?style=for-the-badge&logo=arch-linux&logoColor=white">
</p>

## Setup
Setting up **Br0ther Ey3** is very simple. You can use it directly from the directory **or** use the `setup.sh` program to install it in such a way that you can access it from anywhere in the system.

<li>Clone this repository</li>

```
git clone https://github.com/gsvprharsha/Br0ther_Ey3.git
```

<li>Make the setup.sh an executable using the following command</li>

```
chmod +x setup.sh
```

<li>Execute the setup.sh as root</li>

```
sudo ./setup.sh
```

**Note: The file will not allow you to execute it if you run it as a normal user.**

Congratulations !!!,Br0ther Ey3 is installed successfully; type `sudo broeye` or `broeye` to start using it</li> 

## Usage
To use Br0ther Ey3, execute the following command in your terminal. Just replace `<username>` with the username of your choice.
```
broeye -u <username>
```
If you are using it directly from the directory without installing it with `setup.sh` then, you can use the following command to continue using Br0ther Ey3.
```
python3 broeye -u <username>
```
## Optional Arguments 
```
usage: broeye.py [-h] --username USERNAME [--T10] [--t T] [--fbset] [--tiktok] [--tiktok_with_profile_pic]

Br0ther Ey3 OSINT Tool v0.0.2

optional arguments:
  -h, --help            show this help message and exit
  --username USERNAME   Profile Username
  --T10                 Scans only Top 10 websites from list
  --t T                 Take custom number of lists
  --fbset               Scans the websites owned by Facebook
  --tiktok, --tt        Gather information only on tiktok only
  --tiktok_with_profile_pic, --ttwp
                        Tiktok OSINT that also collects the user's profile picture

Embrace The Data :)
```

## Notice
This tool is for educational and ethical practices only. The developers are not responsible if the tool is misused by an individual.

## To Contributors
Thank you so much for considering to contribute to the Project. Place a pull request and it will be merged into the main branch of this repository once testing is done.
