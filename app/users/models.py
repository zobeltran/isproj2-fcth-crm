"""
This is the User's Model
"""
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserMixin, SQLAlchemyAdapter, UserManager
from flask_migrate import Migrate

DB = SQLAlchemy()
MIGRATE = Migrate()


class User(DB.Model, UserMixin):
    """
    User Model
    """
    id = DB.Column('User_id', DB.Integer, primary_key=True)

    # User email information
    email = DB.Column('User_email', DB.String(255),
                      nullable=False, unique=True)
    confirmed_at = DB.Column('User_confirmed', DB.DateTime())

    # User information
    is_enabled = DB.Column(DB.Boolean(), nullable=False, default=False)
    first_name = DB.Column('User_First_Name', DB.String(50), nullable=False)
    last_name = DB.Column('User_Last_Name', DB.String(50), nullable=False)
    active = DB.Column('User_active', DB.Boolean())


class UserAuth(DB.Model, UserMixin):
    """
    User Authentication
    """
    id = DB.Column(DB.Integer, primary_key=True)
    # user_id = DB.Column(DB.Integer(), DB.ForeignKey('user.id', ondelete='CASCADE'))

#     # User authentication information
#     username = DB.Column(DB.String(50), nullable=False, unique=True)
#     password = DB.Column(DB.String(255), nullable=False)

#     # Relationships
#     user = DB.relationships('User', uselist=False, foreign_key=user_id)


# Flask-User Initialization
DB_ADAPTER = SQLAlchemyAdapter(DB, User, UserAuthClass=UserAuth)
