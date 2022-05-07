#리스트로 구현
"""
head = "www.hufs.ac.kr" #초기 주소
pointer = 0             #현재 사이트를 가리키는 인덱스
addr_history = [head]   #기록 저장 리스트(앞 뒤 이동용)
history = [head]        #go로 이동한 주소만 저장(history용)
print(head)             #초기 주소 출력

while True:
    user = input()
    if user == "quit":
        break
    elif "go" in user:
        addr = user[3:] #주소부분만 잘라냄
        addr_history = addr_history[:pointer+1] #forward불가능
        addr_history.append(addr)
        pointer += 1
        if addr in history: #방문한 적 있다면
            history.remove(addr)
            history.append(addr)
        else:   #처음 방문시
            history.append(addr)
            
        print(addr)
        
    elif user == "backward":
        pointer -= 1
        print(addr_history[pointer])
        
    elif user == "forward":
        if pointer == len(addr_history)-1:      #다음 페이지가 없는 경우
            continue
        else:
            pointer += 1
            print(addr_history[pointer])
            
    elif user == "history":
        for i in history[::-1]:
            print(i)
    else:                                       #그외에 지정되지 않은 입력
        continue
        
"""
#이중연결리스트로 구현
"""
class browser:
    def __init__(self,data):
        self.back = None    #앞에 연결된 노드
        self.forth = None   #뒤에 연결된 노드
        self.addr = data


class dl_list:
    def __init__(self):
        self.head = None
        
    def go(self,e):
        global pointer, go_list
        e = e[3:]
        new_browser = browser(e)
        new_browser.back = pointer      #새로운 노드 앞이 pointer
        pointer.forth = new_browser     #pointer 뒤가 new브라우저
        pointer = new_browser           #포인터를 옮김
        if new_browser.addr in go_list: #방문한적이 있을 때
            go_list.remove(new_browser.addr)
        go_list.append(new_browser.addr)
        print(pointer.addr)             #옮긴 주소 출력
    def forward(self):
        global pointer
        if pointer.forth==None:         #앞으로가기가 불가능인 경우
            return
        else:
            pointer = pointer.forth         #포인터 이동
            print(pointer.addr)
    def backward(self):
        global pointer
        pointer = pointer.back          #포인터 이동
        print(pointer.addr)
        
    def history(self):
        global go_list
        for i in go_list[::-1]:
            print(i)
        
    
hufs_addr = "www.hufs.ac.kr"
head = browser(hufs_addr)   #노드형 인스턴스
history = dl_list()         #앞뒤 이동용
go_list = [head.addr]                #history함수 용
history.head = head         #헤드가 가리키는 노드가 hufs인스턴스
pointer = head                 #현재 사이트를 가리키는 노드
print(head.addr)

while True:
    user = input()
    if user == "quit":
        break
    elif "go" in user:
        history.go(user)
    elif user == "backward":
        history.backward()
    elif user == "forward":
        history.forward()

    elif user == "history":
        history.history()
    else:
    
        continue
        
"""
