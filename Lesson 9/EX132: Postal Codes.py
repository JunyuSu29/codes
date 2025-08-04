def canadian_postal_code(code):
    provinces={"A":"Newfoundland",
              "B":"Nova Scotia",
              "C":"PEI",
              "E":"New Brunswick",
              "G":"Quebec",
              "H":"Quebec",
              "J":"Quebec",
              "K":"Ontario",
              "L":"Ontario",
              "M":"Ontario",
              "N":"Ontario",
              "P":"Ontario",
              "R":"Manitoba",
              "S":"Saskatchewan",
              "T":"Alberta",
              "V":"British Columbia",
              "X": "Nunavut or NW Territories",
              "Y":"Yukon"}
    if len(code)!=6 or (code[0] not in provinces) or (code[1].isdigit()==False) or (code[2].isdigit()==True):
        return "Error! This postal code is not a valid Canadian Postal Code"
    
    the_province_letter=code[0]
    province=provinces[the_province_letter]
    if code[1]=='0':
        status="rural"
    else:
        status="urban"
    
    return (province,status)
print(canadian_postal_code("N2J0E9"))
