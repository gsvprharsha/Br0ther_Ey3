#!/bin/bash

GREEN='\033[0;32m'
PURPLE='\033[1;35m'
NC='\033[0m'


if [ "$EUID" -ne 0 ]
  then echo " "
  echo -e "${RED}[-] Please run as root${NC}"
  echo " "
  exit
else

echo " "
echo -e "${GREEN}[+] Installing Dependencies for ${NC}${PURPLE}Br0ther_Ey3${NC}"
echo " "
pip3 install requests
echo " "
pip3 install termcolor
echo " "
echo -e "${PURPLE}[+] Br0ther_Ey3 Successfully Installed${NC}"

fi
