
import tensorflow.lite as tensor
from tensorflow.lite.python.interpreter import Interpreter
interpreter=Interpreter(model_path="best.tflite")
interpreter.get_input_details()
