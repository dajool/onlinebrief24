import paramiko

class Client(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.sftp = None


    def login():
        # todo: login to the ssh server with paramiko
        # transport = paramiko.Transport((myhost, 22))
        # transport.connect(username = self.username, password = self.password)
        # self.sftp = paramiko.SFTPClient.from_transport(transport)
        pass


    def upload(path_to_file):
        # todo: upload file to server
        # possible kwargs:
        #    * color
        #    * duplex
        #    * envelope
        #    * distribution
        #    * registered
        #
        # self.sftp.put(path_to_file, remote_path)
        pass


    def disconnect():
        self.sftp.close()

