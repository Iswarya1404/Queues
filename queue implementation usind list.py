queue = []
def enqueue():
    element = input("enter element")
    queue.append(element)
    print("element is added in queue")
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e = queue.pop(0)
        print("removed element",e)
def display():
    print(queue)
while True:
    print("select an operation 1.Enqueue 2.Dequeue 3.Show 4.Quit")
    choice = int(input())
    if choice==1:
        enqueue()
    elif choice ==2:
        dequeue()
    elif choice ==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter correct option")