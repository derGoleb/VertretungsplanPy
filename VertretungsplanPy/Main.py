from xml.dom.minidom import parseString
from VertretungsplanParserSQL import parse_html_table as table_parse
from NextcloudDownloader import download
from TeacherAbbrevation import replace_abbreviations
from GetMyClasses import get_table_data
from CreateText import create_text
from CourseAbbrevation import remove_abb as course_abbrevation
from py_imessage import imessage
import time
from checkCache import checkCache,renewCache

my_courses = ["PL G1","M L1", "SW ZKZ2","E L2","BI G3","IF G2","EK G1","GE G1","SP G1","D G1"]
s_courses = ["PA G1","M L1", "SW ZKZ2","E L2","BI G1","GE ZKZ1","PL G2","S1 G2","SP G1","D G1"]

if download():


    table_parse("heute.htm","heute")
    table_parse("morgen.htm","morgen")

    replace_abbreviations("heute")
    replace_abbreviations("morgen")



    data_today = str(get_table_data("heute", "Q2", my_courses))
    data_tomorrow = str(get_table_data("morgen", "Q2", my_courses))

    str_today = create_text(data_today)
    str_tomorrow = create_text(data_tomorrow)
    final = "Dein Vertretungsplan\n\nHeute:\n"+str_today+"\nMorgen:\n"+str_tomorrow

    final = course_abbrevation(final).replace("\n","\r\n")
    if not checkCache(final, "g"):
        print(final)
        guid = imessage.send("gabriel.buechner@icloud.com", final)
        renewCache(final,"g")

    time.sleep(15)
    datas_today = str(get_table_data("heute", "Q2", s_courses))
    datas_tomorrow = str(get_table_data("morgen", "Q2", s_courses))

    strs_today = create_text(datas_today)
    strs_tomorrow = create_text(datas_tomorrow)
    finals = "Dein Vertretungsplan\n\nHeute:\n"+strs_today+"\nMorgen:\n"+strs_tomorrow

    finals = course_abbrevation(finals).replace("\n","\r\n")
    if not checkCache(finals, "s"):
        print(finals)
        guid = imessage.send("sarah.werthschulte@icloud.com", finals)
        renewCache(finals,"s")
    