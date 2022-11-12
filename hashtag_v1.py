
var= input()

if var.startswith("#"):
    print(True)
else:
    print(False)
    var="#"+var
print(var)