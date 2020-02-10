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

X = tf.placeholder(tf.float32, shape=[None, 2])
y = tf.placeholder(tf.float32, shape=[None])

# 2. 가중치와 절편의 Variable 텐서 선언

# 선형회기를 위한 선형방정식
# x1 * w1 + x2 * w2 ... xN * wN + b
# X * W + b = y

# 가중치 변수의 벡터 선언
# (X의 각 특성에 가중치 변수를 부여)
# X 데이터의 형태 : 9 X 2
# W 데이터의 형태 : 2 X 1
# 결과 데이터의 형태 : 9 X 1
W = tf.Variable(tf.zeros(shape=[2, 1]))

# 절편
b = tf.Variable(0.0)

# 3. 머신러닝/딥러닝의 가설 텐서 선언
# - 행렬곱 연산을 사용한 가설 선언
# - 9 X 2 * 2 X 1 -> 9 X 1
# - 2차원 형태의 텐서가 반환
#h = tf.matmul(X, W) + b

# 손실 계산을 위한 h 텐서의 형 변환

# - y 데이터가 1차원이므로 1차원 텐서로 변환
# - tf.reshape 사용
#h_reshape = tf.reshape(h, [-1])

# - tf.transpose 사용(전치)
#h_transpose = tf.transpose(h)

# 전치를 활용한 가설 텐서를 생성
h = tf.transpose(tf.matmul(X, W) + b)

# 4. 손실(오차)의 값을 계산할 수 있는 텐서 선언
# - 실제정답(y)과 예측값(h)의 차를 제곱하여 평균값을 계산
#loss_1 = y - h
#loss_reshape = y - h_reshape
#loss_transpose = y - h_transpose

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
    
    """
    #print(sess.run(loss_1, feed_dict=feed_dict))
    print(sess.run(loss_reshape, feed_dict=feed_dict))
    print(sess.run(loss_transpose, feed_dict=feed_dict))
    
    print(sess.run(tf.reduce_mean(loss_reshape), feed_dict=feed_dict))
    print(sess.run(tf.reduce_mean(loss_transpose), feed_dict=feed_dict))    
    """
    
    for step in range(1, 10001) :
        sess.run(train, feed_dict=feed_dict)
        
        if step % 5 == 0 :
            w_val, b_val, loss_val = sess.run(
                    [W, b, loss], 
                    feed_dict=feed_dict)
            print(step, w_val, b_val, loss_val)

    w_val, b_val, loss_val = sess.run(
                    [W, b, loss], 
                    feed_dict=feed_dict)
    print('학습 종료')
    print(step, w_val, b_val, loss_val)
    












