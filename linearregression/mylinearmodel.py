"""

Author: Francesco Capponi <capponi.francesco87@gmail.com>

License: BSD 3 clause

"""

import numpy as np
from learners.myregressor import MyRegressor


class SimpleLinearRegressor(MyRegressor):
    """
    Simple linear regression class
    To be used for testing the crossvalidation class
    """
    def __init__(self):
        MyRegressor.__init__(self)
        self.learning_type='training_based'
        
    
    def __sanitycheck(self,X,types):
        # sanity check: just to be sure the user is giving the right parameters
        if not isinstance(X, types):
            raise ValueError("Object has to be a ",types)
  
##############################################################################
  
    def fit(self,X,Y):
        """
            Compute the value of linear model parameters, by using exact analytical solution.
            More details can be found in any good machine learning / statistics book
            
            Parameters
            ----------
            X : numpy-like, shape = [n_samples,n_input_features]        
            Y : numpy-like, shape = [n_samples,n_output_features]
        """
        return self._fit(X,Y)
    

    def predict(self,X):
        """
            Compute the prediction array for the input values given by X
             
            Parameters
            ----------
            X : numpy-like, shape = [n_samples,n_input_features]
        """ 
        return self._predict(X)
    
 ##############################################################################
      
    def _fit(self,X,Y):
        self.__sanitycheck(X,np.ndarray)
        self.__sanitycheck(Y,np.ndarray)
        
        if(len(X.shape)==1):
            X=X.reshape(-1,1)
            
        ones=(np.zeros(X.shape[0])+1.).reshape(-1,1)
        MX=np.hstack((ones,X))
        D=np.dot(MX.T,MX)
        invD=np.linalg.inv(D)
        self.linear_model_coefficients=np.dot(invD,np.dot(MX.T,Y))
        
        
    def _predict(self,X):
        self.__sanitycheck(X,np.ndarray)

        if(len(X.shape)==1):
            X=X.reshape(-1,1)

        ones=(np.zeros(X.shape[0])+1.).reshape(-1,1)
        MX=np.hstack((ones,X))

        self.prediction=np.dot(MX,self.linear_model_coefficients)
        
