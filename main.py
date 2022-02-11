import numpy as  np ;
from keras.models  import  Sequential;
from keras.layers.core   import Dense;


training_data = np.array([[0,0],[0,1],[1,0],[1,1]], "float32");
target_data = np.array([[0],[1],[1],[0]], "float32");


# creating   the =>  (neural networks)
model  = Sequential();
model.add(Dense(16,input_dim=2,activation='relu'));
model.add(Dense(1 ,activation='sigmoid'));

model.compile(loss='mean_squared_error',optimizer='adam',
              metrics=['binary_accuracy']);


model.fit(training_data,target_data,epochs=1000,batch_size=64);




target  =  np.array([[0,0]]);
print(model.predict(target));


