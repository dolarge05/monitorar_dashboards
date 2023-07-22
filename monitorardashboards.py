import requests
import time

def medir_tempo_carregamento_dashboard(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        if response.status_code == 200:
            tempo_carregamento = end_time - start_time
            print(f"Tempo de carregamento do dashboard {url}: {tempo_carregamento:.2f} segundos")
        else:
            print(f"Erro ao acessar o dashboard {url}. Código de status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o dashboard {url}: {e}")

if __name__ == "__main__":
    dashboard1_url = "https://exemplo.com/dashboard1"
    dashboard2_url = "https://exemplo.com/dashboard2"

    medir_tempo_carregamento_dashboard(dashboard1_url)
    medir_tempo_carregamento_dashboard(dashboard2_url)