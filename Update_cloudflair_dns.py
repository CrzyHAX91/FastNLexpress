import requests

# Cloudflare API credentials
CLOUDFLARE_API_KEY = 'xBJKtjL-XnBE0T5B1ue5Ut-GDSPXoKDUU-UnNLSe'
CLOUDFLARE_EMAIL = 'your_email@example.com'  # Replace with your Cloudflare account email
ZONE_ID = 'your_zone_id'  # Replace with your Cloudflare zone ID
RECORD_ID = 'your_record_id'  # Replace with the DNS record ID you want to update

# AWS EC2 IP address
AWS_EC2_IP = '35.176.181.233'

def update_dns_record():
    url = f'https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{RECORD_ID}'
    headers = {
        'Authorization': f'Bearer {CLOUDFLARE_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'type': 'A',
        'name': 'your_domain.com',  # Replace with your domain
        'content': AWS_EC2_IP,
        'ttl': 1,
        'proxied': False
    }
    
    response = requests.put(url, headers=headers, json=data)
    if response.status_code == 200:
        print('DNS record updated successfully.')
    else:
        print('Failed to update DNS record:', response.json())

if __name__ == '__main__':
    update_dns_record()
