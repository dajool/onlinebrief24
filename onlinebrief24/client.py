# -*- coding: utf-8 -*-

import os
import ntpath
import paramiko


LETTER_ENVELOPE_FORMATS = {
    'din_lang': 0,
    'c4': 1,
}

LETTER_DISTRIBUTION_FORMATS = {
    'auto': 0,
    'national': 1,
    'international': 2,
}

LETTER_REGISTERED_OPTIONS = {
    'none': 0,
    'insertion': 1,
    'standard': 2,
    'personal': 3,
}


LETTER_PAYMENT_SLIP_OPTIONS = {
    'none': 0,
    'national': 1,
    'sepa': 2,
}


class Letter(object):
    """\
    Conversion from local PDF file to remote PDF file.
    """

    def __init__(self, path_to_pdf_file, color=True, duplex=True, envelope='din_lang',
                 distribution='auto', registered=None, payment_slip=None, cost_center=None, test=False):
        """\
        Initializing and checking values.
        """

        self.local_filename = ntpath.basename(path_to_pdf_file)
        self.test = test
        self.color = color
        self.duplex = duplex
        registered = 'none' if registered is None else registered
        payment_slip = 'none' if payment_slip is None else payment_slip

        if envelope in LETTER_ENVELOPE_FORMATS.keys():
            self.envelope = envelope
        else:
            raise ValueError(
                'keyword envelope should be on of those: %s' % ", ".join(LETTER_ENVELOPE_FORMATS.keys()))

        if distribution in LETTER_DISTRIBUTION_FORMATS.keys():
            self.distribution = distribution
        else:
            raise ValueError(
                'keyword distribution should be on of those: %s' % ", ".join(LETTER_DISTRIBUTION_FORMATS.keys()))

        if registered in LETTER_REGISTERED_OPTIONS.keys():
            self.registered = registered
        else:
            raise ValueError(
                'keyword registered should be on of those: %s' % ", ".join(LETTER_REGISTERED_OPTIONS.keys()))

        if payment_slip in LETTER_PAYMENT_SLIP_OPTIONS.keys():
            self.payment_slip = payment_slip
        else:
            raise ValueError(
                'keyword payment_slip should be on of those: %s' % ", ".join(LETTER_PAYMENT_SLIP_OPTIONS.keys()))

        # cost_center should be a string and not longer than 18 characters.
        if cost_center is not None:
            if not isinstance(cost_center, basestring):
                raise ValueError("cost_center must be a string.")

            if len(cost_center) < 18:
                self.cost_center = cost_center
            else:
                raise ValueError(
                    'cost_center should not be longer than 18 chars. Yours is %s chars long.' % (len(cost_center), ))
        else:
            self.cost_center = None

        self.remote_filename = self._generate_remote_filename()

    def get_remote_filename(self):
        """\
        Returns the remote filename.
        """
        return self.remote_filename

    def _generate_remote_filename(self):
        """\
        Generates the remote filename with the options and the local filename. The remote filename should follow
        this pattern: 0000000000000-filename.pdf or 0000000000000-filename#cost_center#.pdf
        The fist 6 digits are used at the moment. Digits 7 to 13 should always be zero.
        Chars that are officially allowed in the filename: A-Z a-z 0-9 . - _ #
        """
        if self.test:
            remote_filename = "TEST_"
        else:
            remote_filename = ""
        remote_filename += str(int(self.color))
        remote_filename += str(int(self.duplex))
        remote_filename += str(LETTER_ENVELOPE_FORMATS.get(self.envelope))
        remote_filename += str(LETTER_DISTRIBUTION_FORMATS.get(self.distribution))
        remote_filename += str(LETTER_REGISTERED_OPTIONS.get(self.registered))
        remote_filename += str(LETTER_PAYMENT_SLIP_OPTIONS.get(self.payment_slip))
        remote_filename += "0000000-"
        if self.cost_center:
            filename, file_extension = os.path.splitext(self.local_filename)
            remote_filename += filename + "#" + self.cost_center + "#" + file_extension
        else:
            remote_filename += self.local_filename
        print remote_filename
        return remote_filename


class Client(object):
    """\
    Client for OnlineBrief24.de.
    """

    def __init__(self, username, password, host="api.onlinebrief24.de", port=22, upload_path="/upload/api"):
        # host, port and upload_path should only be changed for testing.
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.upload_path = upload_path
        self.sftp = None

    def __enter__(self):
        """\
        Enter the with-statement and return self so that it can be used as 'as'.
        """
        self.login()
        return self

    def __exit__(self, type, value, traceback):
        """\
        Exit the with-statement, disconnect from the sftp server.
        """
        self.disconnect()

    def login(self):
        """\
        Login to the sftp server.
        """
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.password)
        self.sftp = paramiko.SFTPClient.from_transport(transport)

    def upload(self, path_to_file, **kwargs):
        """\
        Upload file to the sftp server.
        Possible kwargs:
           * color
           * duplex
           * envelope
           * distribution
           * registered
           * payment_slip
           * cost_center
           * test
        """
        letter = Letter(path_to_file, **kwargs)
        self.sftp.put(path_to_file, os.path.join(self.upload_path, ntpath.basename(letter.get_remote_filename())))

    def disconnect(self):
        """\
        Disconnect from the sftp server.
        """
        self.sftp.close()
