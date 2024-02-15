import requests

access_token = '*****'


class VKAPIClient:
    # https://<адрес-сервера>/method/<имя-API-метода>?<параметры>
    API_BASE_URL = 'https://api.vk.com/method/'
    
    def __init__(self, token, user_id):       
        self.token = token
        self.user_id = user_id
        
    def get_common_params(self):
        return {
           'access_token': self.token,
           'v': '5.131' 
        }
    
    def _build_status(self, api_methot):
        return f'{self.API_BASE_URL}/{api_methot}'
        
    def get_status(self):
        params = self.get_common_params()
        params.update({'user_id': self.user_id})
        response = requests.get(self._build_status('status.get'), params=params)
        return response.json().get('response', {}).get('text')
    
    def set_status(self, new_status):
        params = self.get_common_params()
        params.update({'user_id': self.user_id, 'text': new_status})
        response = requests.get(self._build_status('status.set'), params=params)
        response.raise_for_status()

    def replace_status(self, target, replace_string):
        status = self.get_status()
        if status is not None:
            new_status = status.replace(target, replace_string)
            self.set_status(new_status)
        
    def get_profile_photos(self):
        params = self.get_common_params()
        params.update({'owner_id':self.user_id, 'album_id': 'profile'})
        response = requests.get(self._build_status('photos.get'), params=params)
        return response.json()

if __name__ == '__main__':
    vk_client = VKAPIClient(access_token, 261235804)
    #print(vk_client.get_status())
    #vk_client.replace_status('test', 'ТЕСТ API_VK')
    print(vk_client.get_profile_photos())