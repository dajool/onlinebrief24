# -*- coding: utf-8 -*-

import paramiko


class Client(object):
    """\
    Client for OnlineBrief24.de.
    """

    def __init__(self, username, password):
        self.host = "localhost"
        self.port = 22
        self.username = username
        self.password = password
        self.upload_path = "/home/breuer/foo"
        self.sftp = None

    def __enter__(self):
        """\
        Enter the with-statement and return self so that it can be used as 'as'.
        """
        self.login()
        return self

    def __exit__(self, type, value, traceback):
        """\
        Exit the with-statement and disconnect from the sftp server.
        """
        self.disconnect()


    def login(self):
        """\
        Login to the sftp server.
        """
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username = self.username, password = self.password)
        self.sftp = paramiko.SFTPClient.from_transport(transport)


    def upload(self, path_to_file):
        """\
        Upload file to the sftp server.
        Possible kwargs:
           * color
           * duplex
           * envelope
           * distribution
           * registered
        """
        self.sftp.put(path_to_file, self.upload_path)
        pass


    def disconnect(self):
        self.sftp.close()

