import os


def downver(mc_dir,version):
    import json,requests
    with open(f'{mc_dir}\\versions\\{version}\\{version}.json','r') as json_file:
        server_url=json.loads(json_file.read())
    server_url=server_url["downloads"]['server']['url']
    print(f"downloading {version}.jar URL:{server_url}")
    server_jar=requests.get(url=server_url)
    with open(f'{mc_dir}\\versions\\{version}\\{version}_server.jar','w') as file:
        file.write(str(server_jar))
    try:
        with open(f'{mc_dir}\\server.txt','a') as filae:
            filae.write('\n'+str(version))
    except FileNotFoundError:
        with open(f'{mc_dir}\\server.txt','w') as filae:
                filae.write(str(version))        
    return 'exit'

def run_server(mc_dir=str(),version=str()):
     os.system(f'cd {mc_dir}\\version\\{version}')
     os.system(f'{version}_server.jar')