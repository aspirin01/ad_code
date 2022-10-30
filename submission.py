"""
Code for delete order
add order
make 2 order_books for maintaining buy and sell orders

"""
# read data from xml file
import xml.etree.ElementTree as ET
import heapq

# declaring the order book
# dictionary of list, with each list having 3 elements order_book[book]=[price,volume,order_id,order_type,]
order_book = []
order_type={}
# Class book having price,volume,order_id,order_type as attributes
class Book:
    def __init__(self,book_no):
        self.book_no=book_no
        self.buyList = []
        heapq.heapify(self.buyList)
        self.sellList = []
        heapq.heapify(self.sellList)
    def add_order(self, order):
        self.price = order.price
        self.volume = order.volume
        self.order_id = order.order_id
        self.order_type = order.order_type
        # if order_type is buy
        # key= lambda x: x.price
        if self.order_type == 'BUY':
            # self.buyList.add((self.price, self.volume, self.order_id),key=key,reverse=True)
            heapq.heappush(self.buyList,[self.order_id,self.volume,-self.price])#self.buyList.append([self.order_id,self.volume,self.price])
            self.buyList.sort(key=lambda x: x[2],reverse=True)
        # if order_type is sell
        elif self.order_type == 'SELL':
            self.buyList.append([self.order_id,self.volume,self.price])
            self.sellList.sort(key=lambda x: x[2])
            # self.sellList.add((self.price, self.volume, self.order_id),key=key)

    def delete_order(self, order_id):
        for i in self.buyList:
            if i.order_id == order_id:
                self.buyList.remove(i)
                break
        for i in self.sellList:
            if i.order_id == order_id:
                self.sellList.remove(i)
                break
    def buyList(self):
        return self.buyList
    def sellList(self):
        return self.sellList
    # def updateList(self):






def readFromXml():
    tree = ET.parse('sample.xml')
    root = tree.getroot()
    # for child in root:
        # if(child.tag == 'AddOrder'):
        #     # addOrder(child.attrib)
        # elif(child.tag=='DeleteOrder'):
        #     deleteOrder(child.attrib)


        # print(child.tag, child.attrib)
readFromXml()





