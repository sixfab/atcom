
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
le910c1_comp1 = Modem(vid="1bc7", pid="1201", vendor_name="Telit", product_name="LE910C1", com_ifs="if04")
le910c1_comp2 = Modem(vid="1bc7", pid="1206", vendor_name="Telit", product_name="LE910C1", com_ifs="if05")
me910c1_comp1 = Modem(vid="1bc7", pid="1101", vendor_name="Telit", product_name="ME910C1", com_ifs="if01")
me910c1_comp2 = Modem(vid="1bc7", pid="1102", vendor_name="Telit", product_name="ME910C1", com_ifs="if01")
fn980n_comp1 = Modem(vid="1bc7", pid="1050", vendor_name="Telit", product_name="FN980n", com_ifs="if05")
fn980n_comp3 = Modem(vid="1bc7", pid="1053", vendor_name="Telit", product_name="FN980n", com_ifs="if05")

# List of supported modem
supported_modems = [
    ec25,
    ec21,
    le910c1_comp1,
    le910c1_comp2,
    me910c1_comp1,
    me910c1_comp2,
    bg96,
    bg95,
    ep06,
    fn980n_comp1,
    fn980n_comp3,
    ]