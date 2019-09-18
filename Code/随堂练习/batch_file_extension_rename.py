import os
import argparse

def batche_rename(work_dir,old_dir,new_ext):
    """
    :param work_dir:
    :param old_dir:
    :param new_ext:
    :return:
    """
    #files = os.listdir(workdir)
    for filename in os.listdir(work_dir): #返回指定文件包含的文件的列表
        split_file = os.path.splitext(filename)#分离文件名与扩展名，并返回元组
        file_ext = split_file[1] #获取文件扩展名
        if old_dir == file_ext:
            newfile = split_file[0]+new_ext
            os.rename(                          #文件重命名
                os.path.join(work_dir,filename),#路径和文件拼接
                os.path.join(work_dir,newfile)
            )

def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('work_dir',metavar='WORK_DIR',type=str,nargs=1,
                        help='the directory where to change extension')
    parser.add_argument('old_ext',metavar='OLD_EXT',type=str,nargs=1,help='old extension')
    parser.add_argument('new_ext',metavar='NEW_EXT',type=str,nargs=1,help='new extension')
    return parser

def main():
    """
    :return:
    """
    parser = get_parser()
    args = vars(parser.parse_args())
    work_dir = args['work_dir'][0]
    old_ext = args['old_ext'][0]
    if old_ext[0] != '.':
        old_ext = '.' + old_ext

    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.'+ new_ext

    batche_rename(work_dir,old_ext,new_ext)

if __name__ == '__main__':
    main()

