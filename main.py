from keras.layers.core  import Dense;
from keras.models import Sequential;
import numpy   as  np ;

train =np.array([[0,0]
                ,[0,1]
                ,[1,0]
                ,[1,1]]
                );

target = np.array([
     [0]
    ,[1]
    ,[1]
    ,[1]]
);


model =  Sequential();
model.add(Dense(4,input_dim=2 ,activation='relu'));
model.add(Dense(1,activation='sigmoid'));

# compile the keras model
model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
);

model.fit(train , target , epochs=1000 , batch_size=10);

model.summary();


# testando o modelo criado
# inputs =np.array([ [0,0]
#                   ,[0,1]
#                   ,[1,0]
#                   ,[1,1]
#                  ]);
# accuracy   = model.evaluate(train ,target);

# predicaco =    model.predict(inputs);
