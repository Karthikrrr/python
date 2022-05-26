try:
def f():
z=['foo','bar']
for i in z:
if i == 'foo':
except IndentationError as e:
print(e)