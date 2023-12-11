from api import PetFriends
from settings import *

pf = PetFriends()

def test_get_apy_key_for_valid_user(email=valid_email, password=valid_password):
    """Позитивный тест на запрос ключа"""
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_api_pets_with_valid_key(filter = ''):
    """Позитивный тест на запрос питомцев с валидным ключом без установки фильтра"""
    _, auth_key = pf.get_api_key(valid_email,valid_password)
    status,result = pf.get_list_of_pets(auth_key['key'], filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_post_add_information_about_new_pet_with_valid_key(name = name, animal_type = animal_type, age = age, pet_photo = pet_photo):
    """Позитивный тест на добавление нового питома с фото с валидным ключом и корректными данными по питомцу"""
    _, auth_key = pf.get_api_key(valid_email,valid_password)
    status, result = pf.post_add_information_about_new_pet(auth_key['key'], name, animal_type, age, pet_photo)
    assert status == 200
    assert 'id' in result

def test_delete_pet_from_database_with_valid_key():
    """Позитивный тест на удаление питомца с валидным ключом и валидныи ID"""
    _, auth_key = pf.get_api_key(valid_email,valid_password)
    _, pet_id = pf.post_add_information_about_new_pet(auth_key['key'], name, animal_type, age,pet_photo)
    _, get = pf.get_list_of_pets(auth_key['key'], "my_pets")
    status = pf.delete_pet_from_database(auth_key['key'],pet_id)
    assert status == 200
    assert pet_id['id'] not in get

def test_update_name_about_pet_with_valid_key(name ='', animal_type = '', age = ''):
    """Позитивный тест на изменение информации об имени питомце с валидным ключом и валидным ID"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pet_id = pf.post_add_information_about_new_pet(auth_key['key'], name, animal_type, age, pet_photo)
    status, result = pf.update_information_about_pet(auth_key['key'], pet_id, name1, animal_type, age)
    assert status == 200
    assert result['name'] == name1

def test_update_animal_type_about_pet_with_valid_key(name ='', animal_type = '', age = ''):
    """Позитивный тест на изменение информации о типе питомце с валидным ключом и валидным ID"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pet_id = pf.post_add_information_about_new_pet(auth_key['key'], name, animal_type, age, pet_photo)
    status, result = pf.update_information_about_pet(auth_key['key'], pet_id, name, animal_type1, age)
    assert status == 200
    assert result['animal_type'] == animal_type1

def test_add_information_about_new_pet_without_photo_with_valid_key(name = name, animal_type = animal_type, age = age):
    """Позитивный тест на добавление нового питомца без фото с валидным ключом"""
    _, auth_key = pf.get_api_key(valid_email,valid_password)
    status, result = pf.add_information_about_new_pet_without_photo(auth_key['key'], name, animal_type, age)
    assert status == 200
    assert 'id' in result

def test_add_photo_of_pet_with_valid_key(pet_photo = pet_photo):
    """Позитивный тест на добавление фото для ранее созданного питомца с валидным ключом и валидным ID"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pet_id = pf.add_information_about_new_pet_without_photo(auth_key['key'], name, animal_type, age)
    status, result = pf.add_photo_of_pet(auth_key['key'], pet_id, pet_photo)
    assert status == 200
    assert 'pet_photo' in result

def test_get_apy_key_for_incorrect_email(email=invalid_email, password=valid_password):
    """Негативный тест на запрос ключа - некорректный email"""
    status, _ = pf.get_api_key(email, password)
    assert status == 403

def test_get_apy_key_for_incorrect_email(email=valid_email, password=invalid_password):
    """Негативный тест на запрос ключа - некорректный пароль"""
    status, _ = pf.get_api_key(email, password)
    assert status == 403

def test_get_api_pets_with_invalid_key(filter = ''):
    """Негативный тест на запрос питомцев с невалидным ключом без установки фильтра"""
    status,_ = pf.get_list_of_pets(invalid_key, filter)
    assert status == 403


def test_post_add_information_about_new_pet_with_invalid_key(name = name, animal_type = animal_type, age = age, pet_photo = pet_photo):
    """Негативный тест на добавление нового питомца с фото с невалидным ключом и корректным данными по питомцу"""
    status, _ = pf.post_add_information_about_new_pet(invalid_key, name, animal_type, age, pet_photo)
    assert status == 403

def test_post_add_information_about_new_pet_with_name_is_incorrect(name = incorrect_name1, animal_type = animal_type, age = age, pet_photo = pet_photo):
    """Негативный тест на добавление нового питомца с фото с валидным ключом и некорректным именем(имя - пробел)"""
    _, auth_key = pf.get_api_key(valid_email,valid_password)
    status, _ = pf.post_add_information_about_new_pet(auth_key['key'], name, animal_type, age, pet_photo)
    assert status == 400

def test_post_add_information_about_new_pet_with_name_is_incorrect(name = incorrect_name2, animal_type = animal_type, age = age, pet_photo = pet_photo):
    """Негативный тест на добавление нового питомца с фото с валидным ключом и некорректным именем(имя из спецсимволов- "!@#$%^&*((((("""
    _, auth_key = pf.get_api_key(valid_email,valid_password)
    status, _ = pf.post_add_information_about_new_pet(auth_key['key'], name, animal_type, age, pet_photo)
    assert status == 400

def test_post_add_information_about_new_pet_with_name_is_incorrect(name = incorrect_name3, animal_type = animal_type, age = age, pet_photo = pet_photo):
    """Негативный тест на добавление нового питомца с фото с валидным ключом и некорректным именем(количество символов имени превыышает допустимое - 30 символов"""
    _, auth_key = pf.get_api_key(valid_email,valid_password)
    status, _ = pf.post_add_information_about_new_pet(auth_key['key'], name, animal_type, age, pet_photo)
    assert status == 400

def test_post_add_information_about_new_pet_with_animal_type_is_incorrect(name = name, animal_type = incorrect_animal_type, age = age, pet_photo = pet_photo):
    """Негативный тест на добавление нового питомца с валидным ключом и некорректным типом питомца(тип питомца  - пробел)"""
    _, auth_key = pf.get_api_key(valid_email,valid_password)
    status, _ = pf.post_add_information_about_new_pet(auth_key['key'], name, animal_type, age, pet_photo)
    assert status == 400

def test_delete_pet_from_database_with_invalid_key():
    """Негативный тест на удаление питомца с невалидным ключом и валидныи ID"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pet_id = pf.post_add_information_about_new_pet(auth_key['key'], name, animal_type, age,pet_photo)
    status = pf.delete_pet_from_database(invalid_key,pet_id)
    assert status == 403

def test_delete_pet_from_database_with_invalid_id():
    """Негативный тест на удаление питомца с валидным ключом и невалидныи ID"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pet_id = pf.post_add_information_about_new_pet(auth_key['key'], name, animal_type, age,pet_photo)
    status = pf.delete_pet_from_database(auth_key['key'],invalid_id)
    assert status == 403

def test_update_name_about_pet_with_invalid_key(name ='', animal_type = '', age = ''):
    """Негатитивный тест на изменение информации об имени питомце с невалидным ключом"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pet_id = pf.post_add_information_about_new_pet(auth_key['key'], name, animal_type, age, pet_photo)
    status, _ = pf.update_information_about_pet(invalid_key, pet_id, name, animal_type1, age)
    assert status == 403



