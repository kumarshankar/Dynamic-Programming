import msgpack
import json
import random


def msg_pack_example_1():
    example_dict ={str(i) : random.random() for i in range(1000)}

    with open("json_file.json",'w') as f:
        json.dump(example_dict, f)

    with open("json_file.json") as f:
        back_from_json = json.load(f)


    # saving and loading as msgpack

    with open("msgpack_file.msgpack", "wb") as f:
        f.write(msgpack.packb(example_dict))

    with open("msgpack_file.msgpack", "rb") as f:
        back_from_msg_pack = msgpack.unpackb(f.read())


    # Data integrity

    print(type(next(iter(back_from_json.keys()))))
    print(type(next(iter(back_from_msg_pack.keys()))))


if __name__ == "__main__":
    msg_pack_example_1()