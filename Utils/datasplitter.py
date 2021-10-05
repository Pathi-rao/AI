import shutil
import os
# select a random sample without replacement
from random import seed
from random import sample
# seed random number generator
seed(13)

def split_dataset_into_3(path_to_dataset, train_ratio, valid_ratio):
    """
    split the dataset in the given path into three subsets(validation,train)
    :param path_to_dataset:
    :param train_ratio:
    :param valid_ratio:
    :return:
    """
    _, sub_dirs, _ = next(iter(os.walk(path_to_dataset)))  # retrieve name of subdirectories
    sub_dir_item_cnt = [0 for i in range(len(sub_dirs))]  # list for counting items in each sub directory(class)

    # directories where the splitted dataset will lie
    dir_train = os.path.join(os.path.dirname(path_to_dataset), 'new_train')
    dir_valid = os.path.join(os.path.dirname(path_to_dataset), 'new_validation')
    # # dir_test = os.path.join(os.path.dirname(path_to_dataset), 'test')

    for i, sub_dir in enumerate(sub_dirs):

        dir_train_dst = os.path.join(dir_train, sub_dir)  # directory for destination of train dataset
        # print(dir_train_dst)
        dir_valid_dst = os.path.join(dir_valid, sub_dir)  # directory for destination of validation dataset
        # dir_test_dst = os.path.join(dir_test, sub_dir)  # directory for destination of test dataset

        # variables to save the sub directory name(class name) and to count the images of each sub directory(class)
        class_name = sub_dir
        sub_dir = os.path.join(path_to_dataset, sub_dir) # ..\..\Dataset\MVTEC_AD\Train\bottle
        sub_dir_item_cnt[i] = len(os.listdir(sub_dir))  # [209, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        items = os.listdir(sub_dir) # ['000.png', '001.png', '002.png'.....]

        # print(sub_dir_item_cnt[i]) # 209 for bottle
        # print(sub_dir_item_cnt[i] * train_ratio) # float 

        # transfer data to trainset
        trainratio = round((sub_dir_item_cnt[i] + 1)* train_ratio)
        # prepare a sequence
        sequence = [i for i in range(sub_dir_item_cnt[i])]
        # print(sequence)
        # select a subset without replacement
        train_subset = sample(sequence, trainratio) # percentage of random numbers of size trainratio
        
        for i in range(len(sequence)):
            
            if i in train_subset:
                if not os.path.exists(dir_train_dst):
                    os.makedirs(dir_train_dst)
                source_file = os.path.join(sub_dir, items[i])
                dst_file = os.path.join(dir_train_dst, items[i])
                shutil.copyfile(source_file, dst_file)
            else:
                if not os.path.exists(dir_valid_dst):
                    os.makedirs(dir_valid_dst)
                source_file = os.path.join(sub_dir, items[i])
                dst_file = os.path.join(dir_valid_dst, items[i])
                shutil.copyfile(source_file, dst_file)


        # for i in train_subset:

        #     if not os.path.exists(dir_train_dst):
        #         os.makedirs(dir_train_dst)

        #     source_file = os.path.join(sub_dir, items[i])
        #     dst_file = os.path.join(dir_train_dst, items[i])
        #     shutil.copyfile(source_file, dst_file)


        # for item_idx in range(round(sub_dir_item_cnt[i] * train_ratio )):
        #     if not os.path.exists(dir_train_dst):
        #         os.makedirs(dir_train_dst)
        #     print(item_idx)
            # source_file = os.path.join(sub_dir, items[item_idx])
            # dst_file = os.path.join(dir_train_dst, items[item_idx])
            # shutil.copyfile(source_file, dst_file)

        # # transfer data to validation
        # for item_idx in range(round(sub_dir_item_cnt[i] * train_ratio) + 1,
        #                       round(sub_dir_item_cnt[i] * (train_ratio + valid_ratio))):
        #     if not os.path.exists(dir_valid_dst):
        #         os.makedirs(dir_valid_dst)

        #     source_file = os.path.join(sub_dir, items[item_idx])
        #     dst_file = os.path.join(dir_valid_dst, items[item_idx])
        #     shutil.copyfile(source_file, dst_file)

        # # transfer data to testset
        # for item_idx in range(round(sub_dir_item_cnt[i] * (train_ratio + valid_ratio)) + 1, sub_dir_item_cnt[i]):
        #     if not os.path.exists(dir_test_dst):
        #         os.makedirs(dir_test_dst)

        #     source_file = os.path.join(sub_dir, items[item_idx])
        #     dst_file = os.path.join(dir_test_dst, items[item_idx])
        #     shutil.copyfile(source_file, dst_file)

    return

split_dataset_into_3('..\..\Dataset\MVTEC_AD\Train' , 0.8, 0.2)