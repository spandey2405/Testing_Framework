def get_routes(BR,endpoint):
    graph_motes={"routes":[
                "aaaa::212:4b00:42a:e9a9->aaaa::212:4b00:42a:e989",
                "aaaa::212:4b00:42a:e989->aaaa::212:4b00:42a:e989",
                "aaaa::212:4b00:42a:e9bd->aaaa::212:4b00:42a:e9bd",
                "aaaa::212:4b00:42a:e9fc->aaaa::212:4b00:42a:e9fc",
                "aaaa::212:4b00:42a:e94b->aaaa::212:4b00:42a:e94b",
                "aaaa::212:4b00:42a:ea76->aaaa::212:4b00:42a:ea76",
                "aaaa::212:4b00:42a:e8d1->aaaa::212:4b00:42a:e8d1",
                "aaaa::212:4b00:42a:ea8a->aaaa::212:4b00:42a:e8d1",
                "aaaa::212:4b00:42a:e9cb->aaaa::212:4b00:42a:e9cb",
                "aaaa::212:4b00:42a:e9ad->aaaa::212:4b00:42a:e9ad",
                "aaaa::212:4b00:42a:ea1b->aaaa::212:4b00:42a:ea1b" ]
                }
    return graph_motes["routes"]

def get_motes(BR,endpoint):
    motes = []
    b = get_routes(BR,endpoint)
    for values_b in b:
        value_b = values_b.split('->')
        motes.append(value_b[0])
    unique_motes = list(set(motes))
    return unique_motes

