import os
import random
from random import sample
from xml.dom.minidom import parse

def generate(apiName):
    if os.path.exists('api/'+apiName+'.xml'):
        with open('api/'+apiName+'.xml', 'r', encoding='UTF-8') as f:
            domTree = parse('api/'+apiName+'.xml')
            # 文档根元素
            root = domTree.documentElement
            parameters = root.getElementsByTagName("parameter")
            addstr='model.add(keras.layers.'+apiName+'('
            for parameter in parameters:
                name = parameter.childNodes[1].childNodes[0].data
                type = parameter.childNodes[3].childNodes[0].data
                if type=='int' :
                    num = parameter.childNodes[5].childNodes[0].data
                    minimum = parameter.childNodes[7].childNodes[1].childNodes[0].data
                    maximum = parameter.childNodes[7].childNodes[3].childNodes[0].data
                    if int(num)==1:
                        randnum=random.randrange(int(minimum),int(maximum))
                        addstr=addstr+name+'='+str(randnum)+','
                    if int(num)==2:
                        randnum1 = random.randrange(int(minimum), int(maximum))
                        randnum2 = random.randrange(int(minimum), int(maximum))
                        addstr = addstr + name + '=(' + str(randnum1) + ','+str(randnum2)+'),'
                elif type=='float':
                    num = parameter.childNodes[5].childNodes[0].data
                    minimum = parameter.childNodes[7].childNodes[1].childNodes[0].data
                    maximum = parameter.childNodes[7].childNodes[3].childNodes[0].data
                    if int(num)==1:
                        randnum=random.uniform(int(minimum),int(maximum))
                        addstr=addstr+name+'='+str(randnum)+','
                    if int(num)==2:
                        randnum1 = random.uniform(int(minimum), int(maximum))
                        randnum2 = random.uniform(int(minimum), int(maximum))
                        addstr = addstr + name + '=(' + str(randnum1) + ','+str(randnum2)+'),'
                elif type=='str':
                    value=parameter.childNodes[5].childNodes[0].data.split(',')
                    # print(sample(value, 1)[0])
                    addstr=addstr+name+'='+'\''+sample(value, 1)[0]+'\''+','
            addstr=addstr.strip(',')+'))'
            return addstr
    else:
        print("该接口范围不存在")

if __name__ == '__main__':
    generate("BatchNormalization")