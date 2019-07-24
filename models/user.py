
import os
import hashlib

import sqlalchemy


class User:
    
    @staticmethod
    def initialize(metadata):
        User.table = sqlalchemy.Table('users', metadata,

            sqlalchemy.Column(
                'id', 
                sqlalchemy.Integer,
                primary_key=True
            ),

            sqlalchemy.Column(
                'name',
                sqlalchemy.String(100),                        
            ),

            sqlalchemy.Column(
                'email',
                sqlalchemy.String(100),
                unique=True
            ),

            sqlalchemy.Column(
                'password',
                sqlalchemy.String(255),            
            )

        )

    @staticmethod
    def get_all_users():
        return [ 
            User(**u) for u in sqlalchemy.select([ 
                User.table 
            ]).execute()
        ]

    @staticmethod
    def find_by_email(email):
        result = [ 
            u for u in sqlalchemy.select([ 
                User.table 
            ]).where(User.table.c.email == email).execute()
        ]
        if len(result) == 0:
            return None
        return User(**result[0])

    def __init__(self, name, email, password, **kwargs):
        self.user_id = kwargs.get('id')
        self.name = name
        self.email = email
        self.password = password

    def authenticate(self, password):
        return hashlib.sha256(password.encode()).hexdigest() == self.password

    def save(self):
        user = User.find_by_email(self.email)
        if not user:
            sqlalchemy.insert(User.table).values(
                name=self.name,
                email=self.email,
                password=hashlib.sha256(self.password.encode()).hexdigest()
            ).execute()
        else:
            sqlalchemy.update(User.table).where(
                User.table.c.email == self.email
            ).values(
                name=self.name,
                # email=self.email,
                password=hashlib.sha256(self.password.encode()).hexdigest()
            ).execute()