from keras.models import  Sequential;
from keras.layers.core  import  Dense;
import numpy  as np ;

class NetWork:

      def __init__(self , inputs , targets):
          self.inputs = np.array(inputs ,"float32");
          self.targets = np.array(targets ,"float32");
          self.model  = Sequential();

      def  Treinar(self):
          self.model.add(Dense(16, input_dim=2, activation='relu'));
          self.model.add(Dense(1, activation='sigmoid'));
          self.model.compile(loss='mean_squared_error', optimizer='adam',
                        metrics=['binary_accuracy']);
          self.model.fit(self.inputs,self.targets, epochs=1000, batch_size=64);


      def Predicao(self ,inputs):
          inputs = np.array([inputs]);
          return self.model.predict(inputs);

