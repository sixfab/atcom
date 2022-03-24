
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

        
supported_modems = [
    # Quectel
    Modem(vid="2c7c", pid="0125", vendor_name="Quectel", product_name="EC25", com_ifs="if02"),
    Modem(vid="2c7c", pid="0121", vendor_name="Quectel", product_name="EC21", com_ifs="if02"),
    Modem(vid="2c7c", pid="0296", vendor_name="Quectel", product_name="BG96", com_ifs="if02"),
    Modem(vid="2c7c", pid="0700", vendor_name="Quectel", product_name="BG95", com_ifs="if02"),
    Modem(vid="2c7c", pid="0306", vendor_name="Quectel", product_name="EP06", com_ifs="if02"),
    Modem(vid="2c7c", pid="0800", vendor_name="Quectel", product_name="RM5XXQ", com_ifs="if02"),

    # Telit
    Modem(vid="1bc7", pid="1201", vendor_name="Telit", product_name="LE910Cx RMNET", com_ifs="if04"), # rmnet
    Modem(vid="1bc7", pid="1203", vendor_name="Telit", product_name="LE910Cx RNDIS", com_ifs="if05"), # rndis
    Modem(vid="1bc7", pid="1204", vendor_name="Telit", product_name="LE910Cx MBIM", com_ifs="if05"), # mbim
    Modem(vid="1bc7", pid="1206", vendor_name="Telit", product_name="LE910Cx ECM", com_ifs="if05"), # ecm
    Modem(vid="1bc7", pid="1031", vendor_name="Telit", product_name="LE910Cx ThreadX RMNET", com_ifs="if02"), # rmnet
    Modem(vid="1bc7", pid="1033", vendor_name="Telit", product_name="LE910Cx ThreadX ECM", com_ifs="if02"), # ecm
    Modem(vid="1bc7", pid="1034", vendor_name="Telit", product_name="LE910Cx ThreadX RMNET", com_ifs="if00"), # rmnet
    Modem(vid="1bc7", pid="1035", vendor_name="Telit", product_name="LE910Cx ThreadX ECM", com_ifs="if00"), # ecm
    Modem(vid="1bc7", pid="1036", vendor_name="Telit", product_name="LE910Cx ThreadX OPTION ONLY", com_ifs="if00"), # just option driver

    Modem(vid="1bc7", pid="1101", vendor_name="Telit", product_name="ME910C1", com_ifs="if01"),
    Modem(vid="1bc7", pid="1102", vendor_name="Telit", product_name="ME910C1", com_ifs="if01"),

    Modem(vid="1bc7", pid="1052", vendor_name="Telit", product_name="FN980 RNDIS", com_ifs="if05"), # rndis
    Modem(vid="1bc7", pid="1050", vendor_name="Telit", product_name="FN980 RMNET", com_ifs="if04"), # rmnet
    Modem(vid="1bc7", pid="1051", vendor_name="Telit", product_name="FN980 MBIM", com_ifs="if05"), # mbim
    Modem(vid="1bc7", pid="1053", vendor_name="Telit", product_name="FN980 ECM", com_ifs="if05"), # ecm

    # Thales
    Modem(vid="1e2d", pid="0069", vendor_name="Thales/Cinterion", product_name="PLSx3", com_ifs="if04"), # ecm
    Modem(vid="1e2d", pid="006f", vendor_name="Thales/Cinterion", product_name="PLSx3", com_ifs="if04"), # wwan
]
