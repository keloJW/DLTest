from xml.dom.minidom import parse
import xml.dom.minidom
import re
import os

def addCorrectGraph(head,tail,newCode):
    api = r"keras.layers.*"
    dom = parse('graph.xml')
    root = dom.documentElement
    #添加第一个connection
    connection1 = dom.createElement('connection')
    head1 = dom.createElement('head')
    head1.appendChild(dom.createTextNode(str(head)))
    connection1.appendChild(head1)
    detail={}
    res = re.findall(api, newCode)
    detail['node'] = res[0].split(".")[2].split("(")[0]
    connection1.setAttribute('title', head+'_'+detail['node'])
    tail1 = dom.createElement('tail')
    tail1.appendChild(dom.createTextNode(str(detail['node'])))
    connection1.appendChild(tail1)
    num1=dom.createElement('num')
    num1.appendChild(dom.createTextNode(str('1')))
    connection1.appendChild(num1)
    root.appendChild(connection1)
    #添加第二个connection
    connection2 = dom.createElement('connection')
    connection2.setAttribute('title', detail['node'] + '_' + tail)
    head2 = dom.createElement('head')
    head2.appendChild(dom.createTextNode(str(detail['node'])))
    connection2.appendChild(head2)
    tail2 = dom.createElement('tail')
    tail2.appendChild(dom.createTextNode(str(tail)))
    connection2.appendChild(tail2)
    num2 = dom.createElement('num')
    num2.appendChild(dom.createTextNode(str('1')))
    connection2.appendChild(num2)
    root.appendChild(connection2)
    # 将dom对象写入本地xml文件
    with open('graph.xml', 'w', encoding='UTF-8') as f:
        dom.writexml(f, addindent='  ', encoding='UTF-8')

def addIncorrectGraph(head,tail,newCode):
    api = r"keras.layers.*"
    file='wrong_graph.xml'
    try:
        dom = parse(file)
        root = dom.documentElement
        # 添加第一个connection
        connection1 = dom.createElement('connection')
        head1 = dom.createElement('head')
        head1.appendChild(dom.createTextNode(str(head)))
        connection1.appendChild(head1)
        detail = {}
        res = re.findall(api, newCode)
        detail['node'] = res[0].split(".")[2].split("(")[0]
        connection1.setAttribute('title', head + '_' + detail['node'])
        tail1 = dom.createElement('tail')
        tail1.appendChild(dom.createTextNode(str(detail['node'])))
        connection1.appendChild(tail1)
        num1 = dom.createElement('num')
        num1.appendChild(dom.createTextNode(str('1')))
        connection1.appendChild(num1)
        root.appendChild(connection1)
        # 添加第二个connection
        connection2 = dom.createElement('connection')
        connection2.setAttribute('title', detail['node'] + '_' + tail)
        head2 = dom.createElement('head')
        head2.appendChild(dom.createTextNode(str(detail['node'])))
        connection2.appendChild(head2)
        tail2 = dom.createElement('tail')
        tail2.appendChild(dom.createTextNode(str(tail)))
        connection2.appendChild(tail2)
        num2 = dom.createElement('num')
        num2.appendChild(dom.createTextNode(str('1')))
        connection2.appendChild(num2)
        root.appendChild(connection2)
        # 将dom对象写入本地xml文件
        with open(file, 'w', encoding='UTF-8') as f:
            dom.writexml(f, addindent='  ', encoding='UTF-8')
    except:
        doc = xml.dom.minidom.Document()
        # 创建一个根节点Graphs对象
        root = doc.createElement('graph')
        doc.appendChild(root)
        connection1 = doc.createElement('connection')
        head1 = doc.createElement('head')
        head1.appendChild(doc.createTextNode(str(head)))
        connection1.appendChild(head1)
        detail = {}
        res = re.findall(api, newCode)
        detail['node'] = res[0].split(".")[2].split("(")[0]
        connection1.setAttribute('title', head + '_' + detail['node'])
        tail1 = doc.createElement('tail')
        tail1.appendChild(doc.createTextNode(str(detail['node'])))
        connection1.appendChild(tail1)
        num1 = doc.createElement('num')
        num1.appendChild(doc.createTextNode(str('1')))
        connection1.appendChild(num1)
        root.appendChild(connection1)
        # 添加第二个connection
        connection2 = doc.createElement('connection')
        connection2.setAttribute('title', detail['node'] + '_' + tail)
        head2 = doc.createElement('head')
        head2.appendChild(doc.createTextNode(str(detail['node'])))
        connection2.appendChild(head2)
        tail2 = doc.createElement('tail')
        tail2.appendChild(doc.createTextNode(str(tail)))
        connection2.appendChild(tail2)
        num2 = doc.createElement('num')
        num2.appendChild(doc.createTextNode(str('1')))
        connection2.appendChild(num2)
        root.appendChild(connection2)
        # 将dom对象写入本地xml文件
        fp = open(file, 'w', encoding='utf-8')
        doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
        fp.close()

if __name__ == '__main__':
    addIncorrectGraph("ELU","ThresholdedReLU","model.add(keras.layers.Dropout(theta=0.20433079965894296))")