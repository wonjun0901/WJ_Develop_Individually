# -*- coding: utf-8 -*-

import tensorflow as tf

x = tf.Variable(10)
y = tf.Variable(7)

add = tf.add(x, y)
subtract = tf.subtract(x, y)
multiply = tf.multiply(x, y)
div = tf.divide(x, y)
mod = tf.mod(x, y)

with tf.Session() as sess:
    # tf.Variable 을 통해 생성된 텐서의 초기화를 
    # 위해서 작성된 코드
    init_variables = tf.global_variables_initializer()
    sess.run(init_variables)
    
    # feed_dict = {x:10, y:5}
    sess.run(tf.assign(x, 10))
    sess.run(tf.assign(y, 5))
    print("add({0}, {1}) -> {2}".format(\
          sess.run(x), sess.run(y), sess.run(add)))
    
    # feed_dict = {x:100, y:50}
    sess.run(x.assign(100))
    sess.run(y.assign(50))
    print("subtract({0}, {1}) -> {2}".format(\
          sess.run(x), sess.run(y), sess.run(subtract)))
    
    # feed_dict = {x:7, y:3}
    # sess.run 메소드를 사용하여
    # 다수개의 텐서를 실행하기 위해서는
    # 리스트의 형태로 입력합니다.
    sess.run([x.assign(7), y.assign(3)])
    print("multiply({0}, {1}) -> {2}".format(\
          sess.run(x), sess.run(y), sess.run(multiply)))
    
    # feed_dict = {x:10, y:3}
    sess.run([x.assign(10), y.assign(3)])
    print("div({0}, {1}) -> {2}".format(\
          sess.run(x), sess.run(y), sess.run(div)))
    
    # feed_dict = {x:10, y:5}
    sess.run([x.assign(10), y.assign(5)])
    print("mod({0}, {1}) -> {2}".format(\
          sess.run(x), sess.run(y), sess.run(mod)))
    
    
    
    
    
    
    
    
    
    