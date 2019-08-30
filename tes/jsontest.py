import json
import numpy as np

d = {'a': [1], 'b': [2, 3]}
d = str(d)
print(d)

d = json.dumps(d)
# print(type(d))
d = json.loads(str(d))
print(d)
# l = []
# l1 = np.array([1, 2])
# l2 = np.array([2, 3])
# l.append(l1.tolist())
# l.append(l2.tolist())
# print(l)
test_dict = {'a': 1, 'b': [2, 3]}
print(test_dict)
print(type(test_dict))
json_str = json.dumps(test_dict)
print(json_str)
print(type(json_str))
new_dict = json.loads(json_str)
print(new_dict)
print(type(new_dict))
new_dict = json.loads(json_str)
print(new_dict)
print(type(new_dict))
with open('./record.json', 'w') as f:
    json.dump(new_dict, f)
#     print('加载完成')
with open('./receive_file/meeting2_34825.json', 'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)
#     print(type(load_dict))
# load_dict['c'] = [i for i in range(10)]
# with open('./record.json', 'w') as dump_f:
#     json.dump(load_dict, dump_f)

