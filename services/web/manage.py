from flask.cli import FlaskGroup

from project import app

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    app.db.drop_all()
    app.db.create_all()
    app.db.session.commit()

if __name__ == "__main__":
    cli()

