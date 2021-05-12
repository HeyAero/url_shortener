import uuid

def create_url():

    new_url_ext = str(uuid.uuid4())[0:5]

    return new_url_ext