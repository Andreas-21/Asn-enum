import sys
import requests

if len(sys.argv) < 2:
    print("Usage: python3 asn_domains.py <ASN>")
    sys.exit(1)

asn = sys.argv[1]
url = f"https://otx.alienvault.com/api/v1/indicators/ASN/{asn}/passive_dns"

print(f"Fetching domains for ASN: {asn}...")
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if "passive_dns" in data:
        domains = set(entry["hostname"] for entry in data["passive_dns"] if "hostname" in entry)
        if domains:
            print("\n[+] Associated Domains:")
            for domain in sorted(domains):
                print(domain)
        else:
            print("[-] No domains found for this ASN.")
    else:
        print("[-] No data found.")
else:
    print(f"[-] Failed to fetch data (Status Code: {response.status_code})")
