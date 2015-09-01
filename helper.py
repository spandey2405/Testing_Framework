import xlrd

def get_ipv6(m_name, workbook):
    workbook = xlrd.open_workbook(workbook)
    worksheet = workbook.sheet_by_name('Sheet1')
    a = True
    row = 1
    column = 0
    mote_name = m_name
    Mote_IPv6 = None
    while(a==True):
        Mote_Name = worksheet.cell(row, column).value
        if mote_name == Mote_Name:
            Mote_IPv6= worksheet.cell(row, column+1).value
            a=False
        row = row +1
        if (Mote_Name == "END"):
            a=False

    return Mote_IPv6

def get_name(m_ipv6,workbook):

    workbook = xlrd.open_workbook(workbook)
    worksheet = workbook.sheet_by_name('Sheet1')
    a = True
    row = 1
    column = 0
    mote_ipv6 = m_ipv6
    Mote_Name = None
    while(a==True):
        Mote_IPv6 = worksheet.cell(row, column+1).value
        if mote_ipv6 == Mote_IPv6:
            Mote_Name= worksheet.cell(row, column).value
            a=False
        row = row +1
        if (Mote_Name == "END"):
            a=False

    return Mote_Name

def get_motes_with_name(BR,endpoint,workbook):
    import fetch
    motes = fetch.get_motes(BR,endpoint)
    for mote in motes:
        Name = get_name(mote,workbook)
        print("Mote IPv6 : " + mote + "\tMote Name : " + Name)

    print "\n"


def draw_graph(BR,endpoint,workbook):
    import networkx
    import matplotlib.pyplot as plt
    import fetch
    import layout
    lables = {}
    lables["BR"]= "BR"
    graph_obj = networkx.DiGraph()
    nodes = fetch.get_motes(BR,endpoint)
    graph_obj.add_node("BR")
    for node in nodes:
        graph_obj.add_node(node)

    edges = fetch.get_routes(BR,endpoint)
    for edge in edges:
        edge = edge.split('->')
        source = edge[1]
        destination = edge[0]
        Name = get_name(edge[0],workbook)
        lables[edge[0]]= Name
        if source == destination:
            graph_obj.add_edge("BR",destination)
        else:
            graph_obj.add_edge(source,destination)


    pos = layout.get_pos(graph_obj)
    networkx.draw_networkx_labels(graph_obj, pos,labels=lables,font_color="black", font_size=8,font_weight='bold')
    networkx.draw(graph_obj, pos,nodelist = ["BR"], node_color="Blue", node_size=2000,node_shape="p")
    networkx.draw(graph_obj, pos,nodelist = nodes, node_color="green",node_size=1000,node_shape="s")
    plt.show()

