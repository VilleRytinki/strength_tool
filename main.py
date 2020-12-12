from classes.Exercise import Exercise
from classes.Session import Session
import _sqlite3 as sq


def create_log():
    try:
        conn = sq.connect('test.db')
        print('Database created.')
    except RuntimeError:
        print('Database creation unsuccesful')


exercises = []

pystypunnerrus = 'pystypunnerrus'
paino = 77.5
toistot = 3
sarjoja = 1

pystypunnerrus1 = Exercise(1, pystypunnerrus, paino, sarjoja, toistot)
pystypunnerrus2 = Exercise(2, 'pystypunnerrus', 70, 1, 3)
penkkipunnerrus = Exercise(3, 'penkkipunnerrus', 97.5, 5, 5)

exercises.append(pystypunnerrus1)
exercises.append(pystypunnerrus2)
exercises.append(penkkipunnerrus)

trainingSession = Session(date='6.12.2020', name='Sunday squat session', exercises=exercises, duration=1.30)

trainingSession.calculate_volume_for_exercise('pystypunnerrus')
print()
trainingSession.calculate_tonnage_for_exercise('pystypunnerrus')
print()
trainingSession.get_session_information()
print()
trainingSession.calculate_volume_for_all()

conn = sq.connect('test.db')
#
# conn.execute('''CREATE TABLE EXERCISE
#         (ID   TEXT PRIMARY KEY NOT NULL,
#         NAME    CHAR(50)        NOT NULL,
#         WEIGHT  INT             NOT NULL,
#         WORK_SETS   INT         NOT NULL,
#         REPETITIONS INT         NOT NULL);''')
# conn.close()

# conn.execute('INSERT INTO EXERCISE VALUES ({},"{}",{},{},{})'.format(pystypunnerrus1.id, pystypunnerrus1.name,
#                                                                    pystypunnerrus1.weight,pystypunnerrus1.work_sets,
#                                                                    pystypunnerrus1.repetitions));
#conn.commit()
cursor = conn.execute('SELECT * FROM EXERCISE')

for row in cursor:
    print(row[0], row[1], row[2], row[3], row[4])
conn.close()

