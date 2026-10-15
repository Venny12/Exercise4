"""Validators: functions that answer yes/no. Every validator RETURNS True or False (never prints)."""


def is_in_range(value, low, high):
    """Return True if low <= value <= high (both ends included)."""
    # TODO: one comparison; Python allows low <= value <= high
    if low <= value <= high:
        return True
    return False


def is_valid_test_id(test_id, prefix="TC", digits=3):
    """Return True for IDs like 'TC-007': the prefix, a dash, then exactly `digits` digits."""
    if not test_id.startswith(prefix):
        return False
    suffix = test_id[len(prefix) + 1:]
    if not suffix.isdigit():
        return False
    if len(suffix) != digits:
        return False
    return True


# ------------------ person B

def is_valid_email(email):
    """Return True for a simple email shape (a deliberately simple teaching version).

    Rules: no spaces, exactly one '@', something before the '@',
    and a domain that contains a '.' but does not start or end with one.
    """
    if " " in email:
        return False

    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    if not username:
        return False

    if "." not in domain:
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    return True


#--------------- person B
def is_strong_password(password, min_length=8):
    """Return True if the password has at least `min_length` characters and
    contains at least one uppercase letter, one lowercase letter and one digit."""
    if len(password) < min_length:
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    for character in password:
        if character.isupper():
            has_upper = True
        if character.islower():
            has_lower = True
        if character.isdigit():
            has_digit = True

    return has_upper and has_lower and has_digit

def is_valid_status_code(code):
    """Return True for HTTP status codes from 100 to 599. Reuses is_in_range."""
    # TODO: ONE line: reuse is_in_range
    return is_in_range(code,100,599)



#------------------ person B
def all_pass(value, *checks):
    """Return True only if EVERY check function returns a true value for `value`.

    With no checks at all, return True.
    Example: all_pass("TC-001", is_valid_test_id, lambda s: s.endswith("1"))
    """
    for check in checks:
        if not check(value):
            return False

    return True