import tensorflow as tf
import numpy as np

# 케라스 학습모델 생성
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=2, input_dim=2, activation='sigmoid'))   # ①
model.add(tf.keras.layers.Dense(units=1,  activation='sigmoid'))		# ②

# 최적화 방법으로 경사하강법을 사용(학습률 lr = 0.1)
sgd = tf.keras.optimizers.SGD(lr=0.1)

# 학습과정 구성(손실함수로 평균 제곱 오차를 지정)
model.compile(loss='mean_squared_error', optimizer=sgd)

# 입력 데이타셋, 출력 데이타 셋을 주고 XOR 학습을 진행
X = np.array([[0, 0],[0, 1],[1, 0],[1, 1]])
# y = np.array([[0], [1], [1], [0]])

# p.709 LAB -> OR 학습
y = np.array([[0], [1], [1], [1]])

model.fit(X, y, batch_size=1, epochs=10000)

# 예측값 테스트
print( model.predict(X) )