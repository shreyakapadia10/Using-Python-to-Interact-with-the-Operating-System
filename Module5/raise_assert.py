def validate_username(username, minlen):
    """ To check whether the given username is valid and of minimum length provided """

    assert type(username) == str, "Username must be string"

    if minlen < 1:
        raise ValueError("Minimum Length should be atleast 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True
