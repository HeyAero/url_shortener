import app
from werkzeug.exceptions import BadRequest

def create(url_short, url_long):
  app.query_db('insert into urls (id, url) values (?, ?);', (url_short, url_long))
  return url_short

def find_by_id(id):
  try:
    return app.query_db('select url from urls where id = (?);', (id,))
  except:
    raise BadRequest(f"This short URL {id} does not lead anywhere :(")