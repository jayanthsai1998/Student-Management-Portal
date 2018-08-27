import threading
import requests
def getUrlForStudentList(collegeid, studentid):
    #url='http://127.0.0.1:8000/onlineapp/studentserialize/'+str(collegeid)
    url = 'http://127.0.0.1:8000/colleges_/' + str(collegeid) + '/students/' + str(studentid)
    reqs=requests.get(url)
    print(threading.current_thread().getName(),reqs.json())


thread_list = []

for i in range(5):
    thread_list.append(threading.Thread(target=getUrlForStudentList,args=(4,i+2)))

for i in range(5):
    thread_list[i].start()

for i in range(5):
    thread_list[i].join()

# t1=threading.Thread(target=getUrlForStudentList,args=(4,4))
# t2=threading.Thread(target=getUrlForStudentList,args=(4,6))
# t1.start()
# t2.start()
# t1.join()
# t2.join()