import os , argparse , sys
import helper

parser = argparse.ArgumentParser()
parser.add_argument("-ip", default="10.10.10.210", help="Set Ip")
parser.add_argument("-endpoint", default="/w/v1/routes/", help="Set Ip")
parser.add_argument("-workbook", default="data/worksheet.xlsx", help="Set Ip")
args = parser.parse_args()
os.system("clear")
print "1. Get IPv6 From Mote Name\n2. Get Mote Name From IPV6\n3. Get All Motes Detail From Routes\n4. Draw Graph\n5. Exit\n\n"

class Detail():

    def Get(self):
        try:
            choice = int(raw_input(">>\t"))
        except:
            print "Please Input A Valid Choice from 1-5"
            self.Get()

        os.system("clear")

        if choice == 1:
            self.get_ipv6_from_mote_name()

        elif choice == 2:
            self.get_motename_from_ipv6()

        elif choice == 3:
            self.get_all_motes_detail()

        elif choice == 4:
            self.draw_a_graph()

        elif choice == 5:
            exit()

        else:
            print "false choice"

        self.detail_continue()


    def get_ipv6_from_mote_name(self):
        mote_name = raw_input(">> Input Mote Name :")
        ipv6 = helper.get_ipv6(mote_name,args.workbook)
        if ipv6:
            print("\n\nIPv6 : " + ipv6 + "Mote Name : " + mote_name + "\n\n")
        else:
            print "\n\nIPv6 Not Found In Database \n\n"
        self.detail_continue()


    def get_motename_from_ipv6(self):
        mote_ipv6 = raw_input(">> Input Mote IPv6 :")
        name = helper.get_name(mote_ipv6,args.workbook)
        if name:
            print("\n\nIPv6 : " + mote_ipv6 + " | Mote Name : " + name + "\n\n")
        else:
            print "\n\nName Not Found In Database \n\n"
        self.detail_continue()

    def get_all_motes_detail(self):
        helper.get_motes_with_name(args.ip,args.endpoint,args.workbook)
        self.detail_continue()


    def detail_continue(self):
        print "1. Get IPv6 From Mote Name\n2. Get Mote Name From IPV6\n3. Get All Motes Detail From Routes\n4. Draw Graph\n5. Exit\n\n"
        self.Get()


    def exit_system(self):
        sys.exit(0)

    def draw_a_graph(self):
        helper.draw_graph(args.ip,args.endpoint,args.workbook)
        return None

def init():
    a = Detail()
    a.Get()

if __name__ == '__main__':
    init()



