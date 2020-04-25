import os
import tempfile
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')
args = parser.parse_args()
#print(args.key,args.val)

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

with open(storage_path, 'r') as f:
    s= f.read()
    if not s:
        base = dict()
    else:
        base = eval(s)

if args.key and args.val:
    if not base.get(args.key, None):
        base[args.key] = args.val
    else:
        base[args.key] += f', {args.val}'
    with open(storage_path, 'w') as f:
        f.write(str(base))

elif args.key and not args.val:
    if(base.get(args.key, None)):
        print(base[args.key])
    else:
        print("No item for such key")
