#-*-coding:utf-8-*-

import tensorflow as tf 

with tf.Session() as sess:
    filename = ['A.jpg', 'B.jpg', 'C.jpg']
    # string_input_producer�����һ���ļ�������
    filename_queue = tf.train.string_input_producer(filename, shuffle=False, num_epochs=5)
    # reader���ļ��������ж����ݡ���Ӧ�ķ�����reader.read
    reader = tf.WholeFileReader()
    key, value = reader.read(filename_queue)
    # tf.train.string_input_producer������һ��epoch������Ҫ�������г�ʼ��
    tf.local_variables_initializer().run()
    # ʹ��start_queue_runners֮�󣬲ŻῪʼ������
    threads = tf.train.start_queue_runners(sess=sess)
    i = 0
    while(i<15):
        i += 1
        # ��ȡͼƬ���ݲ�����
        image_data = sess.run(value)
        with open('result/test_%d.jpg' % i, 'wb') as f:
            f.write(image_data)