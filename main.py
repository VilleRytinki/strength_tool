from classes.Exercise import Exercise
from classes.Session import Session

exercises = []


pystypunnerrus = 'pystypunnerrus'
paino = 77.5
toistot = 3
sarjoja = 1

pystypunnerrus = Exercise(pystypunnerrus, paino, sarjoja, toistot)
penkkipunnerrus = Exercise('penkkipunnerrus', 97.5, 5, 5)

exercises.append(pystypunnerrus)
exercises.append(penkkipunnerrus)


trainingSession = Session(date='6.12.2020', name='Sunday squat session', exercises=exercises, duration=1.30)


trainingSession.get_session_information()



#if __name__ == '__main__':
#   main()
