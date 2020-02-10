# -*- coding: utf-8 -*-

# 이진 분류를 위한 데이터 셋 정의
X_data = [1,2,3,4,5,6,7,8,9,10]
y_data = [0,0,0,1,0,1,1,1,1,1]

import tensorflow as tf

X = tf.placeholder(tf.float32, shape=[None])
y = tf.placeholder(tf.float32, shape=[None])

w = tf.Variable(0.0)
b = tf.Variable(0.0)

# 텐서플로우를 활용하여
# 이진 데이터를 분류하는 방법
# 1. 선형방정식을 사용하여 값을 예측 (X * w + b)
# 2. 예측한 값을 활성화 함수를 사용하여
#    지정된 영역 내부로 값을 압축
# 3. 활성화 함수별로 지정된 기준값을
#    사용하여 분류값을 예측
#    (sigmoid 함수의 경우 0.5가 기준값)

# 선형방정식을 사용하여 값을 예측
pre_h = X * w + b

# 활성화 함수를 사용하여 지정된 
# 영역 내부로 값을 압축
h = tf.sigmoid(pre_h)

# 양성데이터(1인 경우)의 오차를 계산
# - sigmoid 함수의 실행 결과과 1에 가까질수록
#   오차의 값이 작음
# - -tf.log 의 결과를 사용함
loss_1 = y * -tf.log(h)

# 음성데이터(0인 경우)의 오차를 계산
# - sigmoid 함수의 실행 결과과 0에 가까질수록
#   오차의 값이 작음
# - tf.log 의 결과를 사용함
loss_0 = (1-y) * -tf.log(1-h)

# 음성, 양성 데이터에 대한 오차의 값들을
# 하나의 텐서 변수로 통합
loss_sum = loss_0 + loss_1

# 오차를 제곱한 후, 평균값을 계산
#loss = tf.reduce_mean(tf.square(loss_sum))

# 위의 오차식을 한 줄의 실행문으로 작성하는 예제
loss = tf.reduce_mean(tf.square(
        y * -tf.log(h) + (1-y) * -tf.log(1-h)))

optimizer = tf.train.AdamOptimizer()
train = optimizer.minimize(loss)

init_op = tf.global_variables_initializer()

# 예측 값 생성을 위한 텐서
predict_bool = h >= 0.5
predict = tf.cast(predict_bool, tf.float32)

# 정확도 반환을 위한 텐서
accuracy_1 = tf.equal(predict, y)
accuracy_2 = tf.cast(accuracy_1, tf.float32)
accuracy_3 = tf.reduce_mean(accuracy_2)

accuracy = tf.reduce_mean(
        tf.cast(tf.equal(y, predict), tf.float32))

# 세션 객체를 사용하여 학습을 진행
with tf.Session() as sess :
    sess.run(init_op)
    
    
    feed_dict = {X:X_data, y:y_data}    
    
    for step in range(1, 10001) :
        sess.run(train, feed_dict=feed_dict)
        
        if step % 5 == 0 :
            loss_val = sess.run(loss, 
                    feed_dict=feed_dict)
            print(step, loss_val)

    h_val, pred, acc, loss_val = sess.run(
            [h, predict, accuracy, loss], 
            feed_dict=feed_dict)
    print('학습 종료')
    print('오차', loss_val)
    #print('예측', h_val)
    print('예측', pred)
    print('정확도', acc)
    












