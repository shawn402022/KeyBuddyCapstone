from models import db, User

#create a function to seed

def seed_users():
    #create a bunch of users in an array

    seed_data = [
        User(username='user1', full_name='Shawn Norbert', password="password", email='user1@example.com'),
        User(username='user2', full_name='Bouchra Norbert', password="password", email='user2@example.com'),
        User(username='user3', full_name='Hamzah Norbert', password="password", email='user3@example.com'),
        User(username='user4', full_name='Shahid Alexander', password="password", email='user4@example.com'),
        User(username='user5', full_name='Shirley Kay', password="password", email='user5@example.com'),
        User(username='user6', full_name='Trevor Khan', password="password", email='user6@example.com'),
        User(username='user7', full_name='Shamir Roberts', password="password", email='user7@example.com'),
        User(username='user8', full_name='Allison Nutley', password="password", email='user8@example.com')
    ]

    #buld insert seeds into db

    db.session.bulk_save_objects(seed_data)

    #Commit the changes to the dn
    db.session.commit()
    print("Seeded users")
