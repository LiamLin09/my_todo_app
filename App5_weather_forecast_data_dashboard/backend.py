import requests

APIkey = 'f73a3a8c87ac41c9244e886e3f602b33'


def get_data(place, forecast_days=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == '__main__':
    print(get_data(place='Boston', forecast_days=3))