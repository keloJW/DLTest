from xml.dom.minidom import parse
import os
import re
import linecache
import GenerateCode as gc
import AddGraph as ag
import CheckCode as cc

def checkXML(head, tail):
    result = False
    domTree = parse("graph.xml")
    # 文档根元素
    rootNode = domTree.documentElement
    connections = rootNode.getElementsByTagName("connection")
    for connection in connections:
        headName = connection.getElementsByTagName("head")[0]
        # print(headName.nodeName, ":", headName.childNodes[0].data)
        tailName = connection.getElementsByTagName("tail")[0]
        # print(tailName.nodeName, ":", tailName.childNodes[0].data)
        if head == headName.childNodes[0].data and tail == tailName.childNodes[0].data:
            result = True
    return result


def addCode(file, addHead,addTail,code):
    lines = []
    f = open(file, 'r')  # your path!
    for line in f:
        lines.append(line)
    f.close()
    with open(file, "r+", encoding='UTF-8') as f:
        # print(len(f.readlines()))
        i=1
        for line in f.readlines():
            res1 = linecache.getline(file, i).strip().find(addHead)
            res2 = linecache.getline(file, i+1).strip().find(addTail)
            if res1>=0 and res2>=0:
                file1 = str(file).split(".")[0]
                newFile='new_'+file1+'.py'
                lines.insert(i, code+'\n')
                s=''.join(lines)
                f = open(newFile, 'w+')  # 重新写入文件
                f.write(s)
            i=i+1
            if i==len(f.readlines()):
                f.close()
                break
    return newFile

def readCode(file,addHead,addTail,code):
    end=False
    api = r"keras.layers.*"
    node = []
    with open(file, "r", encoding='UTF-8') as f:
        for line in f.readlines():
            res = re.findall(api, line)
            if (res):
                node.append(res[0].split(".")[2].split("(")[0])
    for i in range(len(node)-1):
        if addHead==node[i] and addTail==node[i+1]:
            checkXMLResult = checkXML(addHead,addTail)
            newCode=gc.generate(code)
            newFile = addCode(file, addHead, addTail, newCode)
            if checkXMLResult == True:
                end=True
            else:
                checkCodeResult=cc.check(newFile)
                if checkCodeResult==True:
                    ag.addCorrectGraph(addHead, addTail, newCode)
                else:
                    ag.addIncorrectGraph(addHead, addTail, newCode)
                    os.remove(newFile)
                end=True
        # else:
        #     print("头尾节点不存在")
        #     return False
        return end

if __name__ == '__main__':
    readResult=readCode("test_0.py","ELU","ThresholdedReLU","Conv2D")
    print(readResult)
    # result = checkXML("InputLayer", "Dense")
    # print(result)
    # addCode("test_0.py","ELU","ThresholdedReLU","Conv2D")
