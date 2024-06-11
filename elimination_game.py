class elimination:
    def item_list():
        item=[]
        print('Enter the list of items...')
        for i in range(9):
            i=int(input())
            item.append(i)
        return item
    def eliminate(items):
        n=len(items)
        start=1
        step=2
        pos = 1
        while n > 1:
            start = pos*(step * (n//2)-step//2)
            n //= 2
            step *= 2
            pos *= 1
        return items[start+1]
lis=[]
el=elimination
lis=el.item_list()
lis.sort()
print(lis," ")
print([el.eliminate(lis)])



      
