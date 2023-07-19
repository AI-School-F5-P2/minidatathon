import requests
import pandas as pd

def fetch_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al hacer la solicitud. Código de estado: {response.status_code}")
        return None

def save_data_to_csv(data, file_path):
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    api_url = " https://api.covidtracking.com/v1/states/daily.json" 
    data = fetch_data_from_api(api_url)

    if data:
        csv_file = "covid_data.csv"  # Nombre del archivo CSV que se creará
        save_data_to_csv(data, csv_file)
        print(f"Datos guardados correctamente en {csv_file}")