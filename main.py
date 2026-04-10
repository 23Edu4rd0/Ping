import logging
import requests 
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

WEBSITE_URL = 'https://formulario-oi3p.onrender.com/'
BREAK = 60 * 14 # 14 minutes, substitute fourteen for the number of minutes that you desire

def ping():
    try:
        response = requests.get(WEBSITE_URL, timeout=10)
        logging.info(f'Ping ok - status code: {response.status_code}')
    except Exception as e:
        logging.error(f'Ping error: {e}')


if __name__ == "__main__":
    logging.info('Initializing keep-alive')
    while True:
        ping()
        time.sleep(BREAK)
