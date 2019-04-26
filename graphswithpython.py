from graph_app import Graph

OTU2path = { #variaveis de cliente
			"OTU2_XFEC" : ["OTU2"],
			"OTU2_GFEC" : ["OTU2"],
			"OTU2_FECdisabled" : ["OTU2"],
			"STM-64" : ["OTU2"],
			"10GbE_LAN73" : ["OTU2"],
			"FC8" : ["OTU2"],
			"10GbE_RateLimit" : ["OTU2"],
			
			#variaveis de FEC
			"OTU2" : ["XFEC", "ReedSolomon"],
			
			#presença de XFP
			"XFEC" : ["XFP_presente", "XFP_ausente"],
			"ReedSolomon" : ["XFP_presente", "XFP_ausente"],
			
	}

		
def generate_edges(OTU2_path):
    edges = []
    for node in OTU2_path:
        for neighbour in OTU2_path[node]:
            edges.append((node, neighbour))

    return edges

#print(generate_edges(g))

g = Graph(OTU2path)


clients = []

for i in range(0, 7):
 clients.append(g.vertices()[i])
