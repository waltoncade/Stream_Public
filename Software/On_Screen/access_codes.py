filepath = "C:/Git/Stream/Software/On_Screen/DANGER"

def channel_codes():
    f = open("{}/codes.txt".format(filepath), "r+")
    r = f.readlines()
    ID = r[0].split('=')[1][:-1]
    Auth = r[1].split('=')[1][:-1]
    f.close()
    return ID, Auth

def bot_codes():
    f = open("{}/codes.txt".format(filepath), "r+")
    r = f.readlines()
    ID = r[2].split('=')[1][:-1]
    Auth = r[3].split('=')[1][:-1]
    Secret = r[4].split('=')[1][:-1]
    f.close()
    return ID, Auth, Secret

def app_codes():
    f = open("{}/codes.txt".format(filepath), "r+")
    r = f.readlines()
    ID = r[5].split('=')[1][:-1]
    Auth = r[6].split('=')[1][:-1]
    Secret = r[7].split('=')[1][:-1]
    f.close()
    return ID, Auth, Secret

if __name__ == "__main__":
    print(app_codes())