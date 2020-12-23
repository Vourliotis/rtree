from rtree import *

def main():
    r_seed = 1
    np.random.seed(seed = r_seed)

    rtree = RTree()

    #ENTRIES = RECTANGLES
    #entries = rtree.create_random(18, r_seed)

    #ENTRIES = POINTS FROM CSV FILE
    data_set = 'data'
    entries, time_elapsed_tree = rtree.import_csv(data_set)

    #ENTIRES = POINTS
    #entries, time_elapsed_tree = rtree.create_random_points(5, r_seed)

    #PRINT TREE IN CONSOLE
    print(repr(rtree))

    #SHOW ENTRIES - POINTS
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect = 'equal')
    plt.xlim([rtree.root.mbr.lower_left.x - 10, rtree.root.mbr.upper_right.x + 10])
    plt.ylim([rtree.root.mbr.lower_left.y - 10, rtree.root.mbr.upper_right.y + 10])
    patches = []
    for i in range(len(entries)):
        ax.add_patch(plt.Circle((entries[i].mbr.lower_left.x, entries[i].mbr.lower_left.y), 0.5, color = 'blue'))
    plt.show(block = False)

    #SHOW ENTRIES - RECTANGLES
    #fig = plt.figure()
    #ax = fig.add_subplot(111, aspect = 'equal')
    #plt.xlim([rtree.root.mbr.lower_left.x - 10, rtree.root.mbr.upper_right.x + 10])
    #plt.ylim([rtree.root.mbr.lower_left.y - 10, rtree.root.mbr.upper_right.y + 10])
    #patches = []
    #for i in range(len(entries)):
    #    ax.add_patch(matplotlib.patches.Rectangle((entries[i].mbr.lower_left.x, entries[i].mbr.lower_left.y), entries[i].mbr.width, entries[i].mbr.height, fill=None, edgecolor = c[0]))
    #plt.show()

    #PRINT R-TREE IF ENTRIES ARE RECTANGLES
    #rtree.show()

    #PRINT R-TREE IF ENTRIES ARE POINTS
    rtree.show_points()

    #PRINT SKYLINE ENTRIES IN CONSOLE
    skyline, time_elapsed_skyline = rtree.bbs_skyline()
    print("\nShowing Skyline Points:")
    for num_skylines in range(len(skyline)):
        print("")
        print(repr(skyline[num_skylines].mbr))

    #SHOW SKYLINE WITHOUT THE TREE
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect = 'equal')
    plt.xlim([rtree.root.mbr.lower_left.x - 10, rtree.root.mbr.upper_right.x + 10])
    plt.ylim([rtree.root.mbr.lower_left.y - 10, rtree.root.mbr.upper_right.y + 10])
    patches = []
    for i in range(len(entries)):
        ax.add_patch(plt.Circle((entries[i].mbr.lower_left.x, entries[i].mbr.lower_left.y), 0.5, color = 'blue'))
    for i in range(len(skyline)):
        ax.add_patch(plt.Circle((skyline[i].mbr.lower_left.x, skyline[i].mbr.lower_left.y), 0.5, color = 'coral'))
    plt.show(block = False)

    #PRINT SKYLINE IN R-TREE
    rtree.show_skyline(skyline)

    #RANGE QUERY IN R-TREE
    range_rec = Rectangle(Point(40, 40), Point(60, 60))
    query_entries, time_elapsed_query_entries = rtree.range_query(range_rec)

    #PRINT RANGE QUERY ENTRIES IN CONSOLE
    print("\nShowing Range Query Points")
    for num_entries in range(len(query_entries)):
        print("")
        print(repr(query_entries[num_entries]))
        
    #SHOW ENTRIES - POINTS
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect = 'equal')
    plt.xlim([rtree.root.mbr.lower_left.x - 10, rtree.root.mbr.upper_right.x + 10])
    plt.ylim([rtree.root.mbr.lower_left.y - 10, rtree.root.mbr.upper_right.y + 10])
    patches = []
    for i in range(len(entries)):
        ax.add_patch(plt.Circle((entries[i].mbr.lower_left.x, entries[i].mbr.lower_left.y), 0.5, color = 'blue'))
    plt.show(block = False)

    #SHOW QUERY ENTRIES WITHOUT THE R-TREE
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect = 'equal')
    plt.xlim([rtree.root.mbr.lower_left.x - 10, rtree.root.mbr.upper_right.x + 10])
    plt.ylim([rtree.root.mbr.lower_left.y - 10, rtree.root.mbr.upper_right.y + 10])
    patches = []
    ax.add_patch(matplotlib.patches.Rectangle((range_rec.lower_left.x, range_rec.lower_left.y), range_rec.width, range_rec.height, fill = None, edgecolor = 'coral'))
    for i in range(len(query_entries)):
        ax.add_patch(plt.Circle((query_entries[i].mbr.lower_left.x, query_entries[i].mbr.lower_left.y), 0.5, color = 'blue'))
    plt.show()

    #RANGE QUERY SKYLINE ENTRIES IN CONSOLE
    skyline, time_elapsed_skyline_query = rtree.bbs_skyline_range_query(range_rec)
    print("\nShowing Skyline Points given a range query:")
    for num_skylines in range(len(skyline)):
        print("")
        print(repr(skyline[num_skylines].mbr))

    #SHOW ENTRIES - POINTS
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect = 'equal')
    plt.xlim([rtree.root.mbr.lower_left.x - 10, rtree.root.mbr.upper_right.x + 10])
    plt.ylim([rtree.root.mbr.lower_left.y - 10, rtree.root.mbr.upper_right.y + 10])
    patches = []
    for i in range(len(entries)):
        ax.add_patch(plt.Circle((entries[i].mbr.lower_left.x, entries[i].mbr.lower_left.y), 0.5, color = 'blue'))
    plt.show(block = False)

    #SHOW SKYLINE ENTRIES GIVEN A RANGE QUERY
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect = 'equal')
    plt.xlim([rtree.root.mbr.lower_left.x - 10, rtree.root.mbr.upper_right.x + 10])
    plt.ylim([rtree.root.mbr.lower_left.y - 10, rtree.root.mbr.upper_right.y + 10])
    patches = []
    ax.add_patch(matplotlib.patches.Rectangle((range_rec.lower_left.x, range_rec.lower_left.y), range_rec.width, range_rec.height, fill = None, edgecolor = 'coral'))
    for i in range(len(query_entries)):
        ax.add_patch(plt.Circle((query_entries[i].mbr.lower_left.x, query_entries[i].mbr.lower_left.y), 0.5, color = 'blue'))
    for i in range(len(skyline)):
        ax.add_patch(plt.Circle((skyline[i].mbr.lower_left.x, skyline[i].mbr.lower_left.y), 0.5, color = 'coral'))
    plt.show(block = False)

    #SHOW SKYLINE ENTRIES GIVEN A RANGE QUERY IN THE R-TREE
    rtree.show_skyline(skyline)

    print("\nTime elapsed creating the tree: " + str(time_elapsed_tree) + "s")
    print("Time elapsed finding the Skyline points: " + str(time_elapsed_skyline) + "s")
    print("Time elapsed finding the range query entries: " + str(time_elapsed_query_entries) + "s")
    print("Time elapsed finding the Skyline entries given a range: " + str(time_elapsed_skyline_query) + "s")

if __name__ == '__main__':
    main()