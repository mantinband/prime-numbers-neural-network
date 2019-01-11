from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
import numpy

NUMBER_OF_COLUMS = 15
dataset = numpy.loadtxt("dataset_base_3.csv", delimiter=",")

numpy.random.shuffle(dataset)
X = dataset[:, 0:NUMBER_OF_COLUMS]
Y = dataset[:, NUMBER_OF_COLUMS]

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = Sequential()
model.add(Dense(NUMBER_OF_COLUMS, input_dim=NUMBER_OF_COLUMS, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dropout(.2))
model.add(Dense(128, activation='relu'))
model.add(Dropout(.2))
model.add(Dense(128, activation='relu'))
model.add(Dropout(.2))
model.add(Dense(1, activation='sigmoid')) # soft-max == all or nothing. sigmoid ~(0-1)

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])

# call the function to fit to the data (training the network)
model.fit(x_train, y_train, epochs=3, batch_size=50, validation_data=(x_test, y_test))

# save the model
model.save('prime_model.model')
