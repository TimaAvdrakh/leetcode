def numUniqueEmails(emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    unique = set()
    for email in emails:
        i = email.index('@')
        if '+' in email[:i]:
            j = email.index('+')
            new_name = email[:j].replace('.','') + "@" + email[i:]
        else:
            new_name = email[:i].replace('.','') + "@" + email[i:]
        unique.add(new_name)
    return len(unique)
numUniqueEmails(['email@gmail.com','eqwer@gmail.com'])