import os
import re

def get_name(file_list):
    img_name = []
    for file in file_list:
        name,ex = os.path.splitext(file)
        if ex == '.txt':
            img_name.append(name)
    return img_name

# def create_txt(path,img,text):
#     for name in img:
#         file_name = name + '.txt'
#         file_name = os.path.join(path,file_name)
#         if not os.path.exists(file_name):
#             with open(file_name,'w') as f:
#                 f.write(text)
#                 f.close()

def content_write(img,path):
    for name in img:
        file_name = name + '.txt'
        file_name = os.path.join(path,file_name)
        file = open(file_name,'r') 
        new_file = ''
        
        for line in file:
            s = line[:2]
            f = line[2:]
            new_word = '0 ' + f
            # print(new_word)
            if s.strip() == '15':
                new_word = '0 ' + f
                new_file += new_word 
            elif s.strip() == '16':
                new_word = '1 ' + f
                new_file += new_word 
            elif s.strip()=='0':
                new_word = line 
                new_file += new_word 
            elif s.strip()=='1':
                new_word = line 
                new_file += new_word 
        file.close()

        writting = open(file_name,'w')
        writting.write(new_file)
        writting.close()


if __name__ == '__main__':
    file_list = os.listdir('test')
    img_name = get_name(file_list)
    path = 'test'
    # text = '0 0.405273 0.329235 0.083984 0.133880'
    # create_txt(path,img_name,text)
    content_write(img_name,path)


# img = ['and','or','for']
# path = 't'
# for name in img:
#         file_name = name + '.txt'
#         file_name = os.path.join(path,file_name)
#         file = open(file_name,'r') 
#         new_file = ''
        
#         for line in file:
#             s = line[:2]
#             f = line[2:]
#             new_word = '0 ' + f
#             # print(new_word)
#             if s.strip() == '15':
#                 new_word = '0 ' + f
#                 new_file += new_word 
#             elif s.strip() == '16':
#                 new_word = '1 ' + f
#                 new_file += new_word 
#             elif s.strip()=='0':
#                 new_word = line 
#                 new_file += new_word 
#             elif s.strip()=='1':
#                 new_word = line 
#                 new_file += new_word 
#         file.close()

#         writting = open(file_name,'w')
#         writting.write(new_file)
#         writting.close()



    
