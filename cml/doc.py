def open_minecraft_docs(version:str):
    url = 'https://zh.minecraft.wiki/w/Java版{version}'
    import webbrowser
    webbrowser.open(url.format(version=version))


