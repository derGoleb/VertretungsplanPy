import nextcloud_client
import os
import filecmp
import time


def download():
    nc = nextcloud_client.Client('https://cloud.hhgdo.de')

    nc.login('gabriel', 'gpph12')

    nc.get_file("/Vertretungsplan/heute/subst_001.htm")
    heute_change = not filecmp.cmp("subst_001.htm", "heute.htm", shallow=False)
    if heute_change:
        os.rename("subst_001.htm","heute.htm")
    else:
        os.remove("subst_001.htm")

    nc.get_file("/Vertretungsplan/morgen/subst_001.htm")
    morgen_change = not filecmp.cmp("subst_001.htm", "morgen.htm", shallow=False)
    if morgen_change:
        os.rename("subst_001.htm","morgen.htm")
    else:
        os.remove("subst_001.htm")

    return heute_change or morgen_change

