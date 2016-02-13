from gemt.data.util.data_util import get_current_date_formated
from gemt.data.database import add_key, get_key, authenticate_key


class KeysHandler(object):

    def __init__(self, key_value):
        self.key_value = key_value
        self.created_date = ''

    def add_key(self):
        self.created_date = get_current_date_formated()
        add_key(reader_key=self.key_value, created_date=self.created_date)
        return 'Success!'

    def validate_key(self, machine_id=None):
        """
        Checks if a given key is not activated yet or if a given machine_id is the same
        :param machine_id:
        :return:
        """
        key_entity = get_key(self.key_value)
        if key_entity is None:
            return 'Invalid value'
        if key_entity['machine_id'] is not None:
            if key_entity['machine_id'] == machine_id:
                return 'Already authenticated by machine_id.'
            else:
                return None
        return 'This key is available.'

    def authenticate_key(self, machine_id):
        key_entity = get_key(self.key_value)
        if key_entity is None:
            return 'Invalid value'
        if key_entity['machine_id'] is not None:
            if key_entity['machine_id'] == machine_id:
                return 'Already authenticated by machine_id.'
            else:
                return 'Key is used by other machine'
        authenticate_key(entity_id=key_entity['id'], machine_id=machine_id)
        return 'Authenticated!'