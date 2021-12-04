import tensorflow as tf
from tensorflow import keras

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

inputDataTrain = [[1,1,1],[0,0,0],[0,1,0],[1,0,0],[1,1,0],[0,0,1]]
outputDataTrain = [[1],[1],[1],[0],[0],[0]]
inputDataValidate = [[1,0,1],[0,1,1]]
outputDataValidate = [[1],[0]]

trainDataset = tf.data.Dataset.from_tensor_slices(inputDataTrain,outputDataTrain)
validateDataset = tf.data.Dataset.from_tensor_slices(inputDataValidate,outputDataValidate)

model = keras.Sequential([
    keras.layers.Reshape(target_shape=(1), input_shape=(3,1)),
    keras.layers.Dense(units=3, activation='relu'),
    keras.layers.Dense(units=1, activation='softmax')
])


model.compile(optimizer='adam', 
              loss=tf.losses.CategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])


history = model.fit(
    trainDataset.repeat(), 
    epochs=10, 
    steps_per_epoch=100,
    validation_data=validateDataset.repeat(), 
    validation_steps=2
)

predictions = model.predict(validateDataset)
print(predictions)