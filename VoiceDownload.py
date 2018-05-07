from suds.client import Client
import urllib

accountId = "Aumali"
password = "This15=Rddt!g3R5"
soapclient = Client("https://cerevoice.com/soap/soap_1_1.php?WSDL")

def request(text, voice="Jess", audioFormat="wav"):
    """
    Makes a SOAP request to the CereProc Cloud API
    to synthesise voice for the given text.

    Args:
      text:  Message to synthesise.
      voice: Voice to be used for synthesis.

    Returns:
      Reply from SOAP request.
    """
    return soapclient.service.speakExtended(accountId, password, \
                                            voice, text, audioFormat, 22050, False, False)

def download(text, voice="Jess", audioFormat="wav", file=""):
    """
    Downloads a synthesised voice audio file and
    saves to the given filename. If no filename is
    provided, the following format is used:
      <voice>_<text>.<format>

    Args:
      text:        Message to synthesis.
      voice:       Voice to be used for synthesis.
      audioFormat: Format of audio file.
      file:        Output filename.

    Returns:
      Download status as boolean.
    """
    reply = request(text, voice, audioFormat)

    if file == "":
        file = "%s_%s.%s" % (voice, text, audioFormat)

    if reply.resultCode != 1:
        print("Unable to download file:", reply.resultDescription)
        return False
    else:
        urllib.urlretrieve(reply.fileUrl, file)
        print("Retrieved synthesised voice for '%s'" % text)
        return True
