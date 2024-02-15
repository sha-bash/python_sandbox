import requests


class VK:


    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()


access_token = 'vk1.a.5WK6GOMYP7KKivlFIO8uQLzgZ3Iq1ih_xw7o4wwuuy5FbRNgkPXQcKiRB3qmiJYTnGclKgEBXYwHWHBy-aKV7QX-znIQJmM11q0amlaYTokhH4loziWPVuGp23kVA7PTMTtN7eZTllAZ5GuNbgoLyw59kPsZqs6FphPhTMYEqIPKddYfUgARVIfS0EPcgGLPFxTV7XxriXWsot8DHFhB_g'
user_id = 'filatkova_olga'
vk = VK(access_token, user_id)

print(vk.users_info())

