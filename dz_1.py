import json

def to_json(func):
    def wrapped(*args, **kwargs):
        return_value = json.dumps(func(*args, **kwargs))
        print(return_value)
        return return_value
    return wrapped

@to_json
def get_data():
  return {
    'data': 42,
    'ebalo': 'sad',
    234: 333,
    123: 'ebalo'
  }
  
get_data()  # вернёт '{"data": 42}'