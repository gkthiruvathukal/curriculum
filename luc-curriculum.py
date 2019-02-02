import graphviz


def set_general_cluster_properties(c):
    c.attr(style='filled')
    c.attr(color='lightgrey')
    c.node_attr.update(style='filled', color='white')


clusters = {
    "core" : {
        '125' : None,
    },
    
    "core-writing" : {
        '111' : None,
        '250' : None,
        '317' : None,
    },

    "cs-1" : {
        '150*' : None,
        '170' : ['150*'],
        '163' : None,
        '171' : None,
    },

    "cs-2" : {
        "264" : ["163", "170", "171"],
        "271" : ["163", "170", "171"],
        "272" : ["271"],
    },

    "cs-3" : {
        '310' : ['271'],
        '363' : ['272'],
        '371' : ['272'],
    },
 
    
    "math" : {
        "M161" : None, 
        "M162" : ["M161"],
        "M263" : None,
        "M264" : None,
        "M212" : None,
        "S203" : None
    },
    

    "depth-se" : {
        '313' : ['271'],
        '330' : ['271']
    },

    
    "depth-cs-systems-arch" : {
        '337' : ['310', '313'],
        '339' : ['310'],
        '362' : ['264'],
        '364' : ['310'],
    },
    
    "depth-cs-languages" : {
        '335' : ['330', '371'],
        '382' : ['310', '371'],
        '376' : ['371']
    },
    
    "depth-cs-theory" : {
        '363' : ['272', 'M162'],
        '356' : ['363']
    },


    "depth-cs-ai" : { },
    
    "depth-cs-methods" : { },
}


# In[4]:


def add_cluster(subgraph, cluster_name, prerequisites):
    for course_number in prerequisites.keys():
        prereq_list = prerequisites[course_number]
        if prereq_list != None:
            for course_prereq in prereq_list: 
                subgraph.edge(course_prereq, course_number)
        else:
            subgraph.node(course_number)
        subgraph.attr(label=cluster_name)

def add_clusters(graph, clusters):
    clusters_keys = list(clusters.keys())
    clusters_keys.sort()
    for cluster_name in clusters_keys:
        print("Adding cluster %s" % cluster_name)
        with graph.subgraph(name="cluster_{}".format(cluster_name)) as cluster:
            set_general_cluster_properties(cluster)
            add_cluster(cluster, cluster_name, clusters[cluster_name])


# In[5]:


from graphviz import Digraph



def get_cs():
    curriculum = Digraph('G', filename='curriculum.gv')
    curriculum.attr(compound='true')
    curriculum.body.extend(['rankdir=LR', 'size="8,5"'])


    add_clusters(curriculum, clusters)
    return curriculum

cs = get_cs()
cs.save()
cs.render()


cs


# In[ ]:





# In[ ]:




