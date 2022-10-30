"""
Code for delete order
add order
make 2 order_books for maintaining buy and sell orders

"""
# read data from xml file
import xml.etree.ElementTree as ET
import heapq
import json

# declaring the order book
# dictionary of list, with each list having 3 elements order_book[book]=[price,volume,order_id,order_type,]
order_book = []
order_type={}#price,volume,order_id,order_type
# Class book having price,volume,order_id,order_type as attributes
def updateBook(buyHeap,sellHeap):
    while(len(buyHeap)>0 and len(sellHeap)>0):
        buy=heapq.heappop(buyHeap)
        sell=heapq.heappop(sellHeap)
        if(-1*buy[0]>sell[0]):
            if(buy[1]>sell[1]):
                buy[1]-=sell[1]
                heapq.heappush(buyHeap,buy)
            elif(buy[1]<sell[1]):
                sell[1]-=buy[1]
                heapq.heappush(sellHeap,sell)
        else:
            break
    return buyHeap,sellHeap



class Book:
    def __init__(self,book_no):
        self.book_no=book_no
        self.buyList = []
        heapq.heapify(self.buyList)
        self.sellList = []
        heapq.heapify(self.sellList)
    def add_order(self, order):
        self.price = order['price']
        self.volume = order['volume']
        self.order_id = order['orderId']
        self.order_type = order['operation']
        # if order_type is buy
        # key= lambda x: x.price
        if self.order_type == 'BUY':
            # self.buyList.add((self.price, self.volume, self.order_id),key=key,reverse=True)
            heapq.heappush(self.buyList,[-1*self.price,self.order_id,self.volume])#self.buyList.append([self.order_id,self.volume,self.price])
            #self.buyList.sort(key=lambda x: x[2],reverse=True)
        # if order_type is sell
        elif self.order_type == 'SELL':
            #self.buyList.append([self.order_id,self.volume,self.price])
            #self.sellList.sort(key=lambda x: x[2])
            heapq.heappush(self.sellList,[self.price,self.order_id,self.volume])
            self.buyList,self.buyList=updateBook(self.buyList,self.buyList)
            # self.sellList.add((self.price, self.volume, self.order_id),key=key)
        return self.buyList,self.sellList

    def delete_order(self, order_id):
        for i in self.buyList:
            if i.order_id == order_id:
                self.buyList.remove(i)
                break
        for i in self.sellList:
            if i.order_id == order_id:
                self.sellList.remove(i)
                break
        return self.buyList,self.sellList

    def buy_List(self):
        return self.buyList
    def sell_List(self):
        return self.sellList
    # def updateList(self):

# {a:{},b:2,c:3}
books={}
def readFromXml():
    tree = ET.parse('sample.xml')
    root = tree.getroot()
    for child in root:
        books[child.attrib['book']]=Book(child.attrib['book'])
        if(child.tag == 'AddOrder'):
            # addOrder(child.attrib)
            if(not Book(child.attrib['book'])):books[child.attrib['book']]=Book(child.attrib['book'])
            books[child.attrib['book']]=[books[child.attrib['book']].add_order(dict(child.attrib))]



        elif(child.tag=='DeleteOrder'):
            books[child.attrib['book']]=books[child.attrib['book']].delete_order(child.attrib['orderId'])

    print(books)
    for book in books:
        # print(book.value())
        print(book)
readFromXml()





