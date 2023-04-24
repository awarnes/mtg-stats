import requests

class ScryFall():
    BASE_URL: str = ''

    def __init__(self):
        pass

    def get_illustration(self, illustration_id):
        response = requests.get(f"{self.BASE_URL}/{illustration_id}")
        if not response.error:
            return response
        print(f"Error: {response.error}")

