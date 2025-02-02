# class FileDown:
#     def __init__(self):
#         self.dn=0
# first=FileDown()
# second=FileDown()
# first.dn,second.dn=map(int,input().split())
# play=0
# while True:
#     if first.dn<100:
#         first.dn+=1
#     if second.dn<100:
#         second.dn+=1
#     play+=1
#     if first.dn&second.dn==100:
#         break
# print(play)

# arr=list(input().split())
# for i in range(5):
#     print(*arr)
#     for z in range(1):
#         arr.remove(arr[z])

# arr=[]
# for i in range(3):
#     brr=list(map(int,input().split()))
#     arr.append(brr)
# Sum=0
# for i in range(3):
#     for z in range(3):
#         if i>=z:
#             Sum+=arr[i][z]
# print(Sum)

# vect=[3,5,1,1,2,3,2]
# arr=list(map(int,input().split()))
# for i in range(4):
#     Coun=vect.count(arr[i])
#     print(f'{arr[i]}={Coun}개')

# arr=list(map(int,input().split()))
# arr.sort(reverse=True)
# print(*arr,sep='')

# Str=input()
# new=sorted(Str)
# print(*new,sep='')

# arr=[10,50,40,20,30,40]
# brr=[0]*6
# brr=list(map(int,input().split()))
# for i in range(6):
#     Coun=0
#     for z in range(6):
#         if brr[i]<arr[z]:
#             Coun+=1
#     print(f'{brr[i]}={Coun}개')

# a,b=input().split()
# point1=a
# point2=b
# a=point2
# b=point1
# print(a,b)

# shape=int(input())
# arr=[]
# if shape==1:
#     for i in range(5):
#         brr=list(map(int,input().split()))
#         arr.append(brr)
#     for i in range(5):
#         for z in range(5):
#             if i>=z:
#                 print(arr[i][z],end=' ')
#         print()
# if shape==2:
#     for i in range(5):
#         brr=list(map(int,input().split()))
#         arr.append(brr)
#     for i in range(5):
#         for z in range(5):
#             if 4-i>=z:
#                 print(arr[i][z],end=' ')
#         print()

# a=int(input())
# i=0
# while i<3:
#     z=0
#     while z<5:
#         print(a,end='')
#         z+=1
#     print()
#     i+=1

# class Mart:
#     def __init__(self):
#         self.딸기=0
#         self.메론=0
#         self.수박=0
# A=Mart()
# A.딸기=300
# A.메론=500
# A.수박=1000
# B=Mart()
# B.딸기=450
# B.메론=450
# B.수박=900
# C=Mart()
# C.딸기=200
# C.메론=150
# C.수박=700
# a=input()
# print(round((a.딸기+a.메론+a.수박)/3))

# class Mart:
#     def __init__(self,a,b,c):
#         self.딸기=a
#         self.메론=b
#         self.수박=c
#     def aver(self):
#         return round(((self.딸기)+(self.메론)+(self.수박))/3)
# marts={'A':Mart(300,500,1000),
#         'B':Mart(450,450,900),
#         'C':Mart(200,150,700)}
# shop=input()
# print(marts[shop].aver())

stat1,stat2=input().split()
new1=sorted(stat1)
new2=sorted(stat2)
print(new1,new2,end='')