def lower_dict(d):
   new_dict = dict((k.lower(), v.lower()) for k, v in d.items())
   return new_dict
a ={"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
    "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6"
      , "aquamarine4": "#458b74", "azure1": "#f0ffff"}
b=(lower_dict(a))
#print(b)

Color_Code = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
              "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6"
              , "aquamarine4": "#458b74", "azure1": "#f0ffff"}
print (Color_Code)
color = str(input("Enter color name: "))
while color != "":

    if color in b:
        print(b[color])
    elif color in Color_Code:
        print(Color_Code[color])
    else:
        print("invalid")


    color = str(input("Enter color name: "))