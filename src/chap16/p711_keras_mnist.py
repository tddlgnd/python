import matplotlib.pyplot as plt
import tensorflow as tf

mnist = tf.keras.datasets.mnist

# 훈련 데이터와 테스트 데이터를 가져온다.
(x_train, y_train),(x_test, y_test) = mnist.load_data()	

# 넘파이를 사용하여 0에서 255사이의 값을 0.0에서 1.0 사이로 변환.
# 신경망 입력은 0.0에서 1.0으로 정규화되어야 함
x_train, x_test = x_train / 255.0, x_test / 255.0

plt.imshow(x_train[1], cmap="Greys")


# 레이어를 쌓아서 모델 생성
model = tf.keras.models.Sequential()

# Flatten 레이어 : 입력 28*28을 784*1로 만든다.
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))

# Dense 레이어 : 전체 뉴론이 512개로 연결된 레이어 추가. 활성화 함수로 ReLU 지정
model.add(tf.keras.layers.Dense(512, activation='relu'))

# Dropout 레이어 : 몇개의 학습을 제외(0.2비율의 뉴론)하여 과잉적합을 회피하는 레이어. 
model.add(tf.keras.layers.Dropout(0.2))

# 출력을 위한 Dense 레이어 추가. 활성화 함수로 softmax 지정
# softmax : 출력 노드 중에서 하나만 1로 만들고 나머지는 0으로 만드는 활성화 함수
model.add(tf.keras.layers.Dense(10, activation='softmax'))

# 학습을 위해 옵티마이저, 손실 함수, 평가기준으로 정확도를 지정
# adam : 학습 도중에 학습률을 적응적으로 변경시키는 최적화 알고리즘
# sparse_categorical_crossentropy : 교차 엔트로피 값을 손실 함수로 지정
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 학습수행과 평가
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)

# # 테스트하기
# import cv2 as cv

# image = cv.imread('mytest.png', cv.IMREAD_GRAYSCALE)
# image = cv.resize(image, (28, 28))
# image = image.astype('float32')
# image = image.reshape(1, 784)
# image = 255-image
# image /= 255.0

# plt.imshow(image.reshape(28, 28),cmap='Greys')
# plt.show()

# pred = model.predict(image.reshape(1, 784), batch_size=1)
# print("판별 숫자=", pred.argmax())
