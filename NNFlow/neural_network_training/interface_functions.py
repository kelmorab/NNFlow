from __future__ import absolute_import, division, print_function

from NNFlow.session_config.session_config                  import SessionConfig        as NNFlowSessionConfig
from NNFlow.neural_network_training.neural_network_trainer import NeuralNetworkTrainer as NNFlowNeuralNetworkTrainer
from NNFlow.neural_network_training.neural_network_trainer_regression import NeuralNetworkTrainerRegression as NNFlowNeuralNetworkTrainerRegression



def train_neural_network(save_path,
                         model_name,
                         model_id,
                         network_type,
                         hidden_layers,
                         activation_function_name,
                         dropout_keep_probability,
                         l2_regularization_beta,
                         early_stopping_intervall,
                         path_to_training_data_set,
                         path_to_validation_data_set,
                         optimizer,
                         batch_size_training,
                         batch_size_classification   = 200000,
                         session_config              = None
                         ):


    if session_config is None:
        session_config = NNFlowSessionConfig()

        
    neural_network_trainer = NNFlowNeuralNetworkTrainer()

    neural_network_trainer.train(save_path                   = save_path,
                                 model_name                  = model_name,
                                 model_id                    = model_id,
                                 network_type                = network_type,
                                 hidden_layers               = hidden_layers,
                                 activation_function_name    = activation_function_name,
                                 dropout_keep_probability    = dropout_keep_probability,
                                 l2_regularization_beta      = l2_regularization_beta,
                                 early_stopping_intervall    = early_stopping_intervall,
                                 path_to_training_data_set   = path_to_training_data_set,
                                 path_to_validation_data_set = path_to_validation_data_set,
                                 optimizer                   = optimizer,
                                 batch_size_training         = batch_size_training,
                                 batch_size_classification   = batch_size_classification,
                                 session_config              = session_config
                                 )

def train_regression_network(save_path,
                             model_id,
                             hidden_layers,
                             activation_function_name,
                             dropout_keep_probability,
                             l2_regularization_beta,
                             early_stopping_intervall,
                             path_to_training_data_set,
                             path_to_validation_data_set,
                             path_to_test_data_set,
                             parameter,
                             batch_size_training):
    neural_network_trainer = NNFlowNeuralNetworkTrainerRegression()

    neural_network_trainer.train(save_path= save_path,
                                 model_id= model_id,
                                 hidden_layers= hidden_layers,
                                 activation_function_name= activation_function_name,
                                 dropout_keep_probability= dropout_keep_probability,
                                 l2_regularization_beta= l2_regularization_beta,
                                 early_stopping_intervall= early_stopping_intervall,
                                 path_to_training_data_set= path_to_training_data_set,
                                 path_to_validation_data_set= path_to_validation_data_set,
                                 path_to_test_data_set = path_to_test_data_set,
                                 parameter= parameter,
                                 batch_size_training= batch_size_training
              )
              