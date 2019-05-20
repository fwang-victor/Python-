import os
import argparse

def batche_rename_file_ext(work_dir,old_ext,new_ext):
    #遍历需要替换文件夹中的每个文件
    for filename in os.listdir(work_dir):
        #对文件进行切割
        split_file = os.path.splitext(filename)
        #获取文件扩展名
        file_ext = split_file[1]
        if old_ext == file_ext:
            new_file = split_file[0] + new_ext
            os.rename(
                    os.path.join(work_dir,filename),
                    os.path.join(work_dir,new_file))



def parser_args():
    parse = argparse.ArgumentParser(description='批量修改文件的后缀')
    parse.add_argument('work_dir',type=str,nargs=1,help='文件夹')
    parse.add_argument('old_ext',type=str,nargs=1,help='需要替换的文件后缀')
    parse.add_argument('new_ext',type=str,nargs=1,help='新的文件后缀')
    args = vars(parse.parse_args())
    return args

def main():
    args = parser_args()
    work_dir = args['work_dir'][0]
    old_ext = args['old_ext'][0]
    new_ext = args['new_ext'][0]
    print(args)

    batche_rename_file_ext(work_dir,old_ext,new_ext)

if __name__ == '__main__':
    main()