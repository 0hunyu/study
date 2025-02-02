# a,b=map(int,input().split())
# c,d=input().split()
# p1=a
# p2=b
# p3=c
# p4=d
# for i in range(p1):
#     print(p3,end='')
# print()
# for i in range(p2):
#     print(p4,end='')

# mat=[['D','A','D'],
#      ['Q','W','Q'],
#      ['A','S','D'],
#      ['A','S','D']]
# def main():
#     a=input()
#     find(a)
# def find(a):
#     b=0
#     for i in range(4):
#         for z in range(3):
#             if mat[i][z]==a:
#                 b+=1
#     if b>0:
#         print('존재')
#     else:
#         print('없음')
# main()

# mat=[[0]*5 for _ in range(5)]
# num=int(input())
# for i in range(5):
#     for z in range(5):
#         if (i==0)|(i==4)|(z==0)|(z==4):
#             mat[i][z]=num
#         else:
#             mat[i][z]='_'
# for i in range(5):
#     for z in range(5):
#         print(mat[i][z],end='')
#     print()

# mat=[[4,5,4,5,4],
#      [8,9,8,9,8],
#      [1,2,1,2,1],
#      [4,5,4,5,4],
#      [6,7,6,7,6]]
# for i in range(5):
#     a,b=map(int,input().split())
#     mat[a][b]+=1
#     if mat[a][b]==10:
#         mat[a][b]=0
# for i in range(5):
#     for z in range(5):
#         print(mat[i][z],end='')
#     print()

# def main():
#     vect=input()
#     b=len(vect)
#     cou=vect.count(vect[b-1])
#     print(b)
#     print(cou)
# main()

# a=input()
# b=input()
# c=input()
# if (len(a)>len(b))|(len(a)>len(c)):
#     print(a)
# elif (len(b)>len(a))|(len(b)>len(c)):
#     print(b)
# else:
#     print(c)

# num=int(input())
# mat=[[0]*3 for _ in range(3)]
# for i in range(3):
#     for z in range(3):
#         if (2-i)<=z:
#             mat[i][z]=num
#             num+=1
#         else:
#             mat[i][z]=0
# for i in range(3):
#     for z in range(3):
#         print(mat[i][z],end='')
#     print()

# def main():
#     a,b=getName()
#     if ord(a)>ord(b):
#         print(b)
#     else:
#         print(a)
# def getName():
#     a,b=input().split()
#     return a,b
# main()

# def main():
#     age=int(input())
#     result=moom(age)
#     print(*result)
# def moom(age):
#     arr=[0]*3
#     arr[0]=age-4
#     arr[1]=age+3
#     arr[2]=age*2
#     return arr
# main()

# def main():
#     Str=input()
#     result=stringLen(Str)
#     print(f'{result}글자')
# def stringLen(Str):
#     return len(Str)
# main()

# def main():
#     a,b=map(int,input().split())
#     SUM,GOP=ABC(a,b)
#     print(SUM,GOP)
# def ABC(a,b):
#     return a+b,a*b
# main()

# def main():
#     a,b=KFC()
#     print(f'대문자{a}개\n소문자{b}개')
# def KFC():
#     a=0
#     b=0
#     Str=input()
#     for i in Str:
#         if i.isupper():
#             a+=1
#         else:
#             b+=1
#     return a,b
# main()

# mat=[[4,5,6,1,3,1],
#      [2,1,3,6,3,6]]
# def INPUT():
#     a,b,c=map(int,input().split())
#     return a,b,c
# def process(a,b,c):
#     a_count=mat[0].count(a)+mat[1].count(a)
#     b_count=mat[0].count(b)+mat[1].count(b)
#     c_count=mat[0].count(c)+mat[1].count(c)
#     return a_count,b_count,c_count
# def output(a,b,c,A,B,C):
#     print(f'{a}={A}개')
#     print(f'{b}={B}개')
#     print(f'{c}={C}개')
# def main():
#     a,b,c=INPUT()
#     A,B,C=process(a,b,c)
#     output(a,b,c,A,B,C)
# main()

