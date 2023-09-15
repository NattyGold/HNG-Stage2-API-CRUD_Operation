from app import db
from app.routes import app
from app.models import Person



@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Person=Person)


