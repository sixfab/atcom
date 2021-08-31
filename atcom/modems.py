
class Modem():
    desc_vendor=None
    desc_product=None

    def __init__(
        self, 
        vid, 
        pid, 
        vendor_name, 
        product_name, 
        com_ifs
        ):
        self.vid = vid
        self.pid = pid
        self.vendor_name = vendor_name
        self.product_name = product_name
        self.com_ifs = com_ifs
    
# Quectel 
ec25 = Modem(vid="2c7c", pid="0125", vendor_name="Quectel", product_name="EC25", com_ifs="if02")
ec21 = Modem(vid="2c7c", pid="0121", vendor_name="Quectel", product_name="EC21", com_ifs="if02")
bg96 = Modem(vid="2c7c", pid="0296", vendor_name="Quectel", product_name="BG96", com_ifs="if02")
bg95 = Modem(vid="2c7c", pid="0700", vendor_name="Quectel", product_name="BG95", com_ifs="if02")
ep06 = Modem(vid="2c7c", pid="0306", vendor_name="Quectel", product_name="EP06", com_ifs="if02")

# Telit
le910cx_comp1 = Modem(vid="1bc7", pid="1201", vendor_name="Telit", product_name="LE910Cx", com_ifs="if04")
le910cx_comp2 = Modem(vid="1bc7", pid="1206", vendor_name="Telit", product_name="LE910Cx", com_ifs="if05")
me910c1_comp1 = Modem(vid="1bc7", pid="1101", vendor_name="Telit", product_name="ME910C1", com_ifs="if01")
me910c1_comp2 = Modem(vid="1bc7", pid="1102", vendor_name="Telit", product_name="ME910C1", com_ifs="if01")

# Thales
plsx3_comp1 = Modem(vid="1e2d", pid="0069", vendor_name="Thales/Cinterion", product_name="PLSx3", com_ifs="if04") # ecm
plsx3_comp2 = Modem(vid="1e2d", pid="006f", vendor_name="Thales/Cinterion", product_name="PLSx3", com_ifs="if04") # wwan

# List of supported modem
supported_modems = [
    ec25,
    ec21,
    le910cx_comp1,
    le910cx_comp2,
    me910c1_comp1,
    me910c1_comp2,
    bg96,
    bg95,
    ep06,
    plsx3_comp1,
    plsx3_comp2,
    ]