# mat=[['A','D','F'],
#      ['Q','W','E'],
#      ['Z','X','C']]
# def main():
#     alp=input()
#     x,y=find(alp)
#     print(f'{x},{y}')
# def find(a):
#     for i in range(3):
#         for z in range(3):
#             if mat[i][z]==a:
#                 coor_x=i
#                 coor_y=z
#                 break
#     return coor_x,coor_y
# main()

# def main():
#     arr=[3,5,1,2,7]
#     brr=[0]*5
#     brr=list(map(int,input().split()))
#     CompareGo(arr,brr)
# def CompareGo(arr,brr):
#     if arr==brr:
#         print("두배열은완전같음")
#     else:
#         print("두배열은같지않음")
# main()

# class PROFILE:
#     def __init__(self):
#         self.name=[]
#         self.age=0
#         self.weight=0
# person1=PROFILE()
# person2=PROFILE()
# person1.name=input()
# person1.age=int(input())
# person1.weight=int(input())
# person2.name=input()
# person2.age=int(input())
# person2.weight=int(input())
# print(f'{person1.name} & {person2.name}\n평균{round((person1.age+person2.age-0.00001)/2)}세\n평균{round((person1.weight+person2.weight)/2)}KG')

# distance=[4,2,5,1,6,7,3]
# a,b=input().split()
# total_distance=0
# for i in range(ord(a)-65,ord(b)-66):
#     total_distance+=distance[i+1]
# print(total_distance)

# mat=[[3,4,1,6],
#      [3,5,3,6],
#      [0,0,0,0],
#      [5,4,6,0]]
# arr=list(map(int,input().split()))
# for i in range(4):
#     mat[2][i]=arr[i]
# MAX=-1
# MIN=1
# MAX_x=0
# MIN_x=0
# MAX_y=0
# MIN_y=0
# for i in range(4):
#     for z in range(4):
#         if MAX<mat[i][z]:
#             MAX=mat[i][z]
#             MAX_x=i
#             MAX_y=z
#         if MIN>mat[i][z]:
#             MIN=mat[i][z]
#             MIN_x=i
#             MIN_y=z
# print(f'MAX={MAX}({MAX_x},{MAX_y})\nMIN={MIN}({MIN_x},{MIN_y})')

# mat=[['4','5','7','1','3','2'],
#      ['D','F','Q','W','G','Z']]
# num=int(input())
# for i in range(6):
#     if int(mat[0][i])==num:
#         print(mat[1][i])

# def main():
#     stat_1=input()
#     stat_2=input()
#     A,B,C=FindABC(stat_1,stat_2)
#     print(f'A:{A}\nB:{B}\nC:{C}')
# def FindABC(a,b):
#     count_A=a.count('A')
#     count_A+=b.count('A')
#     count_B=a.count('B')
#     count_B+=b.count('B')
#     count_C=a.count('C')
#     count_C+=b.count('C')
#     return count_A,count_B,count_C
# main()

# mat=[['D','A','S'],
#      ['Q','W','V'],
#      ['R','T','Y']]
# def main():
#     y_1,x_1=map(int,input().split())
#     y_2,x_2=map(int,input().split())
#     apl_1,apl_2=Find(y_1,x_1,y_2,x_2)
#     print(apl_1,apl_2)
# def Find(x,y,z,w):
#     apl1=mat[x][y]
#     apl2=mat[z][w]
#     return apl1,apl2
# main()

# A=input()
# B=input()
# C=input()
# if A==B and B==C:
#     print('YES')
# else:
#     print("NO")

# a,b=map(int,input().split())
# while True:
#     print(a,end=' ')
#     a+=1
#     if a==b+1:
#         break

# brr=[[0]*4 for _ in range(5)]
# for i in range(5):
#     for z in range(1):
#         arr=list(map(int,input().split()))
#     brr[i]=arr
# for i in range(5):
#     b=0
#     for z in brr[i]:
#         b+=z
#     print(b,end=' ')