import numpy as np
import tensorflow as tf
from tensorflow import keras

print(tf.version)

# gpu_devices = tf.config.experimental.list_physical_devices('GPU')
# for device in gpu_devices:
#     tf.config.experimental.set_memory_growth(device, True)

# import tensorflow_text as tf_text

# def preprocess(vocab_table, example_text):

#   # Normalize text
#   tf_text.normalize_utf8(example_text)

#   # Tokenize into words
#   word_tokenizer = tf_text.WhitespaceTokenizer()
#   tokens = word_tokenizer.tokenize(example_text)

#   # Tokenize into subwords
#   subword_tokenizer = tf_text.WordpieceTokenizer(
#        lookup_table, token_out_type=tf.int64)
#   subtokens = subword_tokenizer.tokenize(tokens).merge_dims(1, -1)

#   # Apply padding
#   padded_inputs = tf_text.pad_model_inputs(subtokens, max_seq_length=16)
#   return padded_inputs


inputDataTrain = np.array([[0,0],[0,1],[1,0],[1,1]])
outputDataTrain = np.array([[0],[1],[1],[0]])
inputDataValidate = np.array([[0,0]])

model = keras.Sequential([
    keras.layers.Dense(4, input_dim=2, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])


model.compile(optimizer='adam',
              loss='mean_squared_error',
              metrics=['accuracy'])


history = model.fit(
    inputDataTrain,
    outputDataTrain,
    epochs=500,
    #verbose=0
)

predictions = model.predict(inputDataValidate).round()
print(predictions)