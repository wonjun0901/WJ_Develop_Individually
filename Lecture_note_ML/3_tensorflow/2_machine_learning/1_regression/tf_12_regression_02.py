# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf

# 텐서플로우를 활용한 선형회기
# X 데이터의 특성이 다수개인 경우

# 학습데이터 X
# 키와 성별 정보
X_train = np.array([
    [158, 1],
    [170, 1],
    [183, 1],
    [191, 1],
    [155, 0],
    [163, 0],
    [180, 0],
    [158, 0],
    [170, 0]
])

# 학습데이터 y
# 몸무게 정보
y_train = np.array([64, 86, 84, 80, 
                    49, 59, 67, 54, 67])

# 1. 데이터를 전달받기 위한 실행매개변수 선언
# - 학습데이터를 전달받기 위한 실행매개변수 선언
# - 다차원 배열을 실행매개변수로 전달받는 경우
#  행의 개수에 상관없이 특성이 2개인 데이터를 전달
X = tf.placeholder(tf.float32, shape=[None, 2])
y = tf.placeholder(tf.float32, shape=[None])

# 2. 가중치와 절편의 Variable 텐서 선언

# 가중치(X의 각 특성에 가중치 변수를 부여)
w1 = tf.Variable(1.0)   # 키에 대한 가중치
w2 = tf.Variable(1.0)   # 성별에 대한 가중치

# 절편
b = tf.Variable(0.0)

# 3. 머신러닝/딥러닝의 가설 텐서 선언
h = X[:,0] * w1 + X[:,1] * w2 + b

# 4. 손실(오차)의 값을 계산할 수 있는 텐서 선언
# - 실제정답(y)과 예측값(h)의 차를 제곱하여 평균값을 계산
loss = tf.reduce_mean(tf.square(y-h))

# 5. 경사하강법 객체의 선언과 손실의 값을
# 줄여나가는 방향으로 학습을 할 수 있는 텐서 선언

#optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
optimizer = tf.train.AdamOptimizer()

train = optimizer.minimize(loss)

init_op = tf.global_variables_initializer()

# 세션 객체를 사용하여 학습을 진행
with tf.Session() as sess :
    sess.run(init_op)
    
    feed_dict = {X:X_train, y:y_train}
    
    for step in range(1, 10001) :
        sess.run(train, feed_dict=feed_dict)
        
        if step % 5 == 0 :
            w1_val, w2_val, b_val, loss_val = sess.run(
                    [w1, w2, b, loss], 
                    feed_dict=feed_dict)
            print(step, w1_val, w2_val, b_val, loss_val)

    w1_val, w2_val, b_val, loss_val = sess.run(
                    [w1, w2, b, loss], 
                    feed_dict=feed_dict)
    print('학습 종료')
    print(step, w1_val, w2_val, b_val, loss_val)













