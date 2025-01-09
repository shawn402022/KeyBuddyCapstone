from app import app, db

from app.models.user_models import  User

with app.app_context():
    db.drop_all()  # drop all tables before recreating them
    db.create_all()

    # create some sample data

    user1 = User(username='user1', full_name='Shawn Norbert', password="password", email='user1@example.com')
    user2 = User(username='user2', full_name='Bouchra Norbert', password="password", email='user2@example.com')
    user3 = User(username='user3', full_name='Hamzah Norbert', password="password", email='user3@example.com')

    #lesson_key1 = LessonKey(lesson_id=1, key_id=1)
    #lesson_key1 = LessonKey(lesson_id=2, key_id=2)

    #course_lesson1 = CourseLesson(course_id=1, lesson_id=1)
    #course_lesson2 = CourseLesson(course_id=2, lesson_id=2)

    #key1 = Key(key_name = 'C')
    #key2 = Key(key_name = 'C#')
    #key3 = Key(key_name = 'D')
    #key4 = Key(key_name = 'D#')
   # key5 = Key(key_name = 'E')
    #key6 = Key(key_name = 'F')
    #key7 = Key(key_name = 'F#')
    #key8 = Key(key_name = 'G')
    #key9 = Key(key_name = 'G#')
    #key10 = Key(key_name = 'A')
    #key11 = Key(key_name = 'A#')
    #key12 = Key(key_name = 'B')

    #chord1 = Chord(chord_name='C Major')
    #chord2 = Chord(chord_name='D Minor')

    #song1 = Song(song_name='Song 1', key_id=1, chord_id=1)
    #song2 = Song(song_name='Song 2', key_id=2, chord_id=2)

    #course1 = Course(course_name='Course 1')
    #course2 = Course(course_name='Course 2')

    #lesson1 = Lesson(lesson_name='Lesson 1', course_id=1)
    #lesson2 = Lesson(lesson_name='Lesson 2', course_id=2)

    #progression1 = Progression(progression_name='Progression 1')

    # add to the seed
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    # commit the db changes (saves the changes in the db)
    db.session.commit()

    print('Database has been seeded successfully.')
