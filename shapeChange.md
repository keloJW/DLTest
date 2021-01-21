Conv2d: input(a, b, c)
Conv2D(input_shape=(a, b, c), kernel_size=(d, d), filters=e, activation=‘*’)
output()

MaxPool2D：input(a, b, c)
MaxPool2D(pool_size=(d, d), strides=2, padding=‘*’)
output(0.5a, 0.5b, c)

Flatten：input(a, b, c)
Flatten()
output(a*b*c)

Dense: input(a)
Dense(b, activation=‘*’)
output(b)
