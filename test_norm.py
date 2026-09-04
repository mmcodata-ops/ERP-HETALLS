def normalize_portal(portal: str) -> str:
    p = portal.upper()
    if 'ETSY' in p and 'MKM' in p:
        return 'ETSY-MKM'
    return p
print(normalize_portal('ETSY -MKM HOMES CRAFT'))
