import time
from gemt.data.database import add_key, get_key


class KeysHandler(object):

    def __init__(self, key_value):
        self.key_value = key_value
        self.created_date = ''

    def add_key(self):
        self.created_date = time.strftime("%y/%m/%d - %H:%M:%S")
        add_key(reader_key=self.key_value, created_date=self.created_date)
        return 'Success!'

    def validate_key(self, machine_id=None):
        """
        Checks if a given key is not activated yet or if a given machine_id is the same
        :param machine_id:
        :return:
        """
        key_entity = get_key(self.key_value)[0]
        if key_entity['machine_id'] is not None:
            if key_entity['machine_id'] == machine_id:
                return 'Already authenticated by machine_id.'
            else:
                return None
        return 'This key is available.'
