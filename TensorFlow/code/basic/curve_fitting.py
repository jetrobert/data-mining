# coding:utf-8
import tensorflow as tf
import numpy as np

# ģ������100�����ݶ�, ��Ӧ�ĺ���Ϊy = x * 0.1 + 0.3
x_data = np.random.rand(100).astype("float32")
y_data = x_data * 0.1 + 0.3

# ָ��w��b������ȡֵ��Χ��ע������Ҫ����TensorFlow���õ�w��b��ֵ��
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b

# ��С���������
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# ��ʼ��TensorFlow����
init = tf.initialize_all_variables()

# ����������ͼ��ע������һ���ſ�ʼִ�м�����̣�
sess = tf.Session()
sess.run(init)

# �۲��ε�������ʱ��w��b�����ֵ
for step in xrange(201):
	sess.run(train)
	if step % 20 == 0:
		print(step, sess.run(W), sess.run(b))

# ��õ������w��b�ֱ�ӽ���������0.1��0.3