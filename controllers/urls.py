import app
from werkzeug.exceptions import BadRequest, NotFound

def create(url_short, url_long):
  app.query_db('insert into urls (id, url) values (?, ?);', (url_short, url_long))
  return url_short

def find_by_id(id):
  try:
    url = app.query_db('select url from urls where id = (?);', (id,))
    if not url:
      raise NotFound(f"This short URL {id} does not lead anywhere :(  Try again, and include http:// in your request.")
    else:
      return url
  except:
    raise NotFound(f"This short URL {id} does not lead anywhere :(  Try again, and include http:// in your request.")