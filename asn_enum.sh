#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: ./asn_enum.sh <domain>"
    exit 1
fi

DOMAIN=$1
echo "[+] Resolving IP for $DOMAIN..."
IP=$(dig +short $DOMAIN | head -n 1)

if [ -z "$IP" ]; then
    echo "[-] Unable to resolve IP!"
    exit 1
fi

echo "[+] Found IP: $IP"

ASN=$(curl -s "https://ipinfo.io/$IP/json" | jq -r '.org' | awk '{print $1}')

if [ "$ASN" == "null" ]; then
    echo "[-] ASN not found!"
    exit 1
fi

echo "[+] ASN Number: $ASN"
echo "[+] Fetching domains for ASN $ASN..."
python3 asn_domains.py $ASN
