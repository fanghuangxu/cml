def get_forge_mod():
    import requests as w
    json=w.get('https://fanghuangxu.github.io/mcl_mod/mod.json')
    json=json.json()
    mod_list=[]
    for mod in json['forge']:
        mod_list.append(mod)
    return mod_list
def get_fabric_mod():
    import requests as w
    json=w.get('https://fanghuangxu.github.io/mcl_mod/mod.json')
    json=json.json()
    mod_list=[]
    for mod in json['fabric']:
        mod_list.append(mod)
    return mod_list
