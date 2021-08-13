# -*- coding: utf-8 -*-
# import usb.core
# import usb.util
#
#
# import os
# """Demo program to print to the POS58 USB thermal receipt printer. This is
# labeled under different companies, but is made by Zijiang. See
# http:zijiang.com"""
#
# # In Linux, you must:
# #
# # 1) Add your user to the Linux group "lp" (line printer), otherwise you will
# #    get a user permissions error when trying to print.
# #
# # 2) Add a udev rule to allow all users to use this USB device, otherwise you
# #    will get a permissions error also. Example:
# #
# #    In /etc/udev/rules.d create a file ending in .rules, such as
# #    33-receipt-printer.rules with the contents:
# #
# #   # Set permissions to let anyone use the thermal receipt printer
# #   SUBSYSTEM=="usb", ATTR{idVendor}=="0416", ATTR{idProduct}=="5011", MODE="666"
#
# # Find our device
# # 0416:5011 is POS58 USB thermal receipt printer
# dev = usb.core.find(idVendor=0x0416, idProduct=0x5011)
#
# # Was it found?
# if dev is None:
#     raise ValueError('Device not found')
#
# # Disconnect it from kernel
# needs_reattach = False
# if dev.is_kernel_driver_active(0):
#     needs_reattach = True
#     dev.detach_kernel_driver(0)
#
# # Set the active configuration. With no arguments, the first
# # configuration will be the active one
# dev.set_configuration()
#
# # get an endpoint instance
# cfg = dev.get_active_configuration()
# intf = cfg[(0, 0)]
#
# ep = usb.util.find_descriptor(
#     intf,
#     # match the first OUT endpoint
#     custom_match = \
#     lambda e: \
#         usb.util.endpoint_direction(e.bEndpointAddress) == \
#         usb.util.ENDPOINT_OUT)
#
# assert ep is not None
#
# # write the data
# ep.write('Hello, Alexander!\n\n')
# #         000000000111111111122222222223
# #         123456789012345678901234567890
# ep.write(' JOPA\n')
# # ep.write('facere aut. Modi placeat et\n')
# # ep.write('eius voluptate sint ut.\n')
# # ep.write('Facilis minima ex quia quia\n')
# # ep.write('consectetur ex ipsa. Neque et\n')
# # ep.write('voluptatem ipsa enim error\n')
# # ep.write('reprehenderit ex dolore.\n')
# ep.write('\n\n\n\n')
#
# dev.reset()
# if needs_reattach:
#     dev.attach_kernel_driver(0)
#     print("Reattached USB device to kernel driver")


import sys
import os
from escpos.printer import Usb

this_dir, this_filename = os.path.split(__file__)
GRAPHICS_PATH = os.path.join(this_dir, "")

def forecast_icon():
    image = GRAPHICS_PATH + "safaripdf.png"
    return image

def usage():
    print("usage: qr_code.py <content>")

def print_qr():
    content = f"ST00012|Name=ООО \"РКС-энерго\"|PersonalAcc=40702810655320183766|BankName=Северо-Западный банк ОАО \"Сбербанк России\"|BIC=044030653|CorrespAcc=30101810500000000653|PayeeINN=3328424479|PersAcc=1200034433|PaymPeriod=022021|Sum=624273|AddAmount=3441|Category=1300000693"

    p = Usb(0x0416, 0x5011, profile="POS-5890")
    # content = "google.com"

    p.image(forecast_icon())
    p.text(f"{content}")
    # p.qr(content, ec=3, center=True)
    # p.text("\n")
    # p.text("\n")
    # p.text("\n")
    # p.text("\n")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print_qr()
        sys.exit(1)

    # content = sys.argv[1]
    # # content = "google.com"
    #
    # # Adapt to your needs
    # p = Usb(0x0416, 0x5011, profile="POS-5890")
    # p.qr(content, center=True)

