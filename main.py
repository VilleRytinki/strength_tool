from classes.Exercise import Exercise
from classes.Session import Session

exercises = []

pystypunnerrus = 'pystypunnerrus'
paino = 77.5
toistot = 3
sarjoja = 1

pystypunnerrus1 = Exercise(pystypunnerrus, paino, sarjoja, toistot)
pystypunnerrus2 = Exercise('pystypunnerrus', 70, 1, 3)
penkkipunnerrus = Exercise('penkkipunnerrus', 97.5, 5, 5)

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

# if __name__ == '__main__':
#   main()
