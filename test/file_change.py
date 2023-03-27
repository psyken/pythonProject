import os
import configparser

# INI 파일에서 경로 읽어오기
config = configparser.ConfigParser()
config.read('../config.ini') # 'config.ini' 파일을 읽어옴
path = config['DEFAULT']['path'] # 'DEFAULT' 섹션의 'path' 키 값을 가져옴

# 경로에 있는 파일 리스트 가져오기
files = os.listdir(path) # 해당 경로에 있는 파일 리스트를 가져옴, <class 'list'>
print(type(files))

# 파일명 변경
for i, filename in enumerate(files): # 파일 리스트에서 파일의 인덱스를 가져옴
    # 파일 확장자 추출
    ext = os.path.splitext(filename)[-1] # 파일의 확장자를 추출하여 저장

    # 새 파일명 생성
    new_filename = str(i + 1) + ext # 파일명을 1부터 순서대로 변경하여 새로운 파일명을 생성

    print(os.path.join(path, filename)+" => "+os.path.join(path, new_filename))
    # 파일 이동
    os.rename(os.path.join(path, filename), os.path.join(path, new_filename)) # 파일 이동을 수행하여 파일명 변경

    #git 체크 하냐?

    #새로운 가지다.

    #add4다.