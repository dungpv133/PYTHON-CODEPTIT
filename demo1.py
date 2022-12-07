OPERATION_PERMISSION = { 'read': 'R', 'write': 'W', 'execute': 'X', } 
ﬁle_permissions = {} 
for i in range(int(input())): 
    ﬁle, *permissions = input().split() 
    ﬁle_permissions[ﬁle] = set(permissions) 
for i in range(int(input())): 
    operation, ﬁle = input().split() 
    if OPERATION_PERMISSION[operation] in ﬁle_permissions[ﬁle]: 
        print('OK') 
    else: 
        print('Access denied')

