import pytest

from neoway.app_factory import create_app
from neoway.extensions import db
from neoway.models import CPFModel, CNPJModel

@pytest.fixture(scope='module')
def app():
    """Instância da aplicação principal do Flask"""
    app = create_app()

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/dev.db'

    with app.app_context():
        db.create_all()
        populate_db(db)
        yield app

        db.drop_all()

@pytest.fixture()
def client(app):
    return app.test_client()

def populate_db(db):
    db.session.add(CPFModel(cpf='11421433923'))
    db.session.add(CPFModel(cpf='44826646186'))

    db.session.add(CNPJModel(cnpj='46911271000108'))
    db.session.add(CNPJModel(cnpj='13617419000139'))

    db.session.commit()