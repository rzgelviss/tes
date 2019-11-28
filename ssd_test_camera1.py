
import os
import math
import random

import numpy as np
import tensorflow as tf
import cv2

import tensorflow as tf
import keras.backend as K
import time

def get_flops(model):
    run_meta = tf.RunMetadata()
    opts = tf.profiler.ProfileOptionBuilder.float_operation()

    # We use the Keras session graph in the call to the profiler.
    flops = tf.profiler.profile(graph=K.get_session().graph,
                                run_meta=run_meta, cmd='op', options=opts)

    return flops.total_float_ops  # Prints the "flops" of the model.


# .... Define your model here ....
# ckpt_filename = './train_model/model.ckpt-2960'
# ckpt_filename = '../checkpoints/VGG_VOC0712_SSD_300x300_ft_iter_120000.ckpt'
# isess.run(tf.global_variables_initializer())
# saver = tf.train.Saver()
# saver.restore(isess, ckpt_filename)

# graph = tf.get_default_graph()
# graphdef = graph.as_graph_def()
# _ = tf.train.import_meta_graph("./train_model/model.ckpt-6839.meta")
# print(get_flops(graph))
#
# import sys
# sys.exit()

slim = tf.contrib.slim
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
sys.path.append('../')
from nets import ssd_vgg_300, ssd_common, np_methods
from preprocessing import ssd_vgg_preprocessing
from notebooks import visualization
# TensorFlow session: grow memory when needed. TF, DO NOT USE ALL MY GPU MEMORY!!!
gpu_options = tf.GPUOptions(allow_growth=True)
config = tf.ConfigProto(log_device_placement=False, gpu_options=gpu_options)
isess = tf.InteractiveSession(config=config)
# Input placeholder.
net_shape = (300, 300)
data_format = 'NHWC'
img_input = tf.placeholder(tf.uint8, shape=(None, None, 3))
# Evaluation pre-processing: resize to SSD net shape.
image_pre, labels_pre, bboxes_pre, bbox_img = ssd_vgg_preprocessing.preprocess_for_eval(
    img_input, None, None, net_shape, data_format, resize=ssd_vgg_preprocessing.Resize.WARP_RESIZE)
print(bbox_img)
image_4d = tf.expand_dims(image_pre, 0)

# Define the SSD model.
reuse = True if 'ssd_net' in locals() else None
ssd_net = ssd_vgg_300.SSDNet()
with slim.arg_scope(ssd_net.arg_scope(data_format=data_format)):
    predictions, localisations, _, _ = ssd_net.net(image_4d, is_training=False, reuse=reuse)
print(predictions)
print(localisations)
# Restore SSD model.
ckpt_filename = './xm2/model.ckpt-1000000'
# ckpt_filename = '../checkpoints/VGG_VOC0712_SSD_300x300_ft_iter_120000.ckpt'
isess.run(tf.global_variables_initializer())
# saver = tf.train.Saver()
# saver.restore(isess, ckpt_filename)



# SSD default anchor boxes.
ssd_anchors = ssd_net.anchors(net_shape)


# Main image processing routine.
def process_image(img, select_threshold=0.6, nms_threshold=.45, net_shape=(300, 300)):
    # Run SSD network.
    softmax = isess.graph.get_tensor_by_name("ssd_300_vgg/softmax_5/Reshape_1:0")
    conv62 = isess.graph.get_tensor_by_name("ssd_300_vgg/block11_box/Reshape:0")
    rimg, rpredictions, rlocalisations, rbbox_img = isess.run([image_4d, predictions, localisations, bbox_img],
                                                              feed_dict={img_input: img})

    # Get classes and bboxes from the net outputs.
    rclasses, rscores, rbboxes = np_methods.ssd_bboxes_select(
        rpredictions, rlocalisations, ssd_anchors,
        select_threshold=select_threshold, img_shape=net_shape, num_classes=2, decode=True)

    rbboxes = np_methods.bboxes_clip(rbbox_img, rbboxes)
    rclasses, rscores, rbboxes = np_methods.bboxes_sort(rclasses, rscores, rbboxes, top_k=400)
    rclasses, rscores, rbboxes = np_methods.bboxes_nms(rclasses, rscores, rbboxes, nms_threshold=nms_threshold)
    # Resize bboxes to original image shape. Note: useless for Resize.WARP!
    rbboxes = np_methods.bboxes_resize(rbbox_img, rbboxes)
    return rclasses, rscores, rbboxes
# Test on some demo image and visualize output.
''''''
path = './demo/'
image_names = sorted(os.listdir(path))
for i in image_names:
    img = mpimg.imread(path + i)
    rclasses, rscores, rbboxes = process_image(img)

    # visualization.bboxes_draw_on_img(img, rclasses, rscores, rbboxes, visualization.colors_plasma)
    visualization.plt_bboxes(img, rclasses, rscores, rbboxes)
print(',,,')

import cv2
camera_type = [0, 1]
chose_camera = camera_type[0]
capture = cv2.VideoCapture(r'D:\PythonProject\data\视频\视频\IMG_2352.MOV')
print('opencamara')
i = 0
with tf.Graph().as_default():
    output_graph_def = tf.GraphDef()
    with open('./pb_model/mobilenetssd.pb', "rb") as f:
        output_graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(output_graph_def, name="")
    while capture.isOpened():
        # print('in')
        ret, frame = capture.read()
        if i % 30 == 0:

            # print(frame)
            cv2.namedWindow("test", cv2.WINDOW_NORMAL)
            img_path = './demo/000032.jpg'
            # img = cv2.imread(img_path)
            img = frame.copy()
            t = time.time()
            classes, scores, bboxes = process_image(img)
            print(time.time() - t)
            # print(rclasses)
            # print(rscores)
            # print(rbboxes)
            height = img.shape[0]
            width = img.shape[1]
            shape = img.shape
            for i in range(classes.shape[0]):
                cls_id = int(classes[i])
                if cls_id >= 0:
                    score = scores[i]
                    bbox = bboxes[i]
                    color = [0, 255, 255]
                    # Draw bounding box...
                    p1 = (int(bbox[0] * shape[0]), int(bbox[1] * shape[1]))
                    p2 = (int(bbox[2] * shape[0]), int(bbox[3] * shape[1]))
                    cv2.rectangle(img, p1[::-1], p2[::-1], color, 1)
                    # Draw text...
                    s = '%s/%.3f' % (classes[i], scores[i])
                    p1 = (p1[0] - 5, p1[1])
                    cv2.putText(img, s, p1[::-1], cv2.FONT_HERSHEY_DUPLEX, 2, color, 2)
        i += 1
        cv2.imshow("test", img)
        kk = cv2.waitKey(1)  # 每帧数据延时1ms
    capture.release()
    cv2.destroyAllWindows()