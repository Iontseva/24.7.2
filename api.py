import requests

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email:str, password:str) ->tuple:
        """Метод делает запрос к API сервера и возвращает стратус запроса и результат в формате
        JSON с уникальным ключом пользователя, найденного по указанным email и паролем"""
        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'api/key', headers = headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status,result

    def get_list_of_pets(self, auth_key: str, filter: str = "") -> tuple:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
         со списком найденных питомцев, совпадающих с фильтром. На данный момент фильтр пожет иметь
        либо пустое занмчение - получить список всех питомцев, либо 'my_pets - получить
        список собственных питомцев"""
        headers = {'auth_key' : auth_key}
        filter = {'filter' : filter}
        res = requests.get(self.base_url + 'api/pets', headers = headers, params = filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_add_information_about_new_pet(self,auth_key:str, name: str, animal_type: str, age: int, pet_photo:str) -> tuple:
        """Метод делает запрос к API сервера, добавляет на сервер информацию о новом питомце и возвращает статус
        запроса и результат в формате JSON с параметрами добавленного животного"""
        data = {
            'name': name,
            'animal_type': animal_type,
            "age": age
        }
        headers = {'auth_key' : auth_key}
        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}
        res = requests.post(self.base_url+'api/pets', headers = headers, data = data, files = file)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delete_pet_from_database(self, auth_key:str, pet_id: str) -> str:
        """Метод делает запрос к API сервера, удаляет данные по ID животного и возвращает статус запроса"""
        headers = {'auth_key' : auth_key}
        res = requests.delete(self.base_url+'api/pets/'+pet_id['id'], headers = headers)
        status = res.status_code
        return status

    def update_information_about_pet(self, auth_key:str, pet_id: str, name: str, animal_type: str, age: int) ->tuple:
        """Метод делает запрос к Api сервера, изменяет данные по ID животного и ввозвращает статус
        запроса и результат в формате JSON с параметрами измененного животного"""
        data = {
            'name': name,
            'animal_type': animal_type,
            "age": age
        }
        headers = {'auth_key' : auth_key}
        res = requests.put(self.base_url+'api/pets/'+pet_id['id'], headers = headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_information_about_new_pet_without_photo(self, auth_key:str, name:str, animal_type: str, age: int) -> tuple:
        """Метод делает запрос к API сервера, добавляет на сервер информацию о новом питомце без приложения фото
        и возвращает статус запроса и результат в формате JSON с параметрами добавленного животного"""
        data = {
            'name': name,
            'animal_type': animal_type,
            "age": age
        }
        headers = {'auth_key' : auth_key}
        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_photo_of_pet(self, auth_key:str, pet_id:str, pet_photo:str) ->tuple:
        """Метод делает запрос к Api сервера, добавляет фотографиюпо ID животного и ввозвращает статус
                запроса и результат в формате JSON с параметрами измененного животного"""
        headers = {'auth_key' : auth_key}
        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}
        res = requests.post(self.base_url+'/api/pets/set_photo/'+pet_id['id'], headers=headers, files=file)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
