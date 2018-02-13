import base64
class mytokeng():
    def generate(self,username,password):
        encoded = base64.b64encode(bytes(username))
        return encoded;
