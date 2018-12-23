class DefaultConfigs(object):
    train_data = "/home/markpeng/kaggle/hpa/train/" # where is your train data
    test_data = "/home/markpeng/kaggle/hpa/test/"   # your test data
    weights = "/home/markpeng/kaggle/hpa/checkpoints/"
    best_models = "/home/markpeng/kaggle/hpa/checkpoints/best_models/"
    submit = "/home/markpeng/kaggle/hpa/submit/"
    model_name = "bninception_bcelog"
    num_classes = 28
    img_weight = 512
    img_height = 512
    channels = 4
    lr = 0.03
    batch_size = 32
    epochs = 50

config = DefaultConfigs()
